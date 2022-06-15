import { defineConfig } from 'vite';
import preact from '@preact/preset-vite';

export default (args) => {
  const generateScopedName =
    args.mode === 'production' ? '[hash:base64:5]' : '[local]__[hash:base64:2]';

  return defineConfig({
    resolve: {
      alias: {},
    },
    plugins: [preact()],
    css: {
      localConvention: 'camelCase',
      generateScopedName,
    },
  });
};
