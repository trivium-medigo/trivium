# ai-accounting-drafts (API module)

AI-assisted **draft** accounting artifacts — **not** the general ledger system of record.

## Lifecycle (mandatory)

1. **Draft created** — structured proposal (e.g. suggested journal, categorization, reconciliation match). Stored as draft with `source_kind` metadata for downstream `journal_entries` if promoted.  
2. **Evidence attached** — links to bank lines, invoices, payroll lines, retrieval chunks (`draft_evidence.sql`). No draft is “high confidence” without evidence pointers when policy requires.  
3. **Retrieval ACL checked** — `ai-copilot` / retrieval paths respect `retrieval_acl_logs` and tenant data boundaries.  
4. **Hallucination / confidence guards** — policy: low-confidence suggestions require human review; blocked auto-post.  
5. **Approval gate** — `draft_approval_gates.sql` + `approval-policy-engine` for high-risk accounts, periods, or amounts.  
6. **Posting-engine** — **only** posting-engine performs deterministic validation and commits **posted** `journal_entries` / `journal_lines`.  
7. **Hard rule**: AI services **must not** write **posted** `journal_lines` or flip `status` to `posted` on `journal_entries`.

## Relationship to posting-engine

- Drafts may generate **payloads** consumed by posting-engine as **draft** journals (`status = draft`).  
- Transition to `posted` is **solely** posting-engine after approvals and invariant checks.

## Payment and bank-detail boundaries

- AI may **extract**, **categorize**, and **suggest** line items, dimensions, and match candidates when evidence is attached and retrieval ACL allows.  
- AI may **not** approve bills or payments, initiate ACH/wire/check/card disbursements, change vendor bank or payee instructions, or flip journals to `posted`.  
- Payment workflows and vendor bank detail changes require **human or system policy gates** (`approval-policy-engine`, identity governance, `policies/dashboard-access.md`).

## References

- `docs/architecture/deterministic-accounting.md`  
- `apps/api/src/modules/posting-engine/README.md`  
- `databases/.../ledger-integrity/journal_entries.sql` (`source_kind`, immutability)  
