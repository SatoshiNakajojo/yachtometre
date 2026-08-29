/* Yachtomètre — stockage local.
   C'est ce qui rend le bateau vivant : on garde la mesure d'hier
   pour pouvoir annoncer le delta ce matin. */

import AsyncStorage from '@react-native-async-storage/async-storage';

const CLE = 'yachtometre:v1';

const DEFAUT = {
  stack: 0.35,
  annee: new Date().getFullYear() + 6,
  bande: 2,
  derniereMesure: null,   // { date: 'YYYY-MM-DD', longueur: number, prix: number }
  notifsActives: false,
};

export async function charger() {
  try {
    const brut = await AsyncStorage.getItem(CLE);
    return brut ? { ...DEFAUT, ...JSON.parse(brut) } : { ...DEFAUT };
  } catch (_) {
    return { ...DEFAUT };
  }
}

export async function sauver(etat) {
  try { await AsyncStorage.setItem(CLE, JSON.stringify(etat)); } catch (_) {}
}

export const aujourdhui = () => new Date().toISOString().slice(0, 10);
