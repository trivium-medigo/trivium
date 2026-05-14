# accounting-canonical-model

**Cross-module contract** for how **economic events** become **accounting events** and **journal templates**, before the **posting-engine** commits posted `journal_entries` / `journal_lines`.

## Purpose

- One vocabulary for: *what happened* → *which journal shape* → *which GL accounts and dimensions*.  
- Prevents parallel, incompatible definitions in finance-ops, payroll, spend, bank, and AI drafts.

## Event sources (non-exhaustive)

| Source | Canonical event examples | Downstream |
|--------|---------------------------|------------|
| **Stripe / subscription billing** | Invoice paid, refund, dispute, payout, fee, subscription period | Deferred revenue schedule, recognized revenue, cash, AR |
| **Revenue recognition** | Schedule line due, catch-up adjustment | Accrual journals via deterministic schedule engine |
| **Payroll runs** | Gross pay, withholding, employer tax, benefits, net pay | Payroll journal template → posting_batch |
| **Spend / card** | Card capture, expense report approval | Category-to-GL mapping → journal |
| **Bank** | Settled txn, fee, transfer | Bank GL mapping + reconciliation link |
| **Invoices / bills / payments** | AR invoice issued, AP bill approved, payment applied | Subledger + GL posting |
| **External providers** | QBO/Xero/NS line synced | `gl_account_external_mappings` + canonical event |

## Canonical events (foundation vocabulary)

Cross-team names for economic → accounting transitions (extend in code when implemented):

| Event | Typical source | Notes |
|-------|----------------|-------|
| `bill_received` | AP intake | Inbox / OCR / portal — draft only until validated |
| `bill_coded` | AP clerk / AI suggestion | Draft vs approved coding split on `bills.sql` |
| `bill_approved` | Approval policy | Unlocks payment readiness |
| `payment_scheduled` | Treasury / AP batch | Selection into `payments` run |
| `payment_initiated` | Bank rail / processor | Transmitted, not yet settled |
| `payment_settled` | Bank ack | Triggers posting-engine cash + AP/AR application |
| `payment_failed` | Bank / processor | Reversal or retry per policy |
| `credit_memo_created` | AR/AP credits | `credits.sql` — application to invoices/bills |
| `vendor_bank_details_changed` | Vendor master workflow | High-risk; human attestation + audit |
| `card_statement_closed` | Issuer feed | Statement period boundary |
| `card_payment_settled` | Bank / card program | Clears card liability GL |
| `project_cost_recorded` | Payroll / spend / procurement | Dimensions tie to `organization-graph/projects.sql` |

## Pipeline (mandatory order)

1. **Ingest** provider or internal event → **canonical event** record (type, amounts, ids, dimensions).  
2. **Map** event type → **journal template** (balanced lines, account roles, dimension slots) — deterministic rules + tables.  
3. **Validate** template against COA, period locks, basis (`ledger_id`).  
4. **posting-engine** creates **posted** `journal_entries` / `journal_lines` (or creates draft for human approval when policy requires).  
5. **AI** may propose a template or line edits **only** as draft payloads wired through `ai-accounting-drafts`; engine rejects invalid posts.

## AI boundary

Canonical model **never** trusts free-form model output as amounts. Suggestions carry **confidence** and **evidence** references; humans or rule engines accept or reject before posting-engine runs.

## Implementation note

This package (`src/`) will hold shared types, validators, and event↔template registries. Until then, this README is the **architectural source of truth** for cross-team alignment.

## References

- `docs/architecture/deterministic-accounting.md`  
- `docs/architecture/finance-accounting.md`  
- `docs/architecture/financial-reporting.md`  
