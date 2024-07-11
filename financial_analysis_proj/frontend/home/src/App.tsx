import { memo } from 'react';
import type { FC } from 'react';

import classes from './App.module.css';
import resets from './components/_resets.module.css';
import { Desktop1 } from './components/Desktop1/Desktop1.js';
import { Routes,Route } from 'react-router-dom';

interface Props {
  className?: string;
}
export const App: FC<Props> = memo(function App(props = {}) {
  return (
    <div className={`${resets.clapyResets} ${classes.root}`}>
      {/* <Routes> */}
        {/* <Route path="/home" element={<Desktop1 />} /> */}
        {/* Add other routes as needed */}
      {/* </Routes> */}

      <Desktop1 /> 
    </div>
  );
});
