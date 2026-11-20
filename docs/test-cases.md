# Manual Test Cases

| Field | Value |
|---|---|
| Project | Demo Web Shop — QA Portfolio (Manual + Selenium) |
| Document | Manual Test Case Catalogue |
| Version | 0.1 — Batch 1 (Registration + Authentication) |
| Author | Milan Dahal |
| Date | 18 November 2026 |
| Application | https://demowebshop.tricentis.com/ |
| Related | `test-scenarios.md`, `requirements-traceability-matrix.md`, `bug-reports.md` |

---

## 1. How this document is maintained

Each test case contains the fields requested by the project standard, plus two
traceability fields (`Related scenario`, `Automation candidate`).

| Field | Meaning |
|---|---|
| Test Case ID | Unique identifier (`TC-xxx`) |
| Module | Application area under test |
| Related scenario | Scenario from `test-scenarios.md` |
| Test Case Title | Short behaviour-focused description |
| Preconditions | State required before step 1 |
| Test Data | Inputs, sourced from `config/test_data.py` or `.env` |
| Test Steps | Numbered, repeatable actions |
| Expected Result | What the application must do |
| Actual Result | What was actually observed — filled only during execution |
| Status | Pass / Fail / Blocked / Not Run |
| Priority | Critical / High / Medium / Low |
| Evidence | Screenshot or report reference |
| Linked defect | `BUG-xxx` when a confirmed defect exists |

### Status rules

- **Not Run** — no execution yet. This is the default for every case below.
- **Pass** — the observed result matched the expected result, with evidence recorded.
- **Fail** — observed behaviour differed and the difference was reproduced.
- **Blocked** — could not execute because of an environment or dependency problem,
  with the reason recorded.

A case is never marked Pass from memory or assumption. If a result changes after a
retest, the status and actual result are updated in place.

### Evidence convention

```
docs/screenshots/manual/TC-001_registration-success.png
docs/screenshots/manual/TC-011_login-error.png
```

Screenshots must show the relevant page state and, where useful, the validation message.
No fabricated, stock, or edited evidence is permitted.

---

## 2. Test data conventions

Credentials are **never** written into this document. They live in the project `.env`
and are referenced here as `<TEST_EMAIL>` / `<TEST_PASSWORD>`.

| Data item | Value / source | Notes |
|---|---|---|
| Base URL | `https://demowebshop.tricentis.com/` | Public demo |
| Test account email | `<TEST_EMAIL>` from `.env` | Created once by TC-001 |
| Test account password | `<TEST_PASSWORD>` from `.env` | Minimum length assumption A1 |
| First name / Last name | `Milan` / `Dahal` | Non-sensitive demo data |
| Invalid email formats | `milan.qa@`, `milan.qa.example.com` | Equivalent invalid classes |
| Wrong password | `WrongPass!2026` | Deliberately incorrect |
| Unregistered email | `not.registered.qa@example.com` | Valid format, no account |
| Known product | `Computing and Internet` (Books) | Price 10.00 at analysis time |
| Known product | `Build your own computer` | Configurable product |

**Important:** prices and product availability on the public demo can change. Assertions
on exact prices must be re-checked immediately before execution and recorded as observed.

---

## 3. Case ID allocation

| Module | Reserved range | Status |
|---|---|---|
| Registration | TC-001 – TC-006 | Written (Batch 1) |
| Authentication / password recovery | TC-010 – TC-017 | Written (Batch 1) |
| Catalog / navigation | TC-020 – TC-023 | Pending Batch 2 |
| Product detail | TC-030 – TC-035 | Pending Batch 2 |
| Search | TC-040 – TC-043 | Pending Batch 2 |
| Sort / filter / paging | TC-050 – TC-055 | Pending Batch 3 |
| Cart | TC-060 – TC-067 | Pending Batch 3 |
| Checkout | TC-080 – TC-088 | Pending Batch 4 |
| Orders | TC-090 – TC-092 | Pending Batch 4 |
| Wishlist / compare | TC-100 – TC-103 | Pending Batch 5 |
| My account | TC-110 – TC-114 | Pending Batch 5 |
| Contact / newsletter | TC-120 – TC-123 | Pending Batch 5 |
| Session / edge | TC-130 – TC-132 | Pending Batch 5 |

---

## 4. Execution summary (updated after each batch)

| Status | Count |
|---|---:|
| Total written | 14 |
| Passed | 11 |
| Failed | 3 |
| Blocked | 0 |
| Not Run | 0 |
| Confirmed defects | 3 |

**Batch 1 complete.** All 14 cases executed: 11 passed, 3 failed, 0 blocked. Failures: TC-012 → BUG-001, TC-013 → BUG-002, TC-017 → BUG-003. No Critical or High severity defects found.

---

## 5. Batch 1 — Registration

### TC-001 — Register with valid mandatory data

| Field | Value |
|---|---|
| Test Case ID | TC-001 |
| Module | Registration |
| Related scenario | SC-REG-01 |
| Test Case Title | A new visitor can register with valid mandatory data |
| Priority | Critical |
| Automation candidate | Yes |
| Preconditions | Store reachable; browser signed out; `<TEST_EMAIL>` has no existing account |
| Test Data | Gender: Male · First name: `Milan` · Last name: `Dahal` · Email: `<TEST_EMAIL>` · Password: `<TEST_PASSWORD>` · Confirm password: `<TEST_PASSWORD>` |
| Test Steps | 1. Open the home page.<br>2. Click **Register** in the header.<br>3. Confirm the Registration page is displayed.<br>4. Complete every mandatory field with the test data.<br>5. Click **Register**.<br>6. Observe the confirmation and the header state.<br>7. Reload the page. |
| Expected Result | Registration completes with a success confirmation (expected message: "Your registration completed" — exact wording to be recorded). The header shows the account email and a **Log out** link, confirming an authenticated session. The confirmation persists after reload without duplicate submission. |
| Actual Result | Registration succeeded. The page displayed **"Your registration completed"** and redirected to `/registerresult/1`. The header showed the account email and a **Log out** link, confirming an authenticated session. The session survived a page reload, and `/customer/info` opened the account page. |
| Status | **Pass** |
| Evidence | `docs/screenshots/manual/TC-001_registration-form.png`<br>`docs/screenshots/manual/TC-001_registration-success.png` |
| Linked defect | — |
| Notes | This case creates the shared test account used by the remaining authenticated cases. Record the email/password in local `.env` only. This is a documented dependency, not a hidden one. |

---

### TC-002 — Submit registration with all mandatory fields empty

| Field | Value |
|---|---|
| Test Case ID | TC-002 |
| Module | Registration |
| Related scenario | SC-REG-02 |
| Test Case Title | Registration is blocked when mandatory fields are empty |
| Priority | High |
| Automation candidate | Yes |
| Preconditions | Store reachable; browser signed out; Registration page open |
| Test Data | All fields empty; gender left unselected |
| Test Steps | 1. Open `/register`.<br>2. Leave every field empty.<br>3. Click **Register**.<br>4. Record every validation message displayed.<br>5. Confirm the page does not navigate away and no session is created. |
| Expected Result | Submission is blocked. Each mandatory field shows a required-field message (e.g. "First name is required."). The URL remains `/register`, the form retains no invalid submission, and no account or session is created. |
| Actual Result | Submission was blocked and the form stayed on the registration page. Page-level messages were displayed: **"First name is required."**, **"Last name is required."**, **"Email is required."**, and **"Password is required."** for **both** the Password and Confirm password fields. No message appeared for Gender. No success message or redirect occurred. |
| Status | **Pass** |
| Evidence | `docs/screenshots/manual/TC-002_empty-form-errors.png` |
| Linked defect | — |
| Notes | The absence of a Gender message is consistent with Gender being optional (assumption now supported). Capture the exact message text — automation assertions will reuse it. Verify whether validation is client-side, server-side, or both. |

---

### TC-003 — Register with malformed email addresses

| Field | Value |
|---|---|
| Test Case ID | TC-003 |
| Module | Registration |
| Related scenario | SC-REG-03 |
| Test Case Title | Malformed email addresses are rejected at registration |
| Priority | High |
| Automation candidate | Yes |
| Preconditions | Store reachable; browser signed out; Registration page open |
| Test Data | Valid first/last name and password; Email value 1: `milan.qa@` · Email value 2: `milan.qa.example.com` |
| Test Steps | 1. Complete the form with Email value 1.<br>2. Click **Register**.<br>3. Record the validation message and page behaviour.<br>4. Replace the email with Email value 2.<br>5. Click **Register** again.<br>6. Record the result. |
| Expected Result | Both values are rejected as invalid email addresses. The form remains displayed with a clear email validation message. No account is created and no session is started. |
| Actual Result | Both values were rejected. **`milan.qa@`** and **`milan.qa.example.com`** each produced the page-level message **"Wrong email"** next to the email field. No redirect occurred and no success message appeared. The message is server-rendered rather than a native browser tooltip, indicating server-side (or unobtrusive client-side) validation. |
| Status | **Pass** |
| Evidence | `docs/screenshots/manual/TC-003_invalid-email-1.png`<br>`docs/screenshots/manual/TC-003_invalid-email-2.png` |
| Linked defect | — |
| Notes | Two equivalent invalid classes are tested in one case to avoid duplicate case overhead. The rendered message is exactly "Wrong email" — automation will assert on that text. |

---

### TC-004 — Register with an already registered email

| Field | Value |
|---|---|
| Test Case ID | TC-004 |
| Module | Registration |
| Related scenario | SC-REG-04 |
| Test Case Title | Duplicate email registration is rejected |
| Priority | High |
| Automation candidate | Partial |
| Preconditions | TC-001 completed; `<TEST_EMAIL>` already exists; browser signed out |
| Test Data | Email: `<TEST_EMAIL>` · First name: `Duplicate` · Last name: `Tester` · Password: `<TEST_PASSWORD>` |
| Test Steps | 1. Open `/register`.<br>2. Complete the form using the existing account email.<br>3. Click **Register**.<br>4. Record the error and check the header for a session. |
| Expected Result | Registration is refused with a duplicate-email message (expected: an error stating the email already exists). No second account is created and no session is started. |
| Actual Result | Registration was refused. The form displayed the banner **"The specified email already exists"** and stayed on the registration page (URL unchanged). No session was created and no second account exists for that address. |
| Status | **Pass** |
| Evidence | `docs/screenshots/manual/TC-004_duplicate-email.png` |
| Linked defect | — |
| Notes | Verifies assumption A8 (email uniqueness) — **confirmed**. |

---

### TC-005 — Password confirmation must match

| Field | Value |
|---|---|
| Test Case ID | TC-005 |
| Module | Registration |
| Related scenario | SC-REG-05 |
| Test Case Title | Mismatched password confirmation blocks registration |
| Priority | High |
| Automation candidate | Yes |
| Preconditions | Store reachable; browser signed out; Registration page open |
| Test Data | Email: a fresh unique address · Password: `<TEST_PASSWORD>` · Confirm password: `DifferentPass!2026` |
| Test Steps | 1. Complete the form with valid values.<br>2. Enter a different value in **Confirm password**.<br>3. Click **Register**.<br>4. Record the validation message.<br>5. Confirm no session or account was created. |
| Expected Result | Registration is blocked with a password-mismatch message (expected: "The password and confirmation password do not match."). The form remains on screen. |
| Actual Result | Registration was blocked with **"The password and confirmation password do not match."** displayed next to the confirm field. The URL did not change, no success message appeared, and no session was created. A first attempt was discarded because the email field still contained the TC-001 address and produced a duplicate-email error alongside the mismatch; the case was re-executed from a clean form with a new address. |
| Status | **Pass** |
| Evidence | `docs/screenshots/manual/TC-005_password-mismatch.png` |
| Linked defect | — |
| Notes | The discarded attempt is a test-data issue, not an application defect. Lesson recorded: change one variable at a time and start from a clean form. |

---

### TC-006 — Password length boundary

| Field | Value |
|---|---|
| Test Case ID | TC-006 |
| Module | Registration |
| Related scenario | SC-REG-06 |
| Test Case Title | Password length boundary is enforced at registration |
| Priority | Medium |
| Automation candidate | Partial |
| Preconditions | Store reachable; browser signed out; two unused email addresses available |
| Test Data | Email A + password `Ab1!x` (5 characters) · Email B + password `Ab1!xy` (6 characters) |
| Test Steps | 1. Open `/register`.<br>2. Complete the form using Email A and the 5-character password in both password fields.<br>3. Submit and record the result.<br>4. Repeat with Email B and the 6-character password.<br>5. Record whether registration succeeds. |
| Expected Result | The 5-character password is rejected with a minimum-length message. The 6-character password is accepted, confirming assumption A1. If the application accepts 5 characters or rejects 6, record the observed rule instead of forcing the assumption. |
| Actual Result | Boundary confirmed. The 5-character password (`Ab1!x`) was rejected with **"The password should have at least 6 characters."** The 6-character password (`Ab1!xy`) was accepted and the account was created, showing **"Your registration completed"**. Minimum length is therefore exactly 6 characters. |
| Status | **Pass** |
| Evidence | `docs/screenshots/manual/TC-006_password-5chars.png`<br>`docs/screenshots/manual/TC-006_password-6chars.png` |
| Linked defect | — |
| Notes | Assumption A1 is **confirmed**. The 6-character registration created a second demo account (`milan.qa.boundary6.2026@example.com`); this is expected demo noise, not a defect. |

---

## 6. Batch 1 — Authentication and password recovery

### TC-010 — Sign in with valid credentials

| Field | Value |
|---|---|
| Test Case ID | TC-010 |
| Module | Authentication |
| Related scenario | SC-AUTH-01 |
| Test Case Title | A registered user can sign in with valid credentials |
| Priority | Critical |
| Automation candidate | Yes |
| Preconditions | `<TEST_EMAIL>` account exists; browser signed out |
| Test Data | Email: `<TEST_EMAIL>` · Password: `<TEST_PASSWORD>` |
| Test Steps | 1. Open `/login`.<br>2. Enter the registered email and correct password.<br>3. Optionally tick **Remember me** — record whether it is ticked.<br>4. Click **Log in**.<br>5. Observe the landing page and header.<br>6. Open `/customer/info`. |
| Expected Result | Login succeeds. The user is redirected away from the login page, the header shows the account email and a **Log out** link, and `/customer/info` opens instead of redirecting. |
| Actual Result | Login succeeded. The user was redirected to the home page (`https://demowebshop.tricentis.com/`) and the header displayed the account email and a **Log out** link. `/customer/info` opened the **My account – Customer info** page with the registered first name, last name, and email. |
| Status | **Pass** |
| Evidence | `docs/screenshots/manual/TC-010_login-success.png` |
| Linked defect | — |
| Notes | The header also showed **Shopping cart (5)** before any cart case was executed. This is pre-existing session/account cart state, not a defect; the cart must be emptied before the cart batch to establish a known baseline. |

---

### TC-011 — Sign in with an incorrect password

| Field | Value |
|---|---|
| Test Case ID | TC-011 |
| Module | Authentication |
| Related scenario | SC-AUTH-02 |
| Test Case Title | Incorrect password is rejected |
| Priority | High |
| Automation candidate | Yes |
| Preconditions | Registered account exists; browser signed out |
| Test Data | Email: `<TEST_EMAIL>` · Password: `WrongPass!2026` |
| Test Steps | 1. Open `/login`.<br>2. Enter the registered email with the wrong password.<br>3. Click **Log in**.<br>4. Record the error message.<br>5. Check the header and open `/customer/info`. |
| Expected Result | Login fails with a generic credentials error (expected: "Login was unsuccessful. Please correct the errors and try again." and "The credentials provided are incorrect."). No session is created; `/customer/info` redirects to login. |
| Actual Result | Login failed. The page displayed **"Login was unsuccessful. Please correct the errors and try again."** and **"The credentials provided are incorrect"**. The email field retained its value, the password field was cleared, and the URL remained `/login`. No authenticated header was shown. |
| Status | **Pass** |
| Evidence | `docs/screenshots/manual/TC-011_login-wrong-password.png` |
| Linked defect | — |

---

### TC-012 — Sign in with an unregistered email

| Field | Value |
|---|---|
| Test Case ID | TC-012 |
| Module | Authentication |
| Related scenario | SC-AUTH-03 |
| Test Case Title | Unregistered email cannot sign in and is not disclosed |
| Priority | High |
| Automation candidate | Yes |
| Preconditions | Browser signed out; email has no account |
| Test Data | Email: `not.registered.qa@example.com` · Password: `AnyPass!2026` |
| Test Steps | 1. Open `/login`.<br>2. Enter the unregistered email and a password.<br>3. Click **Log in**.<br>4. Compare the message with the message from TC-011. |
| Expected Result | Login fails. The message does not reveal whether the email exists and should be equivalent to the invalid-password message. No session is created. |
| Actual Result | Login failed, but the message **differs from TC-011**: the page displayed **"Login was unsuccessful. Please correct the errors and try again."** and **"No customer account found"**. The URL stayed at `/login`, no session was created, and the behaviour reproduced on a second, different unregistered address (`another.unknown.qa@example.com`). This discloses whether an email is registered. |
| Status | **Fail** |
| Evidence | `docs/screenshots/manual/TC-012_login-unregistered-email.png`<br>`docs/screenshots/manual/TC-012_login-unregistered-email-2.png` |
| Linked defect | **BUG-001** |
| Notes | User enumeration (CWE-204). Default nopCommerce behaviour, but still a reportable privacy weakness. See `bug-reports.md`. |

---

### TC-013 — Submit login with empty credentials

| Field | Value |
|---|---|
| Test Case ID | TC-013 |
| Module | Authentication |
| Related scenario | SC-AUTH-04 |
| Test Case Title | Empty login fields are rejected |
| Priority | High |
| Automation candidate | Yes |
| Preconditions | Browser signed out; login page open |
| Test Data | Email: empty · Password: empty |
| Test Steps | 1. Open `/login`.<br>2. Leave both fields empty.<br>3. Click **Log in**.<br>4. Record validation feedback and the page state. |
| Expected Result | Submission is blocked with validation feedback (e.g. "Email is required." / "Password is required."). No session is created. |
| Actual Result | The form **submitted with both fields empty**. No required-field messages appeared. The page displayed **"Login was unsuccessful. Please correct the errors and try again."** and **"No customer account found"**. The URL did not change and no session was created. The rendered inputs have no `required`/`data-val-required` attributes, confirming there is no client-side required validation. Reproduced 2/2 on clean forms. |
| Status | **Fail** |
| Evidence | `docs/screenshots/manual/TC-013_empty-credentials.png` |
| Linked defect | **BUG-002** |
| Notes | Record whether the browser's native HTML5 validation appears before any server-side message — in this run it did not, because Email is `type="text"` and no `required` attributes are present. Both client-side and server-side required checks are missing. |

---

### TC-014 — Sign out ends the session

| Field | Value |
|---|---|
| Test Case ID | TC-014 |
| Module | Authentication |
| Related scenario | SC-AUTH-05 |
| Test Case Title | Logout terminates the authenticated session |
| Priority | Critical |
| Automation candidate | Yes |
| Preconditions | User signed in (TC-010) |
| Test Data | None |
| Test Steps | 1. From any page, click **Log out** in the header.<br>2. Observe the landing page and header.<br>3. Open `/customer/info` directly.<br>4. Open `/wishlist` directly. |
| Expected Result | Logout redirects to the home page and the header changes to **Register** / **Log in**. The account email is no longer displayed. `/customer/info` redirects to the login page. The wishlist is **guest-accessible by design** and shows an empty guest wishlist, not account data — the original expectation that it would redirect was an incorrect assumption. |
| Actual Result | Logout returned the user to the home page (`/`). The header displayed **Register**, **Log in**, **Shopping cart(0)**, and **Wishlist(0)** — the account email was gone and the cart counter reset. `/customer/info` redirected to `/login?ReturnUrl=%2fcustomer%2finfo`. `/wishlist` opened the **Wishlist** page with **"The wishlist is empty!"** instead of redirecting, confirming guest wishlist support. |
| Status | **Pass** |
| Evidence | `docs/screenshots/manual/TC-014_logout-header.png`<br>`docs/screenshots/manual/TC-014_protected-redirect-1.png`<br>`docs/screenshots/manual/TC-014_protected-redirect-2.png` |
| Linked defect | — |
| Notes | Assumption corrected: wishlist is not a protected resource on this store. An unauthenticated request to `/wishlist` also returns the empty guest wishlist. Recorded as assumption A9 in the traceability matrix, not as a defect. |

---

### TC-015 — Protected page redirects to login with return URL

| Field | Value |
|---|---|
| Test Case ID | TC-015 |
| Module | Authentication |
| Related scenario | SC-AUTH-06 |
| Test Case Title | Unauthenticated access to a protected page redirects to login |
| Priority | High |
| Automation candidate | Yes |
| Preconditions | Browser signed out |
| Test Data | Target URL: `/customer/info` |
| Test Steps | 1. Open `https://demowebshop.tricentis.com/customer/info` directly.<br>2. Record the resulting URL, including the `ReturnUrl` value.<br>3. Open `https://demowebshop.tricentis.com/customer/orders` directly.<br>4. Record the resulting URL, including the `ReturnUrl` value.<br>5. Confirm no account data is visible on either page. |
| Expected Result | Both protected pages redirect to `/login` with a `returnUrl` pointing at the requested page: `/login?ReturnUrl=%2fcustomer%2finfo` and `/login?ReturnUrl=%2Fcustomer%2Forders`. The login form is displayed and no account information is exposed. |
| Actual Result | `/customer/info` redirected to `/login?ReturnUrl=%2fcustomer%2finfo` and showed the login form, with no account data. `/customer/orders` redirected to `/login?ReturnUrl=%2Fcustomer%2Forders`, also with no account data. Both redirects verified with screenshots. |
| Status | **Pass** |
| Evidence | `docs/screenshots/manual/TC-015_customer-info-redirect.png`<br>`docs/screenshots/manual/TC-015_customer-orders-redirect.png` |
| Linked defect | — |
| Notes | The original step used `/order/history`, which is **not a route on this store** and returns a 404 (`TC-015_invalid-route-404.png`). That was a test-design error, not an authorization defect. Lesson: confirm the real endpoint before classifying an access-control failure. |

---

### TC-016 — Login returns the user to the requested page

| Field | Value |
|---|---|
| Test Case ID | TC-016 |
| Module | Authentication |
| Related scenario | SC-AUTH-07 |
| Test Case Title | Successful login honours the return URL |
| Priority | Medium |
| Automation candidate | Partial |
| Preconditions | TC-015 executed and login form reached with a `returnUrl` |
| Test Data | Email: `<TEST_EMAIL>` · Password: `<TEST_PASSWORD>` |
| Test Steps | 1. Starting from the redirected login page in TC-015, sign in with valid credentials.<br>2. Observe the landing page.<br>3. Confirm the header shows an authenticated session. |
| Expected Result | After login, the user lands on the originally requested page (`/customer/info`) rather than the home page, and the page is fully rendered for the authenticated user. |
| Actual Result | After signing in from the redirected login page, the user landed on `https://demowebshop.tricentis.com/customer/orders`, showing **My account – Orders** with "No orders" and an authenticated header. The return URL was honoured. |
| Status | **Pass** |
| Evidence | `docs/screenshots/manual/TC-016_return-url.png` |
| Linked defect | — |
| Notes | Depends on TC-015; the dependency is documented and deliberate. The header again showed **Shopping cart (5)**, confirming the cart is persisted server-side for this account. |

---

### TC-017 — Password recovery does not disclose account existence

| Field | Value |
|---|---|
| Test Case ID | TC-017 |
| Module | Password recovery |
| Related scenario | SC-AUTH-08 |
| Test Case Title | Password recovery returns a neutral response for known and unknown emails |
| Priority | Medium |
| Automation candidate | No |
| Preconditions | Browser signed out; registered and unregistered email addresses available |
| Test Data | Registered: `<TEST_EMAIL>` · Unregistered: `not.registered.qa@example.com` |
| Test Steps | 1. Open `/passwordrecovery`.<br>2. Submit the registered email.<br>3. Record the confirmation message.<br>4. Return to `/passwordrecovery` and submit the unregistered email.<br>5. Compare both messages.<br>6. Do **not** click any emailed reset link (email delivery is out of scope). |
| Expected Result | Both submissions produce an equivalent neutral confirmation (expected: a message stating that email instructions have been sent). The response does not reveal whether the account exists. No error page is shown. |
| Actual Result | The responses differ. The registered email produced **"Email with instructions has been sent to you."** The unregistered email produced **"Email not found."** Both stayed on `/passwordrecovery`; the differing messages disclose whether an address is registered. |
| Status | **Fail** |
| Evidence | `docs/screenshots/manual/TC-017_registered-email.png`<br>`docs/screenshots/manual/TC-017_unregistered-email.png` |
| Linked defect | **BUG-003** |
| Notes | Same user-enumeration class as BUG-001 but a different endpoint, so it is tracked separately. Email delivery itself remains out of scope. |

---

## 7. Manual execution protocol

For every case:

1. Confirm preconditions, including that the test account still exists.
2. Execute the steps exactly as written.
3. Capture a screenshot for any visual or message-based result.
4. Record the **observed** behaviour in `Actual Result` — not a paraphrase of the
   expected result.
5. Set **Status** to Pass / Fail / Blocked.
6. If Fail, reproduce once from a clean state before raising a defect in
   `bug-reports.md`.
7. Add the evidence path and defect ID to the case.
8. Update Section 4 and the traceability matrix after the batch is reviewed.

### Batch plan

| Batch | Cases | Focus |
|---|---|---|
| 1 | TC-001 – TC-006, TC-010 – TC-017 | Registration and authentication (this document) |
| 2 | TC-020 – TC-023, TC-030 – TC-035, TC-040 – TC-043 | Catalog, product detail, search |
| 3 | TC-050 – TC-055, TC-060 – TC-067 | Sorting/filtering, cart |
| 4 | TC-080 – TC-088, TC-090 – TC-092 | Checkout and orders |
| 5 | TC-100 – TC-103, TC-110 – TC-114, TC-120 – TC-123, TC-130 – TC-132 | Wishlist, account, contact, session |
