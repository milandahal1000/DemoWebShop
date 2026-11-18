# Project Overview

| Field | Value |
|---|---|
| Project title | Demo Web Shop — QA Portfolio (Manual + Selenium) |
| Document | Project Overview |
| Version | 0.1 (Phase 1 — awaiting review) |
| Author | Milan Dahal |
| Date | 18 November 2026 |
| Repository | `github.com/milandahal1000/DemoWebShop` |

---

## 1. Project introduction

This project is an end-to-end software testing engagement against a public e-commerce
demo application. It covers the full QA lifecycle: application analysis, test planning,
manual test design and execution, defect reporting, Selenium automation with the Page
Object Model, HTML reporting, execution evidence, and portfolio documentation.

The purpose is twofold:

1. **Demonstrate practical QA skills** in a realistic, evidence-based way for a
   beginner-to-intermediate QA Engineer portfolio.
2. **Build genuine testing knowledge** by explaining *why* each test, locator, fixture,
   and architectural decision exists.

This is a **testing project**, not a product. No application code is being developed or
modified.

---

## 2. Application under test

| Attribute | Detail |
|---|---|
| Application name | Tricentis Demo Web Shop |
| URL | https://demowebshop.tricentis.com/ |
| Application type | Public e-commerce demo storefront (B2C) |
| Platform | Web application, server-rendered HTML, responsive theme |
| Underlying product | nopCommerce (identified from the site footer) |
| Environment | Public shared demo — **not** production customer data, **not** a staging environment we control |
| Currency | US Dollar (USD) |
| Observed content | 7 top-level categories, featured products, newsletter, community poll, blog/news, product reviews |
| Public API | None exposed — `/api/` and `/api/products` returned HTTP 404 |
| Crawling policy | `robots.txt` returns `Disallow: /` |

### 2.1 Why this application

- It is published by Tricentis explicitly as a practice/demo system, so functional
  testing is appropriate and authorised.
- It contains the workflows recruiters expect to see: authentication, catalog,
  search, filtering, cart, checkout, and account management.
- It has realistic validation rules and configurable products, which allows meaningful
  positive, negative, and boundary testing instead of trivial happy-path scripts.
- It has **no public API**, which is a realistic constraint: API testing is documented
  as out of scope rather than forced or invented.

### 2.2 Testing limitations of this application

| Limitation | Impact on testing |
|---|---|
| Shared public database | Other testers create accounts, reviews, and orders; data can change between runs. Tests must not depend on exact global counts. |
| Periodic demo resets | Pre-registered accounts may disappear. Credentials live in a local `.env`; tests should fail with a clear message if the account is missing. |
| No admin access | Product/price/stock setup cannot be controlled; tests verify observed behaviour, not seeded fixtures. |
| No test/staging environment | Negative and destructive-looking actions are limited to harmless demo data. |
| `robots.txt` disallows crawling | Automation is kept to a single headed browser session at human pace. No load, stress, or crawl testing. |
| External availability | Site latency/outages are environment issues, not application defects. |

---

## 3. Target users

| User type | Description | Relevant workflows |
|---|---|---|
| Guest shopper | Unauthenticated visitor | Browse, search, filter, cart, guest checkout |
| Registered customer | Signed-in shopper | Account, addresses, wishlist, checkout, order history, reviews |
| Returning customer | Registered user signing in again | Login, password recovery, order history |
| QA engineer / trainee | Person testing the demo | All workflows, validation, regression |

---

## 4. Main application modules

| # | Module | Key functionality observed |
|---|---|---|
| 1 | Home | Header, navigation, featured products, newsletter, poll, footer |
| 2 | Registration | Gender radio, first name, last name, email, password, confirm password |
| 3 | Login / Logout | Email, password, remember me, forgot password, form authentication |
| 4 | Password recovery | Email submission and confirmation message |
| 5 | Catalog | 7 top-level categories; Computers has 3 sub-categories |
| 6 | Product detail | Price/old price, availability, quantity, description, reviews, tags, related products |
| 7 | Configurable products | "Build your own computer" — dropdown, radio, and checkbox attributes that change price |
| 8 | Gift cards | Recipient name/email, sender name/email, message |
| 9 | Digital downloads | Downloadable sample and cart behaviour |
| 10 | Search | Header search box, results page, advanced search panel |
| 11 | Sort / filter / paging | Sort by position/name/price/created, price ranges, 4/8/12 per page, grid/list view |
| 12 | Shopping cart | Add, update quantity, remove, subtotal, discount code, gift card code, estimate shipping, terms |
| 13 | Checkout | Guest or registered, billing address, shipping method, payment method, confirm order |
| 14 | Orders | Confirmation page, order history, order details |
| 15 | Wishlist / Compare | Add, view, remove, move to cart, comparison table |
| 16 | My account | Customer info, addresses, orders, downloads, reward points, change password |
| 17 | Contact us | Full name, email, enquiry |
| 18 | Newsletter | Email subscription and validation |
| 19 | Content pages | Sitemap, shipping & returns, privacy, conditions, about, blog, news |

---

## 5. Project objectives

1. Produce professional test planning artefacts (overview, plan, scenarios, traceability).
2. Design repeatable manual test cases with realistic test data.
3. Execute a prioritised manual regression set and record only confirmed results.
4. Report defects that are genuinely reproducible and evidenced.
5. Build a maintainable Selenium + Pytest suite using the Page Object Model.
6. Centralise test data and fixtures, capture failure screenshots, and publish an HTML report.
7. Present accurate results, limitations, and evidence in a recruiter-ready README.

---

## 6. Testing approach

**Hybrid manual + automation**, delivered in reviewed phases.

| Layer | Approach |
|---|---|
| Test design | Derived requirements from observed behaviour; risk-based prioritisation |
| Manual testing | Exploratory-informed scripted cases; positive, negative, boundary, session, business-rule checks |
| Automation | Selenium + Pytest, module-by-module, Page Object Model, explicit waits |
| Data | Centralised non-sensitive data in `config/test_data.py`; credentials in `.env` |
| Evidence | Manual screenshots in `docs/screenshots/manual/`; automation report and failure screenshots in `reports/`, final copies in `docs/` |
| Reporting | pytest-html with environment metadata, plus `docs/test-execution-summary.md` |

**Testing types in scope:** functional, positive, negative, boundary value, equivalence
partitioning, input validation, navigation/UI, session and authentication, error
handling, business-rule validation, regression.

**Explicitly out of scope:** API testing (no public API), performance/load,
security penetration testing, accessibility audit, admin-panel testing, mobile native
apps, real payment processing, email delivery verification, multi-currency/localisation,
and cross-browser matrix beyond the primary browser.

---

## 7. Technology stack

| Technology | Purpose | Status |
|---|---|---|
| Python 3.14.10 | Automation language | Installed |
| Selenium WebDriver 4.x | Browser automation | To install (Phase 3) |
| Pytest | Test runner, fixtures, parametrisation | To install (Phase 3) |
| pytest-html | HTML reporting | To install (Phase 3) |
| Page Object Model | Automation architecture | Phase 5 |
| Brave 1.99.57 (Chromium 157) | Primary test browser | Installed |
| Google Chrome 157 (Flatpak) | Fallback browser | Installed |
| Git + GitHub | Version control and portfolio hosting | Configured |
| VS Code / editor | Development environment | Available |
| fish shell | Local shell | Active |

**Why no API testing tools:** the application exposes no public API. Adding Postman
would produce no genuine evidence.

---

## 8. Deliverables

| Deliverable | Location | Phase |
|---|---|---|
| Project overview | `docs/project-overview.md` | 1 |
| Test plan | `docs/test-plan.md` | 1 |
| Test scenarios | `docs/test-scenarios.md` | 1 |
| Requirements traceability matrix | `docs/requirements-traceability-matrix.md` | 1, updated in 9 |
| Manual test cases | `docs/test-cases.md` | 2 |
| Bug reports | `docs/bug-reports.md` | 2 |
| Manual execution summary | Section in `docs/test-cases.md` / results file | 2 |
| Automation framework | `config/`, `pages/`, `tests/`, `conftest.py` | 3–6 |
| HTML report | `reports/automation-report.html` → `docs/reports/` | 7, 9 |
| Test execution summary | `docs/test-execution-summary.md` | 9 |
| Portfolio README | `README.md` | 10 |
| Evidence screenshots | `docs/screenshots/` | 2, 9 |

---

## 9. Assumptions

1. The site is published for practice and low-volume functional testing is acceptable.
2. Requirements are **derived from observed behaviour**, because no formal specification
   is published. Every derived requirement is labelled as an assumption.
3. Demo payment methods (cash on delivery, check/money order) involve no real money.
4. The default nopCommerce password policy is assumed to be a minimum of 6 characters;
   this must be verified in Phase 2 before any test depends on it.
5. One dedicated test account is sufficient for authenticated coverage.
6. Tests target a single browser (Brave) as the primary supported environment.

---

## 10. Document index

| Document | Purpose |
|---|---|
| `project-overview.md` | This document |
| `test-plan.md` | Scope, strategy, environment, criteria, risks |
| `test-scenarios.md` | Prioritised scenario inventory by module |
| `requirements-traceability-matrix.md` | Requirement → scenario → test coverage mapping |
| `test-cases.md` *(planned, Phase 2)* | Detailed executable manual cases |
| `bug-reports.md` *(planned, Phase 2)* | Confirmed defects only |
| `test-execution-summary.md` *(planned, Phase 9)* | Final verified results |
