# AP and payment automation (BILL.com–class architecture)

Maps **BILL / Melio / Airbase / Ramp / Brex / Oracle Payables**-style capabilities onto TRIVIUM modules **without** autonomous AI payments.

Public reference patterns (examples): BILL AP and approvals ([BILL AP](https://www.bill.com/product/accounts-payable), [BILL payment approvals](https://www.bill.com/product/payment-approvals)); Ramp Bill Pay OCR and controls ([Ramp bill pay](https://ramp.com/bill-pay/)); Brex bill pay sync ([Brex bill pay](https://www.brex.com/product/bill-pay)); Oracle Fusion invoices and payment process requests ([Oracle invoices landing](https://docs.oracle.com/en/cloud/saas/financials/25d/fappp/introducing-the-invoices-landing-page.html), [PPR](https://docs.oracle.com/en/cloud/saas/financials/25d/fappp/payment-process-requests.html)).

## End-to-end flow

1. **Bill intake** — email, upload, API, vendor portal, OCR pipeline → `finance-operations/bills.sql` + `object-storage/import-uploads`, `object-storage/attachments`.  
2. **Invoice inbox / state machine** — draft → needs_info → pending_approval → approved → payment_ready → paid / void; see `bills.sql` spec.  
3. **OCR / extraction** — deterministic job + AI assist; **no** OCR table in v1 — phase-2 `ocr_jobs.sql` candidate; evidence in `ai-accounting-drafts` / `draft_evidence.sql`.  
4. **Coding** — GL draft vs **approved** coding; only approved coding eligible for payment batch.  
5. **Duplicate bill detection** — fuzzy match hooks on vendor + invoice # + amount + date; phase-2 dedicated matcher service.  
6. **Approvals** — `approval-policy-engine` + SoD: creator ≠ approver ≠ payer; dual control for vendor bank changes ([BILL dual control](https://www.bill.com/product/payment-approvals)).  
7. **Vendor onboarding** — `vendor-master/*`, `vendor-portal`.  
8. **Vendor bank detail changes** — human + policy gates + audit; **AI must not** change bank details (`deterministic-accounting.md`).  
9. **Payment runs** — ACH, check, wire, virtual card, internal transfer; batching like Oracle **PPR** (phase-2 `payment_process_requests.sql`).  
10. **Settlement** — bank ack, remittance evidence, failures/reversals → `payments.sql` spec.  
11. **1099 / W-9** — `vendor_tax_profiles.sql` + portal tax docs; **filing** phase-2 `vendor_1099_filings.sql`.  
12. **Accounting sync** — `accounting-sync`, `outbound-sync`, `gl_account_external_mappings.sql`.  
13. **GL posting** — **posting-engine only**; canonical events in `packages/accounting-canonical-model/README.md`.

## AI boundary (hard)

- AI may **extract, categorize, suggest, summarize**.  
- AI **must not**: approve bills, authorize payment, execute ACH/wire/check/card, change vendor bank details, or post to GL.  
- Align with Ramp/Brex marketing emphasis on automation **with** controls ([Ramp](https://ramp.com/bill-pay/), [Brex](https://www.brex.com/product/bill-pay)).

## Phase-2 candidates

`ocr_jobs.sql`, `payment_process_requests.sql`, `vendor_1099_filings.sql`, `encumbrances.sql` — referenced here only.

## References

- `docs/architecture/deterministic-accounting.md`  
- `docs/architecture/finance-operations.md`  
- `docs/architecture/cash-liquidity-forecasting.md`  
- `policies/dashboard-access.md`  
