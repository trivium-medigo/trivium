# analytics

**Analytics is not the source of accounting truth.** Posted GL, subledgers, and operational facts owned by product domains feed pipelines and warehouse models here.

- **Metrics reconcile** to deterministic owners: ledger / TB, payroll engine outputs, procurement facts, and versioned warehouse definitions (`analytics/warehouse-models/metric-lineage.md`).  
- **Metric catalog** (`analytics/metrics/metric-catalog.md`) and **dashboard catalog** (`analytics/dashboards/dashboard-catalog.md`) own human-readable definitions, formula ownership, and AI role boundaries.  
- Dashboards consume projections from warehouse models; charting is visualization-only (`packages/charting/README.md`).

## References

- `docs/architecture/dashboard-and-metrics.md`  
- `docs/architecture/financial-reporting.md`  
- `docs/architecture/deterministic-accounting.md`  
