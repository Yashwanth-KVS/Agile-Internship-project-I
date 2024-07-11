import { memo, SVGProps } from 'react';

const Rectangle1Icon = (props: SVGProps<SVGSVGElement>) => (
  <svg preserveAspectRatio='none' viewBox='0 0 1440 379' fill='none' xmlns='http://www.w3.org/2000/svg' {...props}>
    <path d='M8.10623e-06 9.53674e-07H1440V379H8.10623e-06V9.53674e-07Z' fill='black' />
  </svg>
);

const Memo = memo(Rectangle1Icon);
export { Memo as Rectangle1Icon };
