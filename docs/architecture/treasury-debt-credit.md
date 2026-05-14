# Treasury, debt, and credit facilities (architecture — **phase 2** default)

This document **scopes** treasury, **term debt**, **credit facilities**, **loans**, **covenants**, **interest accrual**, and **liquidity planning** so teams do **not** invent shadow tables during v1.

## v1 (in scope today)

- **Bank accounts**, **balances**, **feeds**, **reconciliation** — `bank-connectivity`, `bank-reconciliation`, `bank_account_gl_mapping.sql`.  
- **Cash visibility** and **AP/AR-driven cash impact** — `finance-operations`, `cash-liquidity-forecasting.md`.  
- **Corporate cards** as liabilities + statement cycles — `spend-travel/card_transactions.sql` spec.  
- **Customer credit limits** and **collections** — `customer_credit_limits.sql`, `dunning.sql`, `customer_health_scores.sql`.

## Deferred to phase 2 (unless product scope changes)

- **Loan notes**, **credit facilities**, **draw/repay**, **amortization schedules**, **covenant tests**, **interest capitalization** — candidate tables: `debt_facilities.sql`, `covenant_tests.sql` (**not added** in v1).  
- **Treasury workstation** features (investment sweep, intercompany funding) — future `finance-treasury` domain discussion only.

## CFO dashboards

CFO tiles that depend on **debt/covenants** must display **explicit “phase 2”** placeholders or derive only from **v1** bank + AP/AR + payroll per `dashboard-and-metrics.md`.

## Connections

- **Ledger / COA**: `ledger-integrity`, `finance-accounting`, `gl_book_settings.sql`.  
- **Analytics**: `analytics/warehouse-models`, `metric-catalog.md`.  
- **Reporting**: `financial-reporting.md`, `dashboard-and-metrics.md`.

## Rule

**No** debt/covenant production DDL outside a future approved migration set referenced here — prevents fragmentation.
