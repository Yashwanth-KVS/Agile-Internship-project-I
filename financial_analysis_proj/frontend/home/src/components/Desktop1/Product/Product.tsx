import { memo } from 'react';
import type { FC, ReactNode } from 'react';

import resets from '../../_resets.module.css';
import { ArrowCircleRight } from '../ArrowCircleRight/ArrowCircleRight.js';
import classes from './Product.module.css';
import { VectorIcon2 } from './VectorIcon2.js';
import { VectorIcon } from './VectorIcon.js';

interface Props {
  className?: string;
  classes?: {
    image?: string;
  };
  text?: {
    iPhone11ProMaxCopy?: ReactNode;
  };
}
/* @figmaId 35:208 */
export const Product: FC<Props> = memo(function Product(props = {}) {
  return (
    <div className={`${resets.clapyResets} ${classes.root}`}>
      <div className={`${props.classes?.image || ''} ${classes.image}`}></div>
      <div className={classes.frame21}>
        {props.text?.iPhone11ProMaxCopy != null ? (
          props.text?.iPhone11ProMaxCopy
        ) : (
          <div className={classes.iPhone11ProMaxCopy}>Know About Finances</div>
        )}
        <ArrowCircleRight
          className={classes.arrowCircleRight}
          swap={{
            vector: <VectorIcon className={classes.icon} />,
            vector2: <VectorIcon2 className={classes.icon2} />,
          }}
        />
      </div>
    </div>
  );
});
