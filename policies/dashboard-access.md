# Dashboard and metric access (policy)

Role-to-dashboard and role-to-metric visibility. **Enforcement** spans `identity-governance`, `databases/operational-db/rls/*`, and `policies/opa/*` (extend Rego bundles as implementation proceeds).

## Roles (minimum set)

| Role | Dashboards (see `analytics/dashboards/dashboard-catalog.md`) | Sensitive metrics |
|------|------------------------------------------------------------------|---------------------|
| CEO / Founder | Executive, high-level CFO (non-payroll detail) | Cash, runway; **no** individual payroll |
| CFO | Executive, CFO liquidity, board (publish) | All except raw PII; debt **phase 2** |
| Controller | Close, GL production, AI review | GL, recon |
| Accountant | GL production, AP/AR as assigned | Operational GL |
| HR admin | HR health | **No** individual compensation unless HRBP |
| Payroll admin | Payroll ops | Payroll PII — **highly restricted** |
| Dept manager | Dept budget | Own dept only |
| AP manager | AP command | Vendor bank **masked** until dual control |
| AR manager | AR collections | Customer exposure |
| Spend admin | Spend & cards | Card programs |
| Investor / board | Board pack | Published snapshots only |
| Integration ops | Sync health | Technical, no GL edit |
| AI reviewer | AI review queue | Draft payloads, not live payroll PII |

## Sensitive classes

- **Payroll / salary / individual benefits** — highly_restricted.  
- **Cash and runway** — restricted (competitive).  
- **Debt / covenants** — highly_restricted when phase 2 exists.  
- **Vendor bank details** — dual control + masked display.  
- **Customer concentration** — restricted for non-exec roles.

## AI services

AI roles **read** via same RLS as user; **no** service account bypass for tenant production data without break-glass policy.

## References

- `docs/architecture/dashboard-and-metrics.md`  
- `docs/architecture/rls-enforcement-matrix.md` (if present)  
- `identity-governance`  
