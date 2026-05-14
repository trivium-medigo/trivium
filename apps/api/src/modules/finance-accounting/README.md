# finance-accounting (API module)

Bounded **Chart of Accounts** and finance-accounting HTTP surface (stubs today).

## Foundation spec

See **`docs/architecture/finance-accounting.md`** and SQL specs under:

- `databases/operational-db/schemas/finance-accounting/`

## Responsibilities (when implemented)

- CRUD for `gl_accounts` (book-scoped), validation of codes, hierarchy, `is_posting`, inactive rules.
- Read/update `gl_book_settings` control pointers (privileged).
- Coordinate with **period_locks** for COA mutation freeze during close.
- Emit **audit_log** entries on every COA change (before/after payload).

## Non-responsibilities

- Final posting of journals → **posting-engine** + **ledger-integrity**.
- Provider sync workers → **accounting-sync** service/workers.
