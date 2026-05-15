import { defineConfig } from 'vitest/config';

// Phase 1 Step 15 — Vitest default runner (monorepo).
// Projects: https://vitest.dev/guide/workspace
//
// - trivium-tooling: Node-environment smoke proving the runner is wired.
// - apps-api: Node defaults; collects apps/api/tests/unit only (see apps/api/vitest.config.ts).
//
// Per-package Vitest projects are deferred until packages ship real unit tests (avoid one
// project per placeholder folder under packages/).
//
// Browser / component / UI tests: deferred. Coverage: deferred (see report).

export default defineConfig({
  test: {
    projects: [
      {
        test: {
          name: 'trivium-tooling',
          environment: 'node',
          include: ['tests/tooling/**/*.test.ts'],
        },
      },
      './apps/api/vitest.config.ts',
    ],
  },
});
