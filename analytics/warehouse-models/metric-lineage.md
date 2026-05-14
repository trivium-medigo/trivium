# Metric lineage and warehouse ownership

## Source-of-truth hierarchy

1. **Posted general ledger** (`ledger-integrity` + `posting-engine`) — authoritative for financial statement numbers.  
2. **Subledgers** (AP, AR, payroll, inventory when present) — authoritative for open balances feeding forecasts.  
3. **Warehouse models** (`analytics/warehouse-models`, pipelines) — **derived**; must reconcile to (1)+(2) each period.  
4. **Dashboards** — read from (3) with documented **refresh cadence**; never bypass (1) for official numbers.

## Lineage

- Each warehouse fact documents: **upstream table**, **transform version**, **business key**, **reconciliation checkpoint**.  
- **Metric versioning**: breaking formula changes bump `metric_version` (see `metric-catalog.md`).

## Tests

- dbt/SQL tests (future) assert **TB = sum(lines)**, **AR aging = subledger**, etc.

## Board / investor controls

- Published packs are **immutable snapshots** with audit who published (`audit_log`).  
- **No AI-generated official metrics** in packs.

## Reconciliation

- Monthly: warehouse financial facts ↔ **TB snapshot** per book/period.  
- Discrepancies block “publish” flag on investor dashboard tiles.

## Phase-2

Persisted `metric_definitions.sql` in OLTP **not** required for v1 — definitions live in repo + warehouse until governance requires DB registry.

## References

- `docs/architecture/dashboard-and-metrics.md`  
- `docs/architecture/deterministic-accounting.md`  
- `docs/architecture/financial-reporting.md`  
