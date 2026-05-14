# Metric catalog (foundation)

Each metric lists **source domains**, **deterministic formula owner**, **AI role** (explain only), and **RLS sensitivity** (public / internal / restricted / highly_restricted). Official numbers for board/investor packs **must** come from **versioned** warehouse models + ledger reconciliation per `metric-lineage.md`.

| Metric | Source domains | Formula owner | AI role | RLS |
|--------|------------------|---------------|---------|-----|
| **Cash** | `bank-connectivity`, `ledger-integrity` (cash accounts) | Treasury/cash engine + posting-engine | Explain drivers | restricted |
| **Burn** | `ledger-integrity`, `finance-operations`, `spend-travel`, `payroll-benefits` | Finance analytics (warehouse) | Narrate | internal |
| **Runway** | Cash + burn inputs | Finance analytics | Scenario narration | restricted |
| **ARR** | `commercial-lifecycle`, contracts, `revenue_recognition` | Rev-rec engine + warehouse | None for value | restricted |
| **MRR** | Subscription facts + billing events | Rev-rec + warehouse | None for value | restricted |
| **Revenue** | Posted GL + rev-rec schedules | posting-engine + warehouse | Explain | internal |
| **Gross margin** | Revenue + COGS from GL | Warehouse from TB | Explain | internal |
| **EBITDA / Adj EBITDA** | GL mapping policy | Finance (warehouse rules) | Must label adjustments | restricted |
| **CAC / LTV** | CRM/commercial + finance (placeholder) | Growth analytics (phase) | Assist hypotheses only | internal |
| **AR aging / DSO** | `invoices.sql`, payments, GL | AR subledger + warehouse | Collections suggest | internal |
| **AP aging / DPO** | `bills.sql`, `payments.sql` | AP subledger + warehouse | None for value | internal |
| **Cash conversion cycle** | AR + AP + inventory (if any) | Warehouse | Explain | internal |
| **Payroll cost by dimension** | `payroll_runs`, `project_assignments`, org graph | Payroll engine + warehouse | Anomaly flags | **highly_restricted** |
| **Headcount** | `workforce` | HR analytics | None for value | internal |
| **Attrition** | `workforce` | HR analytics | Benchmark narrative | internal |
| **Hiring pipeline** | `workforce`/recruiting (if implemented) | HR | Forecast assist only | internal |
| **Benefits cost** | `payroll-benefits/benefits_enrollments` | Payroll + warehouse | None for value | highly_restricted |
| **Spend by dept/project/vendor** | `spend-travel`, `procurement-spend`, `projects` | Warehouse | Explain | internal |
| **Corporate card liability** | `card_transactions`, GL | Spend + GL | None for value | restricted |
| **Debt / covenant metrics** | **Phase 2** — `treasury-debt-credit.md` | Future treasury engine | N/A until enabled | highly_restricted |
| **Project profitability / ROI** | `projects`, `journal_lines` dimensions, subledgers | Warehouse + finance | Explain | internal |

## Rules

- **AI** never authors official metric values for **restricted** or **highly_restricted** metrics.  
- **Versioning**: each metric has `metric_version` in warehouse docs (`metric-lineage.md`).  
- **Reconciliation**: financial metrics tie to **TB** each close.

## References

- `docs/architecture/dashboard-and-metrics.md`  
- `analytics/warehouse-models/metric-lineage.md`  
- `analytics/dashboards/dashboard-catalog.md`  
