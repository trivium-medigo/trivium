# object-storage

Tenant-scoped object storage for **evidence and documents** that support finance, payroll, tax, and audit. Blobs are **not** the general ledger; amounts and posted state remain in `ledger-integrity` via the posting-engine.

## Typical object categories

| Category | Examples | Notes |
|----------|-----------|-------|
| **AP invoices** | Vendor invoice PDFs, XML, images | Immutable after legal hold; prefix contract |
| **Receipts** | Employee receipts, card images | Linked to spend / card lines |
| **Remittance advice** | ACH/wire remittance PDFs | Evidence for `payments` settlement |
| **Payment confirmation** | Processor receipts, bank confirmations | Pairs with bank acknowledgements |
| **Bank acknowledgements** | Settlement files, MT940 extracts | Reconciliation inputs |
| **Tax forms** | W-9, W-8, withholding certificates | PII/TIN handling per security architecture |
| **Board / investor packs** | Published decks (narrative) | Must not replace deterministic metrics source |

## Retention and legal hold

Align with `docs/architecture/dsar-retention-legal-hold.md` and compliance retention policies: objects under hold are **not** deleted or overwritten; lifecycle transitions are auditable.

## References

- `object-storage/tenant-prefix-contract.md`  
- `docs/architecture/ap-payment-automation.md`  
- `databases/operational-db/schemas/finance-operations/bills.sql`  
