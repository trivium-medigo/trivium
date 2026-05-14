# payroll-benefits (API module)

Payroll, benefits, EOR, and related **deterministic** financial flows.

## GL contract

- **`payroll_run` → journal template → `posting_batch` → `journal_entries` / `journal_lines`** — only **posting-engine** commits posted lines.  
- Liabilities (tax withholding, benefits payable, garnishments), employer taxes, clearing accounts, and expense lines are defined by **rules + COA mappings** (`gl_book_settings` defaults where applicable).  
- **HR/workforce** data supplies **dimensions** (department, cost center, location); see `workforce/compensation.sql` and `payroll_runs.sql` specs.

## Reimbursements

Expense reimbursements through payroll vs AP must follow **one canonical path** per tenant policy (document in `packages/accounting-canonical-model` when codified) so the same receipt is not double-posted.

## Offboarding

Final pay and benefit revocations flow through payroll runs with audit trail; access revocation is `offboarding_revocations` schema — still **posting-engine** for money impact.

## References

- `docs/architecture/deterministic-accounting.md`  
- `databases/.../payroll-benefits/payroll_runs.sql`  
- `apps/api/src/modules/posting-engine/README.md`  
