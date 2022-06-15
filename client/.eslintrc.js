module.exports = {
  ignorePatterns: ['dist', '@emotion', 'prettier'],
  env: {
    browser: true,
    es2021: true,
  },
  extends: ['preact', 'google', 'prettier'],
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  rules: {
    'comma-dangle': 0,
    'react/jsx-filename-extension': [1, { extensions: ['.jsx'] }],
  },
};
