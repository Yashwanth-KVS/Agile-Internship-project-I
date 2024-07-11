import { memo, SVGProps } from 'react';

const MunchyGramIcon = (props: SVGProps<SVGSVGElement>) => (
  <svg preserveAspectRatio='none' viewBox='0 0 65 65' fill='none' xmlns='http://www.w3.org/2000/svg' {...props}>
    <rect x={0.394114} y={0.394076} width={64.0821} height={64.0821} rx={13.2742} fill='url(#paint0_radial_52_36)' />
    <rect x={0.394114} y={0.394076} width={64.0821} height={64.0821} rx={13.2742} fill='url(#paint1_radial_52_36)' />
    <circle cx={31.749} cy={34.0367} r={11.6721} stroke='white' strokeWidth={3.66184} />
    <circle cx={46.3959} cy={18.9311} r={2.97524} fill='white' />
    <rect x={10.0064} y={10.4632} width={44.8575} height={45.773} rx={8.69686} stroke='white' strokeWidth={3.20411} />
    <defs>
      <radialGradient
        id='paint0_radial_52_36'
        cx={0}
        cy={0}
        r={1}
        gradientUnits='userSpaceOnUse'
        gradientTransform='translate(54.5435 73.1273) rotate(-105.945) scale(83.9745 124.903)'
      >
        <stop offset={0.197635} stopColor='#F50B5E' />
        <stop offset={0.52034} stopColor='#DF0897' />
        <stop offset={0.768785} stopColor='#962FBF' />
        <stop offset={0.933441} stopColor='#4F5BD5' />
      </radialGradient>
      <radialGradient
        id='paint1_radial_52_36'
        cx={0}
        cy={0}
        r={1}
        gradientUnits='userSpaceOnUse'
        gradientTransform='translate(21.8616 64.4762) rotate(-54.9721) scale(41.8673 45.7948)'
      >
        <stop offset={0.09375} stopColor='#FEDA75' />
        <stop offset={0.475046} stopColor='#FA7E1E' />
        <stop offset={1} stopColor='#FA7E1E' stopOpacity={0} />
      </radialGradient>
    </defs>
  </svg>
);

const Memo = memo(MunchyGramIcon);
export { Memo as MunchyGramIcon };
