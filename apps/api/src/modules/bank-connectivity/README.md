# bank-connectivity (API module)

Bank connections, accounts, and transaction ingestion (stubs today).

## COA foundation

Cash posting targets bank-specific GL accounts via:

- `databases/operational-db/schemas/bank-connectivity/bank_account_gl_mapping.sql`

See `docs/architecture/finance-accounting.md` for invariants with `gl_accounts`.
