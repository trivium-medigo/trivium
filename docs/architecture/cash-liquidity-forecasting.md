# Cash and liquidity forecasting (architecture)

Deterministic **cash forecast**, **liquidity**, **runway**, and **scenario** planning — distinct from **cash-basis financial reporting** (see `finance-accounting.md` / `financial-reporting.md`).

## Sources (inputs)

| Source | Path / domain |
|--------|----------------|
| Bank balances / transactions | `bank-connectivity`, `bank-reconciliation` |
| Open AP | `finance-operations/bills.sql`, `payments.sql` |
| Open AR | `finance-operations/invoices.sql`, `payment_links.sql` |
| Payroll | `payroll-benefits/payroll_runs.sql` |
| Recurring obligations | `finance-operations/recurring_bills.sql` (and similar) |
| Revenue timing | `revenue_recognition.sql`, `commercial-lifecycle` |
| Spend / cards | `spend-travel/card_transactions.sql` |
| **Debt service (phase 2)** | `treasury-debt-credit.md` — excluded from v1 default formulas unless enabled |

## Deterministic ownership

- **Forecast engine** (future service) computes cash positions from **subledger + known schedules**; outputs are **versioned** (scenario A/B, week granularity).  
- **AI** explains drivers and sensitivity; **does not invent** inflows/outflows.

## Cash forecast vs cash-basis reporting

- **Cash-basis reports** restate **recognized** activity per policy.  
- **Cash forecast** projects **future** settlements — may include **unposted** approved bills/payroll — clearly labeled **forecast**, not GAAP statements.

## Dashboard integration

- Surfaces under **CFO / Founder** dashboards per `analytics/dashboards/dashboard-catalog.md`.  
- Must reconcile back to **bank actuals** when dates pass.

## Phase-2 tables (not added now)

`cash_forecast_scenarios.sql`, persisted forecast lines — optional when product requires multi-scenario storage.

## References

- `docs/architecture/dashboard-and-metrics.md`  
- `docs/architecture/treasury-debt-credit.md`  
- `docs/architecture/deterministic-accounting.md`  
