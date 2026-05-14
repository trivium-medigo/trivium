# accounting-sync (API module)

Inbound/outbound synchronization with external accounting systems (stubs today).

## COA foundation

- **GL-specific provider mappings** → `databases/operational-db/schemas/accounting-sync/gl_account_external_mappings.sql`
- **Generic external ids** → `databases/operational-db/schemas/accounting-sync/external_ids.sql` (do not duplicate GL rows in both places)

See also: `docs/architecture/finance-accounting.md`.
