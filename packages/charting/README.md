# charting

**Visualization only** — charts, graphs, and layout components for web and other surfaces.

- **No calculation truth**: charting does not own formulas, KPI definitions, or ledger numbers. It **consumes metrics** already computed in `analytics/` warehouse models or API projections that enforce deterministic definitions.  
- **Dashboard RLS awareness**: callers must pass scoped datasets or use APIs that apply tenant and role filters per `policies/dashboard-access.md` and session context variables — charting widgets must not bypass permission checks.

## References

- `docs/architecture/dashboard-and-metrics.md`  
- `analytics/dashboards/dashboard-catalog.md`  
- `analytics/metrics/metric-catalog.md`  
