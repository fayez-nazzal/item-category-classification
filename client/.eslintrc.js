module.exports = {
  ignorePatterns: ['dist', '@emotion', 'prettier'],
  env: {
    browser: true,
    es2021: true,
  },
  extends: ['plugin:react/recommended', 'google'],
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  plugins: ['react'],
  rules: {
    'comma-dangle': 0,
    'prettier/prettier': 'error',
    'react/jsx-filename-extension': [1, { extensions: ['.jsx'] }],
  },
};
