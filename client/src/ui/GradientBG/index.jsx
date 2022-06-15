import GradientBGCSS from './index.module.css';

const GradientBG = ({ children }) => {
  return <div className={GradientBGCSS['gradient-bg']}>{children}</div>;
};

export default GradientBG;
