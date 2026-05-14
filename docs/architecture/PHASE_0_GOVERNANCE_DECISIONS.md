# Phase 0 governance decisions (binding)

This document captures **completed** decisions from `docs/architecture/IMPLEMENTATION_EXECUTION_PLAN.md` — **Phase 0, Steps 1–10** — so implementation prompts reference **repository state**, not chat history alone.

**Authority:** These rules are **binding** for TRIVIUM until changed through a **deliberate architecture update** per the execution plan preamble. Deviations require **explicit approval** before implementation.

---

## Step 1 — Non-negotiable architecture sources

The following paths are **binding architecture** for TRIVIUM (same list as **Phase 0, Step 1** in `IMPLEMENTATION_EXECUTION_PLAN.md`):

- `docs/architecture/deterministic-accounting.md`
- `docs/architecture/finance-accounting.md`
- `docs/architecture/ledger-integrity.md`
- `docs/architecture/financial-reporting.md`
- `docs/architecture/dashboard-and-metrics.md`
- `docs/architecture/ap-payment-automation.md`
- `packages/accounting-canonical-model/README.md`
- `apps/api/src/modules/posting-engine/README.md` (where non-placeholder; when still placeholder, treat the README as the **module contract** intent until code exists)

All future design and implementation **must obey** these documents unless an **explicit, approved** architecture change updates them first. **Implementation prompts** must **open and follow** the subset relevant to the task (posting, RLS, metrics, AP, etc.); “chat-only” summaries do **not** replace reading the sources.

---

## Step 2 — Posting-engine supremacy and AI boundaries

- **Posting-engine supremacy:** **Only** the **posting-engine** path may transition `journal_entries` to **`posted`** and persist **`posted`** `journal_lines` that feed trial balance and reporting. APIs, workers, domain services, and AI **call** posting-engine; they **do not** write posted GL directly.
- **AI boundaries:** AI (and similar non-deterministic assistants) **must not**: **post** journals to posted state, **approve** payments or pay runs, **execute** pay (ACH, wire, check, card), **change vendor or payee bank details**, or **own official KPIs**, board metrics, or regulatory-facing numbers. **Deterministic systems** — schemas, constraints, posting-engine rules, reconciliation and calculation modules where specified, and **audit trails** — own **authoritative accounting truth** aligned with `deterministic-accounting.md` and `dashboard-and-metrics.md`.

---

## Step 3 — Repository inventory truth

- **Tree and specs:** `docs/architecture/PLATFORM_TREE.md`, `platform_tree_manifest.json`, and SQL under `databases/operational-db/` (with architecture docs) describe the **intended** platform shape.
- **Runnable product:** Apps, services, workers, and most packages are **largely placeholder** (empty stubs, headers, or non-wired configs) until later phases; do not assume production behavior from folder presence alone.
- **Root workspace:** Root `package.json`, `pnpm-workspace.yaml`, `turbo.json`, and related **tooling** are **not yet** a complete real monorepo bootstrap; treat them as **intent** until **Phase 1** hardens them.
- **Clearly runnable today:** Validator and tree scripts (e.g. `python scripts/validate_platform_tree.py`, `python scripts/create_physical_tree.py`) are the main **reliable** automation surface in early Phase 1.
- **Phase 1 entry:** Work begins at **Phase 1 / Step 11** with **workspace and tooling** (install, lint, typecheck gate); **not** with product features ahead of **Validation gate 1** (`IMPLEMENTATION_EXECUTION_PLAN.md`).

---

## Step 4 — MVP tenancy boundary

- **Multi-tenant SaaS from day one** at **database, API, and security** layers: **`tenant_id`**, **RLS**, **session / tenant context** (e.g. GUC or equivalent), **tenant-scoped audit** and **idempotency**, **tenant-scoped workers**, **tenant-scoped object-storage keys and URLs**, and **tenant-safe AI retrieval** (vector / RAG boundaries must not leak cross-tenant facts).
- **First rollout mode:** **Internal dogfood only** is an **operational** constraint, **not** a license for single-tenant shortcuts in ledger, bank, payroll, payments, or shared core paths.

---

## Step 5 — Operational database product and pin

- **v1 OLTP / ledger system of record:** **PostgreSQL 18** only for operational ledger truth. **SQLite**, **document databases**, and similar stores are **not** authoritative GL or migration history for **`operational-db`**.
- **Local and CI image pin:** **`postgres:18.3`** unless changed by **approved policy** (record the change in architecture governance).
- **Why PostgreSQL:** **RLS** for tenant isolation, **ACID transactions**, **constraints and FK integrity**, and mature ops patterns required for financial system-of-record workloads.

---

## Step 6 — Migration tool

- **Tool:** **Flyway** is the **sole** migration tool for the operational PostgreSQL database; migrations are **SQL-first** (versioned and repeatable SQL under Flyway conventions).
- **Forbidden:** Mixing migration tools over time; **ORM-generated** or ORM-owned schema as **source of truth** for **`operational-db`**; **hand-run `psql` scripts** (or one-off DBA patches) as **authoritative** DDL history — any durable change belongs in a **new** Flyway file per Step 7.

---

## Step 7 — Migration naming and versioning

- **Versioned migrations:** `VYYYYMMDDNNNN__description.sql`  
  - `YYYYMMDD` = calendar date (controlled governance date); `NNNN` = four-digit daily sequence starting at `0001`; `description` = lowercase `snake_case`, ASCII only.
- **Repeatable migrations:** `R__<stable_definition_name>.sql` for idempotent definitions only where policy allows; not a dumping ground for one-off data fixes.
- **Immutability:** **Never** edit or delete migrations **after** they are applied/merged on shared history; fixes are **forward-only** via **new** versioned files.
- **No alternate schemes:** No plain `V0001` monotonic scheme; no second/minute timestamp versions unless **explicitly** approved later.
- **Spec SQL vs Flyway:** Header/spec SQL under `databases/operational-db/` documents **intended** tables, comments, and invariants; **Flyway-applied** files under the repo’s `migrations/` path (once populated per execution plan) are the **only** auditable apply order for environments. Keep spec and migrations **aligned**; when they diverge, **governance + migrations** win after an explicit doc update.

---

## Step 8 — Environment matrix and secret classes (summary)

**Environments (conceptual):** `local`, `ci`, `preview` / review app, `sandbox` / demo, `staging`, `production`, **disaster recovery / restore drill**.

**Hard rules:**

- **No production secrets** in `local` or `ci`.
- **No real secrets** in Git, generated docs, `PLATFORM_TREE.md`, Flyway placeholder files, or committed config.
- **No secrets** in logs, traces, screenshots, test fixtures, **AI prompts**, or **vector indexes**.
- **Break-glass:** **Emergency only**; **MFA**; **time-bound**; **fully audited**; **least privilege**; **never** for routine migrations or shared standing access; post-use review required.

Full secret-class matrix, storage rules, rotation expectations, and external standard cross-references remain in the **Step 8 decision record** and must be expanded into `policies/` and `secrets/` runbooks when those files are promoted from placeholder.

---

## Step 9 — Branch Strategy And PR Size Expectations

Per **Phase 0, Step 9** of `IMPLEMENTATION_EXECUTION_PLAN.md`, the following **branching and review discipline** is binding.

### Trunk and branch lifetimes

- **Trunk-based development:** integrate early and often to `main`.
- **`main`** is the **only** long-lived integration branch.
- **No permanent `develop` branch** (or equivalent long-lived dev line).
- **Short-lived branches only**; delete remote branch after merge when practical.

### Branch naming (`type/short-slug`, lowercase ASCII hyphenated slug)

| Prefix | Use |
|--------|-----|
| `feature/` | New capability or multi-module work (often tied to plan phase/step in slug). |
| `fix/` | Bug or incorrect behavior. |
| `chore/` | Tooling, hygiene, non-product refactors. |
| `docs/` | Documentation-only changes when policy allows dedicated docs PRs. |
| `migration/` | Work dominated by Flyway / DDL; filenames still follow Step 7 (`VYYYYMMDDNNNN__…`). |
| `hotfix/` | **Production incidents** only; see Hotfix below. |
| `release/` | **Optional** stabilization or enterprise release trains; cut from `main`, time-bounded. |
| `experiment/` | **Optional**, time-boxed spikes; must not merge without promotion to a normal `feature/` / `fix/` or abandonment. |
| `ai/` | Cursor/Codex or automation-assisted work; same review bar as human-authored changes. |

### Pull request size and content

- **Small PR default:** prefer easy review and fast feedback.
- **One logical change per PR** (single concern end-to-end).
- **Soft caps (targets, not hard law):** aim for **≤ ~400 lines** changed and **≤ ~25 files** unless the change is trivially mechanical (e.g. generated-only).
- **Generated outputs:** isolate in dedicated commits or PRs when large; PR description **must** state what was generated, generator command, and that validators were run.
- **Docs/spec with behavior:** behavior changes should reference updated specs/architecture paths in the PR description, or land in coordinated small PRs in the same merge window.

### Future required checks (CI)

When CI exists, merges to protected branches **must** be gated by (at minimum):

- install  
- lint  
- typecheck  
- tests (unit; integration where applicable)  
- `python scripts/validate_platform_tree.py`  
- `python scripts/create_physical_tree.py`  
- Flyway **migrate** apply-from-empty (ephemeral Postgres)  
- **RLS** integration tests  
- **Migration naming** check (enforces `VYYYYMMDDNNNN__…` per Step 7)  
- **Security / secret / dependency** scanning (org-standard tools)  

Unique job names across workflows are required so required status checks are unambiguous (GitHub branch protection expectation).

### Branch protection / GitHub rulesets

For **`main`** (and `release/*` when used), configuration **must** enforce:

- **Protect `main`**
- **No direct push** to `main`
- **No force push** to `main`
- **No branch deletion** of `main`
- **Pull request required** before merge
- **Required status checks** (from the list above, as wired)
- **Required reviews** (minimum count per org policy)
- **Dismiss stale approvals** when new commits change the diff
- **CODEOWNERS**-based review requests when a `CODEOWNERS` file is added
- **Restrict bypass** of protections to narrowly scoped roles (no routine admin bypass)

**Rulesets** may complement or supersede classic branch protection; layered rules use the **most restrictive** effective outcome. **Merge queue** is recommended when concurrent PR volume is high (requires `merge_group` CI wiring).

### Review rules (minimum)

| Area | Requirement |
|------|----------------|
| **Normal product code** | **1** reviewer with relevant domain context. |
| **SQL migrations (Flyway)** | **≥1 SQL-aware** reviewer who understands ordering and rollback posture. |
| **Ledger / posting / money movement** | **2** reviewers. |
| **RLS / security / auth / secrets** | **2** reviewers, **≥1 security-aware**. |
| **Payments / banking / payroll** | **2** reviewers. |
| **AI retrieval / vector-store** | **2** reviewers, **≥1 security-aware**. |

Production **hotfix** PRs are expedited but **not unreviewed** unless the **break-glass** incident process (Step 8) explicitly authorizes a temporary deviation, with post-incident review.

### Merge strategy

- **Squash merge** is the **default** into `main` so history stays readable and one PR maps to one integration commit.
- **Merge commits** are **allowed only** for **`release/*`** (or similar stabilization branches) when preserving merge topology is intentionally required.
- **Never rebase or force-push shared `main`.**
- **PR title and body** must preserve audit context under squash (phase/step reference, migration filenames, risk notes).

### Flyway migration conflicts (`VYYYYMMDDNNNN__…`)

- Before allocating a new version, integrate **`origin/main`**; use the agreed calendar date (UTC unless policy states otherwise) and the **next free `NNNN`** for that date already on `main`.
- **First merge wins** on duplicate versions; the other PR **rebases** and **renames** the migration file (and header) to a **new unused version**—**never** reuse a version that appeared on `main`.
- **Applied migrations are immutable** (Step 7); fixes are always **new** versioned files.

### Hotfix process

- **Branch:** `hotfix/<short-slug>` from `main` (or from active `release/*` if production tracks it).
- **Allowed when:** production-impacting incident or equivalent severity—not routine defects.
- **Migrations:** new `VYYYYMMDDNNNN__…` using the **hotfix merge date**; **no** direct production DDL except documented **break-glass** (Step 8).
- **Back-merge:** hotfix lands on `main`; cherry-pick or merge into active **release** branches so trains do not diverge.

### Release tagging and SemVer (high level)

- **Tags** (e.g. `v0.y.z`) apply when a **runnable release slice** and release process exist—not before the product justifies it.
- Follow **[Semantic Versioning](https://semver.org/)** once public or stable APIs exist; **`0.y.z`** is acceptable during initial instability.
- **Release notes** are required for tagged releases; security- and migration-relevant changes must be called out.

### CODEOWNERS and domain ownership (expectations)

Until `CODEOWNERS` exists, route reviews by expertise: **ledger-integrity**, **finance-accounting**, **posting-engine**, **payroll-benefits**, **banking/open-banking**, **payments/AP automation**, **AI/copilot/retrieval/vector-store**, **security/RLS/policies/secrets**, **infra/CI**, **warehouse/analytics/metrics**, **apps/web/UI packages**, **public API/developer platform**, and **platform tree / architecture docs** each require reviewers who understand failure impact; two-person rules above override for sensitive areas.

---

## Step 10 — Internal MVP Scope And Not-Yet List

Per **Phase 0, Step 10** of `IMPLEMENTATION_EXECUTION_PLAN.md` (**Stopping point 0**), the following **internal MVP** boundary is binding.

### Purpose and audience

- **Stopping point 0:** Step 10 closes **Phase 0** governance before **Phase 1** implementation work proceeds at scale.
- **Internal MVP** means **internal dogfood only**—not a public SaaS launch and not external customer onboarding.
- The MVP **validates the deterministic accounting core** and the **multi-tenant security spine**; it does **not** attempt **feature parity** with QuickBooks, NetSuite, Workday, Rippling, BILL, Stripe, Ramp, Brex, or other full platforms.

### Included in MVP

- Monorepo / **tooling foundation** (install, lint, typecheck, tests per execution-plan Phase 1 direction).
- **PostgreSQL 18** + **Flyway** migrations (apply-from-empty in CI when wired).
- **Tenancy**, **RLS**, and **session context** (GUC or equivalent) aligned with `finance-accounting.md`.
- **Identity / authentication skeleton** (toward OIDC and membership; minimal viable path).
- **`audit_log`** append-only semantics for mutations.
- **Idempotency** for financial mutating operations.
- **Outbox spine** (tables + publisher stub) for reliable side effects.
- **COA**, **books**, **ledgers**, **fiscal periods**, **period locks** per specs.
- **Draft journals** and balanced-line validation at API/DB layers.
- **Posting-engine** as the **only** path to transition a **manual, balanced** journal to **`posted`**.
- **Posted journal immutability** (reversals via new entries, not in-place edits).
- **Trial balance** derived from **posted** `journal_lines`.
- **One deterministic read-only dashboard or metric path** whose numbers reconcile to ledger/TB facts—not AI-generated official KPIs.
- **AI boundary / stub only**—no autonomous posting, payment, approval, or bank-detail change.
- **Tests and validation gates** through the execution-plan gates that this slice requires (including `validate_platform_tree.py` / `create_physical_tree.py`).

### Explicit NOT-YET list

The following remain **out of scope** for the internal MVP unless promoted per **Promotion criteria** below:

- Live **ACH / wire / card** payments.
- **Production** bank / **open-banking** sync.
- **Production AI** autoposting or auto-approval.
- **Payroll calculation** and **tax filing**.
- **Full HRIS** workflows.
- **Benefits / EOR** automation.
- **AP payment automation** beyond what existing specs describe for later phases.
- **AR payment links** with live processors.
- **Revenue recognition** automation.
- **Stripe / subscription** ingestion automation.
- **External accounting sync** to QBO / Xero / NetSuite / etc.
- **Public API** and **developer platform**.
- **Customer / vendor / employee / firm** portals beyond placeholders.
- **Mobile / desktop** feature work.
- **Treasury / debt / covenants** (phase-2 default in architecture).
- **Fixed assets / leases** (phase-2 default).
- **OCR jobs**.
- **1099 / W-9 filing**.
- **Encumbrance / budgetary control**.
- **Board / investor packs**.
- **Data portability** exports at scale.
- **Production warehouse / BI** beyond the **single deterministic proof metric** path.
- **Live regional bank** adapters.
- **Marketplace / self-serve** signup.
- **Full platform billing** commercialization.

### Promotion criteria (NOT-YET → in-scope)

A NOT-YET item may enter scope only when **all** applicable items are satisfied:

- Prior **execution-plan gates** for dependencies are **complete** (no skipped phases).
- **Architecture documentation** is updated through an **approved** governance/architecture change (not a coding prompt alone).
- **Required automated tests** exist for the new surface area.
- **Security / compliance review** is complete where the domain demands it (e.g., payments, PII scale-up).
- **Correct reviewers** are involved per Step 9 (including two-person rules for money, RLS, payments, banking, payroll, AI retrieval).
- Impact on **RLS**, **audit**, **secrets**, and **idempotency** is documented and implemented.
- **No skipped dependencies** in the spine (posting-engine, audit, outbox, tenancy order per execution plan).

### MVP success criteria

- Clean **install**, **lint**, **typecheck**, and **tests**.
- **Flyway** migrations apply from **empty** **PostgreSQL 18.3** (local/CI pin per Step 5).
- **RLS** prevents **cross-tenant** reads and writes in integration tests.
- **Manual journals** reach **`posted` only through the posting-engine**.
- **Posted** journals are **immutable** at the row level (reversal pattern only).
- **Trial balance** ties to **posted journal lines** within rounding policy.
- **`audit_log`** captures representative mutating operations.
- **No secrets leak** (per Step 8).
- **No AI path** can post, pay, or approve (`deterministic-accounting.md`).
- **Tree validation** remains green: `python scripts/validate_platform_tree.py` and `python scripts/create_physical_tree.py`.
- **One deterministic metric** reconciles to **fixture** / approved SQL reference data.

### Anti-scope-creep rule

No NOT-YET item may enter scope through a **coding prompt alone**. Promotion requires an **explicit architecture / governance update** first (this document or other approved architecture files), then implementation aligned with the execution plan.

---

## Phase 0 complete

- **Phase 0, Steps 1–10** are **complete** as recorded in this file.
- **Phase 1** may begin only after this governance document and any companion **tree/manifest** changes intended for the same commit boundary are **committed** to version control (so agents and CI reference a single coherent baseline).
- **Phase 1** execution starts at **`IMPLEMENTATION_EXECUTION_PLAN.md` — Phase 1 / Step 11** (repository and workspace bootstrap).
- **No product feature work** begins before **Phase 1 — Validation gate 1** is satisfied (install, lint, typecheck from a clean clone per the execution plan).

---

## References

- `docs/architecture/IMPLEMENTATION_EXECUTION_PLAN.md` — Phase 0 source of truth for step numbering and gates.
