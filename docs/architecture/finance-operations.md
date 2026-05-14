# finance-operations (architecture)

Accounts receivable, accounts payable, invoicing, bills, payments, and **operational** subledgers that **feed the general ledger** through deterministic posting.

## Revenue recognition anchor

- **`revenue_recognition.sql`** owns the **schema home** for recognition schedules and links to GL via posting-engine.  
- **Commercial lifecycle** owns subscription/contract **facts** that drive those schedules.  
- **Stripe** data enters through integrations/bank feeds and is **reconciled** to AR, deferred revenue, and cash — not copied as revenue blindly.

## AP / AR / payments

- Invoices, bills, payments produce canonical events → journal templates → **posting-engine**.  
- Aging and dunning remain subledger concerns; **trial balance** remains ledger truth.

## AP automation (BILL.com–class)

Architecture for intake, coding, duplicate detection, approvals, and disbursement is documented in `docs/architecture/ap-payment-automation.md`. At a high level:

- **Bill intake** — email inbox, upload, vendor portal, API, OCR pipeline (OCR job tables are a **phase-2** schema candidate).  
- **Duplicate bill prevention** — deterministic matching hooks on `bills.sql` (vendor + invoice identity + amount window) before payment readiness.  
- **Approval workflow** — `approval-policy-engine` + SoD; no AI final approval.  
- **Payment automation → posting-engine** — settlement and GL impact only after bank acknowledgement and engine validation (`payments.sql`, `payment_links.sql`).  
- **Vendor bank detail controls** — changes require human/system gates, evidence in object-storage, and canonical `vendor_bank_details_changed` events (see `packages/accounting-canonical-model/README.md`).

## AR and payment links

Customer portal payments, hosted pay links, processor settlement, fees, and chargebacks flow through `payment_links.sql` and reconcile to AR cash application via posting-engine — not direct GL writes from integrations.

## AI boundary

AI may assist invoice coding suggestions; **posted** AP/AR impact only through posting-engine after policy approval when required. AI does not approve, pay, post, or alter bank instructions autonomously (`docs/architecture/deterministic-accounting.md`).

## References

- `docs/architecture/commercial-lifecycle.md`  
- `docs/architecture/deterministic-accounting.md`  
- `docs/architecture/ap-payment-automation.md`  
- `databases/.../finance-operations/revenue_recognition.sql`  
