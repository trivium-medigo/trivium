# Dashboard catalog (role-based)

Each row: **primary user**, **metrics/widgets**, **source domains**, **deterministic owner**, **AI role**, **RLS**, **drilldown**, **related route/package**.

| Dashboard | Primary user | Metrics / widgets | Source domains | Deterministic owner | AI role | RLS | Drilldown | Route / package |
|-----------|--------------|-------------------|----------------|---------------------|---------|-----|-----------|-----------------|
| Executive pulse | Founder / CEO | Cash, runway, burn, ARR | Bank, ledger, commercial, warehouse | Warehouse + GL | Narrate | restricted | TB, cash detail | `apps/web/(shell)/dashboard` |
| CFO liquidity | CFO | Cash forecast, AP aging, card liability | AP, bank, spend, forecast doc | Cash forecast engine (future) | Explain | restricted | Bills, payments | `analytics/dashboards` |
| Controller close | Controller | Close tasks, locks, TB tie-out | `finance-close`, `period_locks`, GL | Close + posting-engine | Summarize | internal | Journals | `finance-close` |
| GL production | Accountant | JE queue, recon exceptions | `ledger-integrity`, `bank-reconciliation` | posting-engine | Draft categorize | internal | `journal_lines` | `ledger-integrity` API |
| HR health | HR admin | HC, attrition, pipeline | `workforce` | HR analytics | Benchmark story | internal | Employee record | `workforce` |
| Payroll ops | Payroll admin | Run status, liabilities, tax | `payroll-benefits` | Payroll engine | Anomaly flags | **highly_restricted** | Payroll lines | `payroll-benefits` |
| Dept budget | Dept manager | Budget vs actual | `budgets.sql`, GL | Warehouse | Variance explain | internal | GL by CC | `procurement-spend` |
| AP command | AP manager | Inbox, aging, payment batch | `bills`, `payments`, approvals | AP + posting-engine | Suggest coding | internal | Vendor, bill | `finance-operations` |
| AR collections | AR manager | Aging, dunning, payment links | `invoices`, `dunning`, `payment_links` | AR subledger | Prioritize | internal | Invoice | `customer-portal` |
| Spend & cards | Spend admin | Policy breaches, stmt close | `spend-travel`, policies | Spend engine | Merchant suggest | restricted | Card txn | `spend-travel` |
| Board / investor | Board | Pack KPIs | Warehouse + GL | Board pack builder | Narrative only | **highly_restricted** | TB | `firm-portal` |
| Sync health | Integration ops | DLQ, lag, errors | `outbound-sync`, workers | Ops SLO | Summarize | internal | Sync run | `integrations-platform` |
| AI review queue | Controller + AI ops | Draft confidence | `ai-accounting-drafts`, approvals | Humans | Suggest fix | internal | Evidence | `ai-accounting-drafts` |

## References

- `docs/architecture/dashboard-and-metrics.md`  
- `policies/dashboard-access.md`  
- `analytics/metrics/metric-catalog.md`  
