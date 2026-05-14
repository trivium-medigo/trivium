# ledger-integrity (architecture)

System of record for **posted** general ledger journals: `journal_entries`, `journal_lines`, `ledgers`, posting batches, trial balance snapshots, retained earnings rollforward.

## Determinism

- **Posting-engine** is the only path to **posted** state. See `docs/architecture/deterministic-accounting.md`.  
- **Immutability**: posted lines are not edited in place; reversals create new entries.

## Dual-basis

- `ledgers.sql` defines **`accounting_basis`** (accrual | cash) per ledger.  
- `journal_entries.sql` ties each entry to one `ledger_id` (single basis per posted entry).  
- TB is **per ledger** — see `docs/architecture/finance-accounting.md` and `docs/architecture/financial-reporting.md`.

## References

- `databases/.../ledger-integrity/journal_entries.sql`  
- `databases/.../ledger-integrity/journal_lines.sql`  
