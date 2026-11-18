# Test Scenarios

| Field | Value |
|---|---|
| Project | Demo Web Shop — QA Portfolio (Manual + Selenium) |
| Document | Test Scenario Inventory |
| Version | 1.0 (Phase 1 — awaiting review) |
| Author | Milan Dahal |
| Date | 18 November 2026 |
| Application | https://demowebshop.tricentis.com/ |
| Related | `test-plan.md`, `requirements-traceability-matrix.md` |

---

## 1. How to read this document

A **test scenario** is a one-line statement of *what* should be tested. Detailed steps,
data, and expected results are added in Phase 2 as manual test cases (`TC-xxx`).

**Derived requirements.** No formal specification is published for this demo store, so
scenarios are derived from observed behaviour and documented as assumptions. Where a
rule could not be confirmed without deeper execution (for example, the exact password
policy or the available payment methods), the scenario is marked **(verify in Phase 2)**.

### Priority definitions

| Priority | Meaning |
|---|---|
| Critical | Core revenue/authentication path; failure blocks the journey |
| High | Important function or validation; failure has major user impact |
| Medium | Useful function or validation with a workaround |
| Low | Minor, cosmetic, or low-frequency behaviour |

### Test types used

`Functional` · `Positive` · `Negative` · `Boundary` · `Validation` · `Navigation` ·
`UI` · `Session` · `Business rule` · `Error handling` · `Smoke`

---

## 2. Scenario inventory

### 2.1 Registration (REG)

| ID | Scenario | Priority | Type |
|---|---|---|---|
| SC-REG-01 | Register a new account with valid mandatory data and confirm the account is created and signed in | Critical | Functional / Positive |
| SC-REG-02 | Submit the registration form with all mandatory fields empty and confirm field-level validation blocks submission | High | Negative / Validation |
| SC-REG-03 | Register with a malformed email address (for example `milan@`, `milan.example.com`) and confirm the email validation error | High | Negative / Validation |
| SC-REG-04 | Register using an email address that already has an account and confirm the duplicate-email error | High | Negative / Business rule |
| SC-REG-05 | Enter different values in Password and Confirm password and confirm validation prevents registration | High | Negative / Validation |
| SC-REG-06 | Verify the password length boundary (below minimum vs exactly minimum) **(verify minimum = 6 in Phase 2)** | Medium | Boundary |

### 2.2 Authentication and password recovery (AUTH)

| ID | Scenario | Priority | Type |
|---|---|---|---|
| SC-AUTH-01 | Sign in with valid credentials and confirm the header shows the account email and protected pages are accessible | Critical | Functional / Positive |
| SC-AUTH-02 | Sign in with a valid email but incorrect password and confirm an error is shown with no session created | High | Negative |
| SC-AUTH-03 | Sign in with an unregistered email address and confirm the generic credentials error | High | Negative |
| SC-AUTH-04 | Submit the login form with empty email and/or password and confirm validation feedback | High | Negative / Validation |
| SC-AUTH-05 | Sign out and confirm the session ends and protected pages are no longer accessible | Critical | Functional / Session |
| SC-AUTH-06 | Request a protected page while signed out and confirm redirection to login with a return URL | High | Session / Error handling |
| SC-AUTH-07 | Sign in from the redirected login page and confirm the user lands on the originally requested page | Medium | Session |
| SC-AUTH-08 | Submit password recovery for a registered and an unregistered email and confirm the response does not disclose whether the account exists | Medium | Functional / Negative |

### 2.3 Catalog and navigation (CAT)

| ID | Scenario | Priority | Type |
|---|---|---|---|
| SC-CAT-01 | Load the home page and confirm header, navigation, featured products, newsletter, and footer content render | High | Smoke / UI |
| SC-CAT-02 | Open each of the seven top-level categories and confirm a product listing is displayed | High | Functional / Navigation |
| SC-CAT-03 | Navigate into the Computers sub-categories (Desktops, Notebooks, Accessories) and confirm correct listings | High | Navigation |
| SC-CAT-04 | Verify breadcrumb links reflect the current category path and navigate back correctly | Medium | Navigation |
| SC-CAT-05 | Toggle grid/list view and confirm the layout changes and the selection persists while paging | Low | UI |
| SC-CAT-06 | Use pagination (next/previous/page number) and confirm the correct page of products is shown | Medium | Functional |

### 2.4 Product detail (PRD)

| ID | Scenario | Priority | Type |
|---|---|---|---|
| SC-PRD-01 | Open a simple product and confirm name, image, price, availability, description, and quantity field | High | Functional |
| SC-PRD-02 | Open a discounted product and confirm the old price, current price, and discount are displayed correctly | Medium | Business rule |
| SC-PRD-03 | Open "Build your own computer" and confirm the default attribute selections and default price | High | Functional |
| SC-PRD-04 | Change processor, RAM, HDD, and software options and confirm the product price updates accordingly | High | Business rule |
| SC-PRD-05 | Add a configurable product to the cart with quantity greater than one and confirm the cart reflects the selected options and quantity | High | Functional |
| SC-PRD-06 | Attempt to add a gift card without recipient/sender details and confirm the required-field validation **(verify exact required set in Phase 2)** | High | Validation / Negative |
| SC-PRD-07 | Open a digital download product, confirm the sample download link, and add it to the cart | Medium | Functional |
| SC-PRD-08 | Add a product to the cart from its detail page and confirm the header cart counter and flyout cart update | High | Functional |

### 2.5 Search (SRC)

| ID | Scenario | Priority | Type |
|---|---|---|---|
| SC-SRC-01 | Search for a known product keyword and confirm relevant results are returned with a result count | High | Functional / Positive |
| SC-SRC-02 | Search for a term with no matches and confirm the no-results message is shown | High | Negative |
| SC-SRC-03 | Search with fewer than three characters and confirm the minimum-length message **(verify threshold in Phase 2)** | Medium | Boundary / Negative |
| SC-SRC-04 | Search using different letter casing and confirm results are case-insensitive | Medium | Functional |
| SC-SRC-05 | Search with special characters (`<script>`, `%`, `'`, `--`) and confirm the application handles them without error | Low | Negative / Error handling |
| SC-SRC-06 | Use the header search box from an inner page and confirm it searches and displays the results page | Medium | Functional / Navigation |

### 2.6 Sorting, filtering, and paging (FLT)

| ID | Scenario | Priority | Type |
|---|---|---|---|
| SC-FLT-01 | Sort a category by Name: A to Z and confirm the displayed order | High | Functional |
| SC-FLT-02 | Sort a category by Name: Z to A and confirm the reverse displayed order | High | Functional |
| SC-FLT-03 | Sort a category by Price: Low to High and confirm ascending prices | High | Functional |
| SC-FLT-04 | Sort a category by Price: High to Low and confirm descending prices | High | Functional |
| SC-FLT-05 | Sort by Created on and confirm the ordering changes predictably | Low | Functional |
| SC-FLT-06 | Apply the "Under 25.00" price filter and confirm every displayed price is below 25.00 | Medium | Business rule |
| SC-FLT-07 | Apply the "25.00 – 50.00" price filter and confirm every displayed price falls inside the range | Medium | Business rule |
| SC-FLT-08 | Apply the "Over 50.00" price filter and confirm every displayed price is above 50.00 | Medium | Business rule |
| SC-FLT-09 | Change page size to 4, 8, and 12 and confirm the number of products per page changes | Medium | Functional |
| SC-FLT-10 | Combine a price filter, a sort order, and a page size and confirm all three remain applied | Medium | Functional / State |

### 2.7 Shopping cart (CART)

| ID | Scenario | Priority | Type |
|---|---|---|---|
| SC-CART-01 | Add one product and confirm the cart page shows one row, correct unit price, quantity, and subtotal | Critical | Functional |
| SC-CART-02 | Add two different products and confirm two rows with a correct combined subtotal | High | Functional |
| SC-CART-03 | Add the same product twice and confirm the quantity increases on a single row | High | Functional |
| SC-CART-04 | Update the quantity on the cart page and confirm the line total and subtotal recalculate | High | Functional / Business rule |
| SC-CART-05 | Remove an item and confirm the row disappears and totals recalculate | High | Functional |
| SC-CART-06 | Open the cart with no items and confirm the empty-cart message and no checkout path | Medium | Error handling |
| SC-CART-07 | Set the quantity to 0 and confirm the item is removed or a validation message is shown (no negative totals) | Medium | Boundary |
| SC-CART-08 | Enter a negative quantity and confirm validation prevents the change | Medium | Negative / Boundary |
| SC-CART-09 | Enter a non-numeric quantity and confirm a numeric validation message | Medium | Negative / Validation |
| SC-CART-10 | Enter a very large quantity (for example 99999) and confirm stock/quantity validation without a crash | Medium | Boundary |
| SC-CART-11 | Apply an invalid discount code and an invalid gift card code and confirm errors with unchanged totals | Medium | Negative / Error handling |
| SC-CART-12 | Navigate away, return to the cart, and refresh the page; confirm cart contents persist | High | Session / Functional |

### 2.8 Checkout (CHK)

| ID | Scenario | Priority | Type |
|---|---|---|---|
| SC-CHK-01 | From an empty cart, attempt checkout and confirm the user is redirected to the cart page | Medium | Error handling |
| SC-CHK-02 | Complete checkout as a guest with valid billing data and confirm the flow reaches order confirmation **(verify guest option availability)** | Critical | Functional / Positive |
| SC-CHK-03 | Complete checkout as a signed-in customer using a saved address | Critical | Functional |
| SC-CHK-04 | Submit billing details with mandatory fields empty and confirm validation blocks progression | High | Negative / Validation |
| SC-CHK-05 | Submit invalid postal code, phone, and email formats in checkout and confirm field validation **(verify exact rules in Phase 2)** | High | Validation / Negative |
| SC-CHK-06 | Select each available shipping method and confirm the shipping cost and order total update | High | Business rule |
| SC-CHK-07 | Complete checkout with the Cash On Delivery payment method | High | Functional |
| SC-CHK-08 | Complete checkout with the Check / Money Order payment method | High | Functional |
| SC-CHK-09 | Confirm the order confirmation page displays an order number and consistent totals | Critical | Business rule |
| SC-CHK-10 | Confirm the checkout cannot proceed while the terms-of-service checkbox is unchecked | High | Validation / Business rule |

### 2.9 Orders (ORD)

| ID | Scenario | Priority | Type |
|---|---|---|---|
| SC-ORD-01 | Confirm a placed order appears in My Account → Orders with correct number, date, status, and total | High | Functional |
| SC-ORD-02 | Open the order details page and confirm products, quantities, addresses, shipping, and totals match the order | High | Functional / Business rule |
| SC-ORD-03 | Attempt to open order history while signed out and confirm redirection to login | Medium | Session / Authorization |

### 2.10 Wishlist and compare (WISH)

| ID | Scenario | Priority | Type |
|---|---|---|---|
| SC-WISH-01 | Add a product to the wishlist and confirm the header wishlist counter increments | Medium | Functional |
| SC-WISH-02 | Open the wishlist and confirm the product, price, and quantity are listed | Medium | Functional |
| SC-WISH-03 | Remove a product from the wishlist and confirm the list and counter update | Medium | Functional |
| SC-WISH-04 | Move a wishlist item to the cart and confirm it appears in the cart and leaves the wishlist | Medium | Functional / Business rule |
| SC-WISH-05 | Add two products to the compare list and confirm the comparison table displays their attributes | Medium | Functional |
| SC-WISH-06 | Remove one product or clear the compare list and confirm the list updates | Low | Functional |

### 2.11 My account (ACC)

| ID | Scenario | Priority | Type |
|---|---|---|---|
| SC-ACC-01 | Update customer information and confirm the change persists after reload and re-login | Medium | Functional |
| SC-ACC-02 | Add a new address with valid data and confirm it is saved and usable at checkout | Medium | Functional |
| SC-ACC-03 | Edit an existing address and confirm the updated values persist | Medium | Functional |
| SC-ACC-04 | Delete an address and confirm it is removed from the address list | Medium | Functional |
| SC-ACC-05 | Submit an address form with mandatory fields empty or invalid and confirm validation | High | Validation / Negative |
| SC-ACC-06 | Change the password with the correct current password and confirm login with the new password | High | Functional |
| SC-ACC-07 | Attempt to change the password with an incorrect current password and confirm the error | Medium | Negative / Validation |

### 2.12 Contact us, newsletter, and reviews (CMS)

| ID | Scenario | Priority | Type |
|---|---|---|---|
| SC-CMS-01 | Submit the contact form with valid data and confirm the success message | Medium | Functional / Positive |
| SC-CMS-02 | Submit the contact form with empty mandatory fields and confirm validation | Medium | Negative / Validation |
| SC-CMS-03 | Submit the contact form with a malformed email and confirm email validation | Medium | Validation / Negative |
| SC-CMS-04 | Subscribe to the newsletter with a valid email and confirm the confirmation message | Low | Functional |
| SC-CMS-05 | Subscribe to the newsletter with an invalid email and confirm validation | Low | Negative / Validation |

### 2.13 Session and edge behaviour (SES)

| ID | Scenario | Priority | Type |
|---|---|---|---|
| SC-SES-01 | Attempt to open account, wishlist, and checkout pages while signed out and confirm each redirects appropriately | High | Session / Authorization |
| SC-SES-02 | Navigate across multiple pages while signed in and confirm the session remains active | High | Session |
| SC-SES-03 | After signing out, use the browser Back button and confirm account data is not re-exposed | High | Session / Security-adjacent |
| SC-SES-04 | Add items as a guest, sign in, and confirm the guest cart is preserved or merged | Medium | Session / Business rule |

---

## 3. Inventory summary

| Module | Scenarios | Critical | High | Medium | Low |
|---|---:|---:|---:|---:|---:|
| Registration | 6 | 1 | 4 | 1 | 0 |
| Authentication | 8 | 2 | 4 | 2 | 0 |
| Catalog / navigation | 6 | 0 | 3 | 2 | 1 |
| Product detail | 8 | 0 | 6 | 2 | 0 |
| Search | 6 | 0 | 2 | 3 | 1 |
| Sort / filter / paging | 10 | 0 | 4 | 5 | 1 |
| Shopping cart | 12 | 1 | 5 | 6 | 0 |
| Checkout | 10 | 3 | 6 | 1 | 0 |
| Orders | 3 | 0 | 2 | 1 | 0 |
| Wishlist / compare | 6 | 0 | 0 | 5 | 1 |
| My account | 7 | 0 | 2 | 5 | 0 |
| Contact / newsletter | 5 | 0 | 0 | 3 | 2 |
| Session / edge | 4 | 0 | 3 | 1 | 0 |
| **Total** | **91** | **7** | **41** | **37** | **6** |

---

## 4. Scope notes

1. **Manual execution priority.** All Critical and High scenarios are executed manually.
   Medium scenarios are executed where they add business value; Low scenarios are
   documented and may be covered by automation only. Any scenario not executed is
   recorded as **Not Run** with a reason — never as Pass.
2. **Automation candidates.** Stable, repeatable flows (authentication, catalog, search,
   sorting, cart totals, checkout, validation) are automated. Destructive account changes
   are automated only in a repeatable, self-restoring way.
3. **Not assumed as defects.** Missing `robots.txt` access, slowness, third-party content,
   or browser warnings are environment observations, not application defects.
4. **Data-affecting scenarios.** Checkout scenarios create harmless demo orders. Product
   review submission is intentionally excluded to avoid polluting shared demo content.
