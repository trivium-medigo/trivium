import { defineProject } from 'vitest/config';

// Phase 1 Step 15 — apps/api unit test defaults.
// Convention: real API unit tests live under tests/unit (see Vitest monorepo guidance:
// https://vitest.dev/guide/workspace ).
//
// Co-located src/modules/**/tests/module.test.ts files are scaffold placeholders (export-only);
// they are intentionally not collected here so `pnpm test` stays green until modules ship tests.

export default defineProject({
  test: {
    name: 'apps-api',
    environment: 'node',
    include: ['tests/unit/**/*.test.ts'],
    clearMocks: true,
  },
});
