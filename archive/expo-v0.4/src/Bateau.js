/* Yachtomètre — silhouettes de bateau, react-native-svg
   La silhouette humaine fait toujours 1,75 m. C'est la blague. */

import React from 'react';
import Svg, { Path, Circle, Ellipse, Rect, Line, G, Text as SvgText } from 'react-native-svg';
import { C } from './theme';

const VB_W = 1000, VB_H = 320, WATER = 244, X0 = 96, HUMAIN = 1.75;

function Humain({ x, pxm, opacity = 0.9 }) {
  const h = HUMAIN * pxm, y = WATER, tete = h * 0.13;
  return (
    <G opacity={opacity}>
      <Circle cx={x} cy={y - h + tete} r={tete} fill={C.papier} />
      <Path
        d={`M ${x} ${y - h + tete * 2.1} L ${x} ${y - h * 0.44}
            M ${x - h * 0.1} ${y - h * 0.68} L ${x + h * 0.1} ${y - h * 0.62}
            M ${x} ${y - h * 0.44} L ${x - h * 0.09} ${y}
            M ${x} ${y - h * 0.44} L ${x + h * 0.09} ${y}`}
        stroke={C.papier} strokeWidth={Math.max(1, h * 0.055)} fill="none" strokeLinecap="round"
      />
    </G>
  );
}

function coque(x0, x1, prof) {
  const len = x1 - x0, y = WATER;
  return `M ${x0} ${y - prof * 0.5}
          L ${x1} ${y - prof * 0.95}
          L ${x1 - len * 0.03} ${y + prof * 0.85}
          Q ${x0 + len * 0.32} ${y + prof * 1.2} ${x0 + len * 0.015} ${y + prof * 0.55} Z`;
}

function Silhouette({ cls, L }) {
  const cadre = Math.max(L, 7);
  const pxm = (VB_W - X0 - 60) / cadre;
  const x0 = X0, x1 = X0 + L * pxm;
  const len = Math.max(x1 - x0, 2);

  switch (cls) {
    case 'rien':
      return (
        <SvgText x={VB_W / 2} y={WATER - 40} textAnchor="middle" fill={C.trait}
                 fontSize={17} letterSpacing={3} fontFamily="monospace">
          RIEN À L'HORIZON
        </SvgText>
      );

    case 'duck': {
      const r = len * 0.42;
      return (
        <G>
          <Ellipse cx={x0 + len * 0.5} cy={WATER - r * 0.15} rx={r} ry={r * 0.55} fill={C.laiton} />
          <Ellipse cx={x0 + len * 0.5} cy={WATER - r * 0.15} rx={r * 0.45} ry={r * 0.24} fill={C.abysse} />
          <Circle cx={x0 + len * 0.86} cy={WATER - r * 0.95} r={r * 0.34} fill={C.laiton} />
          <Circle cx={x0 + len * 0.93} cy={WATER - r * 1.05} r={r * 0.07} fill={C.abysse} />
          <Path d={`M ${x0 + len * 1.13} ${WATER - r * 0.92} l ${r * 0.3} ${r * 0.1} l ${-r * 0.3} ${r * 0.14} z`} fill={C.balise} />
        </G>
      );
    }

    case 'noodle':
      return <Rect x={x0} y={WATER - len * 0.09} width={len} height={len * 0.14} rx={len * 0.07} fill={C.balise} />;

    case 'mattress':
      return (
        <G>
          <Rect x={x0} y={WATER - len * 0.11} width={len} height={len * 0.16} rx={len * 0.03} fill={C.craie} opacity={0.85} />
          <Rect x={x0} y={WATER - len * 0.11} width={len} height={len * 0.05} fill={C.balise} opacity={0.8} />
          <Circle cx={x0 + len * 0.72} cy={WATER - len * 0.16} r={len * 0.022} fill={C.papier} opacity={0.8} />
          <Circle cx={x0 + len * 0.78} cy={WATER - len * 0.24} r={len * 0.015} fill={C.papier} opacity={0.6} />
          <Circle cx={x0 + len * 0.74} cy={WATER - len * 0.31} r={len * 0.01} fill={C.papier} opacity={0.45} />
        </G>
      );

    case 'kayak':
      return (
        <G>
          <Path d={`M ${x0} ${WATER - len * 0.02} Q ${x0 + len * 0.5} ${WATER - len * 0.2} ${x1} ${WATER - len * 0.02}
                    Q ${x0 + len * 0.5} ${WATER + len * 0.13} ${x0} ${WATER - len * 0.02} Z`} fill={C.laiton} />
          <Ellipse cx={x0 + len * 0.5} cy={WATER - len * 0.05} rx={len * 0.17} ry={len * 0.045} fill={C.abysse} />
        </G>
      );

    case 'paddle':
      return (
        <G>
          <Rect x={x0} y={WATER - len * 0.045} width={len} height={len * 0.05} rx={len * 0.025} fill={C.craie} />
          <Humain x={x0 + len * 0.45} pxm={pxm} />
          <Line x1={x0 + len * 0.56} y1={WATER - HUMAIN * pxm * 1.05} x2={x0 + len * 0.62} y2={WATER + 6}
                stroke={C.laiton} strokeWidth={Math.max(2, pxm * 0.05)} />
        </G>
      );

    case 'pedalo': {
      const p = len * 0.28;
      return (
        <G>
          <Path d={coque(x0, x1, p)} fill={C.craie} />
          <Rect x={x0 + len * 0.18} y={WATER - p * 2.4} width={len * 0.5} height={p * 0.22} fill={C.balise} />
          <Line x1={x0 + len * 0.2} y1={WATER - p * 2.3} x2={x0 + len * 0.2} y2={WATER - p * 0.6} stroke={C.craie} strokeWidth={3} />
          <Line x1={x0 + len * 0.64} y1={WATER - p * 2.3} x2={x0 + len * 0.64} y2={WATER - p * 0.6} stroke={C.craie} strokeWidth={3} />
          <Path d={`M ${x0 + len * 0.1} ${WATER - p * 2.2} Q ${x0 - len * 0.14} ${WATER - p * 1.2} ${x0 - len * 0.16} ${WATER + p * 0.4}`}
                stroke={C.laiton} strokeWidth={Math.max(4, p * 0.28)} fill="none" strokeLinecap="round" />
        </G>
      );
    }

    case 'barque': {
      const p = len * 0.2;
      return (
        <G>
          <Path d={coque(x0, x1, p)} fill={C.craie} />
          <Rect x={x0 + len * 0.3} y={WATER - p * 0.62} width={len * 0.3} height={p * 0.16} fill={C.abysse} />
          <Rect x={x0 - len * 0.02} y={WATER - p * 1.5} width={len * 0.1} height={p * 1.05} fill={C.abysse} />
        </G>
      );
    }

    case 'jetski': {
      const p = len * 0.24;
      return (
        <G>
          <Path d={`M ${x0} ${WATER - p * 0.2} L ${x0 + len * 0.72} ${WATER - p * 0.75} L ${x1} ${WATER - p * 0.15}
                    L ${x1 - len * 0.08} ${WATER + p * 0.5} L ${x0 + len * 0.05} ${WATER + p * 0.45} Z`} fill={C.balise} />
          <Path d={`M ${x0 + len * 0.36} ${WATER - p * 0.8} l ${len * 0.2} ${-p * 0.5} l ${len * 0.1} ${p * 0.1}`}
                stroke={C.craie} strokeWidth={Math.max(2, p * 0.12)} fill="none" strokeLinecap="round" />
        </G>
      );
    }

    case 'rib': {
      const p = len * 0.18;
      return (
        <G>
          <Path d={coque(x0, x1, p)} fill={C.abysse} />
          <Rect x={x0} y={WATER - p * 0.85} width={len} height={p * 0.5} rx={p * 0.25} fill={C.craie} />
          <Rect x={x0 + len * 0.4} y={WATER - p * 1.9} width={len * 0.16} height={p * 1.1} fill={C.laiton} />
        </G>
      );
    }

    case 'open': {
      const p = len * 0.17;
      return (
        <G>
          <Path d={coque(x0, x1, p)} fill={C.craie} />
          <Path d={`M ${x0 + len * 0.42} ${WATER - p * 0.75} l ${len * 0.16} ${-p * 0.85} l ${len * 0.09} ${p * 0.2} l ${-len * 0.06} ${p * 0.7} z`}
                fill={C.papier} opacity={0.6} />
          <Rect x={x0 + len * 0.1} y={WATER - p * 0.8} width={len * 0.24} height={p * 0.12} fill={C.abysse} />
        </G>
      );
    }

    case 'sail': {
      const p = len * 0.14, mh = len * 0.95;
      return (
        <G>
          <Path d={coque(x0, x1, p)} fill={C.craie} />
          <Line x1={x0 + len * 0.45} y1={WATER - p * 0.7} x2={x0 + len * 0.45} y2={WATER - mh}
                stroke={C.papier} strokeWidth={Math.max(2, p * 0.14)} />
          <Path d={`M ${x0 + len * 0.47} ${WATER - mh * 0.97} L ${x0 + len * 0.47} ${WATER - p * 1.4} L ${x0 + len * 0.84} ${WATER - p * 1.4} Z`}
                fill={C.craie} opacity={0.85} />
          <Path d={`M ${x0 + len * 0.43} ${WATER - mh * 0.94} L ${x0 + len * 0.43} ${WATER - p * 1.4} L ${x0 + len * 0.16} ${WATER - p * 1.4} Z`}
                fill={C.craie} opacity={0.6} />
        </G>
      );
    }

    case 'vedette': {
      const p = len * 0.15;
      return (
        <G>
          <Path d={coque(x0, x1, p)} fill={C.craie} />
          <Path d={`M ${x0 + len * 0.24} ${WATER - p * 0.8} L ${x0 + len * 0.62} ${WATER - p * 0.8} L ${x0 + len * 0.56} ${WATER - p * 2.1} L ${x0 + len * 0.3} ${WATER - p * 2.1} Z`}
                fill={C.craie} opacity={0.8} />
          <Rect x={x0 + len * 0.32} y={WATER - p * 1.95} width={len * 0.2} height={p * 0.5} fill={C.abysse} opacity={0.7} />
          <Line x1={x0 + len * 0.42} y1={WATER - p * 2.1} x2={x0 + len * 0.42} y2={WATER - p * 3.1} stroke={C.papier} strokeWidth={2} />
        </G>
      );
    }

    default: {
      /* yacht + super : générateur paramétrique */
      const grand = cls === 'super';
      const p = len * (grand ? 0.085 : 0.12);
      const ponts = L < 26 ? 2 : L < 45 ? 3 : L < 80 ? 4 : 5;
      const hp = p * 1.15;
      const decks = [];
      for (let i = 0; i < ponts; i++) {
        const xa = x0 + len * (0.07 + i * 0.055);
        const xb = x0 + len * (0.70 - i * 0.075);
        const ya = WATER - p * 0.7 - hp * (i + 1);
        if (xb <= xa) break;
        decks.push(
          <G key={`d${i}`}>
            <Rect x={xa} y={ya} width={xb - xa} height={hp} fill={C.craie} opacity={0.86 - i * 0.09} />
            <Rect x={xa + (xb - xa) * 0.06} y={ya + hp * 0.3} width={(xb - xa) * 0.82} height={hp * 0.3} fill={C.abysse} opacity={0.55} />
          </G>
        );
      }
      const sommet = WATER - p * 0.7 - hp * ponts;
      const rHeli = len * 0.052, cxH = x0 + len * 0.83, cyH = WATER - p * 1.05;
      const sl = len * 0.055, sx = x0 + len * 0.10, sy = WATER - p * 0.95;
      const shadowL = len * 0.42, shadowX = x0 + len * 0.02, shadowP = p * 0.7;

      return (
        <G>
          {L >= 100 && (
            <G opacity={0.3} translateY={-p * 2.2}>
              <Path d={coque(shadowX, shadowX + shadowL, shadowP)} fill={C.papier} />
              <Rect x={shadowX + shadowL * 0.1} y={WATER - shadowP * 1.9} width={shadowL * 0.42} height={shadowP * 1.2} fill={C.papier} />
            </G>
          )}
          <Path d={coque(x0, x1, p)} fill={C.craie} />
          <Path d={`M ${x0 + len * 0.02} ${WATER - p * 0.12} L ${x1 - len * 0.05} ${WATER - p * 0.5}`}
                stroke={C.laiton} strokeWidth={Math.max(1, p * 0.09)} opacity={0.9} />
          {decks}
          <Line x1={x0 + len * 0.2} y1={sommet} x2={x0 + len * 0.2} y2={sommet - hp * 1.5}
                stroke={C.papier} strokeWidth={Math.max(1.2, p * 0.09)} />
          <Circle cx={x0 + len * 0.2} cy={sommet - hp * 1.5} r={Math.max(2, p * 0.22)} fill={C.papier} />
          {L >= 60 && (
            <G>
              <Ellipse cx={cxH} cy={cyH} rx={rHeli} ry={rHeli * 0.3} fill="none" stroke={C.laiton} strokeWidth={Math.max(1, rHeli * 0.14)} />
              <SvgText x={cxH} y={cyH + rHeli * 0.16} textAnchor="middle" fill={C.laiton}
                       fontSize={Math.max(6, rHeli * 0.7)} fontWeight="600" fontFamily="monospace">H</SvgText>
            </G>
          )}
          {L >= 80 && (
            <G>
              <Ellipse cx={sx} cy={sy} rx={sl} ry={sl * 0.42} fill={C.balise} />
              <Circle cx={sx + sl * 0.4} cy={sy} r={sl * 0.2} fill={C.abysse} />
            </G>
          )}
        </G>
      );
    }
  }
}

export default function Bateau({ cls, L, width }) {
  const cadre = Math.max(L, 7);
  const pxm = (VB_W - X0 - 60) / cadre;
  return (
    <Svg width={width} height={(width * VB_H) / VB_W} viewBox={`0 0 ${VB_W} ${VB_H}`}>
      <Rect x={0} y={WATER} width={X0 - 34} height={VB_H - WATER} fill={C.nuit} />
      <Line x1={0} y1={WATER} x2={X0 - 34} y2={WATER} stroke={C.papier} strokeWidth={2} />
      {cls !== 'paddle' && <Humain x={X0 - 62} pxm={pxm} />}
      <Silhouette cls={cls} L={L} />
      <Line x1={0} y1={WATER} x2={VB_W} y2={WATER} stroke={C.trait} strokeWidth={1.5} />
      <Path d={`M 0 ${WATER + 16} q 30 -7 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0`}
            stroke={C.trait} strokeWidth={1} fill="none" opacity={0.5} />
      <SvgText x={VB_W - 14} y={VB_H - 12} textAnchor="end" fill={C.trait}
               fontSize={11} letterSpacing={1.5} fontFamily="monospace">SILHOUETTE = 1,75 M</SvgText>
    </Svg>
  );
}
