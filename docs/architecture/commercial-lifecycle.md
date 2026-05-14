# commercial-lifecycle (architecture)

Quotes, contracts, orders, renewals, and **subscription economic truth** that feed finance.

## Relationship to revenue recognition

- **Billing provider payloads (e.g. Stripe)** are **ingestion sources**, not the ledger.  
- **Canonical events** (subscription created, period service, upgrade, churn) flow through `packages/accounting-canonical-model` into **revenue recognition schedules** and then **posting-engine** journals.  
- **Deferred revenue** and **recognized revenue** journals are **deterministic** from schedules + contract dates — see `databases/.../finance-operations/revenue_recognition.sql`.

## Stripe / SaaS

- Reconcile **Stripe balance transactions** (charges, refunds, fees, payouts, disputes) to **AR, cash, deferred revenue, revenue, fees** using mapping rules — never assume “Stripe revenue = recognized revenue.”  
- **ARR/MRR**: computed from subscription/contract tables and recognized patterns, documented in `docs/architecture/financial-reporting.md` for management metrics.

## AI boundary

AI may draft contract summaries or anomaly flags; **commercial terms** that affect revenue are human-approved or system-ingested structured data.

## References

- `docs/architecture/deterministic-accounting.md`  
- `docs/architecture/financial-reporting.md`  
- `packages/accounting-canonical-model/README.md`  
