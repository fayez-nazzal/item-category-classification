import { render } from 'preact';
import { App } from './app';
import Providers from './providers';
import './reset.css';

render(
  <Providers>
    <App />
  </Providers>,
  document.getElementById('app')
);
