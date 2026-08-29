import React, { useEffect, useState, useCallback, useMemo } from 'react';
import {
  SafeAreaView, ScrollView, View, Text, TextInput, Pressable,
  StyleSheet, useWindowDimensions, StatusBar, ActivityIndicator,
} from 'react-native';
import { useFonts } from 'expo-font';
import { Anton_400Regular } from '@expo-google-fonts/anton';
import { IBMPlexMono_400Regular, IBMPlexMono_600SemiBold } from '@expo-google-fonts/ibm-plex-mono';
import { IBMPlexSans_400Regular } from '@expo-google-fonts/ibm-plex-sans';

import Bateau from './src/Bateau';
import { C, F } from './src/theme';
import { charger, sauver, aujourdhui } from './src/stockage';
import { demanderPermission, programmerBulletin } from './src/notifications';
import {
  CONTENU, BANDES, CAP, PALIERS, recalibrer, prixProjete, coursBTC,
  longueurPourBudget, palierPourBudget, pick, remplir, seau, bulletin, eur, metres,
} from './src/moteur';

export default function App() {
  const { width } = useWindowDimensions();
  const [police] = useFonts({
    Anton_400Regular, IBMPlexMono_400Regular, IBMPlexMono_600SemiBold, IBMPlexSans_400Regular,
  });

  const [etat, setEtat] = useState(null);
  const [prix, setPrix] = useState(null);
  const [erreur, setErreur] = useState(null);
  const [message, setMessage] = useState(null);   // le bulletin du jour

  /* ─── démarrage ─────────────────────────────────────── */
  useEffect(() => {
    (async () => {
      const e = await charger();
      setEtat(e);
      try {
        const p = await coursBTC();
        setPrix(p);
        recalibrer(p);
        await releverLeMatin(e, p);
      } catch (_) {
        setErreur(CONTENU.systeme.erreurs.cours_indisponible);
        setPrix(100000);
        recalibrer(100000);
      }
    })();
  }, []);

  /* ─── le bateau vivant ──────────────────────────────── */
  const releverLeMatin = useCallback(async (e, p) => {
    const cible = new Date(e.annee, 11, 31);
    const L = longueurPourBudget(e.stack * prixProjete(cible, BANDES[e.bande].off));
    const hier = e.derniereMesure;

    if (hier && hier.date !== aujourdhui()) {
      const variation = (p - hier.prix) / hier.prix;
      const b = bulletin(hier.longueur, L, variation);
      setMessage(b);
      if (e.notifsActives) await programmerBulletin(b.texte);
    }
    const maj = { ...e, derniereMesure: { date: aujourdhui(), longueur: L, prix: p } };
    setEtat(maj);
    await sauver(maj);
  }, []);

  const maj = useCallback((patch) => {
    setEtat((prev) => { const n = { ...prev, ...patch }; sauver(n); return n; });
  }, []);

  /* ─── calculs ───────────────────────────────────────── */
  const calc = useMemo(() => {
    if (!etat || !prix) return null;
    const bande = BANDES[etat.bande];
    const prixFutur = prixProjete(new Date(etat.annee, 11, 31), bande.off);
    const budgetFut = etat.stack * prixFutur;
    const L = longueurPourBudget(budgetFut);
    const pal = palierPourBudget(budgetFut);
    const LAuj = longueurPourBudget(etat.stack * prix);
    const charge = pal.prix ? (pal.prix * 0.10) / Math.max(budgetFut, 1) : 0;
    const etatEntretien = charge <= 0.04 ? 'confortable' : charge <= 0.08 ? 'juste' : 'intenable';
    const tenable = palierPourBudget(budgetFut * 0.40);
    return { bande, prixFutur, budgetFut, L, LAuj, pal, charge, etatEntretien, tenable };
  }, [etat, prix]);

  if (!police || !etat || !calc) {
    return (
      <SafeAreaView style={[s.page, s.centre]}>
        <ActivityIndicator color={C.laiton} />
        <Text style={s.mono}>{pick(CONTENU.systeme.chargement, 0)}</Text>
      </SafeAreaView>
    );
  }

  const { bande, prixFutur, budgetFut, L, pal, charge, etatEntretien, tenable } = calc;
  const iP = PALIERS.indexOf(pal);
  const cap = CAP[pal.cap];

  return (
    <SafeAreaView style={s.page}>
      <StatusBar barStyle="light-content" />
      <ScrollView contentContainerStyle={s.scroll}>

        <View style={s.tete}>
          <Text style={s.marque}>LE YACHTOMÈTRE</Text>
          <Text style={s.mono}>{etat.annee}</Text>
        </View>

        {/* le bulletin du matin : le cœur du bateau vivant */}
        {message && (
          <View style={[s.bulletin, { borderLeftColor: message.delta >= 0 ? C.laiton : C.balise }]}>
            <Text style={s.bulletinTitre}>CE MATIN</Text>
            <Text style={s.bulletinTexte}>{message.texte}</Text>
          </View>
        )}

        <View style={s.scene}>
          <Bateau cls={pal.cls} L={pal.L || L} width={width} />
        </View>

        <View style={s.verdict}>
          <Text style={s.longueur}>{pal.L > 0 ? metres(L) : '—'}</Text>
          <Text style={s.nomPalier}>{pal.nom.toUpperCase()}</Text>
          <Text style={s.punch}>{pick(pal.punch, iP)}</Text>
          <View style={s.capitaine}>
            <Text style={s.capRole}>{cap.role.toUpperCase()}</Text>
            <Text style={s.capLigne}>
              « {pick(pal.dit.concat(cap.repliques), iP + 1)} »
            </Text>
          </View>
        </View>

        {/* réglages */}
        <View style={s.console}>
          <View style={s.champ}>
            <Text style={s.label}>TON STACK (BTC)</Text>
            <TextInput
              style={s.input} keyboardType="decimal-pad" defaultValue={String(etat.stack)}
              onChangeText={(t) => maj({ stack: Math.max(0, parseFloat(t.replace(',', '.')) || 0) })}
              placeholderTextColor={C.trait}
            />
          </View>
          <View style={s.champ}>
            <Text style={s.label}>TU HOLDES JUSQU'EN</Text>
            <View style={s.rangee}>
              <Pressable onPress={() => maj({ annee: Math.max(new Date().getFullYear(), etat.annee - 1) })} style={s.pas}>
                <Text style={s.pasTexte}>−</Text>
              </Pressable>
              <Text style={s.valeur}>{etat.annee}</Text>
              <Pressable onPress={() => maj({ annee: Math.min(new Date().getFullYear() + 16, etat.annee + 1) })} style={s.pas}>
                <Text style={s.pasTexte}>+</Text>
              </Pressable>
            </View>
          </View>
          <View style={s.champ}>
            <Text style={s.label}>TON NIVEAU DE FOI</Text>
            <Pressable onPress={() => maj({ bande: (etat.bande + 1) % BANDES.length })}>
              <Text style={s.valeurBande}>{bande.nom}</Text>
            </Pressable>
          </View>
        </View>

        {/* fiche */}
        <View style={s.fiche}>
          <Stat label="BUDGET PROJETÉ" valeur={eur(budgetFut)} />
          <Stat label="PRIX D'ACHAT" valeur={pal.prix ? eur(pal.prix) : '—'} />
          <Stat label="ENTRETIEN / AN" valeur={pal.prix ? eur(pal.prix * 0.10) : '—'} />
          <Stat label="BTC PROJETÉ" valeur={eur(prixFutur)} />
        </View>

        {/* acheter n'est pas garder */}
        <Section titre="ACHETER N'EST PAS GARDER">
          <Text style={s.duoLabel}>LE BATEAU QUE TU PEUX ACHETER</Text>
          <Text style={[s.duoNom, { color: C.balise }]}>{pal.nom}</Text>
          <Text style={s.note}>
            {pal.prix
              ? remplir(pick(CONTENU.entretien[etatEntretien].lignes, 3), {
                  ans: charge > 0 ? Math.max(1, Math.round(1 / charge)) : 0,
                  montant: eur(pal.prix * 0.10),
                })
              : "Rien à entretenir. C'est le seul avantage."}
          </Text>
          <View style={s.filet} />
          <Text style={s.duoLabel}>LE BATEAU QUE TU PEUX ENTRETENIR</Text>
          <Text style={s.duoNom}>{tenable.nom}</Text>
          <Text style={s.note}>{pick(CONTENU.entretien.confortable.lignes, 7)}</Text>
        </Section>

        {/* notifications */}
        <Section titre="LE BULLETIN DU MATIN">
          <Pressable
            style={[s.bouton, etat.notifsActives && s.boutonActif]}
            onPress={async () => {
              if (etat.notifsActives) { maj({ notifsActives: false }); return; }
              const ok = await demanderPermission();
              if (ok) {
                maj({ notifsActives: true });
                await programmerBulletin('Ton bateau a bougé cette nuit. Viens voir.');
              }
            }}>
            <Text style={s.boutonTexte}>
              {etat.notifsActives ? 'BULLETIN ACTIVÉ — 8H00' : 'RECEVOIR LE BULLETIN À 8H'}
            </Text>
          </Pressable>
          <Text style={s.note}>
            Une notification par jour, jamais plus. Elle te dit de combien ton bateau a rétréci ou grandi pendant la nuit.
          </Text>
        </Section>

        {erreur && <Text style={[s.note, { color: C.balise }]}>{erreur}</Text>}
        <Text style={s.pied}>{CONTENU.systeme.avertissement}</Text>
      </ScrollView>
    </SafeAreaView>
  );
}

const Stat = ({ label, valeur }) => (
  <View style={s.stat}>
    <Text style={s.label}>{label}</Text>
    <Text style={s.statValeur}>{valeur}</Text>
  </View>
);

const Section = ({ titre, children }) => (
  <View style={s.section}>
    <Text style={s.sectionTitre}>{titre}</Text>
    {children}
  </View>
);

const s = StyleSheet.create({
  page: { flex: 1, backgroundColor: C.abysse },
  centre: { alignItems: 'center', justifyContent: 'center', gap: 14 },
  scroll: { paddingBottom: 60 },

  tete: { flexDirection: 'row', alignItems: 'flex-end', justifyContent: 'space-between',
          paddingHorizontal: 18, paddingTop: 14, paddingBottom: 12,
          borderBottomWidth: 1, borderBottomColor: C.trait },
  marque: { fontFamily: F.display, fontSize: 26, color: C.craie, letterSpacing: 0.5 },
  mono: { fontFamily: F.monoR, fontSize: 12, color: C.papier, letterSpacing: 1 },

  bulletin: { backgroundColor: C.nuit, borderLeftWidth: 3, padding: 16, margin: 18, marginBottom: 0 },
  bulletinTitre: { fontFamily: F.mono, fontSize: 10, letterSpacing: 2, color: C.papier, marginBottom: 6 },
  bulletinTexte: { fontFamily: F.sans, fontSize: 16, color: C.craie, lineHeight: 23 },

  scene: { marginTop: 18, borderTopWidth: 1, borderBottomWidth: 1, borderColor: C.trait, backgroundColor: '#0B1E28' },

  verdict: { backgroundColor: C.pont, padding: 20 },
  longueur: { fontFamily: F.mono, fontSize: 40, color: C.laiton },
  nomPalier: { fontFamily: F.display, fontSize: 26, color: C.craie, marginTop: 2, letterSpacing: 0.5 },
  punch: { fontFamily: F.sans, fontSize: 16, color: C.craie, lineHeight: 24, marginTop: 12 },
  capitaine: { marginTop: 16, paddingTop: 12, borderTopWidth: 1, borderTopColor: C.trait },
  capRole: { fontFamily: F.mono, fontSize: 10, letterSpacing: 2, color: C.laiton },
  capLigne: { fontFamily: F.sans, fontSize: 15, color: C.papier, fontStyle: 'italic', marginTop: 5, lineHeight: 22 },

  console: { marginTop: 18, borderTopWidth: 1, borderColor: C.trait },
  champ: { backgroundColor: C.nuit, padding: 14, borderBottomWidth: 1, borderBottomColor: C.trait },
  label: { fontFamily: F.mono, fontSize: 10, letterSpacing: 1.8, color: C.papier, marginBottom: 6 },
  input: { fontFamily: F.mono, fontSize: 20, color: C.craie, padding: 0 },
  rangee: { flexDirection: 'row', alignItems: 'center', gap: 18 },
  pas: { width: 34, height: 34, alignItems: 'center', justifyContent: 'center', borderWidth: 1, borderColor: C.trait },
  pasTexte: { fontFamily: F.mono, fontSize: 20, color: C.craie },
  valeur: { fontFamily: F.mono, fontSize: 20, color: C.craie },
  valeurBande: { fontFamily: F.mono, fontSize: 17, color: C.laiton },

  fiche: { flexDirection: 'row', flexWrap: 'wrap' },
  stat: { width: '50%', backgroundColor: C.nuit, padding: 14, borderBottomWidth: 1, borderRightWidth: 1, borderColor: C.trait },
  statValeur: { fontFamily: F.mono, fontSize: 17, color: C.craie },

  section: { padding: 18, borderBottomWidth: 1, borderBottomColor: C.trait },
  sectionTitre: { fontFamily: F.display, fontSize: 18, color: C.craie, marginBottom: 14, letterSpacing: 0.5 },
  duoLabel: { fontFamily: F.mono, fontSize: 10, letterSpacing: 1.8, color: C.papier },
  duoNom: { fontFamily: F.display, fontSize: 22, color: C.craie, marginTop: 4 },
  note: { fontFamily: F.sans, fontSize: 14, color: C.papier, lineHeight: 21, marginTop: 8 },
  filet: { height: 1, backgroundColor: C.trait, marginVertical: 18 },

  bouton: { borderWidth: 1, borderColor: C.trait, paddingVertical: 13, alignItems: 'center' },
  boutonActif: { borderColor: C.laiton },
  boutonTexte: { fontFamily: F.mono, fontSize: 12, letterSpacing: 1.5, color: C.craie },

  pied: { fontFamily: F.monoR, fontSize: 11, color: C.trait, padding: 18, lineHeight: 18 },
});
