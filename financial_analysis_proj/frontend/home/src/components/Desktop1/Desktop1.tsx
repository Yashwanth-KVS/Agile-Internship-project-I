import { memo } from 'react';
import type { FC } from 'react';

import resets from '../_resets.module.css';
import classes from './Desktop1.module.css';
import { MunchyGramIcon } from './MunchyGramIcon.js';
import { Product } from './Product/Product.js';
import { Rectangle1Icon } from './Rectangle1Icon.js';

interface Props {
  className?: string;
}
/* @figmaId 35:7 */
export const Desktop1: FC<Props> = memo(function Desktop1(props = {}) {
  return (
    <div className={`${resets.clapyResets} ${classes.root}`}>
      <div className={classes.rectangle1}>
        <Rectangle1Icon className={classes.icon} />
      </div>
      <div className={classes.micheileHendersonSoT4MZhyhEUns}></div>
      <div className={classes.stockCakeDigitalFinanceHub_171}></div>
      <div className={classes.frame1}>
        <div className={classes.frame20}>
          <Product />
          <Product
            classes={{ image: classes.image }}
            text={{
              iPhone11ProMaxCopy: <div className={classes.iPhone11ProMaxCopy}>Manage your Finances</div>,
            }}
          />
          <Product
            classes={{ image: classes.image2 }}
            text={{
              iPhone11ProMaxCopy: <div className={classes.iPhone11ProMaxCopy2}>Savings Schemes</div>,
            }}
          />
          <Product
            classes={{ image: classes.image3 }}
            text={{
              iPhone11ProMaxCopy: <div className={classes.iPhone11ProMaxCopy3}>Financial Insights</div>,
            }}
          />
        </div>
        <div className={classes.ourBestResultsFor}>Our Services</div>
      </div>
      <div className={classes.frame19}>
        <div className={classes.home}>Home</div>
        <div className={classes.product}>Product</div>
        <div className={classes.banking}>Banking</div>
        <div className={classes.frame17}>
          <div className={classes.login}>Login</div>
        </div>
      </div>
      <div className={classes.frame33861}>
        <div className={classes.followUsToKnowMore}>Follow us to know more </div>
        <div className={classes.wrapper}>
          <div className={classes.frame33858}>
            <div className={classes.frame21}>
              <div className={classes.linkedIn2668700_640EzgifComCro}></div>
            </div>
          </div>
          <div className={classes.frame33859}>
            <div className={classes.download1}></div>
          </div>
          <div className={classes.frame33860}>
            <div className={classes.instagram}>
              <div className={classes.munchyGram}>
                <MunchyGramIcon className={classes.icon2} />
              </div>
            </div>
          </div>
        </div>
        <div className={classes.download11}></div>
      </div>
      <div className={classes.rectangle2}></div>
      <div className={classes.rectangle3}></div>
      <div className={classes.contactUs}>Contact Us</div>
      <div className={classes.financialWellnessIsAWayOfEffec}>
        <div className={classes.textBlock}>Financial wellness is a way of effectively managing your finances. </div>
        <div className={classes.textBlock2}>
          Not knowing how to deal with your finances can lead to major stress, anxiety or depression.{' '}
        </div>
        <div className={classes.textBlock3}>
          Finance plays a substantial role in your daily wellness and well-being.
        </div>
      </div>
      <div className={classes.finertia_transparent1}></div>
    </div>
  );
});
