# Dashboards and metrics (architecture)

Central policy for **role dashboards**, **KPI catalog**, **metric formula ownership**, **deterministic lineage**, **RLS**, **AI boundaries**, and **data sources** connecting accounting, finance, HR, payroll, spend, treasury (phase 2), and analytics.

## Core principles

1. **Dashboards are deterministic projections** of versioned metrics and ledger/subledger facts — **not** AI-generated truth.  
2. **Metric catalog** definitions live under `analytics/metrics/` (`metric-catalog.md`) and **`analytics/warehouse-models/`** (`metric-lineage.md`) with **code-owned formulas** and tests.  
3. **Financial metrics** ultimately reconcile to **`ledger-integrity`** + **`posting-engine`** + trial balance / subledgers.  
4. **HR / payroll metrics** derive from **`workforce`**, **`payroll-benefits`**, benefits — with strict RLS.  
5. **Spend metrics** derive from **`procurement-spend`**, **`spend-travel`**, **`finance-operations`** (bills/payments).  
6. **AI** (`ai-copilot`, `ai-accounting-drafts`) may **explain, narrate, drill-down, and suggest** — never compute **official** published KPIs, board numbers, or payment decisions. See `deterministic-accounting.md`.

## Role-based dashboard catalog

Authoritative list: **`analytics/dashboards/dashboard-catalog.md`**. Each entry names primary user, widgets, sources, formula owner, AI role, RLS, drilldown, and app route.

## RLS and permissions

High-level matrix: **`policies/dashboard-access.md`**. Implementation spans **`identity-governance`**, **`databases/operational-db/rls/`**, and **`policies/opa/`**.

## Metric lineage and versioning

See **`analytics/warehouse-models/metric-lineage.md`**: source-of-truth hierarchy, ledger → warehouse, metric versioning, reconciliation to GL, refresh cadence, board/investor controls.

## Dashboard freshness

- Near-real-time tiles may read **materialized** aggregates or operational queries with documented **SLA** and **stale-if** rules.  
- **No** silent overwrite of period-close numbers without audit trail (`core/audit_log.sql`).

## Cross-references

- `docs/architecture/financial-reporting.md`  
- `docs/architecture/cash-liquidity-forecasting.md`  
- `docs/architecture/treasury-debt-credit.md` (phase 2)  
- `docs/architecture/ap-payment-automation.md`  
- `docs/architecture/fixed-assets-leases.md` (phase 2)  
- `databases/.../organization-graph/projects.sql`  

## Phase-2 candidates (not in tree as production tables yet)

`metric_definitions.sql`, `dashboard_tiles.sql`, `cash_forecast_scenarios.sql` — see `metric-lineage.md` and `cash-liquidity-forecasting.md`.
