# posting-engine-contracts

Shared **posting contracts** (types, error codes, idempotency keys) consumed by `posting-engine`, workers, and finance APIs.

## Architectural role

Contracts encode **deterministic** posting rules so every caller agrees on:

- What constitutes a valid **posted** journal.  
- Errors when COA, period, basis, or balance checks fail.  
- Idempotency keys for safe retries from workers and sync jobs.

## COA and lifecycle alignment

When implemented, export shared enums/constants for:

- `GlAccountPostingEligibility` (posting vs header, active vs inactive)  
- `PeriodLockViolation`, `BookScopeMismatch`, `InvalidGlAccountReference`  
- `PostedJournalImmutabilityViolation` (attempt to mutate posted lines)  
- `AccountingBasisMismatch` (ledger vs entry)  
- `AiDraftRequiresApproval`, `PostingEngineOnlyMayPost`

## AI boundary

Contracts must make it **impossible** (at type level where feasible) for AI draft modules to import “post committed” helpers reserved for posting-engine.

## Spec sources

- `docs/architecture/deterministic-accounting.md`  
- `docs/architecture/finance-accounting.md`  
- `databases/.../ledger-integrity/journal_lines.sql`  
- `databases/.../ledger-integrity/journal_entries.sql`  
