# bizplatform canonical repository tree

```text
bizplatform/
├─ .github/
│  ├─ workflows/
│  │  ├─ api-contract-tests.yml
│  │  ├─ ci-desktop.yml
│  │  ├─ ci-mobile.yml
│  │  ├─ ci-services.yml
│  │  ├─ ci-web.yml
│  │  ├─ ci-workers.yml
│  │  ├─ ci.yml
│  │  ├─ db-migration-check.yml
│  │  ├─ db-rls-check.yml
│  │  ├─ desktop-build-tests.yml
│  │  ├─ ledger-integrity-tests.yml
│  │  ├─ load-tests-nightly.yml
│  │  ├─ mobile-build-tests.yml
│  │  ├─ openapi-breaking-change.yml
│  │  ├─ performance-regression.yml
│  │  ├─ public-api-compatibility.yml
│  │  ├─ release.yml
│  │  ├─ security-sast.yml
│  │  ├─ security-sca.yml
│  │  ├─ security-scans.yml
│  │  ├─ security-secrets-scan.yml
│  │  ├─ ui-accessibility-tests.yml
│  │  └─ ui-visual-regression.yml
│  ├─ CODEOWNERS
│  └─ pull_request_template.md
├─ analytics/
│  ├─ anomaly-detection/
│  │  └─ README.md
│  ├─ dashboards/
│  │  ├─ dashboard-catalog.md
│  │  └─ README.md
│  ├─ experiments/
│  │  └─ README.md
│  ├─ metrics/
│  │  ├─ metric-catalog.md
│  │  └─ README.md
│  ├─ pipelines/
│  │  └─ README.md
│  ├─ warehouse-models/
│  │  ├─ metric-lineage.md
│  │  └─ README.md
│  └─ README.md
├─ apps/
│  ├─ api/
│  │  ├─ src/
│  │  │  ├─ middleware/
│  │  │  │  └─ README.md
│  │  │  ├─ modules/
│  │  │  │  ├─ accounting-sync/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ ai-accounting-drafts/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ ai-copilot/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ bank-connectivity/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ bank-reconciliation/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ commercial-lifecycle/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ connector-auth/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ customer-master/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ customer-operations/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ data-portability/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ finance-accounting/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ finance-close/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ finance-operations/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ integrations-platform/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ ledger-integrity/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ open-banking/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ outbound-sync/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ payroll-benefits/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ platform-billing/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ posting-engine/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ procurement-spend/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ product-catalog/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ public-api-platform/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ regional-bank-connectivity/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ security-operations/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ spend-travel/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  ├─ vendor-master/
│  │  │  │  │  ├─ tests/
│  │  │  │  │  │  ├─ module.test.ts
│  │  │  │  │  │  └─ README.md
│  │  │  │  │  ├─ controller.ts
│  │  │  │  │  ├─ README.md
│  │  │  │  │  ├─ repository.ts
│  │  │  │  │  ├─ routes.ts
│  │  │  │  │  └─ service.ts
│  │  │  │  └─ workforce/
│  │  │  │     ├─ tests/
│  │  │  │     │  ├─ module.test.ts
│  │  │  │     │  └─ README.md
│  │  │  │     ├─ controller.ts
│  │  │  │     ├─ README.md
│  │  │  │     ├─ repository.ts
│  │  │  │     ├─ routes.ts
│  │  │  │     └─ service.ts
│  │  │  ├─ public-api/
│  │  │  │  └─ v1/
│  │  │  │     ├─ bank.routes.ts
│  │  │  │     ├─ bills.routes.ts
│  │  │  │     ├─ customers.routes.ts
│  │  │  │     ├─ exports.routes.ts
│  │  │  │     ├─ invoices.routes.ts
│  │  │  │     ├─ router.ts
│  │  │  │     ├─ vendors.routes.ts
│  │  │  │     └─ webhooks.routes.ts
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  ├─ unit/
│  │  │  │  └─ vitest-api.smoke.test.ts
│  │  │  └─ README.md
│  │  ├─ package.json
│  │  ├─ README.md
│  │  ├─ tsconfig.json
│  │  └─ vitest.config.ts
│  ├─ bff/
│  │  ├─ bank-connectivity-bff/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  ├─ package.json
│  │  │  └─ README.md
│  │  ├─ customer-master-bff/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  ├─ package.json
│  │  │  └─ README.md
│  │  ├─ customer-portal-bff/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  ├─ package.json
│  │  │  └─ README.md
│  │  ├─ customer-success-bff/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  ├─ package.json
│  │  │  └─ README.md
│  │  ├─ data-portability-bff/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  ├─ package.json
│  │  │  └─ README.md
│  │  ├─ desktop-bff/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  ├─ package.json
│  │  │  └─ README.md
│  │  ├─ developer-platform-bff/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  ├─ package.json
│  │  │  └─ README.md
│  │  ├─ finance-bff/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  ├─ package.json
│  │  │  └─ README.md
│  │  ├─ mobile-bff/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  ├─ package.json
│  │  │  └─ README.md
│  │  ├─ outbound-sync-bff/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  ├─ package.json
│  │  │  └─ README.md
│  │  ├─ platform-billing-bff/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  ├─ package.json
│  │  │  └─ README.md
│  │  ├─ public-api-bff/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  ├─ package.json
│  │  │  └─ README.md
│  │  ├─ regional-bank-bff/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  ├─ package.json
│  │  │  └─ README.md
│  │  └─ web-bff/
│  │     ├─ src/
│  │     │  └─ main.ts
│  │     ├─ tests/
│  │     │  └─ README.md
│  │     ├─ package.json
│  │     └─ README.md
│  ├─ desktop/
│  │  ├─ src/
│  │  │  ├─ main.tsx
│  │  │  └─ secure-local-store.ts
│  │  ├─ src-tauri/
│  │  │  ├─ capabilities/
│  │  │  │  └─ default.json
│  │  │  ├─ permissions/
│  │  │  │  └─ README.md
│  │  │  ├─ updater-signing/
│  │  │  │  └─ README.md
│  │  │  ├─ Cargo.toml
│  │  │  └─ tauri.conf.json
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ updater-signing/
│  │  │  └─ README.md
│  │  ├─ package.json
│  │  ├─ README.md
│  │  ├─ tsconfig.json
│  │  └─ vitest.config.ts
│  ├─ mobile/
│  │  ├─ app/
│  │  │  ├─ approvals/
│  │  │  │  └─ index.tsx
│  │  │  ├─ auth/
│  │  │  │  └─ login.tsx
│  │  │  ├─ banking/
│  │  │  │  └─ transactions.tsx
│  │  │  ├─ mfa/
│  │  │  │  └─ verify.tsx
│  │  │  ├─ _layout.tsx
│  │  │  └─ index.tsx
│  │  ├─ src/
│  │  │  ├─ biometric-unlock.ts
│  │  │  ├─ deep-links.ts
│  │  │  ├─ offline-queue.ts
│  │  │  ├─ push-notifications.ts
│  │  │  ├─ secure-storage.ts
│  │  │  └─ sync-conflicts.ts
│  │  ├─ tests/
│  │  │  └─ README.md
│  │  ├─ app.config.ts
│  │  ├─ eas.json
│  │  ├─ jest.config.ts
│  │  ├─ package.json
│  │  ├─ README.md
│  │  └─ tsconfig.json
│  ├─ portals/
│  │  ├─ customer-portal/
│  │  │  ├─ app/
│  │  │  │  ├─ documents/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ invoices/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ payments/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ profile/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ statements/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ support/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ layout.tsx
│  │  │  │  └─ page.tsx
│  │  │  ├─ tests/
│  │  │  │  └─ smoke.spec.ts
│  │  │  ├─ middleware.ts
│  │  │  ├─ next.config.mjs
│  │  │  ├─ package.json
│  │  │  ├─ README.md
│  │  │  └─ tsconfig.json
│  │  ├─ developer-oauth-consent/
│  │  │  ├─ app/
│  │  │  │  ├─ consent/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ errors/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ revocation/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ revoke/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ scopes/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ layout.tsx
│  │  │  │  └─ page.tsx
│  │  │  ├─ tests/
│  │  │  │  └─ smoke.spec.ts
│  │  │  ├─ middleware.ts
│  │  │  ├─ next.config.mjs
│  │  │  ├─ package.json
│  │  │  ├─ README.md
│  │  │  └─ tsconfig.json
│  │  ├─ employee-portal/
│  │  │  ├─ app/
│  │  │  │  ├─ approvals/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ documents/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ expenses/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ payslips/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ time/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ layout.tsx
│  │  │  │  └─ page.tsx
│  │  │  ├─ tests/
│  │  │  │  └─ smoke.spec.ts
│  │  │  ├─ middleware.ts
│  │  │  ├─ next.config.mjs
│  │  │  ├─ package.json
│  │  │  ├─ README.md
│  │  │  └─ tsconfig.json
│  │  ├─ firm-portal/
│  │  │  ├─ app/
│  │  │  │  ├─ approvals/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ clients/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ delegated-admin/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ exports/
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ layout.tsx
│  │  │  │  └─ page.tsx
│  │  │  ├─ tests/
│  │  │  │  └─ smoke.spec.ts
│  │  │  ├─ middleware.ts
│  │  │  ├─ next.config.mjs
│  │  │  ├─ package.json
│  │  │  ├─ README.md
│  │  │  └─ tsconfig.json
│  │  └─ vendor-portal/
│  │     ├─ app/
│  │     │  ├─ invoices/
│  │     │  │  └─ page.tsx
│  │     │  ├─ onboarding/
│  │     │  │  └─ page.tsx
│  │     │  ├─ payments/
│  │     │  │  └─ page.tsx
│  │     │  ├─ purchase-orders/
│  │     │  │  └─ page.tsx
│  │     │  ├─ tax-documents/
│  │     │  │  └─ page.tsx
│  │     │  ├─ layout.tsx
│  │     │  └─ page.tsx
│  │     ├─ tests/
│  │     │  └─ smoke.spec.ts
│  │     ├─ middleware.ts
│  │     ├─ next.config.mjs
│  │     ├─ package.json
│  │     ├─ README.md
│  │     └─ tsconfig.json
│  └─ web/
│     ├─ app/
│     │  ├─ (auth)/
│     │  │  ├─ callback/
│     │  │  │  └─ page.tsx
│     │  │  ├─ login/
│     │  │  │  └─ page.tsx
│     │  │  └─ mfa/
│     │  │     └─ page.tsx
│     │  ├─ (public)/
│     │  │  ├─ app-entry/
│     │  │  │  └─ page.tsx
│     │  │  ├─ bank-connectivity/
│     │  │  │  └─ page.tsx
│     │  │  ├─ contact-sales/
│     │  │  │  └─ page.tsx
│     │  │  ├─ demo/
│     │  │  │  └─ page.tsx
│     │  │  ├─ developers/
│     │  │  │  └─ page.tsx
│     │  │  ├─ docs/
│     │  │  │  └─ page.tsx
│     │  │  ├─ homepage/
│     │  │  │  └─ page.tsx
│     │  │  ├─ pricing/
│     │  │  │  └─ page.tsx
│     │  │  ├─ product/
│     │  │  │  └─ page.tsx
│     │  │  ├─ products/
│     │  │  │  └─ page.tsx
│     │  │  ├─ security-trust/
│     │  │  │  └─ page.tsx
│     │  │  ├─ status/
│     │  │  │  └─ page.tsx
│     │  │  └─ page.tsx
│     │  ├─ (shell)/
│     │  │  ├─ activity/
│     │  │  │  └─ page.tsx
│     │  │  ├─ dashboard/
│     │  │  │  └─ page.tsx
│     │  │  ├─ notifications/
│     │  │  │  └─ page.tsx
│     │  │  ├─ settings/
│     │  │  │  └─ page.tsx
│     │  │  └─ layout.tsx
│     │  ├─ accounting-sync/
│     │  │  └─ page.tsx
│     │  ├─ ai-accounting-drafts/
│     │  │  └─ page.tsx
│     │  ├─ ai-copilot/
│     │  │  └─ page.tsx
│     │  ├─ bank-connectivity-center/
│     │  │  ├─ accounts/
│     │  │  │  └─ page.tsx
│     │  │  ├─ balances/
│     │  │  │  └─ page.tsx
│     │  │  ├─ connections/
│     │  │  │  └─ page.tsx
│     │  │  ├─ consent-lifecycle/
│     │  │  │  └─ page.tsx
│     │  │  ├─ gl-cash-mapping/
│     │  │  │  └─ page.tsx
│     │  │  ├─ purpose-mapping/
│     │  │  │  └─ page.tsx
│     │  │  ├─ statements/
│     │  │  │  └─ page.tsx
│     │  │  ├─ support-matrix/
│     │  │  │  └─ page.tsx
│     │  │  ├─ sync-health/
│     │  │  │  └─ page.tsx
│     │  │  └─ transactions/
│     │  │     └─ page.tsx
│     │  ├─ commercial-lifecycle/
│     │  │  └─ page.tsx
│     │  ├─ connector-auth/
│     │  │  └─ page.tsx
│     │  ├─ customer-master/
│     │  │  └─ page.tsx
│     │  ├─ customer-operations/
│     │  │  └─ page.tsx
│     │  ├─ customer-portal-admin/
│     │  │  └─ page.tsx
│     │  ├─ customer-success/
│     │  │  └─ page.tsx
│     │  ├─ data-portability-center/
│     │  │  └─ page.tsx
│     │  ├─ developer-platform/
│     │  │  └─ page.tsx
│     │  ├─ finance-accounting/
│     │  │  ├─ chart-of-accounts/
│     │  │  │  └─ page.tsx
│     │  │  └─ fiscal-periods/
│     │  │     └─ page.tsx
│     │  ├─ finance-close/
│     │  │  └─ page.tsx
│     │  ├─ finance-operations/
│     │  │  ├─ bills/
│     │  │  │  └─ page.tsx
│     │  │  └─ invoices/
│     │  │     └─ page.tsx
│     │  ├─ integrations-platform/
│     │  │  └─ page.tsx
│     │  ├─ outbound-sync-center/
│     │  │  └─ page.tsx
│     │  ├─ payroll-benefits/
│     │  │  └─ page.tsx
│     │  ├─ platform-billing/
│     │  │  └─ page.tsx
│     │  ├─ procurement-spend/
│     │  │  └─ page.tsx
│     │  ├─ product-catalog/
│     │  │  └─ page.tsx
│     │  ├─ regional-bank-center/
│     │  │  └─ page.tsx
│     │  ├─ security-operations/
│     │  │  └─ page.tsx
│     │  ├─ spend-travel/
│     │  │  └─ page.tsx
│     │  ├─ vendor-master/
│     │  │  └─ page.tsx
│     │  ├─ workforce/
│     │  │  └─ page.tsx
│     │  ├─ globals.css
│     │  ├─ layout.tsx
│     │  └─ page.tsx
│     ├─ components/
│     │  ├─ app-shell/
│     │  │  └─ ShellLayout.tsx
│     │  ├─ audit-timeline/
│     │  │  └─ AuditTimeline.tsx
│     │  ├─ charts/
│     │  │  └─ RevenueChart.tsx
│     │  ├─ command-palette/
│     │  │  └─ CommandPalette.tsx
│     │  ├─ data-grid/
│     │  │  └─ DataGrid.tsx
│     │  ├─ forms/
│     │  │  └─ FinanceForm.tsx
│     │  ├─ sidebar/
│     │  │  └─ Sidebar.tsx
│     │  └─ top-nav/
│     │     └─ TopNav.tsx
│     ├─ lib/
│     │  ├─ otel-web.ts
│     │  └─ rum.ts
│     ├─ tests/
│     │  ├─ a11y/
│     │  │  └─ homepage.a11y.spec.ts
│     │  └─ e2e/
│     │     └─ smoke.spec.ts
│     ├─ instrumentation.ts
│     ├─ middleware.ts
│     ├─ next.config.mjs
│     ├─ package.json
│     ├─ playwright.config.ts
│     ├─ README.md
│     ├─ tsconfig.json
│     └─ vitest.config.ts
├─ cache/
│  ├─ key-guards/
│  │  └─ README.md
│  ├─ namespaces/
│  │  └─ README.md
│  ├─ ttl-policies/
│  │  └─ README.md
│  ├─ keying-contract.md
│  └─ README.md
├─ databases/
│  ├─ audit-db/
│  │  ├─ retention-policies/
│  │  │  └─ README.md
│  │  ├─ schemas/
│  │  │  └─ immutable_audit_events.sql
│  │  └─ README.md
│  ├─ operational-db/
│  │  ├─ constraints-and-indexes/
│  │  │  ├─ bank_account_gl_mapping_unique.sql
│  │  │  ├─ bank_transaction_dedup_unique.sql
│  │  │  ├─ double_entry_balance.sql
│  │  │  ├─ export_manifest_integrity.sql
│  │  │  ├─ immutable_posted_entries.sql
│  │  │  ├─ outbound_external_id_unique.sql
│  │  │  └─ period_lock_guards.sql
│  │  ├─ migrations/
│  │  │  └─ README.md
│  │  ├─ rls/
│  │  │  ├─ ai_retrieval_scope.sql
│  │  │  ├─ analytics_scope.sql
│  │  │  ├─ bank_account_scope.sql
│  │  │  ├─ bank_connection_scope.sql
│  │  │  ├─ books_scope.sql
│  │  │  ├─ company_scope.sql
│  │  │  ├─ cost_center_scope.sql
│  │  │  ├─ customer_portal_scope.sql
│  │  │  ├─ customer_scope.sql
│  │  │  ├─ delegated_admin_scope.sql
│  │  │  ├─ department_scope.sql
│  │  │  ├─ entity_scope.sql
│  │  │  ├─ export_job_scope.sql
│  │  │  ├─ firm_client_scope.sql
│  │  │  ├─ location_scope.sql
│  │  │  ├─ manager_scope.sql
│  │  │  ├─ open_banking_consent_scope.sql
│  │  │  ├─ outbound_sync_scope.sql
│  │  │  ├─ owner_scope.sql
│  │  │  ├─ platform_billing_scope.sql
│  │  │  ├─ public_api_consent_scope.sql
│  │  │  ├─ regional_bank_scope.sql
│  │  │  ├─ service_account_scope.sql
│  │  │  ├─ team_scope.sql
│  │  │  ├─ tenant_scope.sql
│  │  │  └─ vendor_scope.sql
│  │  ├─ schemas/
│  │  │  ├─ accounting-sync/
│  │  │  │  ├─ connections.sql
│  │  │  │  ├─ external_ids.sql
│  │  │  │  ├─ gl_account_external_mappings.sql
│  │  │  │  ├─ sync_cursors.sql
│  │  │  │  └─ sync_runs.sql
│  │  │  ├─ ai-accounting-drafts/
│  │  │  │  ├─ draft_approval_gates.sql
│  │  │  │  ├─ draft_entries.sql
│  │  │  │  ├─ draft_evidence.sql
│  │  │  │  └─ model_eval_results.sql
│  │  │  ├─ ai-copilot/
│  │  │  │  ├─ prompt_audit_logs.sql
│  │  │  │  ├─ prompts.sql
│  │  │  │  ├─ retrieval_acl_logs.sql
│  │  │  │  ├─ sessions.sql
│  │  │  │  └─ tool_calls.sql
│  │  │  ├─ approval-policy-engine/
│  │  │  │  ├─ approval_tasks.sql
│  │  │  │  ├─ workflow_steps.sql
│  │  │  │  └─ workflows.sql
│  │  │  ├─ authorization-policy/
│  │  │  │  ├─ policies.sql
│  │  │  │  ├─ policy_bindings.sql
│  │  │  │  └─ policy_simulations.sql
│  │  │  ├─ bank-connectivity/
│  │  │  │  ├─ bank_account_entity_books_mapping.sql
│  │  │  │  ├─ bank_account_gl_mapping.sql
│  │  │  │  ├─ bank_account_purpose_mapping.sql
│  │  │  │  ├─ bank_accounts.sql
│  │  │  │  ├─ bank_audit_trail.sql
│  │  │  │  ├─ bank_balances.sql
│  │  │  │  ├─ bank_connections.sql
│  │  │  │  ├─ bank_dedupe_keys.sql
│  │  │  │  ├─ bank_sync_checkpoints.sql
│  │  │  │  ├─ bank_sync_cursors.sql
│  │  │  │  ├─ bank_sync_health.sql
│  │  │  │  ├─ bank_transactions.sql
│  │  │  │  └─ bank_webhook_events.sql
│  │  │  ├─ bank-reconciliation/
│  │  │  │  ├─ reconciliation_bill_links.sql
│  │  │  │  ├─ reconciliation_exceptions.sql
│  │  │  │  ├─ reconciliation_expense_links.sql
│  │  │  │  ├─ reconciliation_invoice_links.sql
│  │  │  │  ├─ reconciliation_journal_links.sql
│  │  │  │  ├─ reconciliation_matches.sql
│  │  │  │  ├─ reconciliation_payroll_links.sql
│  │  │  │  ├─ reconciliation_rules.sql
│  │  │  │  ├─ reconciliation_settlement_links.sql
│  │  │  │  └─ reconciliation_tax_links.sql
│  │  │  ├─ commercial-lifecycle/
│  │  │  │  ├─ contract_amendments.sql
│  │  │  │  ├─ contracts.sql
│  │  │  │  ├─ order_links.sql
│  │  │  │  ├─ quote_lines.sql
│  │  │  │  ├─ quotes.sql
│  │  │  │  └─ renewals.sql
│  │  │  ├─ connector-auth/
│  │  │  │  ├─ connector_tokens.sql
│  │  │  │  ├─ oauth_clients.sql
│  │  │  │  ├─ oauth_states.sql
│  │  │  │  └─ token_rotation_audit.sql
│  │  │  ├─ core/
│  │  │  │  ├─ audit_log.sql
│  │  │  │  ├─ extensions.sql
│  │  │  │  ├─ idempotency_keys.sql
│  │  │  │  └─ outbox.sql
│  │  │  ├─ customer-master/
│  │  │  │  ├─ customer_addresses.sql
│  │  │  │  ├─ customer_contacts.sql
│  │  │  │  ├─ customer_credit_limits.sql
│  │  │  │  ├─ customer_external_ids.sql
│  │  │  │  ├─ customer_health_scores.sql
│  │  │  │  ├─ customer_merge_jobs.sql
│  │  │  │  ├─ customer_payment_terms.sql
│  │  │  │  ├─ customer_statements.sql
│  │  │  │  ├─ customer_tax_profiles.sql
│  │  │  │  └─ customers.sql
│  │  │  ├─ customer-operations/
│  │  │  │  ├─ sla_policies.sql
│  │  │  │  ├─ support_tickets.sql
│  │  │  │  └─ ticket_messages.sql
│  │  │  ├─ data-portability/
│  │  │  │  ├─ checksums.sql
│  │  │  │  ├─ download_grants.sql
│  │  │  │  ├─ encryption_keys.sql
│  │  │  │  ├─ expiry_policies.sql
│  │  │  │  ├─ export_jobs.sql
│  │  │  │  ├─ export_scopes.sql
│  │  │  │  └─ manifests.sql
│  │  │  ├─ finance-accounting/
│  │  │  │  ├─ chart_of_accounts.sql
│  │  │  │  ├─ currencies.sql
│  │  │  │  ├─ fiscal_periods.sql
│  │  │  │  ├─ fx_rates.sql
│  │  │  │  ├─ fx_revaluation_runs.sql
│  │  │  │  ├─ gl_book_settings.sql
│  │  │  │  ├─ intercompany_eliminations.sql
│  │  │  │  ├─ period_locks.sql
│  │  │  │  ├─ tax_codes.sql
│  │  │  │  └─ tracking_categories.sql
│  │  │  ├─ finance-close/
│  │  │  │  ├─ close_checklists.sql
│  │  │  │  ├─ close_evidence.sql
│  │  │  │  └─ close_tasks.sql
│  │  │  ├─ finance-operations/
│  │  │  │  ├─ bills.sql
│  │  │  │  ├─ credits.sql
│  │  │  │  ├─ dunning.sql
│  │  │  │  ├─ invoices.sql
│  │  │  │  ├─ payment_links.sql
│  │  │  │  ├─ payments.sql
│  │  │  │  ├─ recurring_bills.sql
│  │  │  │  ├─ recurring_invoices.sql
│  │  │  │  └─ revenue_recognition.sql
│  │  │  ├─ identity-governance/
│  │  │  │  ├─ access_reviews.sql
│  │  │  │  ├─ custom_roles.sql
│  │  │  │  ├─ delegated_admin_boundaries.sql
│  │  │  │  ├─ firm_client_relationships.sql
│  │  │  │  ├─ permissions.sql
│  │  │  │  ├─ roles.sql
│  │  │  │  ├─ service_accounts.sql
│  │  │  │  └─ users.sql
│  │  │  ├─ integrations-platform/
│  │  │  │  ├─ integration_catalog.sql
│  │  │  │  ├─ integration_events.sql
│  │  │  │  ├─ integration_health.sql
│  │  │  │  └─ integration_instances.sql
│  │  │  ├─ ledger-integrity/
│  │  │  │  ├─ journal_entries.sql
│  │  │  │  ├─ journal_lines.sql
│  │  │  │  ├─ ledgers.sql
│  │  │  │  ├─ posting_batches.sql
│  │  │  │  ├─ reconciliation_links.sql
│  │  │  │  ├─ retained_earnings_rollforward.sql
│  │  │  │  └─ trial_balance_snapshots.sql
│  │  │  ├─ manual-bank-imports/
│  │  │  │  ├─ import_batches.sql
│  │  │  │  ├─ import_dedup_links.sql
│  │  │  │  ├─ import_errors.sql
│  │  │  │  ├─ import_files.sql
│  │  │  │  ├─ import_formats.sql
│  │  │  │  └─ import_parse_results.sql
│  │  │  ├─ open-banking/
│  │  │  │  ├─ open_banking_consent_scopes.sql
│  │  │  │  ├─ open_banking_consents.sql
│  │  │  │  ├─ open_banking_providers.sql
│  │  │  │  ├─ open_banking_reauthorizations.sql
│  │  │  │  ├─ open_banking_revocations.sql
│  │  │  │  └─ open_banking_token_lifecycle.sql
│  │  │  ├─ organization-graph/
│  │  │  │  ├─ books.sql
│  │  │  │  ├─ companies.sql
│  │  │  │  ├─ cost_centers.sql
│  │  │  │  ├─ departments.sql
│  │  │  │  ├─ entities.sql
│  │  │  │  ├─ locations.sql
│  │  │  │  ├─ managers.sql
│  │  │  │  ├─ project_assignments.sql
│  │  │  │  ├─ projects.sql
│  │  │  │  ├─ reporting_lines.sql
│  │  │  │  └─ teams.sql
│  │  │  ├─ outbound-sync/
│  │  │  │  ├─ conflicts.sql
│  │  │  │  ├─ dead_letters.sql
│  │  │  │  ├─ destination_connections.sql
│  │  │  │  ├─ dry_runs.sql
│  │  │  │  ├─ external_id_registry.sql
│  │  │  │  ├─ mapping_profiles.sql
│  │  │  │  ├─ sync_runs.sql
│  │  │  │  └─ tombstones.sql
│  │  │  ├─ payroll-benefits/
│  │  │  │  ├─ benefits_enrollments.sql
│  │  │  │  ├─ eor_contracts.sql
│  │  │  │  ├─ offboarding_revocations.sql
│  │  │  │  ├─ payroll_runs.sql
│  │  │  │  └─ payroll_tax_items.sql
│  │  │  ├─ platform-billing/
│  │  │  │  ├─ add_ons.sql
│  │  │  │  ├─ billing_portal_sessions.sql
│  │  │  │  ├─ entitlements.sql
│  │  │  │  ├─ overages.sql
│  │  │  │  ├─ plans.sql
│  │  │  │  ├─ platform_invoices.sql
│  │  │  │  ├─ subscriptions.sql
│  │  │  │  ├─ tax_lines.sql
│  │  │  │  ├─ trials.sql
│  │  │  │  ├─ usage_events.sql
│  │  │  │  └─ usage_meters.sql
│  │  │  ├─ procurement-spend/
│  │  │  │  ├─ budgets.sql
│  │  │  │  ├─ purchase_orders.sql
│  │  │  │  ├─ receipts.sql
│  │  │  │  ├─ requisitions.sql
│  │  │  │  └─ spend_policies.sql
│  │  │  ├─ product-catalog/
│  │  │  │  ├─ price_books.sql
│  │  │  │  ├─ prices.sql
│  │  │  │  ├─ product_families.sql
│  │  │  │  ├─ products.sql
│  │  │  │  └─ taxability_rules.sql
│  │  │  ├─ public-api-platform/
│  │  │  │  ├─ api_keys.sql
│  │  │  │  ├─ consent_grants.sql
│  │  │  │  ├─ partner_apps.sql
│  │  │  │  ├─ rate_limit_ledgers.sql
│  │  │  │  ├─ usage_logs.sql
│  │  │  │  └─ webhook_subscriptions.sql
│  │  │  ├─ regional-bank-connectivity/
│  │  │  │  ├─ regional_bank_channels.sql
│  │  │  │  ├─ regional_bank_credentials_requirements.sql
│  │  │  │  ├─ regional_bank_fallback_paths.sql
│  │  │  │  ├─ regional_bank_legal_review_flags.sql
│  │  │  │  ├─ regional_bank_limitations.sql
│  │  │  │  ├─ regional_bank_support_matrix.sql
│  │  │  │  └─ regional_banks_catalog.sql
│  │  │  ├─ security-operations/
│  │  │  │  ├─ evidence_links.sql
│  │  │  │  ├─ incident_cases.sql
│  │  │  │  └─ security_alerts.sql
│  │  │  ├─ spend-travel/
│  │  │  │  ├─ card_transactions.sql
│  │  │  │  ├─ expense_reports.sql
│  │  │  │  ├─ mileage_entries.sql
│  │  │  │  └─ trips.sql
│  │  │  ├─ tenancy/
│  │  │  │  ├─ tenant_entitlements.sql
│  │  │  │  ├─ tenant_settings.sql
│  │  │  │  └─ tenants.sql
│  │  │  ├─ vendor-master/
│  │  │  │  ├─ vendor_addresses.sql
│  │  │  │  ├─ vendor_contacts.sql
│  │  │  │  ├─ vendor_external_ids.sql
│  │  │  │  ├─ vendor_payment_terms.sql
│  │  │  │  ├─ vendor_tax_profiles.sql
│  │  │  │  └─ vendors.sql
│  │  │  └─ workforce/
│  │  │     ├─ attendance.sql
│  │  │     ├─ compensation.sql
│  │  │     ├─ contractors.sql
│  │  │     ├─ employees.sql
│  │  │     ├─ learning.sql
│  │  │     ├─ leave_requests.sql
│  │  │     ├─ recruiting.sql
│  │  │     └─ schedules.sql
│  │  ├─ seeds/
│  │  │  └─ README.md
│  │  └─ README.md
│  ├─ search/
│  │  ├─ acl-filters/
│  │  │  └─ README.md
│  │  └─ indices/
│  │     └─ README.md
│  ├─ search-index/
│  │  ├─ mappings/
│  │  │  └─ README.md
│  │  └─ README.md
│  ├─ vector-store/
│  │  ├─ acl-filters/
│  │  │  └─ README.md
│  │  ├─ namespaces/
│  │  │  └─ README.md
│  │  ├─ retrieval-policies/
│  │  │  └─ README.md
│  │  ├─ collections-policy.md
│  │  └─ README.md
│  ├─ warehouse/
│  │  ├─ models/
│  │  │  └─ README.md
│  │  └─ README.md
│  └─ README.md
├─ developer-platform/
│  ├─ portal/
│  │  ├─ docs/
│  │  │  ├─ app-review.md
│  │  │  ├─ changelog-deprecation.md
│  │  │  ├─ getting-started.md
│  │  │  ├─ idempotency-examples.md
│  │  │  ├─ idempotency.md
│  │  │  ├─ oauth-app-registration.md
│  │  │  ├─ oauth-apps.md
│  │  │  ├─ rate-limit-examples.md
│  │  │  ├─ rate-limits.md
│  │  │  ├─ README.md
│  │  │  ├─ sandbox-tenants.md
│  │  │  ├─ scopes.md
│  │  │  └─ webhook-testing.md
│  │  └─ sandbox-tenants/
│  │     └─ README.md
│  ├─ sdk/
│  │  ├─ dotnet/
│  │  │  ├─ examples/
│  │  │  │  └─ README.md
│  │  │  ├─ generated-client/
│  │  │  │  └─ README.md
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  └─ README.md
│  │  ├─ go/
│  │  │  ├─ examples/
│  │  │  │  └─ README.md
│  │  │  ├─ generated-client/
│  │  │  │  └─ README.md
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  └─ README.md
│  │  ├─ java/
│  │  │  ├─ examples/
│  │  │  │  └─ README.md
│  │  │  ├─ generated-client/
│  │  │  │  └─ README.md
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  └─ README.md
│  │  ├─ python/
│  │  │  ├─ examples/
│  │  │  │  └─ README.md
│  │  │  ├─ generated-client/
│  │  │  │  └─ README.md
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  └─ README.md
│  │  └─ typescript/
│  │     ├─ examples/
│  │     │  └─ README.md
│  │     ├─ generated-client/
│  │     │  └─ README.md
│  │     ├─ tests/
│  │     │  └─ README.md
│  │     └─ README.md
│  ├─ tests/
│  │  └─ README.md
│  └─ README.md
├─ docs/
│  ├─ architecture/
│  │  ├─ ai-accounting-drafts.md
│  │  ├─ ai-copilot.md
│  │  ├─ ai-governance.md
│  │  ├─ ap-payment-automation.md
│  │  ├─ api-versioning-compatibility.md
│  │  ├─ approval-policy-engine.md
│  │  ├─ authorization-policy.md
│  │  ├─ bank-account-purpose-mapping.md
│  │  ├─ bank-connectivity-platform.md
│  │  ├─ bank-feed-reconciliation.md
│  │  ├─ bank-statement-imports.md
│  │  ├─ cache-isolation.md
│  │  ├─ cash-liquidity-forecasting.md
│  │  ├─ cisa-secure-by-design-mapping.md
│  │  ├─ commercial-lifecycle.md
│  │  ├─ connector-auth.md
│  │  ├─ core-web-vitals-policy.md
│  │  ├─ customer-lifecycle.md
│  │  ├─ customer-master.md
│  │  ├─ customer-portal.md
│  │  ├─ customer-success-operations.md
│  │  ├─ dashboard-and-metrics.md
│  │  ├─ data-portability.md
│  │  ├─ DATABASE_SCHEMA_PLAN.md
│  │  ├─ deterministic-accounting.md
│  │  ├─ DOMAIN_MODEL.md
│  │  ├─ dsar-retention-legal-hold.md
│  │  ├─ export-package-format.md
│  │  ├─ finance-accounting.md
│  │  ├─ finance-close.md
│  │  ├─ finance-operations.md
│  │  ├─ financial-reporting.md
│  │  ├─ fiscal-calendars-period-locks.md
│  │  ├─ fixed-assets-leases.md
│  │  ├─ frontend-performance-budgets.md
│  │  ├─ gdpr-article-20-portability.md
│  │  ├─ identity-governance.md
│  │  ├─ IMPLEMENTATION_EXECUTION_PLAN.md
│  │  ├─ IMPLEMENTATION_PHASES.md
│  │  ├─ integrations-platform.md
│  │  ├─ intercompany-and-consolidation.md
│  │  ├─ isolation-model.md
│  │  ├─ ledger-integrity.md
│  │  ├─ multi-currency-fx-revaluation.md
│  │  ├─ MULTI_BANK_CONNECTIVITY.md
│  │  ├─ nist-csf-2-mapping.md
│  │  ├─ observability-standard.md
│  │  ├─ open-banking-psd2-connectivity.md
│  │  ├─ organization-graph.md
│  │  ├─ outbound-sync-strategy.md
│  │  ├─ owasp-asvs-mapping.md
│  │  ├─ owasp-top10-controls.md
│  │  ├─ partner-app-platform.md
│  │  ├─ payroll-benefits.md
│  │  ├─ performance-architecture.md
│  │  ├─ PHASE_0_GOVERNANCE_DECISIONS.md
│  │  ├─ platform-billing-metering.md
│  │  ├─ PLATFORM_TREE.md
│  │  ├─ platform_tree_manifest.json
│  │  ├─ posting-engine.md
│  │  ├─ procurement-spend.md
│  │  ├─ product-catalog.md
│  │  ├─ PRODUCT_SCOPE.md
│  │  ├─ public-api-platform.md
│  │  ├─ query-plan-regression-policy.md
│  │  ├─ queue-backpressure-policy.md
│  │  ├─ regional-bank-connectivity.md
│  │  ├─ rls-enforcement-matrix.md
│  │  ├─ rounding-and-money-types.md
│  │  ├─ sanctions-regional-bank-review.md
│  │  ├─ security-architecture.md
│  │  ├─ security-baseline.md
│  │  ├─ session-context-variables.md
│  │  ├─ spend-travel.md
│  │  ├─ subledger-to-gl-reconciliation.md
│  │  ├─ tax-engine-localization.md
│  │  ├─ treasury-debt-credit.md
│  │  ├─ trial-balance-and-retained-earnings.md
│  │  ├─ UI_STACK.md
│  │  ├─ vendor-master.md
│  │  ├─ webhook-subscription-model.md
│  │  └─ workforce.md
│  ├─ compliance/
│  │  ├─ data-residency-policy.md
│  │  ├─ data-residency.md
│  │  ├─ gdpr-dsar-runbook.md
│  │  ├─ gdpr-dsar.md
│  │  ├─ iso27001-control-map.md
│  │  ├─ iso27001-controls.md
│  │  ├─ pci-scope-notes.md
│  │  ├─ retention-legal-hold-policy.md
│  │  ├─ retention-legal-hold.md
│  │  ├─ sanctions-regional-bank-review.md
│  │  ├─ sanctions-review-policy.md
│  │  ├─ soc2-evidence-map.md
│  │  ├─ soc2-evidence.md
│  │  └─ subprocessors.md
│  ├─ providers/
│  │  ├─ accounting-sync/
│  │  │  ├─ acumatica.md
│  │  │  ├─ apideck.md
│  │  │  ├─ bill.md
│  │  │  ├─ codat.md
│  │  │  ├─ dynamics-business-central.md
│  │  │  ├─ freshbooks.md
│  │  │  ├─ netsuite.md
│  │  │  ├─ quickbooks-desktop.md
│  │  │  ├─ quickbooks-online.md
│  │  │  ├─ README.md
│  │  │  ├─ rutter.md
│  │  │  ├─ sage-intacct.md
│  │  │  └─ xero.md
│  │  ├─ bank-feeds/
│  │  │  ├─ gocardless.md
│  │  │  ├─ mercury.md
│  │  │  ├─ plaid.md
│  │  │  ├─ README.md
│  │  │  ├─ stripe-financial-connections.md
│  │  │  ├─ stripe-treasury.md
│  │  │  ├─ teller.md
│  │  │  ├─ truelayer.md
│  │  │  └─ wise.md
│  │  ├─ crm-commerce-support/
│  │  │  ├─ amazon-seller.md
│  │  │  ├─ hubspot.md
│  │  │  ├─ intercom.md
│  │  │  ├─ README.md
│  │  │  ├─ salesforce.md
│  │  │  ├─ shopify.md
│  │  │  ├─ woocommerce.md
│  │  │  └─ zendesk.md
│  │  ├─ hr-payroll/
│  │  │  ├─ adp.md
│  │  │  ├─ bamboohr.md
│  │  │  ├─ checkr.md
│  │  │  ├─ deel.md
│  │  │  ├─ greenhouse.md
│  │  │  ├─ gusto.md
│  │  │  ├─ lever.md
│  │  │  ├─ README.md
│  │  │  ├─ rippling.md
│  │  │  └─ workday.md
│  │  ├─ outbound-destinations/
│  │  │  ├─ acumatica.md
│  │  │  ├─ apideck.md
│  │  │  ├─ bill.md
│  │  │  ├─ codat.md
│  │  │  ├─ dynamics-business-central.md
│  │  │  ├─ freshbooks.md
│  │  │  ├─ netsuite.md
│  │  │  ├─ quickbooks-desktop.md
│  │  │  ├─ quickbooks-online.md
│  │  │  ├─ README.md
│  │  │  ├─ rutter.md
│  │  │  ├─ sage-intacct.md
│  │  │  └─ xero.md
│  │  ├─ regional-banks/
│  │  │  ├─ bulgaria/
│  │  │  │  ├─ d-bank.md
│  │  │  │  ├─ dsk-bank.md
│  │  │  │  ├─ fibank.md
│  │  │  │  └─ postbank.md
│  │  │  ├─ canada/
│  │  │  │  ├─ rbc.md
│  │  │  │  ├─ scotiabank.md
│  │  │  │  └─ td.md
│  │  │  ├─ croatia/
│  │  │  │  ├─ erste-croatia.md
│  │  │  │  ├─ otp-croatia.md
│  │  │  │  ├─ pbz.md
│  │  │  │  └─ zagrebacka-banka.md
│  │  │  ├─ greece/
│  │  │  │  ├─ alpha-bank.md
│  │  │  │  ├─ attica-bank.md
│  │  │  │  ├─ eurobank.md
│  │  │  │  ├─ national-bank-of-greece.md
│  │  │  │  └─ piraeus-bank.md
│  │  │  ├─ india/
│  │  │  │  ├─ axis.md
│  │  │  │  ├─ hdfc.md
│  │  │  │  └─ icici.md
│  │  │  ├─ mexico/
│  │  │  │  ├─ banorte.md
│  │  │  │  ├─ bbva-mexico.md
│  │  │  │  └─ santander-mexico.md
│  │  │  ├─ montenegro/
│  │  │  │  ├─ ckb.md
│  │  │  │  ├─ hipotekarna-banka.md
│  │  │  │  └─ nlb-montenegro.md
│  │  │  ├─ north-macedonia/
│  │  │  │  ├─ halkbank-ad-skopje.md
│  │  │  │  ├─ kdb-bank.md
│  │  │  │  ├─ komercijalna-banka-skopje.md
│  │  │  │  ├─ nlb-banka-skopje.md
│  │  │  │  └─ sparkasse-ad-skopje.md
│  │  │  ├─ poland/
│  │  │  │  ├─ bank-pekao.md
│  │  │  │  ├─ mbank.md
│  │  │  │  ├─ pko-bp.md
│  │  │  │  └─ santander-polska.md
│  │  │  ├─ russia/
│  │  │  │  └─ disabled-legal-review.md
│  │  │  ├─ serbia/
│  │  │  │  ├─ banca-intesa-serbia.md
│  │  │  │  ├─ erste-serbia.md
│  │  │  │  ├─ otp-serbia.md
│  │  │  │  └─ raiffeisen-serbia.md
│  │  │  ├─ singapore-hongkong-asia/
│  │  │  │  ├─ dbs.md
│  │  │  │  ├─ hsbc.md
│  │  │  │  ├─ ocbc.md
│  │  │  │  └─ standard-chartered.md
│  │  │  ├─ turkey/
│  │  │  │  ├─ akbank.md
│  │  │  │  ├─ garanti-bbva.md
│  │  │  │  ├─ isbank.md
│  │  │  │  └─ yapi-kredi.md
│  │  │  ├─ README.md
│  │  │  ├─ REGIONAL_BANK_TEMPLATE.md
│  │  │  └─ support-statuses.md
│  │  ├─ spend/
│  │  │  ├─ brex.md
│  │  │  ├─ expensify.md
│  │  │  ├─ navan.md
│  │  │  ├─ ramp.md
│  │  │  ├─ README.md
│  │  │  ├─ rho.md
│  │  │  └─ sap-concur.md
│  │  ├─ unified-api/
│  │  │  ├─ apideck.md
│  │  │  ├─ bill.md
│  │  │  ├─ codat.md
│  │  │  └─ rutter.md
│  │  ├─ workspace-productivity/
│  │  │  ├─ box.md
│  │  │  ├─ calendly.md
│  │  │  ├─ docusign.md
│  │  │  ├─ dropbox.md
│  │  │  ├─ entra-id.md
│  │  │  ├─ github.md
│  │  │  ├─ google-workspace.md
│  │  │  ├─ jira.md
│  │  │  ├─ microsoft-graph.md
│  │  │  ├─ notion.md
│  │  │  ├─ README.md
│  │  │  ├─ slack.md
│  │  │  ├─ teams.md
│  │  │  └─ zoom.md
│  │  └─ support-statuses.md
│  ├─ public-api/
│  │  ├─ guides/
│  │  │  ├─ api-keys.md
│  │  │  ├─ authentication.md
│  │  │  ├─ deprecation-policy.md
│  │  │  ├─ idempotency.md
│  │  │  ├─ pagination.md
│  │  │  ├─ rate-limits.md
│  │  │  ├─ scopes.md
│  │  │  └─ webhooks.md
│  │  ├─ openapi/
│  │  │  ├─ changelog.md
│  │  │  └─ v1.openapi.yaml
│  │  └─ README.md
│  └─ runbooks/
│     ├─ bank-consent-lifecycle.md
│     ├─ ledger-integrity-incident.md
│     ├─ multi-bank-onboarding.md
│     ├─ outbound-sync-replay.md
│     ├─ period-close-exception.md
│     ├─ README.md
│     ├─ reconciliation-exceptions.md
│     ├─ runbook-registry.md
│     ├─ security-incident-response.md
│     └─ statement-import-fallback.md
├─ infra/
│  ├─ backup-restore/
│  │  └─ README.md
│  ├─ ci-cd/
│  │  └─ README.md
│  ├─ disaster-recovery/
│  │  └─ README.md
│  ├─ helm/
│  │  └─ README.md
│  ├─ kubernetes/
│  │  └─ README.md
│  ├─ local-dev/
│  │  └─ README.md
│  ├─ networking/
│  │  └─ README.md
│  ├─ performance/
│  │  └─ README.md
│  ├─ release-rollback/
│  │  └─ README.md
│  ├─ runbook-registry/
│  │  └─ README.md
│  ├─ security/
│  │  └─ README.md
│  ├─ terraform/
│  │  └─ README.md
│  └─ README.md
├─ object-storage/
│  ├─ attachments/
│  │  └─ README.md
│  ├─ bank-statements/
│  │  └─ README.md
│  ├─ billing-artifacts/
│  │  └─ README.md
│  ├─ export-packages/
│  │  └─ README.md
│  ├─ import-uploads/
│  │  └─ README.md
│  ├─ legal-hold/
│  │  └─ README.md
│  ├─ lifecycle-policies/
│  │  └─ README.md
│  ├─ lifecycle-rules/
│  │  └─ README.md
│  ├─ reconciliation-artifacts/
│  │  └─ README.md
│  ├─ README.md
│  └─ tenant-prefix-contract.md
├─ observability/
│  ├─ alerts/
│  │  └─ README.md
│  ├─ dashboards/
│  │  └─ README.md
│  ├─ grafana/
│  │  └─ README.md
│  ├─ logs/
│  │  └─ README.md
│  ├─ metrics/
│  │  └─ README.md
│  ├─ opentelemetry/
│  │  ├─ collector-config.yaml
│  │  └─ README.md
│  ├─ otel-collector/
│  │  └─ README.md
│  ├─ rum/
│  │  └─ README.md
│  ├─ runbook-index/
│  │  └─ README.md
│  ├─ runbook-links/
│  │  └─ README.md
│  ├─ slo/
│  │  ├─ burn-rate-alerts/
│  │  │  └─ README.md
│  │  ├─ error-budget-policies/
│  │  │  └─ README.md
│  │  ├─ service-level-objectives/
│  │  │  └─ README.md
│  │  └─ README.md
│  ├─ slo-error-budgets/
│  │  ├─ error-budget-policy.md
│  │  ├─ README.md
│  │  └─ slo-definitions.yaml
│  ├─ traces/
│  │  └─ README.md
│  └─ README.md
├─ packages/
│  ├─ accessibility-rules/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ accounting-canonical-model/
│  │  ├─ src/
│  │  │  └─ index.ts
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ api-client/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ app-shell/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ audit-timeline-ui/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ bank-connectivity-core/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ bank-consent-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ bank-reconciliation-core/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ bank-transaction-normalization/
│  │  ├─ src/
│  │  │  └─ index.ts
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ charting/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ commercial-lifecycle-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ customer-master-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ customer-portal-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ customer-success-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ data-grid/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ data-portability-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ dedupe-key-engine/
│  │  ├─ src/
│  │  │  └─ index.ts
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ design-tokens/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ destination-mapping-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ export-package-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ form-engine/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ isolation-context/
│  │  ├─ src/
│  │  │  └─ index.ts
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ ledger-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ money-math/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ navigation-model/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ oauth-provider-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ observability/
│  │  ├─ src/
│  │  │  └─ index.ts
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ open-banking-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ outbound-sync-core/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ payroll-benefits-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ permission-guards/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ platform-billing-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ posting-engine-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ product-catalog-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ public-api-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ reconciliation-matching-core/
│  │  ├─ src/
│  │  │  └─ index.ts
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ regional-bank-adapter-kit/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ regional-bank-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ statement-parser-camt053/
│  │  ├─ src/
│  │  │  └─ index.ts
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ statement-parser-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ statement-parser-csv-xlsx/
│  │  ├─ src/
│  │  │  └─ index.ts
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ statement-parser-fixtures/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ statement-parser-mt940/
│  │  ├─ src/
│  │  │  └─ index.ts
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ statement-parser-ofx-qfx/
│  │  ├─ src/
│  │  │  └─ index.ts
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ sync-status-ui/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ tax-engine-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ testing-fixtures/
│  │  ├─ src/
│  │  │  └─ index.ts
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ ui-desktop-kit/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ ui-finance/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ ui-kit/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ ui-mobile-kit/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ vendor-master-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  ├─ webhook-contracts/
│  │  ├─ package.json
│  │  └─ README.md
│  └─ workflow-ui/
│     ├─ package.json
│     └─ README.md
├─ platform/
│  ├─ backup-restore/
│  │  ├─ README.md
│  │  └─ rpo-rto.md
│  ├─ disaster-recovery/
│  │  ├─ dr-plan.md
│  │  └─ README.md
│  ├─ environment-management/
│  │  ├─ environments.yaml
│  │  └─ README.md
│  ├─ feature-flags/
│  │  └─ README.md
│  ├─ job-orchestration/
│  │  ├─ dag-definitions.yaml
│  │  └─ README.md
│  ├─ messaging/
│  │  └─ README.md
│  ├─ queues/
│  │  ├─ queue-topology.md
│  │  └─ README.md
│  ├─ release-rollback/
│  │  ├─ README.md
│  │  └─ rollback-policy.md
│  ├─ runbook-registry/
│  │  ├─ index.md
│  │  └─ README.md
│  ├─ runtime/
│  │  ├─ backup-restore/
│  │  │  └─ README.md
│  │  ├─ disaster-recovery/
│  │  │  └─ README.md
│  │  ├─ environment-management/
│  │  │  └─ README.md
│  │  ├─ feature-flags/
│  │  │  └─ README.md
│  │  ├─ job-orchestration/
│  │  │  └─ README.md
│  │  ├─ queues/
│  │  │  └─ README.md
│  │  ├─ release-rollback/
│  │  │  └─ README.md
│  │  ├─ runbook-registry/
│  │  │  └─ README.md
│  │  ├─ secrets-injection/
│  │  │  └─ README.md
│  │  ├─ service-catalog/
│  │  │  └─ README.md
│  │  ├─ tenant-provisioning/
│  │  │  └─ README.md
│  │  ├─ workflow-schedules/
│  │  │  └─ README.md
│  │  └─ README.md
│  ├─ secrets-injection/
│  │  ├─ injection-contract.md
│  │  └─ README.md
│  ├─ secrets-integration/
│  │  └─ README.md
│  ├─ service-catalog/
│  │  ├─ README.md
│  │  └─ services.yaml
│  ├─ tenant-provisioning/
│  │  ├─ provisioning-runbook.md
│  │  └─ README.md
│  ├─ workflow/
│  │  └─ README.md
│  ├─ workflow-schedules/
│  │  ├─ README.md
│  │  └─ schedules.yaml
│  └─ README.md
├─ policies/
│  ├─ iam/
│  │  ├─ aws/
│  │  │  └─ README.md
│  │  ├─ gcp/
│  │  │  └─ README.md
│  │  └─ README.md
│  ├─ opa/
│  │  ├─ ai-retrieval/
│  │  │  ├─ README.md
│  │  │  └─ retrieval_acl.rego
│  │  ├─ approval-policy-engine/
│  │  │  ├─ approval_policy.rego
│  │  │  └─ README.md
│  │  ├─ bank-connectivity/
│  │  │  ├─ bank_account_access.rego
│  │  │  └─ README.md
│  │  ├─ data-portability/
│  │  │  ├─ export_scope.rego
│  │  │  └─ README.md
│  │  ├─ outbound-sync/
│  │  │  ├─ entitlement.rego
│  │  │  └─ README.md
│  │  ├─ platform-billing/
│  │  │  ├─ billing_entitlement.rego
│  │  │  └─ README.md
│  │  └─ public-api/
│  │     ├─ consent_scope.rego
│  │     ├─ partner_app.rego
│  │     └─ README.md
│  ├─ access-control.md
│  ├─ dashboard-access.md
│  ├─ data-classification.md
│  ├─ README.md
│  └─ vendor-risk.md
├─ scripts/
│  ├─ create_physical_tree.py
│  ├─ generate_platform_tree_md.py
│  └─ validate_platform_tree.py
├─ search/
│  ├─ acl-filters/
│  │  └─ README.md
│  └─ indices/
│     └─ README.md
├─ secrets/
│  ├─ rotation-runbooks/
│  │  └─ README.md
│  ├─ templates/
│  │  └─ README.md
│  ├─ breakglass-procedure.md
│  ├─ README.md
│  └─ rotation-checklist.md
├─ security/
│  ├─ abuse-detection/
│  │  └─ README.md
│  ├─ incident-response/
│  │  └─ README.md
│  ├─ kms-hsm/
│  │  └─ README.md
│  ├─ policies-as-code/
│  │  └─ README.md
│  ├─ scanners/
│  │  └─ README.md
│  ├─ secret-management/
│  │  └─ README.md
│  ├─ supply-chain-security/
│  │  └─ README.md
│  ├─ threat-models/
│  │  └─ README.md
│  ├─ token-vaulting/
│  │  └─ README.md
│  ├─ webhook-signing/
│  │  └─ README.md
│  ├─ README.md
│  └─ secure-sdlc.md
├─ services/
│  ├─ accounting-sync-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ ai-accounting-drafts-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ ai-copilot-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ analytics-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ audit-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-connectivity-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-reconciliation-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ commercial-lifecycle-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ connector-auth-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ customer-master-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ customer-portal-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ customer-success-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ data-portability-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ destination-mapping-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ developer-app-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ export-package-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ finance-accounting-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ finance-close-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ finance-operations-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ integrations-orchestration-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ integrations-platform-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ ledger-integrity-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ oauth-provider-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ open-banking-consent-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ outbound-sync-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ payroll-benefits-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ platform-billing-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ posting-engine-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ procurement-spend-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ product-catalog-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ public-api-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-connectivity-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ search-index-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ search-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ security-operations-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ spend-travel-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ vendor-master-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ warehouse-sync-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ webhook-delivery-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workforce-service/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  └─ README.md
├─ tests/
│  ├─ accessibility/
│  │  └─ README.md
│  ├─ ai-governance/
│  │  ├─ evidence-controls/
│  │  │  └─ README.md
│  │  ├─ hallucination-guards/
│  │  │  └─ README.md
│  │  ├─ prompt-audit/
│  │  │  └─ README.md
│  │  ├─ red-team/
│  │  │  └─ README.md
│  │  └─ retrieval-acl/
│  │     └─ README.md
│  ├─ bank-connectivity/
│  │  └─ README.md
│  ├─ bank-consent-lifecycle/
│  │  └─ README.md
│  ├─ bank-reconciliation/
│  │  └─ README.md
│  ├─ commercial-lifecycle/
│  │  └─ README.md
│  ├─ contract/
│  │  └─ README.md
│  ├─ customer-master/
│  │  └─ README.md
│  ├─ customer-portal/
│  │  └─ README.md
│  ├─ customer-success/
│  │  └─ README.md
│  ├─ data-portability/
│  │  ├─ manifest/
│  │  │  └─ README.md
│  │  └─ README.md
│  ├─ desktop-e2e/
│  │  └─ README.md
│  ├─ integration/
│  │  └─ README.md
│  ├─ ledger-integrity/
│  │  └─ README.md
│  ├─ load/
│  │  └─ README.md
│  ├─ mobile-e2e/
│  │  └─ README.md
│  ├─ money-math/
│  │  └─ README.md
│  ├─ multi-bank-company-scope/
│  │  └─ README.md
│  ├─ outbound-sync/
│  │  ├─ dry-run/
│  │  │  └─ README.md
│  │  └─ README.md
│  ├─ payroll-benefits/
│  │  └─ README.md
│  ├─ performance/
│  │  └─ README.md
│  ├─ platform-billing/
│  │  └─ README.md
│  ├─ product-catalog/
│  │  └─ README.md
│  ├─ public-api/
│  │  ├─ compatibility/
│  │  │  └─ README.md
│  │  └─ README.md
│  ├─ regional-bank-adapters/
│  │  └─ README.md
│  ├─ security/
│  │  └─ README.md
│  ├─ statement-parsers/
│  │  ├─ camt053/
│  │  │  ├─ fixtures/
│  │  │  │  └─ README.md
│  │  │  ├─ parser.spec.ts
│  │  │  └─ README.md
│  │  ├─ csv-xlsx/
│  │  │  ├─ fixtures/
│  │  │  │  └─ README.md
│  │  │  ├─ parser.spec.ts
│  │  │  └─ README.md
│  │  ├─ mt940/
│  │  │  ├─ fixtures/
│  │  │  │  └─ README.md
│  │  │  ├─ parser.spec.ts
│  │  │  └─ README.md
│  │  └─ ofx-qfx/
│  │     ├─ fixtures/
│  │     │  └─ README.md
│  │     ├─ parser.spec.ts
│  │     └─ README.md
│  ├─ tooling/
│  │  └─ vitest-runner.smoke.test.ts
│  ├─ ui-visual-regression/
│  │  └─ README.md
│  ├─ vendor-master/
│  │  └─ README.md
│  ├─ web-e2e/
│  │  └─ README.md
│  └─ README.md
├─ tools/
│  ├─ bank-connectivity/
│  │  ├─ bank-purpose-mapper-cli/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  └─ README.md
│  │  ├─ consent-lifecycle-simulator/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  └─ README.md
│  │  ├─ multi-bank-seed-generator/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  └─ README.md
│  │  ├─ statement-parser-cli/
│  │  │  ├─ src/
│  │  │  │  └─ main.ts
│  │  │  ├─ tests/
│  │  │  │  └─ README.md
│  │  │  └─ README.md
│  │  └─ support-matrix-builder/
│  │     ├─ src/
│  │     │  └─ main.ts
│  │     ├─ tests/
│  │     │  └─ README.md
│  │     └─ README.md
│  ├─ checkers/
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  └─ README.md
│  ├─ codegen/
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  └─ README.md
│  ├─ customer-master/
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  └─ README.md
│  ├─ data-portability/
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  └─ README.md
│  ├─ db/
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  └─ README.md
│  ├─ ledger/
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  └─ README.md
│  ├─ outbound-sync/
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  └─ README.md
│  ├─ platform-billing/
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  └─ README.md
│  ├─ provider-connectors/
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  └─ README.md
│  ├─ public-api/
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  └─ README.md
│  └─ README.md
├─ vector-store/
│  ├─ acl-filters/
│  │  └─ README.md
│  ├─ namespaces/
│  │  └─ README.md
│  └─ retrieval-policies/
│     └─ README.md
├─ warehouse/
│  ├─ dbt/
│  │  └─ README.md
│  ├─ governance/
│  │  └─ README.md
│  ├─ marts/
│  │  └─ README.md
│  └─ README.md
├─ workers/
│  ├─ accounting-historical-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ accounting-sync-inbound-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ accounting-sync-netsuite-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ accounting-sync-qbo-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ accounting-sync-xero-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ acumatica-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ apideck-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ apideck-rutter-codat-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-account-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-connection-health-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-consent-renewal-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-feed-gocardless-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-feed-mercury-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-feed-plaid-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-feed-stripe-financial-connections-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-feed-stripe-treasury-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-feed-teller-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-feed-truelayer-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-feed-wise-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-import-dedup-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-reconciliation-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-statement-ingest-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bank-statement-parser-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ bill-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ codat-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ commerce-sync-amazon-seller-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ commerce-sync-shopify-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ commerce-sync-woocommerce-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ crm-sync-hubspot-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ crm-sync-salesforce-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ csv-xlsx-sftp-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ customer-dedupe-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ customer-health-score-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ customer-statement-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ data-export-expiry-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ data-export-package-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ data-migration-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ dynamics-bc-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ export-package-builder-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ freshbooks-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ fx-revaluation-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ hr-sync-adp-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ hr-sync-bamboohr-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ hr-sync-deel-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ hr-sync-gusto-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ hr-sync-rippling-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ hr-sync-workday-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ intacct-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ ledger-integrity-check-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ multi-bank-company-scope-audit-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ netsuite-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ oauth-token-rotation-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ outbound-conflict-resolution-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ outbound-sync-conflict-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ outbound-sync-dry-run-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ outbound-sync-replay-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ partner-app-review-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ platform-billing-meter-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ platform-invoice-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ posting-finalization-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ public-api-token-rotation-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ public-api-webhook-delivery-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ qbd-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ qbo-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ rate-limit-ledger-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ recruit-sync-checkr-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ recruit-sync-greenhouse-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ recruit-sync-lever-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-asia-global-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-bulgaria-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-canada-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-croatia-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-greece-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-india-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-mexico-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-montenegro-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-north-macedonia-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-poland-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-russia-disabled-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-serbia-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ regional-bank-turkey-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ retained-earnings-rollforward-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ rutter-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ spend-sync-brex-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ spend-sync-expensify-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ spend-sync-ramp-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ spend-sync-rho-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ subledger-reconciliation-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ support-sync-intercom-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ support-sync-zendesk-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ travel-sync-concur-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ travel-sync-navan-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ trial-balance-snapshot-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workspace-sync-box-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workspace-sync-calendly-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workspace-sync-docusign-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workspace-sync-dropbox-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workspace-sync-entra-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workspace-sync-github-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workspace-sync-google-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workspace-sync-jira-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workspace-sync-microsoft-graph-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workspace-sync-notion-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workspace-sync-slack-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workspace-sync-teams-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ workspace-sync-zoom-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  ├─ xero-outbound-sync-worker/
│  │  ├─ config/
│  │  │  └─ default.yaml
│  │  ├─ observability/
│  │  │  └─ metrics.yaml
│  │  ├─ src/
│  │  │  └─ main.ts
│  │  ├─ tests/
│  │  │  └─ smoke.test.ts
│  │  ├─ Dockerfile
│  │  └─ README.md
│  └─ README.md
├─ .editorconfig
├─ .env.example
├─ .gitattributes
├─ .gitignore
├─ .nvmrc
├─ .prettierignore
├─ .prettierrc.json
├─ CODEOWNERS
├─ CONTRIBUTING.md
├─ eslint.config.mjs
├─ LICENSE
├─ Makefile
├─ package.json
├─ pnpm-lock.yaml
├─ pnpm-workspace.yaml
├─ README.md
├─ TRIVIUM.code-workspace
├─ tsconfig.base.json
├─ tsconfig.json
├─ turbo.json
└─ vitest.config.ts
```
