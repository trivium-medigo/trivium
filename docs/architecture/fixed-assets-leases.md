# Fixed assets and leases (architecture — **phase 2** default)

Scopes **fixed assets**, **depreciation**, **leases**, **ASC 842 / IFRS 16–style** lease accounting, asset books, and amortization — **no production fixed-asset schema exists in v1**.

## v1

- Capital purchases may be posted through **standard AP / GL** with manual journal patterns until FA module exists.  
- **Do not** create ad-hoc `fixed_assets.sql` in silos — see rule below.

## Phase 2 (planned)

- **Candidate** artifacts (not added yet): `fixed_assets.sql`, `leases.sql`, depreciation runs, lease classification, ROU asset/liability, interest.  
- Integration points: **`finance-accounting`** (COA), **`ledger-integrity`**, **`posting-engine`**, **`financial-reporting.md`**, **`accounting-canonical-model`** (asset acquisition / depreciation events).

## Connections

- **Posting-engine** remains sole path to posted GL.  
- **AI** may assist asset tagging suggestions; **never** posts depreciation autonomously.

## Rule

Prevent **shadow** fixed-asset tables during v1; all capital tracking must go through documented AP/GL paths until this module is implemented.
