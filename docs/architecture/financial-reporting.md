# Financial reporting (architecture)

How TRIVIUM produces **financial statements** and **management reporting** without making AI the source of reporting truth.

## Data flow (deterministic)

1. **Chart of accounts** (`gl_accounts`) supplies classification (type, hierarchy, posting flags).  
2. **Posted journal lines** (`ledger-integrity/journal_lines.sql`) are the only inputs to official aggregates.  
3. **Trial balance** (`trial_balance_snapshots.sql` or compute-from-lines) rolls debits/credits **per ledger, period, currency** — see dual-basis rules in `finance-accounting.md` and `ledgers.sql`.  
4. **P&L, balance sheet, cash flow** are **projections** of TB + COA structure + basis rules — not free-form AI tables.  
5. **Retained earnings** close uses `retained_earnings_rollforward.sql` + close journals from `finance-close` + RE account pointer in `gl_book_settings.sql`.

## Cash vs accrual reporting

- If **two ledgers** exist (accrual + cash), each has its own TB and statement pipeline.  
- If **one accrual ledger** + cash-basis **reports**, cash statements use **deterministic rules** (e.g. cash-basis revenue when cash received) applied in **analytics/warehouse** or a reporting engine — documented formulas, versioned, testable — **not** LLM-generated numbers.

## Management reporting & founder metrics

- **Burn, runway, cash flow, ARR/MRR**: sourced from **deterministic** inputs — ledger cash balances, committed expenses, subscription facts (`commercial-lifecycle` / billing events), and warehouse facts in `analytics/`.  
- **AI** may narrate or drill-down; **metrics definitions** live in code + warehouse models, not chat transcripts.

## OLTP ledger vs analytics / warehouse

| Role | Location |
|------|----------|
| **System of record** | `ledger-integrity` + `posting-engine` |
| **Heavy aggregates, cohort metrics, long-range trends** | `analytics/`, `analytics/warehouse-models`, pipelines |
| **Near-real-time dashboards** | May read materialized TB snapshots + operational tables |

Warehouse **must not** become authoritative over the ledger for the same period without an explicit **reconciliation** process to posted GL.

## AI boundary

**Do not** create financial statement truth from AI summaries. AI outputs may be labeled **narrative** or **draft schedules** until validated against TB and posting rules.

## References

- `docs/architecture/deterministic-accounting.md`  
- `docs/architecture/finance-accounting.md`  
- `docs/architecture/dashboard-and-metrics.md` — role dashboards, KPI catalog, metric lineage, RLS, AI boundaries  
- `docs/architecture/cash-liquidity-forecasting.md` — deterministic cash / liquidity forecast and runway inputs  
- `docs/architecture/treasury-debt-credit.md` — phase-2 treasury, debt, and credit facilities scope  
- `docs/architecture/ap-payment-automation.md` — BILL.com–class AP intake, approvals, and payment rails (non-AI truth)  
- `docs/architecture/fixed-assets-leases.md` — phase-2 fixed assets and lease accounting scope (no v1 production schema)  
- `packages/charting/README.md` (presentation layer)  
