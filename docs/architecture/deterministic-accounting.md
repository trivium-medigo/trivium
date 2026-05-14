# Deterministic accounting (architecture)

This document defines **who owns accounting truth** in TRIVIUM. It is policy, not implementation code.

## Principle

**AI does not calculate accounting truth.** AI may draft, explain, classify, suggest, summarize, and prepare work. **Deterministic backend systems** — schemas, constraints, posting-engine rules, reconciliation engines, approved calculation modules, and audit trails — own **final numbers** that hit the general ledger and regulatory reporting.

## Ownership matrix

| Domain | Deterministic owner | AI role (non-authoritative) |
|--------|---------------------|-----------------------------|
| **Posting engine** | Validates and commits posted `journal_entries` / `journal_lines`; enforces period locks, basis, COA scope, balanced entries | May propose draft lines; never writes `posted` without engine |
| **Trial balance** | Aggregates posted lines per ledger/period/currency | May explain variances; does not compute official TB |
| **Retained earnings** | Close journals and rollforward via `ledger-integrity` + `finance-close` + `gl_book_settings` RE pointer | May summarize close checklist |
| **Period locks** | `finance-accounting/period_locks.sql` + posting-engine enforcement | Never bypasses locks |
| **Payroll journals** | Payroll engine builds **journal templates** from rates/rules; posting-engine posts | Classifies earning types only if rules delegate; never final liability amounts without rules |
| **Tax calculations** | Tax engine / `tax_codes` + statutory tables + posting-engine | Suggests codes; does not remit or file |
| **FX revaluation** | `fx_rates` + revaluation run + GL accounts from `gl_book_settings` | None for rates |
| **Revenue recognition** | Schedules and amortization from subscription/contract facts → journals via canonical model | None for recognized revenue amounts |
| **Bank reconciliation** | Matching engine + bank GL mapping; explainability data | May suggest match candidates below confidence threshold with human confirm |
| **Spend / card posting** | Category-to-GL mapping rules + approvals + posting-engine | Suggests category; mapping table wins |
| **AI accounting drafts** | `ai-accounting-drafts` produces **draft** payloads only until approval | Source of suggestions, not ledger |
| **Audit and approvals** | `core/audit_log`, `approval-policy-engine`, identity policies | Logs prompts; does not replace audit |

## Posting-engine supremacy for posted state

Only the **posting-engine** path may transition journals to **posted** and persist **posted** `journal_lines`. APIs, workers, and AI services call posting-engine; they do not write posted GL directly.

## Explicit AI prohibitions (official numbers and money movement)

The following actions are **out of scope** for autonomous AI in TRIVIUM. AI may assist with drafts, extraction, narration, and low-risk suggestions per module policy; **policy gates and deterministic owners** hold authority.

- **AI cannot approve payments** (AP batches, payroll funding, card settlements, or customer refunds).  
- **AI cannot execute** ACH, wire, check, virtual card, or card network payments.  
- **AI cannot change vendor bank details** or other payee instructions; human or controlled workflow with audit is required.  
- **AI cannot calculate official dashboard KPIs** or publish versioned metric definitions — see `analytics/metrics/metric-catalog.md` and `analytics/warehouse-models/metric-lineage.md`.  
- **AI cannot create official board or investor reporting numbers**; published packs reconcile to posted GL / warehouse models with human attestation.

See also `docs/architecture/dashboard-and-metrics.md`, `docs/architecture/ap-payment-automation.md`, and `apps/api/src/modules/ai-accounting-drafts/README.md`.

## Cross-references

- `docs/architecture/finance-accounting.md` — COA, basis, locks  
- `docs/architecture/financial-reporting.md` — TB → statements  
- `packages/accounting-canonical-model/README.md` — event → journal template  
- `apps/api/src/modules/posting-engine/README.md` — module contract  
