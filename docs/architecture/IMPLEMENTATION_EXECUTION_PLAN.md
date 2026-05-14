# TRIVIUM Implementation Execution Plan

This document is the official implementation roadmap for building TRIVIUM from the current architecture/tree into a working platform.

Rules:
- Future implementation must follow this plan step by step.
- Cursor/Codex must not skip phases, reorder foundational phases, or build later-stage features before their prerequisites.
- Any deviation must be explicitly justified and approved before implementation.
- The deterministic accounting spine, tenancy/RLS, audit, idempotency, posting-engine supremacy, and AI assistant-only boundaries are non-negotiable.
- The plan may only be changed through a deliberate architecture update, not during normal coding prompts.
- Implementation prompts should reference the relevant phase/step/gate from this document.

## Phase 0 — Preconditions and constraints (no product code yet)

1. Re-read and treat as non-negotiable: `docs/architecture/deterministic-accounting.md`, `docs/architecture/finance-accounting.md`, `docs/architecture/ledger-integrity.md`, `docs/architecture/financial-reporting.md`, `docs/architecture/dashboard-and-metrics.md`, `docs/architecture/ap-payment-automation.md`, `packages/accounting-canonical-model/README.md`, `apps/api/src/modules/posting-engine/README.md` (where non-placeholder).
2. Record the architectural rule: **only posting-engine** transitions journals to **posted**; AI never approves pays, changes bank details, or owns official KPIs.
3. Inventory which folders are **spec-only** (SQL headers, empty `package.json`, placeholder READMEs) versus runnable code—sets honest "step zero" work.
4. Decide the **MVP accounting boundary**: internal dogfood vs multi-tenant SaaS from day one—document because it changes RLS and every API.
5. Choose **one** operational database product for v1; version-pin for CI and local dev.
6. Choose **one migration tool**; forbid mixing tools across time.
7. Define **migration naming/versioning** and never deviate.
8. Define **environment matrix** and secret classes.
9. Agree **branch strategy** and PR size expectations.
10. **Stopping point 0**: internal MVP scope and explicit "not yet" list (aligned with architecture deferrals).

## Phase 1 — Repository and workspace bootstrap

11. Replace empty root `package.json` / `pnpm-workspace.yaml` with real workspace entries for `apps/*`, `packages/*`, `services/*`, `workers/*` as applicable.
12. Pin **Node LTS** via `engines` and/or `.nvmrc`.
13. Add **TypeScript** base config (`strict`) and shared `tsconfig`.
14. Add **ESLint + Prettier** (or Biome) workspace-wide.
15. Add **Vitest** as default unit runner.
16. Resolve **`turbo.json` intent**: either wire Turbo for orchestration or document deferred use—avoid orphan config without behavior.
17. Establish **package boundary rules** (contracts vs core vs apps).
18. **Validation gate 1**: install, lint, typecheck succeed from clean clone.
19. **Do not** build product features until gate 1 passes.

## Phase 2 — CI/CD skeleton

20. Wire `.github/workflows/ci.yml` to install, lint, typecheck, test.
21. Add CI matrix strategy for OS/Node if needed.
22. Add pnpm caching.
23. Promote `db-migration-check.yml` and `db-rls-check.yml` from placeholders to real Postgres jobs once migrations exist.
24. Ensure **artifact/log retention** policy exists for failing jobs.
25. **Validation gate 2**: trivial PR passes CI.
26. **Do not** production deploy from this phase.

## Phase 3 — Local developer experience

27. Document clone→run paths (later edit `README.md` when allowed).
28. Complete **`.env.example`** patterns (no secrets).
29. Add **docker-compose** or devcontainer: Postgres + optional Redis + MinIO or compatible object storage emulator.
30. Canonical **`pnpm` scripts**: `dev:db`, `dev:api`, `dev:web`, `dev:worker` (names consistent across repo).
31. **Stopping point 1**: new engineer runs DB + API skeleton quickly.

## Phase 4 — Database migrations and physical model discipline

32. Make `migrations/` the only DDL path.
33. Baseline migration: extensions, UUID strategy, timestamps conventions.
34. Define standard columns and audit columns where required by schemas.
35. Create DB roles: migrator, app_rw, app_ro, break-glass admin.
36. Implement **session GUC** strategy for RLS consistent with future `session-context-variables` implementation.
37. CI migration apply-from-empty.
38. **Validation gate 3**: migrations apply cleanly.
39. **Do not** create wide business tables before session GUC strategy is coded.

## Phase 5 — Core tenancy and organization graph

40. Implement `companies`, `entities`, `books`, `ledgers` per specs (books before ledgers).
41. Implement org graph dimensions used by journals: departments, locations, teams, cost centers, reporting lines, managers as required by MVP.
42. Implement **`projects.sql` and `project_assignments.sql`** early for downstream payroll/spend.
43. Implement `tracking_categories.sql` per COA separation rules.
44. Seed minimum org per tenant.
45. **Validation gate 4**: uniqueness and FK graph matches `finance-accounting.md` invariants.

## Phase 6 — Identity, authentication, authorization entry

46. OIDC for humans; align with `identity-governance` doc themes.
47. Tenant membership tables and role assignments.
48. Role catalog aligned to `policies/dashboard-access.md` coarse roles.
49. API middleware: authn, tenant resolution, DB session variables.
50. Service accounts for workers with constrained scopes (`service_account_scope.sql` direction).
51. Start OPA with **one** bundle domain to avoid policy sprawl; expand later.
52. **Validation gate 5**: cross-tenant integration tests pass with RLS enforced.
53. **Do not** ship portals before gate 5.

## Phase 7 — Audit log, idempotency, outbox spine

54. Implement `core/audit_log.sql` append-only semantics.
55. Middleware audit for mutating routes.
56. Idempotency store for financial POSTs.
57. Outbox tables and publisher stub.
58. Standard event envelope across services/workers.
59. **Validation gate 6**: replay safety proven for a sample POST.
60. **Do not** add many workers before outbox exists.

## Phase 8 — COA, books, ledgers, fiscal, locks

61. `chart_of_accounts` DDL + constraints.
62. `gl_book_settings` pointers.
63. `fiscal_periods`, `period_locks`.
64. `ledgers` with `accounting_basis`.
65. Minimal `tax_codes`, `fx_rates` presence if posting validation references them.
66. Seed COA template per MVP vertical choice.
67. finance-accounting CRUD with locks.
68. **Validation gate 7**: posting vs header accounts; COA mutation lock behavior.
69. **Do not** ship statements before posting path exists.

## Phase 9 — Journal entries/lines and immutability

70. `journal_entries`, `journal_lines` DDL.
71. Draft persistence APIs.
72. Balanced-line validation at API.
73. DB-level defenses where spec mandates.
74. `posting_batches` traceability.
75. **Validation gate 8**: DB + API invariants consistent.

## Phase 10 — Posting engine supremacy

76. `packages/posting-engine-contracts`.
77. Posting-engine transaction path `draft→posted`.
78. Re-validate all posting-engine invariants from SQL comments.
79. Emit audit + canonical events on post.
80. Block non-engine posted writes at repository boundary.
81. **Validation gate 9**: only engine can post.
82. **Do not** connect domain posting (payroll/spend) before gate 9.

## Phase 11 — Trial balance, close, RE

83. TB computation/materialization.
84. TB read APIs.
85. finance-close workflow tables and minimal UI/API.
86. RE rollforward behavior per architecture.
87. **Validation gate 10**: TB ties to lines; rounding policy respected.
88. **Do not** automate entire enterprise close day one.

## Phase 12 — Deterministic rules as executable code

89. Encode `deterministic-accounting.md` checks in engine layer.
90. Golden fixtures in `packages/testing-fixtures`.
91. Property tests where feasible.
92. **Validation gate 11**: fast regression suite for posting.

## Phase 13 — Financial reporting read path

93. Statement projections from TB + COA hierarchy—deterministic code.
94. Cash vs accrual reporting path per `financial-reporting.md` decision.
95. RLS-safe reporting reads.
96. **Validation gate 12**: statements reconcile to TB fixtures.
97. **Do not** claim full GAAP/IFRS completeness in MVP.

## Phase 14 — Dashboards, metric lineage, analytics separation

98. Warehouse staging models minimal.
99. Metric definitions as code/tests per `analytics/metrics/metric-catalog.md`.
100. Role widget allowlists per `policies/dashboard-access.md`.
101. `packages/charting` strictly visualization-only.
102. **Validation gate 13**: dashboard numbers match warehouse SQL for fixtures; AI cannot return "official KPI" without labels/guards.
103. **Do not** ship investor packs early.

## Phase 15 — Project dimensions in flows

104. Posting-engine validation includes optional `project_id` rules.
105. API validation ties projects to tenant/book lifecycle.
106. Warehouse project profitability MVP.
107. **Validation gate 14**: mis-scoped project rejected at post time.

## Phase 16 — Payroll/workforce/benefits to GL

108. Workforce tables for employment dimensions.
109. `payroll_runs` and related items minimally to templates.
110. Payroll engine outputs canonical templates only.
111. Route through posting-engine with payroll idempotency keys.
112. **Validation gate 15**: payroll golden tests; payroll RLS sensitivity.
113. **Do not** implement all jurisdictions early.

## Phase 17 — Spend/procurement/cards to GL

114. Procurement tables needed for approvals and PO truth.
115. Card statement lifecycle per `card_transactions.sql` comments.
116. Category-to-GL mapping and approvals.
117. Statement settlement events through posting-engine.
118. **Validation gate 16**: statement totals reconcile.
119. **Do not** start OCR-first spend.

## Phase 18 — AP/payment automation

120. Bills/payments/payment_links/credits DDL.
121. Intake: upload/metadata first.
122. Duplicate detection matcher + human queue.
123. Approval-policy integration + SoD.
124. Payment execution behind flags; no AI approvals.
125. Object storage pointers for remittance/ack artifacts.
126. **Validation gate 17**: payment readiness gates enforced.
127. **Do not** live ACH without fraud controls and reconciliation loops.

## Phase 19 — AR/invoicing/payment links

128. AR invoice tables.
129. Hosted payment links and processor settlement mapping.
130. Cash application only via posting-engine.
131. Dunning optional; explicit defer if not MVP.
132. **Validation gate 18**: AR aging ties to subledger+GL fixtures.

## Phase 20 — Revenue recognition and commercial lifecycle

133. Commercial lifecycle facts driving billing/subscription truth.
134. `revenue_recognition.sql` schedules.
135. Post schedules via engine with versioning/audit.
136. **Validation gate 19**: deferred revenue rollforward fixture.

## Phase 21 — Bank connectivity (feeds) baseline

137. Bank connections/accounts/transactions schemas.
138. `bank_account_gl_mapping` enforcement in posting path for automated bank posts.
139. Ingestion workers with outbox idempotent upserts.
140. **Validation gate 20**: no duplicate bank txn posts on retries.

## Phase 22 — Bank reconciliation

141. `packages/bank-reconciliation-core` matching rules.
142. reconciliation link tables per ledger integrity direction.
143. AI suggestions as ranked candidates with human confirm thresholds.
144. **Validation gate 21**: statement fixture totals tie.

## Phase 23 — Accounting sync and external mappings

145. `gl_account_external_mappings` CRUD + audit.
146. sync runs/dead letters baseline for mapping-first sync.
147. inbound translation to canonical events then posting-engine—no silent GL overwrite.
148. **Validation gate 22**: unmapped provider accounts block posting when policy requires.

## Phase 24 — AI drafts and copilot (assistant-only)

149. `ai-accounting-drafts` persistence tables wired.
150. retrieval ACL logs and prompt audit logs per `ai-copilot` schemas.
151. Copilot endpoints return drafts + evidence pointers only.
152. Hallucination guards and confidence thresholds.
153. **Validation gate 23**: copilot cannot post/approve/pay in tests.
154. **Do not** send PII to third parties without governance.

## Phase 25 — Customer/vendor master and product catalog

155. Customer tables + `customer_scope` RLS.
156. Vendor tables + `vendor_scope` RLS + bank detail workflow.
157. Product catalog for invoicing/revrec prerequisites.
158. **Validation gate 24**: vendor bank detail changes emit canonical events + audit.

## Phase 26 — Platform billing (TRIVIUM's own billing) as needed

159. platform-billing minimal viable for tenant subscription if required.
160. Separate books/entities vs customer accounting if needed to avoid mixing.
161. **Validation gate 25**: no cross-book contamination.

## Phase 27 — Public API platform entry

162. `apps/api/src/public-api/v1` behind OAuth and consent scopes.
163. OPA public API bundles.
164. OpenAPI generated from code + CI diff checks.
165. **Validation gate 26**: contract tests for golden public routes.

## Phase 28 — BFF + web shell entry

166. `web-bff` as browser gateway.
167. `apps/web` shell navigation via `packages/app-shell` patterns.
168. Dashboard shell wired to role catalog endpoints; widgets fill incrementally.
169. **Validation gate 27**: authenticated session flows through BFF with RLS-backed reads.

## Phase 29 — Portals entry (read-only risky areas first)

170. Customer portal minimal invoice/pay.
171. Vendor portal minimal upload/status.
172. Employee portal minimal payslip/expense views.
173. Firm portal **read-only first** with delegated admin boundaries.
174. Developer OAuth consent app wired to real OAuth service.
175. **Validation gate 28**: portal cannot cross tenants; object URLs scoped.

## Phase 30 — Workers and queues scaling pattern

176. Real outbox consumers in `workers/*` with shared bootstrap library.
177. Retry/poison policies aligned with outbound-sync patterns.
178. Worker smoke tests in CI.
179. **Validation gate 29**: crash/restart does not duplicate financial posts.

## Phase 31 — Observability and security operations entry

180. Structured logging conventions across API/workers.
181. Metrics YAML placeholders become real RED metrics for posting/payments/imports.
182. SLO/error budget docs wired to alerts later.
183. Security ops alerts for anomalous auth and bank changes (initial stub).
184. **Validation gate 30**: trace spans across API→DB→worker for one flow.

## Phase 32 — Security/compliance hardening (continuous)

185. Map `security-baseline.md`, `security-architecture.md`, OWASP/NIST/CISA mapping docs into actual controls and CI checks.
186. Enforce `policies/data-classification.md` behaviors in APIs.
187. DSAR/export read path before destructive deletes (`data-portability` themes).
188. **Validation gate 31**: SAST/SCA workflows pass on PR.

## Phase 33 — Testing strategy

189. Unit tests for pure packages.
190. Integration tests with Postgres + RLS for core flows.
191. Contract tests for public API and parsers.
192. E2E web tests sparingly for critical journeys.
193. Nightly long-running separated.
194. **Validation gate 32**: flake budget policy.

## Phase 34 — Documentation and tree validation discipline

195. Update architecture docs when behavior changes; avoid drift.
196. Run `python scripts/validate_platform_tree.py` whenever manifest changes; regenerate `PLATFORM_TREE.md` only when tree intentionally changes.
197. Run `python scripts/create_physical_tree.py` in CI non-destructively to detect drift.
198. Add ADRs for UUID, currency rounding, basis strategy, etc.
199. **Validation gate 33**: PR checklist for manifest/touch rules.

## Phase 35 — Performance and scale

200. Load test posting contention at period close.
201. Indexing pass driven by query plans for TB/AP/AR aging.
202. Read replicas for analytics only.
203. Safe caching for reads; never cache posting decisions.
204. **Validation gate 34**: performance regression workflow signal-to-noise controlled.

## Phase 36 — Data portability, backup/restore, DR, rollback

205. Export pipeline per `export-package-contracts` and `data-portability` modules (subset first).
206. Backup/PITR strategy and restore drills.
207. Release rollback: feature flags + expand/contract migrations policy.
208. **Validation gate 35**: restore drill validates TB checksums.

## Phase 37 — Mobile/desktop later-stage rules

209. Keep `apps/mobile` green with smoke-only until web patterns stabilize.
210. Keep `apps/desktop` smoke-only until offline requirements defined.
211. When starting mobile: OAuth device flow + read-only dashboards first.

## Phase 38 — Explicit "do not build too early" checklist

212. Treasury debt/credit facilities until product/legal readiness.
213. Fixed assets/leases outside phase-2 guardrails.
214. OCR jobs, OLTP metric/dashboard tile registries, payment process requests, encumbrances until promoted by architecture/product.
215. No AI auto-approval for payments/COA changes.
216. Warehouse cannot become authoritative without reconciliation checkpoints.

## Phase 39 — Safe stopping slices

217. Slice A: auth+org+audit+migrations+CI.
218. Slice B: COA+books/ledgers+draft/manual JE+posting-engine+TB.
219. Slice C: bank feeds ingestion+recon MVP+GL mapping.
220. Slice D: AP+AR+payments sandbox rails.
221. Slice E: payroll+spend+card+project costing.
222. Slice F: accounting sync mappings + controlled runs.

223. Establish working monorepo toolchains (Phases 1–3) until CI is green.
224. Bring up Postgres in compose and implement migrations for tenancy + org graph + session GUC + baseline RLS (`tenant_scope`, `company_scope`, … minimal set).
225. Implement identity middleware + one authenticated "health" route proving tenant isolation.
226. Implement audit_log + idempotency storage + outbox skeleton.
227. Implement COA + books/ledgers + fiscal periods + locks tables and finance-accounting CRUD with tests.
228. Implement journal draft persistence + posting-engine post to TB for a **manual balanced journal** only.
229. Prompt 1: "Implement root `pnpm-workspace.yaml` and `package.json` workspaces for `apps/api`, `apps/web`, `packages/posting-engine-contracts`; add shared `tsconfig.base.json`, ESLint, Prettier, Vitest; ensure `pnpm -r typecheck` works."
230. Prompt 2: "Add Docker Compose for Postgres 16; add `pnpm dev:db` scripts; document env vars in `.env.example` without secrets."
231. Prompt 3: "Create migration framework (chosen tool) under `databases/` or `migrations/`; add CI job applying migrations to ephemeral Postgres."
232. Prompt 4: "Implement `tenant`, `company`, `entity`, `book`, `ledger` tables per SQL comment specs + FK graph; seed migration for demo tenant."
233. Prompt 5: "Implement API middleware: OIDC JWT validation stub + `tenant_id` resolution + `SET LOCAL app.tenant_id` for each request + integration tests for RLS."
234. Prompt 6: "Implement `audit_log` table + repository + middleware hook for mutating routes."
235. Prompt 7: "Implement `gl_accounts` + `gl_book_settings` + APIs with validations from `finance-accounting.md`; tests for posting vs header accounts."
236. Prompt 8: "Implement `journal_entries`/`journal_lines` draft create/list APIs with balanced-line validation; forbid posted writes outside posting-engine."
237. Prompt 9: "Implement posting-engine service method `postJournal(entryId)` with transaction, period lock checks, COA checks, immutability; emit audit + canonical event stub."
238. Prompt 10: "Implement TB materialization/query for one ledger/period + tests reconciling to sum(lines)."
239. Risk: Letting any module write **posted** `journal_lines` directly "for speed."
240. Risk: Building UIs before **RLS + tenant session** is proven—creates pervasive security debt.
241. Risk: Mixing **analytics** numbers into operational OLTP workflows as authoritative.
242. Risk: Starting **payments** before **posting-engine + approvals + audit + idempotency** exist.
243. Risk: Expanding **RLS policies** without automated cross-tenant tests—silent data leaks.
244. Risk: Ignoring **migration expand/contract** discipline—blocks rollback and multi-version deploys.
245. Risk: Letting **AI features** ship without evidence + policy gates—regulatory and fraud risk.
246. **Yes—coding should start now**, but only along the disciplined spine: **toolchain → Postgres migrations → tenancy/session → audit/idempotency/outbox → COA/books/ledgers/locks → journals → posting-engine → TB**. That sequence matches the architecture already in the repo and avoids disconnected feature work.
247. **No—do not start** with portals, payments rails, warehouse "AI dashboards," or broad worker fleets until the posting spine and RLS gates reach **Slice B stable** above; starting there would violate your own determinism and safety constraints.

## Phase 40 — Manual bank statement imports (parser pipeline and operational fallbacks)

248. Treat **manual imports** as first-class alongside aggregator feeds: implement `docs/architecture/bank-statement-imports.md` behaviors in product backlog tied to `object-storage/import-uploads` and `object-storage/bank-statements`.
249. Implement operational tables for **import batches**, **files**, **parse runs**, **normalized transactions**, **parse errors**, and **operator review states**—follow existing `bank-connectivity` / `bank-statement-imports` schema comments where present; add migrations only through the migration framework (Phase 4 dependency).
250. Implement **`packages/statement-parser-contracts`** first: normalized transaction shape, error taxonomy, and versioned parser capability flags (dependency: `packages/money-math` for amounts/dates correctness).
251. Implement **`packages/statement-parser-csv-xlsx`**: delimiter detection, column mapping profiles per bank template library, checksum of source file stored in object metadata.
252. Implement **`packages/statement-parser-ofx-qfx`**: OFX/QFX parsing with strict vs lenient modes; lenient mode must still emit explicit warnings, never silent money changes.
253. Implement **`packages/statement-parser-mt940`** and **`packages/statement-parser-camt053`**: bank messaging formats; include bic/account parsing rules and explicit currency handling.
254. Implement **`packages/statement-parser-fixtures`** golden files and snapshot tests for each parser family (dependency: Phase 33 testing strategy).
255. Wire **`packages/bank-transaction-normalization`** after parsers to unify counterparty text, sign conventions, and posting dates vs value dates (document which date drives GL in which jurisdiction mode; do not let AI decide).
256. Wire **`packages/dedupe-key-engine`** to populate dedupe keys consistent with `databases/operational-db/constraints-and-indexes/bank_transaction_dedup_unique.sql` intent (dependency: Phase 21 bank txn tables exist).
257. Implement **import orchestration worker** in `workers/*` dedicated to statement imports (separate from live feed workers) consuming outbox events `statement_import_requested`, `statement_parse_completed` (canonical model extension via `packages/accounting-canonical-model` when codified).
258. Implement **handoff to reconciliation**: parsed normalized txns appear as `bank_transactions` candidates in `pending_review` until matcher runs (dependency: Phase 22).
259. Implement **fallback UX** in `apps/web` bank connectivity center: when feed fails, prompt manual import, show last successful sync, preserve audit trail (dependency: Phase 28 web routes expansion Phase 47).
260. **Validation gate 36**: for each parser family, CI runs fixture suite; import retry does not duplicate deduped txns; failed parses produce actionable operator errors.

## Phase 41 — Regional bank connectivity and sanctions/legal gates

261. Implement **`databases/operational-db/schemas/regional-bank-connectivity/*`** as real DDL in migration order respecting `regional_bank_scope.sql` RLS.
262. Create a **provider support matrix** document derived from `docs/architecture/regional-bank-connectivity.md` and `MULTI_BANK_CONNECTIVITY.md` themes: country, provider, capabilities, consent model, data residency notes (documentation change allowed later; planning assumes it becomes executable checks in worker config).
263. Implement **`services/regional-bank-connectivity-service`** (or equivalent) as the adapter host for region-specific modules; keep adapters behind **`packages/regional-bank-adapter-kit`** contracts (`packages/regional-bank-contracts`).
264. Implement **regional bank workers** from `workers/*regional*` and `workers/*bank*` list in tree only after connector-auth token vaulting exists (dependency: Phase 42 and secrets Phase 54).
265. Wire **legal review flags** using `docs/architecture/sanctions-regional-bank-review.md`: any connection attempt for sanctioned/blocked regions must create a `legal_review_case` record in security operations tables (Phase 44) and block automated sync until cleared.
266. Implement **disabled-country policy** explicitly (example: Russia) as configuration + OPA policy bundle `policies/opa/bank-connectivity` extensions—not as scattered `if` statements in workers.
267. Implement **fallback paths**: if regional adapter unavailable, route operator to manual import (Phase 40) and mark connection `degraded` with observability alerts (Phase 52).
268. **Validation gate 37**: simulated regional adapter tests; legal-review-required paths cannot fetch transactions; audit events emitted.

## Phase 42 — Open banking consent lifecycle (PSD2-style) and token health

269. Implement **`open-banking`** schemas (`open_banking_providers.sql`, `open_banking_consents.sql`, `open_banking_consent_scopes.sql`, `open_banking_token_lifecycle.sql`, `open_banking_reauthorizations.sql`, `open_banking_revocations.sql`) as DDL with FK graph and `open_banking_consent_scope.sql` RLS alignment.
270. Implement **`apps/api/src/modules/open-banking`** routes for consent initiation, callback handling, and status queries—**no** token storage in plaintext (dependency: secrets Phase 54 KMS/token vaulting).
271. Implement **`services/open-banking-service`** as orchestrator for provider SDK calls, keeping provider secrets out of API process where possible.
272. Implement workers: **`bank-consent-renewal-worker`**, **`bank-connection-health-worker`** to proactively refresh/reauthorize and surface expiry dashboards metrics (dependency: observability Phase 52).
273. Implement **consent expiry dashboards** in analytics/warehouse as operational metrics, not financial truth (dependency: Phase 14).
274. Map flows to "GoCardless/TrueLayer/Plaid-style" patterns as configuration templates per provider, not hard-coded brand logic in core (dependency: `developer-platform` provider templates Phase 48).
275. **Validation gate 38**: consent revocation immediately stops fetch workers; reauth required state blocks transaction pulls; audit trail includes consent id on every fetch.

## Phase 43 — Connector auth and integrations platform (OAuth, catalog, health, orchestration)

276. Implement **`connector-auth`** schemas for OAuth clients/states/tokens/rotations with append-only rotation audit (ties to `audit-db` optional immutability patterns if used).
277. Implement **`services/connector-auth-service`** as the only issuer/refresher for integration tokens where feasible; other services request short-lived delegated tokens.
278. Implement **`integrations-platform`** schemas for integration catalog, instances, health, events; align with `apps/api/src/modules/integrations-platform`.
279. Implement **`services/integrations-platform-service`** for CRUD + event emission to outbox for worker orchestration.
280. Implement **`services/integrations-orchestration-service`** (present in tree) as workflow coordinator: schedules, retries, dependency graphs between connectors—**after** outbox and worker bootstrap exist (dependency: Phase 30).
281. Implement **workspace/productivity connectors** workers (`workers/workspace-sync-*`) only after: tenant admin consent, scoped tokens, retrieval ACL alignment (dependency: Phase 45 vector retrieval policies), and least-privilege data mapping per integration.
282. **Validation gate 39**: token rotation does not break in-flight jobs; revoked connector stops all dependent workers within bounded time; health events visible in observability dashboards.

## Phase 44 — Customer operations, customer success, SLA, health scores (non-ledger truth)

283. Implement **`customer-operations`** schemas: support tickets, messages, SLA policies as spec'd under `databases/operational-db/schemas/customer-operations/*` (tickets, sla_policies, etc.).
284. Implement **`apps/api/src/modules/customer-operations`** with strict RLS: agents see only assigned tenants unless break-glass.
285. Wire **`customer_health_scores.sql`** as deterministic-score-owned metrics in warehouse, not AI truth (dependency: Phase 14); AI may suggest narrative features only with evidence.
286. Implement **customer statements** generation as operational artifacts stored in `object-storage` with signed URL policy (dependency: Phase 46); distinguish from **official** financial statements (Phase 13).
287. Implement **customer success operations** dashboards in analytics as operational metrics (time-to-close, SLA breaches), not GL.
288. **Validation gate 40**: ticket PII is classified per `policies/data-classification.md`; search indexes exclude secrets (dependency: Phase 45 search ACL).

## Phase 45 — Search and search-index (discovery, not truth)

289. Implement **`search/search-service`** and **`search/search-index-service`** as separate deployables reading from outbox `search_index_requested` events (dependency: Phase 7).
290. Define **index mappings** under `search/indices` and enforce **ACL filters** at query time using the same identity claims as RLS (defense in depth: search must not bypass tenancy).
291. Implement **reindex** jobs triggered by major entity changes (customer rename merges) with idempotency keys.
292. Document and test: **search is source-of-discovery**, never authoritative for balances; UI must label search hits as navigational.
293. **Validation gate 41**: cross-tenant search attempts return zero results and generate security audit entries.

## Phase 46 — Object storage system (prefix contract, lifecycle, legal hold, evidence)

294. Implement **`object-storage/README.md` contract in code**: S3-compatible SDK wrapper service with tenant prefix enforcement from `object-storage/tenant-prefix-contract.md`.
295. Implement **signed URL policy** with short TTL, one-time download tokens for exports, and explicit content-type validation for uploads.
296. Wire **attachments**, **import-uploads**, **bank-statements**, **reconciliation-artifacts**, **export-packages**, **billing-artifacts**, **legal-hold** paths as separate bucket prefixes or key namespaces with uniform metadata schema.
297. Implement **lifecycle rules** and **legal hold** behavior: hold must block deletion even if retention TTL expired (dependency: compliance Phase 55).
298. Implement **evidence immutability**: WORM or object-lock mode decision for tax/payroll/finance evidence classes (planning choice; implement when compliance signs off).
299. **Validation gate 42**: permission change does not leak previously issued URLs (TTL + revocation list or short-lived JWT pattern).

## Phase 47 — Web app routes (full surface mapping, incremental implementation)

300. Implement **`apps/web/app/(public)/*`** marketing and entry routes with performance budgets per `docs/architecture/frontend-performance-budgets.md` and `core-web-vitals-policy.md`.
301. Implement **`apps/web/app/(auth)/*`** login/MFA/callback flows integrated with identity provider; no business logic in pages—call BFF.
302. Implement **`apps/web/app/(shell)/*`**: dashboard, activity, notifications, settings consuming `packages/navigation-model` and `packages/permission-guards`.
303. Add **bank connectivity center** pages: feeds status, manual import wizard, consent health, regional bank panels (dependencies: Phases 40–42).
304. Add **finance-accounting**, **finance-close**, **finance-operations** centers with role gating (dependencies: Phases 8–19).
305. Add **customer/vendor/product/commercial/platform-billing** admin centers with explicit "draft vs posted" labeling throughout.
306. Add **data-portability center** for export job status (dependency: Phase 56).
307. Add **outbound-sync center** for dry runs and conflict queues (dependency: Phase 57).
308. Add **developer-platform** pages for app registration and webhook testing (dependency: Phase 58).
309. Add **accounting-sync** pages for mapping completeness and sync runs (dependency: Phase 23).
310. Add **workforce/payroll/procurement/spend-travel** centers as modules become live.
311. Add **integrations/connector-auth** admin UI for rotating credentials and viewing health.
312. Add **customer operations** and **security operations** consoles for support/security roles with strong RBAC and session recording policies if required.
313. Add **AI copilot** and **AI accounting drafts** UIs that never show "posted" state unless sourced from ledger reads; include evidence drawers.
314. **Validation gate 43**: route map matches `PLATFORM_TREE.md` web routes; each route has E2E smoke ownership or explicit deferral flag in issue tracker (no silent stubs in prod build).

## Phase 48 — BFF layer (every BFF's purpose and sequencing)

315. Implement **`apps/bff/web-bff`** first as the canonical browser entry for `apps/web` (dependency: Phase 28).
316. Implement **`apps/bff/finance-bff`** when finance modules multiply: aggregates COA/journal/TB reads with stable pagination contracts.
317. Implement **`apps/bff/bank-connectivity-bff`** when bank endpoints and imports become large: isolates provider polling endpoints from core API scaling.
318. Implement **`apps/bff/regional-bank-bff`** when regional adapters go live (dependency: Phase 41).
319. Implement **`apps/bff/customer-master-bff`**, **`vendor-master`** equivalents when CRM-like payloads require shaping.
320. Implement **`apps/bff/customer-portal-bff`**, **`employee-portal`**, **`firm-portal`** BFFs with **stricter** rate limits and narrower scopes than internal admin BFFs.
321. Implement **`apps/bff/public-api-bff`** only when public API traffic segmentation is needed (dependency: Phase 27).
322. Implement **`apps/bff/developer-platform-bff`** for developer portal traffic separation.
323. Implement **`apps/bff/data-portability-bff`** for large export downloads/streaming.
324. Implement **`apps/bff/outbound-sync-bff`** for operator-heavy sync dashboards.
325. Implement **`apps/bff/mobile-bff`** and **`desktop-bff`** when those clients ship beyond smoke (dependency: Phase 37).
326. Document **why BFF exists**: to enforce auth shaping, pagination, field allowlists, stable DTOs, and to prevent browsers from directly accessing privileged service endpoints; BFF must not embed business posting rules that belong in posting-engine services.
327. **Validation gate 44**: each BFF has independent rate limits and observability service name; misconfigured BFF cannot bypass RLS because DB session still set from trusted identity gateway pattern.

## Phase 49 — Mobile and desktop (Expo/Tauri) detailed sequencing and guardrails

328. **`apps/mobile`**: implement Expo auth session storage using secure storage primitives; MFA flows; approvals inbox read/approve only after approval-policy APIs exist (dependency: Phase 60).
329. Banking transactions mobile views are **read-only** until device binding and step-up policies exist (dependency: security Phase 55).
330. Push notifications only after event bus + device token tables exist; never include sensitive amounts in notification bodies by default.
331. **Offline queue** for approvals is **late-stage**: only after idempotency + conflict resolution rules exist; start with "online-only" MVP to avoid double-approvals.
332. **`apps/desktop` (Tauri)**: implement `secure-local-store.ts` patterns for tokens; gate access with OS-level secure enclave where available.
333. **Updater signing**: implement `apps/desktop/src-tauri/updater-signing` process in CI `desktop-build-tests.yml` with signed artifacts and rollback channel.
334. **Desktop permissions**: ship minimal capability manifest; expand only as needed (principle of least privilege).
335. **Biometric unlock** optional wrapper around local session keys—never replaces remote auth for financial actions.
336. **Validation gate 45**: mobile/desktop smoke tests remain green in CI even when features behind flags are incomplete.

## Phase 50 — Portals deep dive (RLS, object storage, BFF separation)

337. **`apps/portals/customer-portal`**: invoices/payments/profile/support routes; portal-specific RLS via `customer_portal_scope.sql`.
338. **`apps/portals/vendor-portal`**: onboarding, invoices, POs, tax-documents routes; integrate vendor bank detail change workflow with dual control (dependency: Phase 25).
339. **`apps/portals/employee-portal`**: payslips/time/expenses/approvals; integrate retrieval policies for documents.
340. **`apps/portals/firm-portal`**: delegated admin; start read-only; enforce `firm_client_scope.sql` and `delegated_admin_scope.sql` strictly.
341. **`apps/portals/developer-oauth-consent`**: consent screens aligned with public API scopes; must match `policies/opa/public-api` bundles.
342. **Validation gate 46**: portal penetration tests for horizontal privilege; object storage URLs scoped to portal user's tenant and customer/vendor identity.

## Phase 51 — Developer platform (SDKs, examples, sandbox tenants, review)

343. Implement **`developer-platform`** docs site and API explorer generation from OpenAPI.
344. Implement app registration, client secrets issuance, webhook endpoints, and sandbox tenant provisioning workflows (`platform/tenant-provisioning` alignment).
345. Implement **SDK generation** pipelines for TypeScript, Python, Go, Java, .NET as **separate packages** published from CI on semver tags—start with **TypeScript** only to avoid multiplying unreleased SDKs.
346. Provide **examples/** per SDK with runnable sandbox fixtures.
347. Implement **app review** workflow for elevated scopes (payments read, GL read) with human approval and audit.
348. Implement **rate limit ledgers** and **usage logs** for developer apps (schemas under `public-api-platform` / `platform-billing` intersections as applicable).
349. **Validation gate 47**: breaking API changes trigger `openapi-breaking-change.yml` and compatibility suite failures as intended.

## Phase 52 — Public API platform deep (webhooks, signing, versioning, partner apps)

350. Implement **partner apps**, **consent grants**, **API keys** with hashed storage and rotation UX.
351. Implement **webhook subscriptions** with signing secret rotation, replay protection, and delivery logs.
352. Implement **idempotency** for public POST endpoints consistent with internal idempotency store patterns.
353. Implement **versioning** per `docs/architecture/api-versioning-compatibility.md`: deprecation windows, sunset headers, compatibility tests in `public-api-compatibility.yml`.
354. **Validation gate 48**: webhook redelivery does not duplicate downstream side effects in partner integration fixtures.

## Phase 53 — Data portability, DSAR, export packages, encryption, expiry (cross-domain)

355. Implement export job tables (`export_job`, scopes, manifests, checksums, encryption keys, download grants, expiry) per `data-portability` schemas and constraints like `export_manifest_integrity.sql`.
356. Implement **`services/data-portability-service`** and workers (`workers/*export*`): package assembly into `object-storage/export-packages` with encryption and manifest signing.
357. Implement **GDPR DSAR** flows per `docs/compliance/*` mapping docs; integrate legal hold checks from object storage phase.
358. **Validation gate 49**: expired download grants cannot be reused; DSAR export does not include other tenants' rows (RLS + manifest cross-check).

## Phase 54 — Outbound sync deep (dry runs, conflicts, tombstones, replay)

359. Implement outbound sync tables: destination connections, mapping profiles, dry runs, sync runs, conflicts, tombstones, dead letters, external id registry—per `outbound-sync` schemas.
360. Implement **`services/outbound-sync-service`** and orchestrator workers; provider-specific workers in `workers/*outbound*` only after mapping profiles stable.
361. Implement **conflict resolution dashboards** in web app with human decisions producing auditable resolutions (dependency: audit Phase 7).
362. Implement **replay workers** with strict idempotency keys tied to outbound external id uniqueness constraints (`outbound_external_id_unique.sql` intent).
363. **Validation gate 50**: dry run never mutates destination; production run produces reversible tombstones per policy.

## Phase 55 — Platform billing deep (plans, meters, entitlements, invoices, tax lines)

364. Implement platform billing schemas: plans, add-ons, subscriptions, trials, usage meters/events, entitlements, overages, invoices, tax lines, billing portal sessions—per `platform-billing` domain schemas in tree.
365. Implement **`services/platform-billing-service`** and workers (`workers/platform-billing-*`, `workers/platform-invoice-*`, `workers/platform-tax-*` as present) with **feature gates** reading entitlements consistently across API modules.
366. Store **billing artifacts** in `object-storage/billing-artifacts` with retention distinct from customer finance artifacts.
367. **Validation gate 51**: feature gating is enforced server-side (never only in UI); meter duplication prevented by idempotent ingestion.

## Phase 56 — Product catalog and commercial lifecycle deep (quotes, contracts, renewals, MRR inputs)

368. Implement catalog tables: products, families, price books, prices, taxability rules—per `product-catalog` schemas.
369. Implement commercial lifecycle: quotes, quote lines, contracts, amendments, renewals, order links—per `commercial-lifecycle` schemas and `services/commercial-lifecycle-service`.
370. Wire **ARR/MRR metric inputs** only from deterministic subscription facts + posted revenue schedules (dependency: Phases 13–20); analytics consumes, does not invent.
371. **Validation gate 52**: quote→contract conversion audit trail; pricing changes cannot retroactively alter posted historical GL (use new schedules/adjustments via engine).

## Phase 57 — Customer/vendor master deep (merge jobs, external IDs, portal links)

372. Implement customers/contacts/addresses/tax profiles/payment terms/credit limits/statements/merge jobs/external IDs per `customer-master` schemas.
373. Implement vendors/contacts/addresses/tax profiles/payment terms/external IDs per `vendor-master` schemas.
374. Implement **duplicate/merge** as asynchronous jobs with operator review and strict locking to prevent double posting during merge (dependency: posting-engine concurrency controls).
375. **Validation gate 53**: merge job cannot complete if open drafts/pending payments exist unless policy resolves them.

## Phase 58 — Approval policy engine and authorization policy (OPA simulations, SoD)

376. Implement workflows/workflow steps/approval tasks tables under `approval-policy-engine` schemas; integrate with AP payments, vendor bank changes, AI draft promotions, spend approvals, procurement thresholds, payroll exceptions, and optional COA mutation approvals (explicitly gated).
377. Extend **`policies/opa/approval-policy-engine`** Rego tests in CI for representative SoD rules (submitter≠approver≠payor).
378. Implement **`authorization-policy`** bindings and simulations; expose "simulation" API for admins to test policy changes safely.
379. **Validation gate 54**: failed policy simulation cannot be promoted to production binding; production binding changes audited.

## Phase 59 — Vector store and AI retrieval (namespaces, ACL logs, red-team tests)

380. Implement `vector-store` namespaces and **retrieval policies** aligned with `databases/vector-store/*` and `policies/opa/ai-retrieval`.
381. Implement ingestion pipelines that **chunk** documents from object storage with tenant labels; never index raw secrets.
382. Implement **`retrieval_acl_logs.sql`** and **`prompt_audit_logs.sql`** enforcement in `ai-copilot-service` paths.
383. Add **AI red-team tests** suite: prompt injection attempts must not retrieve cross-tenant chunks; tool calls must be allowlisted; outputs must carry citations or explicit "no evidence."
384. **Validation gate 55**: retrieval ACL violations emit security alerts (dependency: security operations Phase 44/52).

## Phase 60 — Cache layer (tenant isolation, TTL, invalidation rules)

385. Implement **`cache/keying-contract.md` in code**: mandatory key prefixes including `tenant_id`, `environment`, and `data_domain`.
386. Implement **tenant isolation** guards: never accept tenant id from cache key input without verifying against authenticated session.
387. Implement **TTL policies** per `cache/ttl-policies` README intent: short TTL for permissions, medium for directory lookups, no caching for posting responses.
388. Implement **invalidation hooks** after posting success, payment settlement, permission binding changes, and role assignment changes (call async invalidation via outbox to avoid race conditions).
389. **Validation gate 56**: permission change becomes effective within defined SLA without stale cache allowing old permissions.

## Phase 61 — Warehouse and analytics pipelines (operational truth vs projections)

390. Implement **`warehouse/dbt`** project skeleton with environments `dev/stage/prod` and governance folder policies (`warehouse/governance`).
391. Implement **`databases/warehouse`** schemas if present for staging/marts separation; align naming with `analytics/pipelines` orchestration.
392. Implement **`services/analytics-service`** and **`workers/warehouse-sync-worker`** (or similarly named worker in tree) to extract operational facts on schedule/cdc—**CDC choice** is an architecture decision: logical replication vs batch; document before coding.
393. Wire **anomaly detection** experiments folder as offline-only until metrics stable; do not auto-block payments from anomaly flags early.
394. Reiterate **metric lineage** implementation tests from `analytics/warehouse-models/metric-lineage.md` in CI for financial metrics.
395. **Validation gate 57**: warehouse totals reconcile to operational TB snapshots for the same close period in staging.

## Phase 62 — UI packages and frontend system (design system, accessibility, grids, workflows)

396. Implement **`packages/design-tokens`** then **`packages/ui-kit`** then **`packages/ui-finance`** layering rules (finance-specific components depend on ui-kit, not vice versa).
397. Implement **`packages/ui-mobile-kit`** and **`packages/ui-desktop-kit`** only after web kit stabilizes to reduce triple maintenance.
398. Implement **`packages/app-shell`** navigation and layout integration with `packages/navigation-model` and `packages/permission-guards`.
399. Implement **`packages/accessibility-rules`** checks in CI `ui-accessibility-tests.yml` with real ruleset (axe or equivalent).
400. Implement **`packages/data-grid`** with virtualized large GL views; enforce column-level redaction for sensitive dimensions.
401. Implement **`packages/form-engine`** for consistent validation messaging (server errors mapped deterministically).
402. Implement **`packages/workflow-ui`**, **`packages/sync-status-ui`**, **`packages/audit-timeline-ui`** tied to real APIs as those modules become live.
403. Run **`ui-visual-regression.yml`** on stable components only to avoid flaky noise; start with marketing pages + shell chrome.
404. **Validation gate 58**: accessibility and visual regression jobs are informative at first, then blocking once baselines stabilized.

## Phase 63 — Security operations deep (incidents, evidence, abuse, dashboards)

405. Expand **`apps/api/src/modules/security-operations`** beyond stub: incidents, cases, evidence links to object storage, abuse signals from auth logs and public API rate limiters.
406. Implement **security dashboards** in web shell for security roles only (RLS + role gating).
407. Integrate **`packages/audit-timeline-ui`** with `audit-service` read APIs.
408. **Validation gate 59**: incident access is highly restricted; evidence links expire; all actions audited.

## Phase 64 — Observability deep (OpenTelemetry, collectors, Grafana, burn rate alerts)

409. Implement OpenTelemetry instrumentation libraries shared across `services/*` and `workers/*` (`packages/observability` alignment).
410. Wire `observability/collector` configs for traces/metrics/logs export; define service naming convention matching `platform/service-catalog/services.yaml`.
411. Implement **SLOs and burn-rate alerts** per `observability/slo/*` including posting-engine availability, payment initiation success, bank fetch success, webhook delivery success, export completion latency.
412. Add **runbook links** in alert annotations to `infra/runbooks` or `security` docs where present.
413. **Validation gate 60**: forced failure drills create actionable traces spanning API and worker with correct tenant tags (no PII in labels).

## Phase 65 — Platform runtime, infra, secrets, messaging, DR (Terraform/Kubernetes/Helm)

414. Implement **`infra/terraform`**, **`infra/kubernetes`**, **`infra/helm`**, **`infra/networking`**, **`infra/local-dev`**, **`infra/security`**, **`infra/performance`** iteratively: start with **one** environment (staging) fully reproducible.
415. Align **`platform/service-catalog/services.yaml`** with actual deployable services and owners.
416. Align **`platform/tenant-provisioning`** runbook with automated provisioning jobs and secrets injection patterns.
417. Implement **`platform/workflow-schedules`** integration with orchestrator for recurring jobs (close reminders, consent renewals, warehouse sync).
418. Implement **`secrets/*` templates** and **`secrets/rotation-runbook.md`** operations: rotation cadence, dual control, verification steps; integrate with cloud KMS/HSM choices documented in compliance docs.
419. Implement **breakglass procedure** for RLS bypass admin role: MFA, ticket, time-bound session, automatic audit flagging.
420. Implement **backup/restore** automation and game days (extends Phase 36) with infra-owned schedules.
421. **Validation gate 61**: staging deploy is one command; secrets never appear in logs; rotation drill succeeds without downtime for read paths where promised.

## Phase 66 — `tests/` root harness and cross-package integration

422. Implement **`tests/`** as integration harness for multi-service scenarios (docker compose stack) beyond per-package tests: at minimum "posting + audit + outbox + worker consume" scenario.
423. Add **contract compatibility** tests for each public SDK release pipeline (dependency: Phase 51).

## Phase 67 — `tools/` developer ergonomics (explicitly sequenced after core flows exist)

424. Implement **`tools/*`** CLIs mentioned by tree intent: platform tree validation wrappers, ledger inspection, bank support matrix builder, statement parser CLI, consent lifecycle simulator, multi-bank seed generator, bank purpose mapper CLI, public API tooling, data portability tooling, outbound sync tooling, provider connector tooling, DB tooling/codegen/checkers—**prioritize tools that reduce operational risk** (parser CLI, ledger inspector) before convenience tools.
425. Wire tools releases to the same semver discipline as services (avoid orphan scripts).

## Phase 68 — Compliance mapping execution (SOC2/ISO/GDPR/PCI/NIST/CISA) as engineering workitems

426. Convert `docs/compliance/*` control maps into **tracked controls** with owners, evidence locations, and automated checks where possible (CI jobs already stubbed in `.github/workflows/security-*`).
427. Implement **data residency** enforcement hooks in connector selection and object storage region selection (ties to regional bank phase).
428. Implement **subprocessor registry** updates as operational process (docs + approvals), not code-heavy, but must be linked in security disclosures.
429. **Validation gate 62**: compliance checklist passes internal audit for MVP scope (non-code milestone but blocks "GA" labeling).

## Phase 69 — Worker families sequencing map (dependency-ordered rollout)

430. **Ledger/close/FX/reconciliation workers**: only after posting-engine + TB + bank normalized transactions exist (`workers/*ledger*`, `workers/*close*`, `workers/*fx*`, `workers/*reconciliation*` as present in tree—roll out in that order).
431. **Bank consent/health/account/statement/import/reconciliation workers**: consent renewal before fetch; health checks before heavy imports; statement import workers before recon matching at scale (`bank-consent-renewal-worker`, `bank-connection-health-worker`, `bank-account-sync-worker`, feed workers, import workers).
432. **Public API workers**: webhook delivery, token rotation, rate limit ledger compaction (`workers/*public-api*` patterns).
433. **Data export workers**: export assembly, encryption, expiry (`workers/*export*`).
434. **Outbound sync workers**: provider-specific only after mapping profiles and dry runs are stable (`workers/*outbound*`, `workers/*netsuite*`, `workers/*qbo*`, etc.).
435. **Accounting sync workers**: inbound/outbound accounting sync (`workers/accounting-sync-*`, `workers/accounting-historical-sync-worker`) after `gl_account_external_mappings` stable.
436. **Spend/travel workers** after spend schemas and approvals exist.
437. **HR/recruiting workers** (`workers/*hr*`, `workers/*recruiting*`) after workforce data model stable and legal review for PII.
438. **CRM/support/commerce workers** (`workers/*crm*`, `workers/*support*`, `workers/*commerce*`) after customer operations and commercial lifecycle foundations exist.
439. **Workspace/productivity workers** after integrations orchestration and token vaulting mature.
440. **Customer dedupe/statement/health workers** after customer master and analytics pipelines exist.
441. **Platform billing workers** after entitlements schema stable.
442. **Validation gate 63**: worker dependency graph documented in `platform/workflow` or service catalog; CI checks that new workers declare their outbox subscriptions and retry policies.

## Phase 70 — Packages/contracts matrix (families sequenced to avoid circularity)

443. **Contracts first**: all `packages/*-contracts` packages publish types and JSON schemas/OpenAPI fragments without DB dependencies.
444. **Core second**: `packages/*-core` packages implement algorithms (reconciliation, dedupe, normalization) using contracts only.
445. **Parsers and statement normalization** next (`packages/statement-parser-*`, `packages/bank-transaction-normalization`, `packages/dedupe-key-engine`).
446. **Accounting canonical + isolation context**: `packages/accounting-canonical-model`, `packages/isolation-context` used by API and workers uniformly.
447. **Money math** everywhere amounts touch (`packages/money-math`).
448. **UI packages** after stable API DTOs exist (Phase 62).
449. **Testing fixtures** grow with each domain milestone (`packages/testing-fixtures`).
450. **Validation gate 64**: dependency-cruiser (or turbo rules) reports zero forbidden cycles.

## Known Deferred Items (explicitly remain deferred unless promoted by architecture/product)

451. Treasury debt, credit facilities, covenants, interest schedules as per `docs/architecture/treasury-debt-credit.md` phase-2 posture.
452. Fixed assets and leases (ASC 842 / IFRS 16 style) as per `docs/architecture/fixed-assets-leases.md` phase-2 posture.
453. OCR jobs tables and OCR-first workflows as phase-2 candidates referenced in AP automation docs.
454. `payment_process_requests` style production tables if treated as phase-2 in AP specs.
455. Vendor 1099 filing integrations and related production filing tables as phase-2.
456. Encumbrances/commitment accounting as phase-2 in procurement docs.
457. OLTP `metric_definitions.sql`, `dashboard_tiles.sql` if architecture keeps definitions in repo/warehouse until governance demands DB registry.
458. Cash forecast scenario persistence tables if kept phase-2 per cash-liquidity architecture.
459. Advanced mobile offline approval queues and desktop offline accounting (explicitly late-stage).

## Never Build Too Early (hard guardrails)

460. Never enable **live money movement** (ACH/wire/card) before: posting-engine supremacy, audit logs, idempotency, approvals, reconciliation baseline, observability SLOs, and security ops incident paths exist.
461. Never implement **search or AI retrieval** before tenant RLS patterns are proven—search leaks are catastrophic.
462. Never implement **public webhooks** before signing, replay protection, and idempotent handlers exist.
463. Never implement **firm delegated admin** write capabilities before authorization simulations and breakglass auditing exist.
464. Never connect **warehouse KPIs** to customer-facing "official" statements before reconciliation gates pass in staging repeatedly.
465. Never add **regional bank adapters** for a country without completing sanctions/legal review workflow requirements for that country.

## First Stable Product Slices (unchanged spine, now aligned to expanded domains)

466. **Slice A+**: Slice A plus connector-auth skeleton and object storage signed URL read for internal invoices (still no payments).
467. **Slice B+**: Slice B plus manual bank import parser MVP feeding reconciliation review queue (no auto-post from imports until human confirms).
468. **Slice C+**: Slice C plus open banking consent lifecycle for one provider in one region only.
469. **Slice D+**: Slice D plus outbound sync dry-run for one provider mapping profile.
470. **Slice E+**: Slice E plus HR recruiting workers only if workforce schemas stable (otherwise keep recruiting workers disabled).

## First 10 Implementation Prompts (coding-ready; same spine, tightened for new domains)

471. Prompt 1: Implement monorepo workspaces + TS strict base + eslint/prettier/vitest + CI `ci.yml` green.
472. Prompt 2: Docker compose Postgres + migration tool + apply-from-empty CI job (`db-migration-check.yml`).
473. Prompt 3: Implement tenant/org/book/ledger schema + seed + session GUC middleware + cross-tenant RLS tests.
474. Prompt 4: Implement audit_log + idempotency + outbox tables + publisher stub + integration test for replay safety.
475. Prompt 5: Implement COA + gl_book_settings + finance-accounting CRUD + period lock behaviors + tests.
476. Prompt 6: Implement journal draft APIs + posting-engine post + TB query + golden fixtures.
477. Prompt 7: Implement object storage wrapper + tenant prefix enforcement + signed upload/download integration tests.
478. Prompt 8: Implement statement import batch tables + parser contracts + CSV/XLSX parser MVP + dedupe keys + operator error reporting UI stub in web-bff.
479. Prompt 9: Implement open banking consent tables + consent initiation/callback API skeleton + consent renewal worker stub with feature flag disabled by default.
480. Prompt 10: Implement search-index worker stub that indexes only `customer.name` and `vendor.name` with ACL filters + cross-tenant search test.

## Final Verdict (whole-tree coverage)

481. **Verdict: YES—the upgraded plan now covers the whole TRIVIUM tree at the domain level**, including previously light areas: manual imports and parser packages, regional banking and sanctions gates, open banking consent lifecycle, connector auth and integrations orchestration, customer operations and security operations, search and vector retrieval with ACL and red-team posture, cache invalidation discipline, object storage lifecycle and legal hold, warehouse/dbt and warehouse sync separation from OLTP truth, the full UI package stack and frontend performance/visual/a11y testing strategy, comprehensive web routes and every BFF in the tree with sequencing rationale, mobile/desktop Tauri constraints, all portals and developer platform/SDK concerns, public API webhooks and versioning, data portability and outbound sync depth, expanded platform billing and commercial/catalog depth, deeper master data merge strategies, approval/authorization OPA simulations, compliance mapping execution, observability and infra/secrets/runbooks, root `tests/` integration harness, `tools/` CLIs, and a worker rollout map aligned to `services/` and `workers/` inventory in `PLATFORM_TREE.md`.

482. **Caveat:** the repository still contains many placeholders (`{}` package manifests, placeholder architecture stubs like `IMPLEMENTATION_PHASES.md`); "coverage in plan" means **each folder has an explicit engineering place**, not that code exists yet—implementation must still follow gates to avoid fake progress.

## Full Tree Coverage Appendix (folder → plan reference)

483. **`.github/`** — Phases 2, 33–34, 48–52, 58–60, 62–64 (workflows for CI, DB checks, OpenAPI, security scans, accessibility, visual regression, performance, ledger integrity, load tests).
484. **`analytics/`** — Phases 14, 40–43 (dashboards), 61 (pipelines/models/experiments/anomaly), appendix metric catalogs already in repo (`metrics/`, `dashboards/`, `warehouse-models/`).
485. **`apps/api/`** — Phases 5–29 and domain phases throughout; `src/middleware/`, `src/modules/*`, `src/public-api/` explicitly mapped in Phases 27, 42–44, 47–53, 58–59.
486. **`apps/bff/`** — Phase 48 (each BFF listed in tree).
487. **`apps/desktop/`** — Phases 37, 49, 62, 64 (Tauri, updater signing, permissions, perf).
488. **`apps/mobile/`** — Phases 37, 49, 62, 64 (Expo, MFA, approvals, push, offline rules).
489. **`apps/portals/*`** — Phase 50 (customer/vendor/employee/firm/developer OAuth consent portals).
490. **`apps/web/`** — Phases 28–29, 40–43, 47, 50, 52–55, 58–60, 62–64 (routes and performance/a11y/visual tests).
491. **`cache/`** — Phase 60 (`keying-contract.md`, namespaces, ttl-policies, key-guards).
492. **`databases/audit-db/`** — Phases 7, 36, 53–55, 65 (immutable audit events, retention policies).
493. **`databases/operational-db/`** — Phases 4–25, 40–44, 51–58 (schemas, constraints, migrations, RLS).
494. **`databases/vector-store/`** — Phase 59 (vector schemas/policies alongside `vector-store/` root).
495. **`databases/warehouse/`** — Phase 61 (if used as DB-side warehouse staging; coordinate with `warehouse/`).
496. **`developer-platform/`** — Phase 51 (docs, examples, registration flows).
497. **`docs/`** (architecture, compliance, runbooks) — Phases 0, 32–34, 55, 58, 62, 65, 68 (docs drive executable controls and ADRs).
498. **`infra/`** — Phase 65 (terraform/k8s/helm/networking/local-dev/security/performance).
499. **`object-storage/`** — Phase 46 (prefix contract, attachments, imports, exports, bank statements, recon artifacts, billing artifacts, legal hold, lifecycle rules).
500. **`observability/`** — Phases 31, 52, 64 (collector, slo, dashboards, metrics templates for services/workers).
501. **`packages/*`** — Phase 70 matrix + domain-specific phases (parsers Phase 40, reconciliation Phase 22, UI Phase 62, contracts Phase 70, observability package Phase 64).
502. **`platform/`** (service catalog, tenant provisioning, workflow schedules, workflow) — Phases 30, 51, 54–55, 65, 69.
503. **`policies/`** (OPA bundles, markdown policies including `dashboard-access.md`) — Phases 6, 14, 27, 41–42, 50, 51–52, 58–60, 68.
504. **`scripts/`** — Phase 34 (`validate_platform_tree.py`, `generate_platform_tree_md.py`, `create_physical_tree.py`) plus tooling integration Phase 67.
505. **`search/`** — Phase 45 (`search-service`, `search-index-service`, indices, acl-filters).
506. **`secrets/`** — Phase 65 (templates, rotation runbooks, breakglass alignment).
507. **`security/`** — Phases 32, 44, 55, 63, 65, 68 (policies-as-code, SOC/OWASP/NIST/CISA mappings).
508. **`services/`** — Phases 21–30, 40–43, 51–57, 59, 61, 63–65 (each `services/*` maps to the domain module it backs; implement service only after corresponding schemas + posting rules exist).
509. **`tests/`** — Phase 66 (cross-service integration harness).
510. **`tools/`** — Phase 67 (CLIs and codegen/checkers).
511. **`turbo.json` / root manifests (`package.json`, `pnpm-workspace.yaml`, `Makefile`, `CODEOWNERS`, `.editorconfig`, `.gitattributes`, `.env.example`, `TRIVIUM.code-workspace`)** — Phases 1–3 and 34 (tooling + governance hygiene).
512. **`vector-store/`** (repo root sibling docs for retrieval) — Phase 59 (coordinate with `databases/vector-store/` schemas and policies).
513. **`warehouse/`** (`dbt`, `governance`, `marts`) — Phase 61 (dbt project structure, governance, marts layering).
514. **`workers/`** — Phases 30, 40–43, 53–57, 61, 69 (full worker inventory in `PLATFORM_TREE.md` is covered by the worker sequencing map in Phase 69).

## Closing note (plan completeness vs "shorten")

515. This document **intentionally preserves** your prior **Phases 0–39 / steps 1–222** (plus original stopping slices and guard items) and **extends** with **Phases 40–70 / steps 248–450** plus appendix steps **451–515** so major tree domains are not forgotten, while keeping the **same core sequencing**: foundations first, deterministic ledger spine before money movement, integrations and AI only after controls, portals and multi-surface UX after BFF/security patterns, warehouse always reconciling—not replacing—OLTP truth.
