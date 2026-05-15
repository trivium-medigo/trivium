import { describe, expect, it } from 'vitest';

// Tooling smoke for the apps-api Vitest project (Phase 1 Step 15). Not domain coverage.

describe('apps/api Vitest project', () => {
  it('runs under the node environment', () => {
    expect(typeof process.versions.node).toBe('string');
  });
});
