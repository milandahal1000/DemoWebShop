# Test Plan

| Field | Value |
|---|---|
| Test plan identifier | `TP-DWS-001` |
| Project | Demo Web Shop — QA Portfolio (Manual + Selenium) |
| Version | 1.0 (Phase 1 — awaiting review) |
| Author | Milan Dahal |
| Date | 18 November 2026 |
| Application under test | https://demowebshop.tricentis.com/ |
| Related documents | `project-overview.md`, `test-scenarios.md`, `requirements-traceability-matrix.md` |

---

## 1. Introduction

This test plan defines how Tricentis Demo Web Shop will be tested during this project:
what is in scope, how testing will be performed, which environments and tools are used,
what must be true before testing starts and can be declared finished, and how risks are
managed.

Because the application has no published requirements specification, requirements are
**derived from observed application behaviour**. These derived requirements are recorded
in the traceability matrix and explicitly marked as assumptions.

---

## 2. Testing objectives

1. Verify the core purchase journey end to end: register → sign in → find a product →
   configure it → add to cart → check out → receive confirmation → view the order.
2. Verify form validation and business rules for valid, invalid, and boundary input.
3. Verify navigation, sorting, filtering, paging, search, and cart arithmetic.
4. Verify authentication and session behaviour, including protected-page redirects.
5. Verify account, wishlist, compare, contact, and newsletter functionality.
6. Produce reproducible defects with evidence, without misreporting environment issues.
7. Prove the main regression set is automated and repeatable through Selenium.

---

## 3. Scope

### 3.1 In scope

| Area | Coverage |
|---|---|
| Registration | Mandatory field validation, email format/uniqueness, password confirmation, success |
| Authentication | Valid/invalid login, empty fields, logout, protected pages, return URL, password recovery |
| Catalog | Home, 7 categories, sub-categories, breadcrumbs, grid/list, paging |
| Product detail | Price display, discount, configurable attributes and price change, gift card fields, downloads, add to cart |
| Search | Valid, no result, minimum length, case, special characters, global header search |
| Sorting / filtering | Five sort orders, three price ranges, page size, combined state |
| Cart | Add, duplicate add, quantity updates, remove, empty state, boundary quantities, discount/gift-card codes, persistence |
| Checkout | Guest and registered, billing validation, shipping, payment method, totals, terms, confirmation |
| Orders | Confirmation, order history, order details, access control |
| Wishlist / Compare | Add, remove, move to cart, comparison table, clear |
| My account | Customer info, address add/edit/delete + validation, change password |
| Contact / Newsletter | Valid submission, required fields, email validation |
| Session | Authenticated access, persistence, logout/back-button behaviour, guest cart on login |

### 3.2 Out of scope

| Excluded area | Reason |
|---|---|
| API testing (Postman / Requests) | No public API; `/api/` returns 404 |
| Admin panel | Not publicly accessible; no authorised access |
| Real payment processing | Demo store; no card data will ever be entered |
| Performance, load, stress | Public shared demo; not appropriate, and `robots.txt` disallows crawling |
| Security penetration testing | No written authorisation; only functional auth behaviour is checked |
| Accessibility audit | Requires specialist tooling and criteria outside this project's scope |
| Cross-browser matrix | One primary browser (Brave); Chrome available only as a fallback |
| Mobile/native applications | Web-only application |
| Email delivery | Password recovery and contact-form emails are not verified in an inbox |
| Localisation / multi-currency | Storefront is USD-only in this environment |
| Visual pixel-perfect UI comparison | Functional UI verification only |

### 3.3 Test item identification

The "test items" are the functional modules listed in Section 3.1, reached through the
public storefront URLs. No source code, database, or server configuration is available.

---

## 4. Test strategy

### 4.1 Overall approach

- **Risk-based, requirement-derived.** Business-critical paths (authentication, cart,
  checkout, totals) get the deepest coverage and highest priority.
- **Manual first, then automation.** Manual execution validates behaviour and produces
  evidence before any test is automated.
- **Module by module.** Automation is implemented and executed one module at a time,
  then as a full regression suite.
- **Evidence over assertion.** A test is not marked Pass without an observed result;
  defects are only reported after reproduction.

### 4.2 Manual testing strategy

| Activity | Method |
|---|---|
| Test design | Positive, negative, boundary value analysis, equivalence partitioning, state/session checks |
| Execution | Scripted cases executed in a real browser by the author, guided in batches |
| Evidence | Screenshot per executed case where behaviour is visual; terminal/report output for automation |
| Recording | Actual result, status (Pass/Fail/Blocked/Not Run), and defect reference |

### 4.3 Automation strategy

| Decision | Choice and rationale |
|---|---|
| Framework | Selenium WebDriver + Pytest |
| Pattern | Page Object Model — locators and interactions separated from assertions |
| Scope | Stable, repeatable, high-value regression paths; not every manual case is automated |
| Waits | Explicit waits only; no fixed sleeps for synchronisation |
| Test data | Centralised in `config/test_data.py`; credentials in `.env` |
| Isolation | Function-scoped browser sessions by default; independent tests where practical |
| Reporting | pytest-html with environment metadata and failure screenshots |
| Browser | Brave (Chromium 157) via Selenium Manager driver provisioning |

**Automation exclusions:** destructive account changes (password change, address deletion)
are automated only where they can be safely repeated; visual checks and CAPTCHA-style
manual judgement remain manual.

### 4.4 Regression strategy

A tagged smoke subset (`-m smoke`) covers login, catalog, add-to-cart, and cart totals.
The full suite runs before final reporting. Results are compared with the previous
execution; failures are investigated, never deleted to obtain a green report.

---

## 5. Testing types

| Type | Applied to |
|---|---|
| Smoke | Site availability, login, catalog load, add to cart |
| Functional | All in-scope modules |
| Positive testing | Valid data and expected happy paths |
| Negative testing | Invalid credentials, malformed input, missing mandatory fields |
| Boundary value analysis | Password length, search minimum length, quantity 0/negative/large, price filter edges |
| Equivalence partitioning | Valid/invalid input classes per field |
| Input validation | Registration, login, checkout, address, contact, newsletter, quantities |
| Navigation / UI | Menus, breadcrumbs, paging, view mode, footer links |
| Session / authentication | Login state, protected routes, logout, back button, guest cart merge |
| Business rules | Discounts, configurable product pricing, shipping and totals, duplicate email |
| Error handling | Validation messages, no-result states, invalid codes, empty cart |
| Regression | Full suite re-execution after refactoring and before final reporting |

---

## 6. Test environment

| Component | Detail |
|---|---|
| Operating system | CachyOS Linux (Arch-based) |
| Shell | fish |
| Python | 3.14.10 (`/usr/bin/python3`) |
| Virtual environment | `.venv` in project root |
| Primary browser | Brave 1.99.57 — `/opt/brave-bin/brave` (Chromium 157) |
| Fallback browser | Google Chrome 157 (Flatpak) |
| Driver management | Selenium Manager (no manual driver install required) |
| Application environment | Public demo, shared data, USD |
| Network | Public internet; no VPN or proxy required |
| Display | Local desktop session (headed execution); headless optional for CI-style runs |
| Repository | `github.com/milandahal1000/DemoWebShop` |

**Note:** performance of the public demo is outside our control. Slow responses are
treated as environment conditions, not defects, unless reproducible and clearly
application-driven.

---

## 7. Tools

| Tool | Purpose |
|---|---|
| Selenium WebDriver | Browser automation |
| Pytest | Test execution, fixtures, markers, parametrisation |
| pytest-html | Self-contained HTML report |
| Python `venv` | Isolated dependencies |
| `python-dotenv` | Load local credentials from `.env` (pending Phase 3 confirmation) |
| Git / GitHub | Version control and portfolio publication |
| Browser DevTools | Locator inspection and DOM verification |
| Screenshot tooling | Manual evidence capture |

No API, performance, or security tooling is used, because those areas are out of scope.

---

## 8. Roles and responsibilities

| Role | Responsibility |
|---|---|
| QA Engineer / Author (Milan Dahal) | Planning, test design, manual execution, automation, reporting, evidence |
| Mentor/Reviewer (this AI assistant) | Guidance, review, documentation support, code and result validation |
| Application owner (Tricentis) | Provides the demo environment; no support agreement assumed |

Ethical constraint: testing is limited to the public storefront at human pace, with no
destructive operations beyond normal shopper actions on demo data.

---

## 9. Entry criteria

Phase 2 execution may begin only when:

1. This test plan and the scenario inventory are reviewed and approved.
2. The application is reachable and the login/register pages load.
3. A dedicated test account has been registered and its credentials stored in `.env`.
4. Priority definitions and test data conventions are agreed.
5. Screenshot location and naming convention are established.

Phase 4 automation may begin only when:

1. Manual test cases for the target module exist and are approved.
2. The Python environment, browser launch, and teardown are verified (Phase 3 exit).
3. Stable locators have been identified for the target module.
4. Test data and fixtures approach is agreed.

---

## 10. Exit criteria

Testing is complete when:

1. All Critical and High priority scenarios have been executed or explicitly marked
   Blocked with a documented reason.
2. At least 90% of planned manual cases have a recorded status (Pass/Fail/Blocked);
   the remainder are explicitly "Not Run" with justification.
3. Every Fail has a corresponding confirmed bug report or documented environment issue.
4. Confirmed defects are retested and their status updated.
5. The automated regression suite runs to completion with results matching the report.
6. `docs/test-execution-summary.md` reflects the actual final run (counts, duration,
   environment, limitations).
7. The traceability matrix maps every in-scope requirement to evidence.
8. README, screenshots, and report are reviewed and links verified.

Target thresholds (not guarantees): 0 open Critical/High defects unexplained; automated
pass rate reported honestly, including any known failures.

---

## 11. Suspension and resumption criteria

**Suspend testing** if: the site is unavailable for more than 15 minutes; the demo
database is reset mid-run destroying the test account; the browser/driver cannot launch;
or a blocking defect prevents a whole module from being exercised.

**Resume** when the environment is stable, the account is recreated, or the blocking
condition is resolved. Suspended time and affected cases must be recorded, not hidden.

---

## 12. Risks and mitigation

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R1 | Shared demo data changes between runs (reviews, orders, stock) | High | Medium | Assert on stable properties, not global counts; re-check data before final run |
| R2 | Test account is purged by a demo reset | Medium | High | Store credentials in `.env`; verify login in a session fixture with a clear failure message |
| R3 | Public site latency or outage | Medium | Medium | Explicit waits with sensible timeouts; record as environment issue, retry once |
| R4 | Browser/driver version drift (Brave/Chromium updates) | Medium | Medium | Selenium Manager provisioning; document fallback to Chrome |
| R5 | Password policy assumption is wrong | Medium | Low | Verify actual minimum length in Phase 2 before writing boundary assertions |
| R6 | `robots.txt` discourages crawling | Low | Medium | Single headed session, human pace, no crawling or load generation |
| R7 | Checkout creates demo orders | High | Low | Use COD/check payment only; no real payment data; orders are demo artefacts |
| R8 | Flaky automation due to AJAX/cart flyout timing | Medium | High | Explicit waits on observable state; no fixed sleeps; stabilise in Phase 4–6 |
| R9 | Scope creep beyond one-browser functional testing | Medium | Medium | Scope frozen in this plan; changes require explicit approval |
| R10 | Secrets accidentally committed | Low | High | `.env` git-ignored, `.env.example` placeholders only, review `git status` before push |

---

## 13. Defect severity and priority definitions

| Severity | Definition |
|---|---|
| Critical | Blocks a core journey (cannot log in, cannot add to cart, cannot complete checkout) or causes data loss |
| High | Major function broken with no reasonable workaround; incorrect totals or order data |
| Medium | Function works but with incorrect/incomplete behaviour or validation gaps |
| Low | Cosmetic, wording, or minor usability issue |

| Priority | Definition |
|---|---|
| Critical | Must be fixed before any release |
| High | Should be fixed in the current cycle |
| Medium | Should be fixed soon; workaround exists |
| Low | Fix when convenient |

Severity reflects impact; priority reflects urgency. They are recorded separately.

---

## 14. Deliverables

| Deliverable | Owner | Phase |
|---|---|---|
| Test plan, scenarios, traceability | QA Engineer | 1 |
| Manual test cases and bug reports | QA Engineer | 2 |
| Automation framework and suite | QA Engineer | 3–6 |
| HTML report and execution summary | QA Engineer | 7, 9 |
| README and evidence | QA Engineer | 10 |

---

## 15. Schedule (phase gates)

| Phase | Output | Gate |
|---|---|---|
| 1 | Analysis, plan, scenarios, RTM | Review and approval |
| 2 | Manual cases, execution, defects | Review of results and evidence |
| 3 | Environment and smoke launch | Verified browser launch/teardown |
| 4 | Automated module tests | Module green + reviewed |
| 5 | POM refactor | Behaviour preserved |
| 6 | Data, fixtures, screenshots | Full suite stable |
| 7 | HTML report | Report verified in browser |
| 8 | Code/quality review | Checklist complete |
| 9 | Final run and summary | Results documented |
| 10 | README and evidence | Links and claims verified |
| 11 | Git cleanup and push | Approval before push |
| 12 | Final evaluation | Portfolio readiness assessed |

---

## 16. Approvals

| Role | Name | Status |
|---|---|---|
| QA Engineer | Milan Dahal | Pending review |
| Reviewer | Project mentor | Pending review |

Changes to scope, tools, or exit criteria require an explicit decision recorded in this
document with a version increment.
