# finance-accounting (domain)

This document is the **bounded foundation spec** for the Chart of Accounts (COA) and closely coupled finance-accounting schemas in TRIVIUM. It is not implementation code.

## Goals

- **Book-scoped natural GL accounts** (`gl_accounts` — see `schemas/finance-accounting/chart_of_accounts.sql`).
- **Simple account codes** per `(tenant, book)`; segmented account numbers are explicitly **out of scope for v1** (may be added later without renaming core tables).
- **Dimensions are not COA**: departments, locations, projects, cost centers, classes, etc. live in **tracking categories** and **organization-graph** tables — see `tracking_categories.sql`.
- **Posting vs header** accounts: `is_posting = false` for summary/header rows; journal lines **must** target `is_posting = true` only.
- **Active/inactive** accounts retain history; hard deletes of posted accounts are **forbidden** by product rule.
- **System accounts** flagged on `gl_accounts`; **control pointers** (RE, suspense, FX, tax defaults, etc.) live in **`gl_book_settings.sql`** per book.

## Scope and ownership

| Concern | Owner (schema / module) |
|--------|-------------------------|
| Natural account master | `databases/.../finance-accounting/chart_of_accounts.sql` |
| Book-level control pointers | `databases/.../finance-accounting/gl_book_settings.sql` |
| Fiscal calendar + period locks | `fiscal_periods.sql`, `period_locks.sql` |
| Tax code default GL targets | `tax_codes.sql` |
| FX reference + revaluation runs | `fx_rates.sql`, `fx_revaluation_runs.sql` |
| Posted journals | `databases/.../ledger-integrity/journal_*.sql`, `ledgers.sql` |
| Accounting book anchor | `databases/.../organization-graph/books.sql` |
| Legal entity on journals | `databases/.../organization-graph/entities.sql` |
| Bank → cash GL | `databases/.../bank-connectivity/bank_account_gl_mapping.sql` |
| Provider account ↔ GL | `databases/.../accounting-sync/gl_account_external_mappings.sql` |
| Generic external ids | `accounting-sync/external_ids.sql` (non-COA-specific) |
| Audit trail for mutations | `databases/.../core/audit_log.sql` |

## Invariants (must hold after implementation)

1. **Book consistency**: `journal_lines.gl_account_id` → account where `gl_accounts.book_id = journal_entries.book_id` and same `tenant_id`.
2. **Posting only**: journal lines cannot reference accounts with `is_posting = false`.
3. **Period locks**: when `period_locks.lock_journal_posting` is set for a `(book, period)`, no new **posted** journals in that window. When `lock_coa_mutations` is set, **no COA or gl_book_settings** structural changes for that book/period (policy exactness TBD in migrations).
4. **Bank mapping**: automated bank posting uses `bank_account_gl_mapping` to resolve cash GL accounts.
5. **External sync**: provider account identifiers map through `gl_account_external_mappings` to `gl_accounts.id`.

## Dual-basis / parallel ledger (cash vs accrual)

TRIVIUM supports **both** cash-oriented and accrual-oriented financial truth **without duplicate or conflicting posted GL** by enforcing:

1. **Posted journals are always scoped to exactly one `ledger_id`**, and each ledger carries an **`accounting_basis`** (`accrual` | `cash`) — see `ledger-integrity/ledgers.sql`.
2. **Books** may declare a primary reporting basis and optional parallel cash ledger; see `organization-graph/books.sql`.
3. **Trial balance** is computed **per ledger** (thus per basis and period). Accrual TB and cash TB are separate artifacts when two ledgers exist; they are not merged in one TB without explicit reporting rules.
4. **Alternative**: a single accrual ledger plus **deterministic cash-basis reports** built from ledger + bank settlement data (no second posted ledger). That path is documented in `docs/architecture/financial-reporting.md`. Product chooses (A) parallel ledgers or (B) reporting view — not both silently.
5. **AI does not choose basis**; configuration and posting-engine do.

Cross-references: `docs/architecture/deterministic-accounting.md`, `docs/architecture/financial-reporting.md`.

## Validation layers (combined approach)

- **Database**: FKs, uniqueness, CHECKs where safe (e.g. non-negative line numbers).
- **API** (`apps/api/.../finance-accounting`, `ledger-integrity`): fast user-facing validation, import pre-checks.
- **Posting-engine** (`apps/api/.../posting-engine`, `services/posting-engine-service`): authoritative re-check before post; must match API rules.

## Security (RLS / tenancy)

- Every COA and ledger row carries **`tenant_id`** (and `book_id` where applicable).
- Row-level security attaches **`tenant_id = current_setting('app.tenant_id')`** (or equivalent) in migrations — coordinated with **identity-governance** and API middleware.
- Sensitive audit payloads may be redacted per compliance policy.

## Explicitly deferred (not in v1 foundation tree)

- Segmented account definition tables, statistical accounts, BC-style total rows in COA, posting setup matrix tables, COA approval workflow tables, dedicated COA event store (beyond `audit_log`), book-to-book COA mapping tables, COA import staging tables.

## References

- Platform tree: `docs/architecture/PLATFORM_TREE.md`
- Manifest: `docs/architecture/platform_tree_manifest.json`
