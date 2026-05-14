# ledger-integrity (API module)

Journal and ledger **system of record** API (stubs today).

## COA-related contract

- `journal_entries` carries **`book_id`**, **`ledger_id`**, **`entity_id`**, fiscal period, currency, status.
- `journal_lines` carries **`gl_account_id`** and dimension references.
- All scope invariants are documented in:

  - `databases/operational-db/schemas/ledger-integrity/journal_entries.sql`
  - `databases/operational-db/schemas/ledger-integrity/journal_lines.sql`

Posting-engine is the last line of defense before commit; this module owns persistence shape and queries.
