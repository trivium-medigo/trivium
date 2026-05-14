# posting-engine (API module)

**Authoritative deterministic validation and commit** for posted general ledger journals. This module is the **accounting truth gate** for posted state.

## Supremacy rule

**Only posting-engine** may:

- Transition `journal_entries.status` to **posted**.  
- Persist **posted** `journal_lines` that participate in trial balance and financial statements.  

APIs, workers, payroll, spend, bank sync, and AI must **call posting-engine** with validated payloads — they do not post GL directly.

## Lifecycle integration with AI drafts

1. AI or user creates a **draft** (`ai-accounting-drafts` or manual UI).  
2. Evidence + approvals satisfied per policy.  
3. **Posting-engine** runs: COA scope, `is_posting`, period locks, basis (`ledger.accounting_basis`), balance, currency, dimensions, idempotency.  
4. On success → **posted**; on failure → structured errors; no partial posted state.

## COA and period locks

Re-validates every invariant in `journal_lines.sql` and `journal_entries.sql` comments, including **book / ledger / entity** consistency and **period_locks**.

## References

- `docs/architecture/deterministic-accounting.md`  
- `docs/architecture/finance-accounting.md`  
- `packages/posting-engine-contracts/README.md`  
- `databases/.../ledger-integrity/journal_lines.sql`  
