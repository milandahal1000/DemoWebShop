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

| Metric | Count |
|---|---:|
| Confirmed defects | 1 |
| Open | 1 |
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

## 3. Defects deliberately not raised

| Observation | Why it is not a defect |
|---|---|
| Shopping cart showed 5 items before any cart test | Pre-existing session state from earlier browsing, not application malfunction |
| Success page does not show the header in the saved screenshot | Evidence capture limitation, not application behaviour |
| First TC-005 attempt showed a duplicate-email error as well as the mismatch | Test data error: the form retained the previous email |
| Demo slowness / occasional latency | Shared public environment, not reproducible application behaviour |

---

## 4. Retest log

| Bug ID | Retest date | Build/environment | Result | Status after retest |
|---|---|---|---|---|
| — | — | — | — | — |

The retest log will be completed if a fix becomes available or before the final execution
summary. No defect will be closed without an actual retest.
