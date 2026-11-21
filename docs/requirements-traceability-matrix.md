# Requirements Traceability Matrix

| Field | Value |
|---|---|
| Project | Demo Web Shop — QA Portfolio (Manual + Selenium) |
| Document | Requirements Traceability Matrix (RTM) |
| Version | 1.0 (Phase 1 — planned coverage) |
| Author | Milan Dahal |
| Date | 18 November 2026 |
| Application | https://demowebshop.tricentis.com/ |

---

## 1. Purpose and method

No formal requirements specification is published for this demo store. Requirements in
this matrix were **derived from observed application behaviour**, navigation structure,
form fields, and validation messages. They are therefore treated as assumptions, not as
contractual requirements.

Traceability chain used in this project:

```
Derived requirement (REQ-*)
        └── Test scenario (SC-*)
                └── Manual test case (TC-*)
                        └── Automated test (tests/test_*.py::test_*)
                                └── Execution evidence (report / screenshot / defect)
```

**Phase 1 status.** Manual test case IDs and automated test names do not exist yet. This
version reserves per-module ranges and records whether automation is planned. Exact IDs
and function names are added in Phase 2 (manual cases) and Phase 4 (automation), and
final results are added in Phase 9. No result is marked as executed in this document.

### Status values

| Status | Meaning |
|---|---|
| Planned | Scenario/coverage defined; not yet executed |
| In progress | Case written or automation implemented; execution pending |
| Pass / Fail | Confirmed by an actual execution |
| Blocked | Cannot execute due to environment or dependency |
| Not Run | Deliberately not executed, with a reason |

---

## 2. Requirement traceability

### 2.1 Registration

| REQ ID | Derived requirement (assumption) | Scenario(s) | Manual TCs (planned) | Automation |
|---|---|---|---|---|
| REQ-REG-01 | A visitor can create an account with a unique, valid email and is signed in or redirected appropriately | SC-REG-01 | TC-001–TC-006 | Yes |
| REQ-REG-02 | Mandatory fields (first name, last name, email, password, confirm password) must be completed before submission | SC-REG-02 | TC-001–TC-006 | Yes |
| REQ-REG-03 | Email input must match a valid email format; malformed addresses are rejected | SC-REG-03 | TC-001–TC-006 | Yes |
| REQ-REG-04 | An email address already linked to an account cannot be registered again | SC-REG-04 | TC-001–TC-006 | Partial |
| REQ-REG-05 | Password and Confirm password must match | SC-REG-05 | TC-001–TC-006 | Yes |
| REQ-REG-06 | Password length below the configured minimum is rejected **(minimum assumed 6 — verify)** | SC-REG-06 | TC-001–TC-006 | Partial |

### 2.2 Authentication and password recovery

| REQ ID | Derived requirement (assumption) | Scenario(s) | Manual TCs (planned) | Automation |
|---|---|---|---|---|
| REQ-AUTH-01 | Valid credentials create an authenticated session and expose account-specific UI | SC-AUTH-01, SC-AUTH-07 | TC-010–TC-017 | Yes |
| REQ-AUTH-02 | Invalid password and unregistered email are rejected without revealing which value was wrong | SC-AUTH-02, SC-AUTH-03 | TC-010–TC-017 | Yes |
| REQ-AUTH-03 | Empty login fields produce validation feedback and no session | SC-AUTH-04 | TC-010–TC-017 | Yes |
| REQ-AUTH-04 | Logout terminates the session and protected pages become inaccessible | SC-AUTH-05, SC-SES-03 | TC-010–TC-017 | Yes |
| REQ-AUTH-05 | Protected pages redirect unauthenticated users to login and return them to the requested page after authentication | SC-AUTH-06, SC-AUTH-07, SC-SES-01, SC-ORD-03 | TC-010–TC-017 | Partial |
| REQ-AUTH-06 | Password recovery returns a neutral confirmation regardless of whether the email exists | SC-AUTH-08 | TC-010–TC-017 | No |

### 2.3 Catalog and navigation

| REQ ID | Derived requirement (assumption) | Scenario(s) | Manual TCs (planned) | Automation |
|---|---|---|---|---|
| REQ-CAT-01 | The home page renders global navigation, featured products, newsletter, and footer | SC-CAT-01 | TC-020–TC-023 | Yes |
| REQ-CAT-02 | Each of the seven top-level categories and the Computers sub-categories open a correct listing | SC-CAT-02, SC-CAT-03 | TC-020–TC-023 | Yes |
| REQ-CAT-03 | Breadcrumbs reflect the current hierarchy and link to parent pages | SC-CAT-04 | TC-020–TC-023 | Partial |
| REQ-CAT-04 | Grid/list view and pagination work and preserve the chosen view while paging | SC-CAT-05, SC-CAT-06 | TC-020–TC-023 | Partial |

### 2.4 Product detail

| REQ ID | Derived requirement (assumption) | Scenario(s) | Manual TCs (planned) | Automation |
|---|---|---|---|---|
| REQ-PRD-01 | A product page displays name, image, price, availability, description, and quantity input | SC-PRD-01 | TC-030–TC-036 | Yes |
| REQ-PRD-02 | Discounted products display old price, current price, and a consistent discount | SC-PRD-02 | TC-030–TC-036 | Yes |
| REQ-PRD-03 | Configurable products expose dropdown/radio/checkbox attributes whose selection changes the price | SC-PRD-03, SC-PRD-04, SC-PRD-05 | TC-030–TC-036 | Yes |
| REQ-PRD-04 | Gift cards require recipient and sender details before being added to the cart **(exact required set to verify)** | SC-PRD-06 | TC-030–TC-036 | Partial |
| REQ-PRD-05 | Digital download products expose a sample link and can be added to the cart | SC-PRD-07 | TC-030–TC-036 | Partial |
| REQ-PRD-06 | Adding from the product page updates the header cart counter and cart contents | SC-PRD-08 | TC-030–TC-036 | Yes |

### 2.5 Search

| REQ ID | Derived requirement (assumption) | Scenario(s) | Manual TCs (planned) | Automation |
|---|---|---|---|---|
| REQ-SRC-01 | Keyword search returns relevant product results with a result count, case-insensitively | SC-SRC-01, SC-SRC-04, SC-SRC-06 | TC-040–TC-045 | Yes |
| REQ-SRC-02 | A search with no matches displays an explicit no-results message | SC-SRC-02 | TC-040–TC-045 | Yes |
| REQ-SRC-03 | Search terms shorter than the minimum length are rejected with a message **(threshold assumed 3 — verify)** | SC-SRC-03 | TC-040–TC-045 | Partial |
| REQ-SRC-04 | Special characters in the search term are handled without error or broken layout | SC-SRC-05 | TC-040–TC-045 | Yes |

### 2.6 Sorting, filtering, and paging

| REQ ID | Derived requirement (assumption) | Scenario(s) | Manual TCs (planned) | Automation |
|---|---|---|---|---|
| REQ-FLT-01 | Sorting by name (A–Z, Z–A), price (low–high, high–low), and created date reorders the listing correctly | SC-FLT-01–SC-FLT-05 | TC-050–TC-055 | Yes |
| REQ-FLT-02 | Price filters (under 25, 25–50, over 50) return only products inside the selected range | SC-FLT-06, SC-FLT-07, SC-FLT-08 | TC-050–TC-055 | Yes |
| REQ-FLT-03 | Page size 4/8/12 changes the number of products displayed per page | SC-FLT-09 | TC-050–TC-055 | Yes |
| REQ-FLT-04 | Filter, sort, and page size can be combined and remain applied together | SC-FLT-10 | TC-050–TC-055 | Partial |

### 2.7 Shopping cart

| REQ ID | Derived requirement (assumption) | Scenario(s) | Manual TCs (planned) | Automation |
|---|---|---|---|---|
| REQ-CART-01 | Adding products creates cart rows with correct unit price, quantity, and subtotal; duplicate adds increase quantity | SC-CART-01, SC-CART-02, SC-CART-03 | TC-060–TC-067 | Yes |
| REQ-CART-02 | Updating quantity recalculates line totals and cart subtotal | SC-CART-04 | TC-060–TC-067 | Yes |
| REQ-CART-03 | Removing an item removes the row and recalculates totals | SC-CART-05 | TC-060–TC-067 | Yes |
| REQ-CART-04 | An empty cart shows an explicit empty state and no checkout path | SC-CART-06 | TC-060–TC-067 | Yes |
| REQ-CART-05 | Quantity validation handles 0, negative, non-numeric, and very large values without corrupting totals | SC-CART-07, SC-CART-08, SC-CART-09, SC-CART-10 | TC-060–TC-067 | Yes |
| REQ-CART-06 | Invalid discount and gift-card codes produce an error and do not change totals | SC-CART-11 | TC-060–TC-067 | Partial |
| REQ-CART-07 | Cart contents survive navigation, refresh, and session continuity | SC-CART-12, SC-SES-02 | TC-060–TC-067 | Yes |

### 2.8 Checkout

| REQ ID | Derived requirement (assumption) | Scenario(s) | Manual TCs (planned) | Automation |
|---|---|---|---|---|
| REQ-CHK-01 | Checkout is only reachable with a non-empty cart | SC-CHK-01 | TC-080–TC-088 | Yes |
| REQ-CHK-02 | Guest checkout is available with valid billing data **(verify in Phase 2)** | SC-CHK-02 | TC-080–TC-088 | Partial |
| REQ-CHK-03 | A signed-in customer can complete checkout using a saved address | SC-CHK-03 | TC-080–TC-088 | Yes |
| REQ-CHK-04 | Mandatory billing fields are enforced | SC-CHK-04 | TC-080–TC-088 | Yes |
| REQ-CHK-05 | Postal code, phone, and email formats are validated **(exact rules to verify)** | SC-CHK-05 | TC-080–TC-088 | Partial |
| REQ-CHK-06 | Shipping methods are selectable and affect the order total | SC-CHK-06 | TC-080–TC-088 | Partial |
| REQ-CHK-07 | Available payment methods can be selected and complete the order **(methods to verify)** | SC-CHK-07, SC-CHK-08 | TC-080–TC-088 | Partial |
| REQ-CHK-08 | Confirming an order produces a confirmation page with an order number | SC-CHK-09 | TC-080–TC-088 | Yes |
| REQ-CHK-09 | Order totals (subtotal, shipping, tax, total) are consistent between cart and confirmation | SC-CHK-09 | TC-080–TC-088 | Yes |
| REQ-CHK-10 | Checkout cannot proceed without accepting the terms of service | SC-CHK-10 | TC-080–TC-088 | Yes |

### 2.9 Orders

| REQ ID | Derived requirement (assumption) | Scenario(s) | Manual TCs (planned) | Automation |
|---|---|---|---|---|
| REQ-ORD-01 | A completed order appears in My Account → Orders with number, date, status, and total | SC-ORD-01 | TC-090–TC-092 | Yes |
| REQ-ORD-02 | Order details match the products, quantities, addresses, shipping, and totals of the placed order | SC-ORD-02 | TC-090–TC-092 | Partial |
| REQ-ORD-03 | Order history and order details require authentication | SC-ORD-03 | TC-090–TC-092 | Yes |

### 2.10 Wishlist and compare

| REQ ID | Derived requirement (assumption) | Scenario(s) | Manual TCs (planned) | Automation |
|---|---|---|---|---|
| REQ-WISH-01 | Products can be added to, listed in, and removed from the wishlist with a correct counter | SC-WISH-01, SC-WISH-02, SC-WISH-03 | TC-100–TC-103 | Partial |
| REQ-WISH-02 | A wishlist item can be moved to the cart | SC-WISH-04 | TC-100–TC-103 | Partial |
| REQ-WISH-03 | Products can be added to and removed from a comparison table | SC-WISH-05, SC-WISH-06 | TC-100–TC-103 | Partial |

### 2.11 My account

| REQ ID | Derived requirement (assumption) | Scenario(s) | Manual TCs (planned) | Automation |
|---|---|---|---|---|
| REQ-ACC-01 | Customer information can be updated and persists | SC-ACC-01 | TC-110–TC-114 | Partial |
| REQ-ACC-02 | Addresses can be added, edited, and deleted | SC-ACC-02, SC-ACC-03, SC-ACC-04 | TC-110–TC-114 | Partial |
| REQ-ACC-03 | Address forms enforce mandatory and format validation | SC-ACC-05 | TC-110–TC-114 | Partial |
| REQ-ACC-04 | Password change requires the correct current password and the new password works at login | SC-ACC-06, SC-ACC-07 | TC-110–TC-114 | No |

### 2.12 Contact us and newsletter

| REQ ID | Derived requirement (assumption) | Scenario(s) | Manual TCs (planned) | Automation |
|---|---|---|---|---|
| REQ-CMS-01 | The contact form validates required fields and email format and confirms successful submission | SC-CMS-01, SC-CMS-02, SC-CMS-03 | TC-120–TC-123 | Yes |
| REQ-CMS-02 | Newsletter subscription validates the email and confirms success | SC-CMS-04, SC-CMS-05 | TC-120–TC-123 | Partial |

### 2.13 Session and edge behaviour

| REQ ID | Derived requirement (assumption) | Scenario(s) | Manual TCs (planned) | Automation |
|---|---|---|---|---|
| REQ-SES-01 | An authenticated session persists across navigation until logout or expiry | SC-SES-02 | TC-130–TC-132 | Yes |
| REQ-SES-02 | After logout, cached/back navigation does not expose account data | SC-SES-03, SC-AUTH-05 | TC-130–TC-132 | Partial |
| REQ-SES-03 | Items added as a guest are preserved or merged after signing in **(behaviour to verify)** | SC-SES-04 | TC-130–TC-132 | Partial |

---

## 3. Coverage summary

| Module | Requirements | Scenarios | Planned manual cases | Planned automated tests |
|---|---:|---:|---:|---:|
| Registration | 6 | 6 | 6 | 2 |
| Authentication | 6 | 8 | 8 | 5 |
| Catalog / navigation | 4 | 6 | 4 | 2 |
| Product detail | 6 | 8 | 7 | 4 |
| Search | 4 | 6 | 6 | 3 |
| Sort / filter / paging | 4 | 10 | 6 | 4 |
| Shopping cart | 7 | 12 | 8 | 8 |
| Checkout | 10 | 10 | 9 | 6 |
| Orders | 3 | 3 | 3 | 2 |
| Wishlist / compare | 3 | 6 | 4 | 2 |
| My account | 4 | 7 | 5 | 2 |
| Contact / newsletter | 2 | 5 | 4 | 2 |
| Session / edge | 3 | 4 | 3 | 1 |
| **Total** | **62** | **91** | **73** | **43** |

Planned manual cases are fewer than scenarios because data variations (for example
quantity 0 / negative / non-numeric / large) are consolidated into single cases with
multiple data rows. Planned automated tests cover stable regression paths only; not every
manual case will be automated, and the README will state the real coverage.

---

## 4. Assumptions register (must be verified during Phase 2)

| # | Assumption | Affects | Verification |
|---|---|---|---|
| A1 | Minimum password length is 6 characters | SC-REG-06 | **Confirmed 18 Nov 2026** — 5 rejected, 6 accepted |
| A2 | Minimum search term length is 3 characters | SC-SRC-03 | Submit 1-, 2-, and 3-character terms |
| A3 | Guest checkout is available | SC-CHK-02 | Open checkout with a cart and no session |
| A4 | Payment methods include Cash On Delivery and Check / Money Order | SC-CHK-07, SC-CHK-08 | Inspect payment step |
| A5 | Gift card requires recipient name, recipient email, sender name, sender email | SC-PRD-06 | Submit with individual fields empty |
| A6 | Postal code and phone validation rules exist in checkout | SC-CHK-05 | Submit malformed values |
| A7 | Guest cart is preserved after login | SC-SES-04 | Add as guest, sign in, inspect cart |
| A8 | Email uniqueness is enforced at registration | SC-REG-04 | **Confirmed 18 Nov 2026** — duplicate email rejected |
| A9 | The wishlist requires authentication | SC-SES-01, TC-014 | **Rejected 18 Nov 2026** — guest wishlist is accessible and shows an empty list; not a defect |

Verification outcomes will be recorded in `docs/test-cases.md`; any assumption proven
wrong is corrected here rather than silently ignored.

---

## 5. Explicitly excluded requirements

| Area | Reason for exclusion |
|---|---|
| Public API / REST endpoints | None exposed (`/api/` → 404) |
| Admin/back-office functions | Not publicly accessible |
| Real payment authorisation | Demo store; no card data permitted |
| Email delivery confirmation | No mailbox access |
| Performance / load capacity | Not appropriate for a shared public demo |
| Security vulnerabilities | No penetration-testing authorisation |
| Accessibility conformance | Requires specialist audit criteria |
| Multi-currency / localisation | Not offered in this environment |

---

## 6. Defect traceability

Confirmed defects are traced back to the requirement and test case that exposed them.

| Bug ID | Requirement | Scenario | Test case | Severity | Priority | Status |
|---|---|---|---|---|---|---|
| BUG-001 | REQ-AUTH-02 | SC-AUTH-03 | TC-012 | Low | Medium | Open |
| BUG-002 | REQ-AUTH-03 | SC-AUTH-04 | TC-013 | Low | Low | Open |
| BUG-003 | REQ-AUTH-06 | SC-AUTH-08 | TC-017 | Low | Medium | Open |
| BUG-004 | REQ-PRD-03 | SC-PRD-04 | TC-033 | Low | Medium | Open |
| BUG-005 | REQ-SRC-04 | SC-SRC-04 | TC-044 | Medium | Medium | Open |
| BUG-006 | REQ-CART-06 | SC-CART-11 | TC-067 | Low | Low | Open |

Details and evidence: `bug-reports.md`.

---

## 7. Maintenance

This matrix is updated at three points:

1. **Phase 2** — replace planned TC ranges with actual case IDs and record execution status.
2. **Phase 4** — add automated test module and function names.
3. **Phase 9** — add final execution results and evidence links.

Any requirement added after Phase 1 must reference at least one scenario before it is
considered in scope.
