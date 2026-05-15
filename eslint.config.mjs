// @ts-check
/** ESLint flat config — Phase 1 Step 14 (ESLint + Prettier + typescript-eslint, non–type-aware baseline). */
import js from '@eslint/js';
import eslintConfigPrettier from 'eslint-config-prettier';
import tseslint from 'typescript-eslint';

export default tseslint.config(
  {
    ignores: [
      '**/node_modules/**',
      '**/dist/**',
      '**/build/**',
      '**/coverage/**',
      '**/.next/**',
      '**/.turbo/**',
      '.git/**',
      'pnpm-lock.yaml',
      'docs/architecture/PLATFORM_TREE.md',
      'docs/architecture/platform_tree_manifest.json',
    ],
  },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  eslintConfigPrettier,
);
