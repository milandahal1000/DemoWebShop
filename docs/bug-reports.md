# Bug Reports

| Field | Value |
|---|---|
| Project | Demo Web Shop — QA Portfolio (Manual + Selenium) |
| Document | Defect Log |
| Version | 1.0 |
| Author | Milan Dahal |
| Date | 18 November 2026 |
| Application | https://demowebshop.tricentis.com/ |

Only defects that were **reproduced in the application** are recorded here. Browser
warnings, environment failures, and test-automation mistakes are excluded.

Severity and priority definitions are in `test-plan.md`, Section 13.

---

## 1. Defect summary

| Bug ID | Title | Module | Severity | Priority | Reproducibility | Status |
|---|---|---|---|---|---|---|
| BUG-001 | Login reveals whether an email address is registered | Authentication | Low | Medium | Always (2/2) | Open |
| BUG-002 | Login accepts empty credentials without required-field validation | Authentication | Low | Low | Always (1/1 + DOM) | Open |
| BUG-003 | Password recovery reveals whether an email address is registered | Password recovery | Low | Medium | Always (1/1) | Open |
| BUG-004 | Configurable product page shows only the base price, excluding selected option surcharges | Product detail | Low | Medium | Always (4/4 + cart) | Open |
| BUG-005 | Search term containing a tag-like fragment returns an internal error page | Search | Medium | Medium | Always (5/5 inputs) | Open |
| BUG-006 | Gift-card rejection message refers to a "coupon code" instead of a gift card | Shopping cart | Low | Low | Always (2/2) | Open |

| Metric | Count |
|---|---:|
| Confirmed defects | 6 |
| Open | 6 |
| Retest passed / closed | 0 |

---

## 2. Defect details

### BUG-001 — Login reveals whether an email address is registered

| Field | Value |
|---|---|
| Bug ID | BUG-001 |
| Bug title | Login error message discloses whether an email address has an account (user enumeration) |
| Module | Authentication / Login |
| Environment | Public demo `https://demowebshop.tricentis.com/` · Brave 1.99.57 (Chromium 157) · CachyOS Linux · 18 Nov 2026 |
| Preconditions | User is signed out and the login page is open |
| Steps to reproduce | 1. Open `https://demowebshop.tricentis.com/login`.<br>2. Enter a registered email (`milan.qa.demo.2026@example.com`) with an incorrect password and submit.<br>3. Note the error message.<br>4. Return to the login page.<br>5. Enter an unregistered but valid-format email (`not.registered.qa@example.com`) with any password and submit.<br>6. Note the error message. |
| Expected result | Both attempts return the same generic credentials error, so the response does not reveal whether the email is registered. |
| Actual result | The responses differ. A registered email with a wrong password returns **"The credentials provided are incorrect"**. An unregistered email returns **"No customer account found"**. The different messages let a user determine which email addresses have accounts. |
| Severity | Low |
| Priority | Medium |
| Reproducibility | Always — reproduced 2/2 with two different unregistered addresses (`not.registered.qa@example.com`, `another.unknown.qa@example.com`) |
| Evidence | `docs/screenshots/manual/TC-011_login-wrong-password.png`<br>`docs/screenshots/manual/TC-012_login-unregistered-email.png`<br>`docs/screenshots/manual/TC-012_login-unregistered-email-2.png` |
| Status | Open |
| Related items | Requirement `REQ-AUTH-02` · Scenario `SC-AUTH-03` · Test case `TC-012` |

#### Impact

An attacker can submit candidate email addresses and distinguish registered accounts from
unregistered ones without a password. This is **user enumeration** (CWE-204: Observable
Response Discrepancy). It enables targeted phishing and credential-stuffing shortlists.
No account access is gained directly, which is why severity is Low rather than High.

#### Root-cause hypothesis

The login flow appears to validate the email against the customer record first and surface
a dedicated "no account" message, instead of failing authentication with one generic
message for every unsuccessful attempt.

#### Recommendation

Return a single generic message for all failed logins (for example, only
"Login was unsuccessful. Please correct the errors and try again.") and log the specific
reason server-side. The password-recovery flow should follow the same principle; that is
checked separately in TC-017.

#### Notes

This is default nopCommerce behaviour, so the vendor may classify it as by design. It is
still recorded because it is observable, reproducible, and contradicts the security
expectation stated in the test case. It does not block the demo store's core journey.

---

### BUG-002 — Login accepts empty credentials without required-field validation

| Field | Value |
|---|---|
| Bug ID | BUG-002 |
| Bug title | Login form submits with empty Email and Password and returns an account-lookup error instead of required-field validation |
| Module | Authentication / Login |
| Environment | Public demo `https://demowebshop.tricentis.com/` · Brave 1.99.57 (Chromium 157) · CachyOS Linux · 18 Nov 2026 |
| Preconditions | User is signed out and the login page is open |
| Steps to reproduce | 1. Open `https://demowebshop.tricentis.com/login` in a fresh tab.<br>2. Leave **Email** and **Password** completely empty.<br>3. Click **Log in**.<br>4. Observe that the request is submitted rather than blocked.<br>5. Record the messages shown. |
| Expected result | Submission is blocked with field-level required messages (for example "Email is required." and "Password is required."). No account lookup occurs. |
| Actual result | The form submits with both fields empty. No required-field messages are displayed. The page instead shows **"Login was unsuccessful. Please correct the errors and try again."** and **"No customer account found"**, and the URL stays on `/login`. |
| Severity | Low |
| Priority | Low |
| Reproducibility | Always — confirmed by the screenshot with both fields empty and by DOM inspection |
| Evidence | `docs/screenshots/manual/TC-013_empty-credentials.png` |
| Status | Open |
| Related items | Requirement `REQ-AUTH-03` · Scenario `SC-AUTH-04` · Test case `TC-013` |

#### Impact

A user who submits an incomplete form receives a misleading account-level error instead of
being told which field is missing. It adds avoidable friction and returns a response that
looks like a failed login attempt rather than a validation problem.

#### Technical evidence

The rendered login form contains:

```html
<input class="email" id="Email" name="Email" type="text" value="" />
<input class="password" id="Password" name="Password" type="password" />
```

- Neither input has `required`, `data-val-required`, or any unobtrusive validation attribute.
- Email uses `type="text"`, so the browser's native email validation cannot apply.
- `jquery.validate` and `jquery.validate.unobtrusive` are loaded on the page, but there are
  no validation rules attached to these inputs.

#### Root-cause hypothesis

Required-field rules were not configured for the login inputs, and the server does not
short-circuit empty credentials before performing the customer lookup.

#### Recommendation

Add required-field validation on both client and server side, return field-level messages,
and do not perform an account lookup when either field is empty.

#### Notes

The resulting "No customer account found" message also reinforces BUG-001, but the
underlying cause here is missing validation, so it is tracked separately.

---

### BUG-003 — Password recovery reveals whether an email address is registered

| Field | Value |
|---|---|
| Bug ID | BUG-003 |
| Bug title | Password recovery returns different messages for registered and unregistered email addresses (user enumeration) |
| Module | Password recovery |
| Environment | Public demo `https://demowebshop.tricentis.com/` · Brave 1.99.57 (Chromium 157) · CachyOS Linux · 20 Nov 2026 |
| Preconditions | User is signed out and the password recovery page is open |
| Steps to reproduce | 1. Open `https://demowebshop.tricentis.com/passwordrecovery`.<br>2. Submit the registered email `milan.qa.demo.2026@example.com`.<br>3. Record the message.<br>4. Reload the page and submit an unregistered email `not.registered.qa@example.com`.<br>5. Record the message and compare. |
| Expected result | Both submissions return the same neutral message (for example "Email with instructions has been sent to you."), so the page does not reveal whether an address has an account. |
| Actual result | The registered email returns **"Email with instructions has been sent to you."** The unregistered email returns **"Email not found."** The difference allows an attacker to test which addresses are registered. |
| Severity | Low |
| Priority | Medium |
| Reproducibility | Always — distinct messages observed for both input classes |
| Evidence | `docs/screenshots/manual/TC-017_registered-email.png`<br>`docs/screenshots/manual/TC-017_unregistered-email.png` |
| Status | Open |
| Related items | Requirement `REQ-AUTH-06` · Scenario `SC-AUTH-08` · Test case `TC-017` · Related defect `BUG-001` |

#### Impact

This is the same information-disclosure class as BUG-001, exposed through a different
endpoint. Combined, the two flows give an attacker a reliable way to enumerate customer
accounts. No account access is gained, so severity remains Low.

#### Root-cause hypothesis

The recovery action looks up the email first and returns a dedicated "not found" error
instead of always showing the same confirmation.

#### Recommendation

Always show the neutral confirmation message regardless of whether the email exists, and
perform the lookup/email send asynchronously. Apply the same rule to login (BUG-001) so
both flows behave consistently.

#### Notes

Default nopCommerce behaviour and possibly by design, but still a reportable privacy
weakness. Email delivery is not verified; only the on-screen response is in scope.

---

### BUG-004 — Configurable product page shows only the base price

| Field | Value |
|---|---|
| Bug ID | BUG-004 |
| Bug title | Product page for a configurable product does not include attribute surcharges in the displayed price |
| Module | Product detail / pricing |
| Environment | Public demo `https://demowebshop.tricentis.com/` · Brave 1.99.57 (Chromium 157) · CachyOS Linux · 21 Nov 2026 |
| Preconditions | `/build-your-own-computer` open; user signed in or out (price display is the same) |
| Steps to reproduce | 1. Open `https://demowebshop.tricentis.com/build-your-own-computer` and record the price.<br>2. Change the processor to **2.2 GHz** and record the price.<br>3. Change RAM to **4GB [+20.00]** and record the price.<br>4. Tick **Acrobat Reader [+10.00]** and record the price.<br>5. Configure 2.5 GHz + 8GB + Microsoft Office, set quantity 2, and add to cart.<br>6. Open the cart and compare the unit price with the price shown on the product page. |
| Expected result | The displayed price reflects the current selection: **1265.00** with the defaults (1200 + 15 + 50), **1280.00** after the changes in steps 2–4, and **1325.00** for the configuration added in step 5. Alternatively, if the figure is intentionally a starting price, it should be labelled as such ("from 1200.00"). |
| Actual result | The product page stays at **1200.00** for every configuration, with no recalculation and no request when attributes change. The cart correctly charges **1325.00** (1200 + 15 + 60 + 50) for the configuration added in step 5. The displayed price therefore differs from the amount the customer will be charged, and it also omits the surcharges that are selected by default. |
| Severity | Low |
| Priority | Medium |
| Reproducibility | Always — four price readings across three configurations, plus a cart comparison |
| Evidence | `docs/screenshots/manual/TC-032_configurable-defaults.png`<br>`docs/screenshots/manual/TC-033_price-after-changes.png`<br>`docs/screenshots/manual/TC-034_cart-configurable.png` |
| Status | Open |
| Related items | Requirement `REQ-PRD-03` · Scenario `SC-PRD-04` · Test cases `TC-033`, `TC-034` |

#### Impact

A customer configuring the product sees a price that is lower than the price they will be
charged. No money is taken without disclosure — the cart shows the correct unit price
before checkout — so severity is Low. The commercial impact is reduced price
transparency and possible abandonment at the cart step.

#### Root-cause hypothesis

The stock nopCommerce theme renders the server-calculated base product price. The
product-details page in this theme contains no client-side price recalculation and no
attribute-change endpoint, so attribute surcharges only exist in the cart calculation.

#### Recommendation

Either recalculate the price when an attribute changes (client-side from the option
surcharges, or through an attribute-change endpoint), or explicitly label the figure as
"from 1200.00" so it cannot be mistaken for the final configured price.

#### Notes

Likely standard behaviour of the stock theme rather than a regression, but still
reportable because the displayed and charged prices differ. Automated tests must assert
the cart price, never the product-page price, for configurable products.

---

### BUG-005 — Tag-like search term returns an internal error page

| Field | Value |
|---|---|
| Bug ID | BUG-005 |
| Bug title | A search term containing `<` followed by a letter causes an unhandled server error |
| Module | Search |
| Environment | Public demo `https://demowebshop.tricentis.com/` · Brave 1.99.57 (Chromium 157) · CachyOS Linux · 21 Nov 2026 |
| Preconditions | Store reachable; user signed in or out (the failure is independent of session state) |
| Steps to reproduce | 1. Enter `<script>alert(1)</script>` in the header search box and submit.<br>2. Observe the page.<br>3. Repeat with `x<y`, `<b>`, `<ab`, and `<img src=x>`.<br>4. As controls, search `a<3`, `a< b`, `abc<`, and `price <100`. |
| Expected result | Each term is handled as plain text and produces the normal search results or the no-results message. No error page is shown and no script executes. |
| Actual result | Every term containing `<` immediately followed by a letter renders the generic error page **"We're sorry, an internal error occurred."** with HTTP status **200**. Reproduced with all five inputs above. Control terms where `<` is followed by a digit, a space, or the end of the string return the normal no-results page, so the trigger is specifically a tag-like fragment. No script executes and no stack trace is exposed. |
| Severity | Medium |
| Priority | Medium |
| Reproducibility | Always — 5/5 tag-like inputs, repeated across two sessions |
| Evidence | `docs/screenshots/manual/TC-044_search-special-chars.png` |
| Status | Open |
| Related items | Requirement `REQ-SRC-04` · Scenario `SC-SRC-04` · Test case `TC-044` |

#### Impact

A search for input such as `x<y` fails with an error page instead of results. The store
remains available and the workaround is trivial (remove the `<`), which keeps severity at
Medium. Because the error page is returned with HTTP 200, uptime monitoring and error
alerting may not detect these failures.

#### Root-cause hypothesis

The keyword is passed through a component that parses or strips HTML-like fragments. An
opening angle bracket followed by a letter is interpreted as the start of a tag, and the
parser throws; the exception is caught by the global error handler and rendered as the
Error view.

#### Recommendation

Treat the search term as plain text: HTML-encode or strip tag-like content without
parsing it, and wrap the search in the normal validation path so malformed input returns
the no-results page. Return an actual 5xx status for genuine server errors so monitoring
can detect them.

#### Notes

This is a robustness defect, not a confirmed injection vulnerability: the payload did not
execute and no stack trace was disclosed. A deeper security assessment is out of scope.

---

### BUG-006 — Gift-card rejection message refers to a coupon code

| Field | Value |
|---|---|
| Bug ID | BUG-006 |
| Bug title | The Gift Cards field rejects an invalid code with "The coupon code you entered couldn't be applied to your order" |
| Module | Shopping cart |
| Environment | Public demo `https://demowebshop.tricentis.com/` · Brave 1.99.57 (Chromium 157) · CachyOS Linux · 21 Nov 2026 |
| Preconditions | Signed in; cart contains at least one product |
| Steps to reproduce | 1. Open the cart.<br>2. Expand **Gift Cards** and enter `INVALIDGIFT`.<br>3. Click **Add gift card**.<br>4. Compare with the **Discount Code** box, which returns the same sentence. |
| Expected result | A rejection message in the gift-card block refers to a gift card, for example "The gift card code you entered couldn't be applied to your order." |
| Actual result | The gift-card block shows **"The coupon code you entered couldn't be applied to your order."** The text is rendered inside `<div class="giftcard-box">` directly below the gift-card input, so it is the gift-card feedback and not a leftover message. The discount box produces the same sentence, which is correct there. Reproduced twice in two sessions. The codes are correctly rejected and totals do not change. |
| Severity | Low |
| Priority | Low |
| Reproducibility | Always — 2/2 |
| Evidence | `docs/screenshots/manual/TC-067_cart-invalid-codes.png` — the message is shown inside the Gift Cards box |
| Status | Open |
| Related items | Requirement `REQ-CART-06` · Scenario `SC-CART-11` · Test case `TC-067` |

#### Impact

Users who mistype a gift card are told that a **coupon** failed. The two inputs sit side by side
and use different labels, so the wording blurs which artefact was rejected. No functional
impact: the code is not applied, the Sub-Total is unchanged, and retrying in the correct
field works.

#### Root-cause hypothesis

The gift-card action reuses the coupon error resource string instead of a gift-card-specific
one. The nopCommerce resource likely exists as a separate key that was not wired up for this
view.

#### Recommendation

Give the gift-card path its own message ("The gift card code you entered couldn't be applied
to your order") or a neutral wording such as "The code you entered couldn't be applied to
your order."

#### Notes

Cosmetic content defect. The functional behaviour required by `REQ-CART-06` passed, so
TC-067 remains a Pass with this defect linked.

---

## 3. Defects deliberately not raised

| Observation | Why it is not a defect |
|---|---|
| Shopping cart showed 5 items before any cart test | Pre-existing session state from earlier browsing, not application malfunction |
| Success page does not show the header in the saved screenshot | Evidence capture limitation, not application behaviour |
| First TC-005 attempt showed a duplicate-email error as well as the mismatch | Test data error: the form retained the previous email |
| `/order/history` returns a 404 | Invalid route, not a broken access control. The real endpoint is `/customer/orders`, which redirects to login correctly |
| Demo slowness / occasional latency | Shared public environment, not reproducible application behaviour |
| Configurable product's HDD group is required but has no default selection | The required attribute is enforced: add-to-cart without HDD returns "Please select HDD". A conscious choice is valid design; the inconsistency with other groups was logged as an observation, not a defect |
| `%`, `'`, and `--` return "Search term minimum length is 3 characters" | Correct enforcement of the three-character rule — each input is shorter than three characters. A test-design error in TC-044, not an application defect |
| A price filter with zero matching products shows an empty product area and no no-results message | REQ-FLT-02 only requires the filter to return in-range products, which it does. The search page shows a message but the category filter does not; logged as a UX observation, not a defect |
| A quantity of 0 or -1 silently removes the line, with no validation message | The cart shows the explicit empty state and no negative total is ever produced, which is the requirement (`REQ-CART-05`). Removal is a valid interpretation of a non-positive quantity |
| A non-numeric quantity (`abc`) reverts to the previous value with no visible message | The value is rejected, the totals stay correct, and no error page appears. The missing feedback is a UX gap; `REQ-CART-05` only requires totals to remain valid |
| Checkout accepts `!!` as a postal code and `abc` as a phone number | Assumption A6 asked for the exact rules to be verified. Only presence is enforced for these fields; the email format is validated. Recorded as an assumption correction, not a defect |
| All shipping methods are priced 0.00 | Demo store configuration, not a calculation fault. TC-085 therefore verifies selectability and total consistency rather than price differentiation |

---

## 4. Retest log

| Bug ID | Retest date | Build/environment | Result | Status after retest |
|---|---|---|---|---|
| — | — | — | — | — |

The retest log will be completed if a fix becomes available or before the final execution
summary. No defect will be closed without an actual retest.
