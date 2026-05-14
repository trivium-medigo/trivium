# Tenant prefix contract (object storage)

Canonical **key prefixes** for multi-tenant isolation and lifecycle automation. Actual bucket layout may vary by cloud; paths below are logical.

| Prefix pattern | Contents |
|----------------|----------|
| `{tenant}/ap/invoices/` | Vendor invoice PDFs and intake artifacts |
| `{tenant}/ap/attachments/` | Supporting docs for bills and approvals |
| `{tenant}/ar/receipts/` | Customer remittance and payment confirmations |
| `{tenant}/tax/vendor/` | W-9, W-8, withholding forms (vendor) |
| `{tenant}/tax/payroll/` | Payroll tax filings evidence (phase-2 integrations) |
| `{tenant}/payments/confirmations/` | ACH/wire/card settlement confirmations |
| `{tenant}/payments/remittance/` | Remittance advice |
| `{tenant}/bank/acknowledgements/` | Bank feed ack files and statements |
| `{tenant}/cards/statements/` | Corporate card statement PDFs / issuer exports |
| `{tenant}/payroll/evidence/` | Registers, third-party pay stubs exports (sensitive) |
| `{tenant}/board/packs/` | Published investor/board materials (RLS restricted) |

Prefixes are **not** authorization: enforce RLS and signed URLs per `policies/access-control.md` and `identity-governance`.
