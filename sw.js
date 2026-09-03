/* Le Yachtomètre — service worker
 *
 * Garde le jeu ouvrable sans réseau. Il ne stocke que les fichiers du site :
 * aucune donnée de l'utilisateur ne passe par ici, le stack reste dans
 * localStorage et ne quitte pas l'appareil.
 *
 * La ligne VERSION est réécrite à chaque `python3 build.py`. Ne la fixe pas
 * à la main : c'est elle qui purge l'ancien cache après une mise à jour.
 */
const VERSION = '5923f7ebfd';
const CACHE = 'yachtometre-' + VERSION;

const COQUE = [
  './', './index.html', './yachtometre.html', './manifest.webmanifest',
  './icones/icone-32.png', './icones/icone-180.png',
  './icones/icone-192.png', './icones/icone-512.png'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE)
      .then(c => Promise.allSettled(COQUE.map(u => c.add(u))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(k => Promise.all(k.filter(n => n !== CACHE).map(n => caches.delete(n))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  // Le cours du BTC ne se met jamais en cache : un prix périmé est pire
  // qu'un prix absent, le repli manuel existe pour ça.
  if (/api\.(coingecko|coinbase|binance)\.com$/.test(url.hostname)) return;

  // Polices Google : on sert le cache d'abord, on complète au besoin.
  if (/^fonts\.(googleapis|gstatic)\.com$/.test(url.hostname)) {
    e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(r => {
      const copie = r.clone();
      caches.open(CACHE).then(c => c.put(req, copie)).catch(() => {});
      return r;
    })));
    return;
  }

  // Le site lui-même : réseau d'abord pour ne jamais bloquer sur une
  // vieille version, cache en repli quand il n'y a pas de réseau.
  //
  // `cache: 'no-store'` court-circuite le cache HTTP du navigateur. Sans lui,
  // « réseau d'abord » ne suffit pas : GitHub Pages sert le HTML avec
  // max-age=600, donc le fetch pouvait être servi par le cache du navigateur
  // et rendre une version publiée invisible pendant dix minutes — le temps
  // qu'il faut pour croire que la publication a échoué.
  if (url.origin === self.location.origin) {
    e.respondWith(
      fetch(req, { cache: 'no-store' }).catch(() => fetch(req)).then(r => {
        if (r && r.ok) {
          const copie = r.clone();
          caches.open(CACHE).then(c => c.put(req, copie)).catch(() => {});
        }
        return r;
      }).catch(() => caches.match(req).then(hit => hit || caches.match('./index.html')))
    );
  }
});
