/* Yachtomètre — moteur
   Aucun texte ici. Tout le texte vit dans contenu.json. */

import CONTENU from './contenu.json';

export { CONTENU };

/* ─── Rainbow chart ─────────────────────────────────────── */
const GENESIS = Date.UTC(2009, 0, 3);
const RB_A = 2.0;
const RB_B = -12.364;

export const BANDES = [
  { off: -0.70, nom: "Ton beau-frère qui dit que c'est une bulle" },
  { off: -0.35, nom: 'Réaliste' },
  { off:  0.00, nom: 'Optimiste raisonnable' },
  { off: +0.35, nom: 'Ton pote sur X' },
  { off: +0.70, nom: 'Michael Saylor' },
];

const jours = (d) => Math.max(1, (d.getTime() - GENESIS) / 86400000);
export const prixRainbow = (d, off) => Math.pow(10, RB_A * Math.log(jours(d)) + RB_B + off);

let CAL = 1;
export const recalibrer = (prixReel) => { CAL = prixReel / prixRainbow(new Date(), 0); };
export const prixProjete = (d, off) => prixRainbow(d, off) * CAL;

/* ─── Paliers et courbe prix → longueur ─────────────────── */
export const PALIERS = CONTENU.paliers.map((p) => ({
  id: p.id, prix: p.prix, L: p.longueur, cls: p.classe,
  cap: p.cap, nom: p.nom, punch: p.punch, dit: p.dit,
}));

export const CAP = CONTENU.capitaine;

const COURBE = PALIERS
  .filter((p) => p.prix > 0)
  .filter((p, i, t) => i === 0 || p.L > t[i - 1].L)
  .map((p) => ({ p: p.prix, L: p.L }));

export function longueurPourBudget(budget) {
  if (budget <= COURBE[0].p) return 0;
  const last = COURBE[COURBE.length - 1];
  if (budget >= last.p) return last.L;
  for (let i = 0; i < COURBE.length - 1; i++) {
    const a = COURBE[i], b = COURBE[i + 1];
    if (budget >= a.p && budget <= b.p) {
      const t = (Math.log(budget) - Math.log(a.p)) / (Math.log(b.p) - Math.log(a.p));
      return Math.exp(Math.log(a.L) + t * (Math.log(b.L) - Math.log(a.L)));
    }
  }
  return last.L;
}

export function palierPourBudget(budget) {
  let idx = 0;
  PALIERS.forEach((p, i) => { if (budget >= p.prix) idx = i; });
  return PALIERS[idx];
}

/* ─── Sélection de texte ────────────────────────────────── */
let SEED = Math.floor(Math.random() * 99991);
export const nouvelleGraine = () => { SEED = Math.floor(Math.random() * 99991); };

export function pick(arr, salt = 0) {
  if (!arr || !arr.length) return '';
  return arr[(SEED + salt) % arr.length];
}

export function remplir(tpl, vars) {
  return Object.keys(vars).reduce((s, k) => s.split(`{${k}}`).join(vars[k]), tpl);
}

export function seau(table, v) {
  for (const cle of Object.keys(table)) {
    const s = table[cle].seuil || table[cle].seuil_m;
    if (s && v >= s[0] && v < s[1]) return cle;
  }
  return Object.keys(table)[0];
}

/* ─── Formatage ─────────────────────────────────────────── */
export function eur(n) {
  if (n >= 1e9) return (n / 1e9).toFixed(2).replace('.', ',') + ' Md€';
  if (n >= 1e6) return (n / 1e6).toFixed(n < 1e7 ? 2 : 1).replace('.', ',') + ' M€';
  if (n >= 1000) return Math.round(n).toLocaleString('fr-FR') + ' €';
  return n.toFixed(n < 10 ? 2 : 0).replace('.', ',') + ' €';
}

export function metres(m) {
  if (m <= 0) return '0 m';
  if (m < 1) return (m * 100).toFixed(0) + ' cm';
  return m.toFixed(m < 10 ? 2 : 1).replace('.', ',') + ' m';
}

/* ─── Le bateau vivant ──────────────────────────────────── */
/* Compare la longueur d'aujourd'hui à la dernière mesure enregistrée
   et renvoie la ligne de notification correspondante. */
export function bulletin(longueurAvant, longueurApres, variationPct) {
  const cle = seau(CONTENU.notifications, variationPct);
  const d = longueurApres - longueurAvant;
  return {
    cle,
    delta: d,
    texte: remplir(pick(CONTENU.notifications[cle].lignes, Math.round(Math.abs(d) * 10)), {
      pct: (variationPct > 0 ? '+' : '') + (variationPct * 100).toFixed(0) + ' %',
      delta: metres(Math.abs(d)),
      longueur: metres(longueurApres),
    }),
  };
}

/* ─── Cours du BTC ──────────────────────────────────────── */
export async function coursBTC() {
  const r = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur');
  const j = await r.json();
  if (!j?.bitcoin?.eur) throw new Error('cours indisponible');
  return j.bitcoin.eur;
}
