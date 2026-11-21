# Manual Test Evidence

This directory holds genuine screenshots captured during manual execution. Screenshots
are referenced from `docs/test-cases.md` and from the root `README.md`.

## Naming convention

```
TC-001_registration-success.png
TC-011_login-error.png
TC-015_protected-redirect.png
```

- Prefix with the test case ID.
- Use a short lowercase description separated by hyphens.
- Add a suffix (`-2`, `-3`) when a case needs more than one image.
- Crop to the relevant page area; keep validation messages and page context readable.

## Rules

1. Only real screenshots of the application under test — never stock images or mock-ups.
2. Do not include credentials, email inbox contents, or personal information.
3. When a screenshot shows an account email, it is the dedicated demo address only.
4. If a screenshot is retaken after a fix, replace the file so the record stays current,
   and note the retest date in `docs/test-cases.md`.

## Index

| Test case | File | Captured |
|---|---|---|
| TC-001 | `TC-001_registration-form.png` | 18 Nov 2026 |
| TC-001 | `TC-001_registration-success.png` | 18 Nov 2026 |
| TC-002 | `TC-002_empty-form-errors.png` | 18 Nov 2026 |
| TC-003 | `TC-003_invalid-email-1.png` | 18 Nov 2026 |
| TC-003 | `TC-003_invalid-email-2.png` | 18 Nov 2026 |
| TC-004 | `TC-004_duplicate-email.png` | 18 Nov 2026 |
| TC-005 | `TC-005_password-mismatch.png` | 18 Nov 2026 |
| TC-006 | `TC-006_password-5chars.png` | 18 Nov 2026 |
| TC-006 | `TC-006_password-6chars.png` | 18 Nov 2026 |
| TC-010 | `TC-010_login-success.png` | 18 Nov 2026 |
| TC-011 | `TC-011_login-wrong-password.png` | 18 Nov 2026 |
| TC-012 | `TC-012_login-unregistered-email.png` | 18 Nov 2026 |
| TC-012 | `TC-012_login-unregistered-email-2.png` | 18 Nov 2026 |
| TC-013 | `TC-013_empty-credentials.png` | 18 Nov 2026 |
| TC-013 | `TC-013_empty-credentials-2.png` | 18 Nov 2026 |
| TC-014 | `TC-014_logout-header.png` | 18 Nov 2026 |
| TC-014 | `TC-014_protected-redirect-1.png` | 18 Nov 2026 |
| TC-014 | `TC-014_protected-redirect-2.png` | 18 Nov 2026 |
| TC-015 | `TC-015_customer-info-redirect.png` | 20 Nov 2026 |
| TC-015 | `TC-015_customer-orders-redirect.png` | 20 Nov 2026 |
| TC-015 | `TC-015_invalid-route-404.png` | 20 Nov 2026 (test-design evidence) |
| TC-017 | `TC-017_registered-email.png` | 20 Nov 2026 |
| TC-017 | `TC-017_unregistered-email.png` | 20 Nov 2026 |
| TC-016 | `TC-016_return-url.png` | 20 Nov 2026 |
| TC-020 | `TC-020_home-page.png` | 21 Nov 2026 |
| TC-022 | `TC-022_computers-subcategory.png` | 21 Nov 2026 |
| TC-023 | `TC-023_breadcrumb.png` | 21 Nov 2026 |
| TC-020 | `TC-020_home-featured.png` | 21 Nov 2026 |
| TC-030 | `TC-030_laptop-detail.png` | 21 Nov 2026 |
| TC-032 | `TC-032_configurable-defaults.png` | 21 Nov 2026 |
| TC-033 | `TC-033_price-after-changes.png` | 21 Nov 2026 |
| TC-034 | `TC-034_cart-configurable.png` | 21 Nov 2026 |
| TC-035 | `TC-035_giftcard-validation.png` | 21 Nov 2026 |
| TC-036 | `TC-036_music2-add.png` | 21 Nov 2026 |
| TC-040 | `TC-040_search-computer.png` | 21 Nov 2026 |
| TC-041 | `TC-041_search-no-results.png` | 21 Nov 2026 |
| TC-042 | `TC-042_search-short-term.png` | 21 Nov 2026 |
| TC-043 | `TC-043_search-case.png` | 21 Nov 2026 |
| TC-044 | `TC-044_search-special-chars.png` | 21 Nov 2026 |
| TC-045 | `TC-045_search-from-category.png` | 21 Nov 2026 |
| TC-050 | `TC-050_sort-name-az.png` | 21 Nov 2026 |
| TC-051 | `TC-051_sort-price-asc.png` | 21 Nov 2026 |
| TC-052 | `TC-052_sort-price-desc.png` | 21 Nov 2026 |
| TC-053 | `TC-053_filter-under25.png` | 21 Nov 2026 |
| TC-053 | `TC-053_filter-25-50.png` | 21 Nov 2026 |
| TC-053 | `TC-053_filter-over50.png` | 21 Nov 2026 |
| TC-054 | `TC-054_pagesize-4.png` | 21 Nov 2026 |
| TC-055 | `TC-055_combined.png` | 21 Nov 2026 (pre-filter state, retained for sort/page size) |
| TC-055 | `TC-055_combined-applied.png` | 21 Nov 2026 (filter, sort and page size together) |
| TC-060 | `TC-060_cart-empty.png` | 21 Nov 2026 |
| TC-061 | `TC-061_cart-one-item.png` | 21 Nov 2026 |
| TC-062 | `TC-062_cart-two-items.png` | 21 Nov 2026 |
| TC-063 | `TC-063_cart-duplicate-add.png` | 21 Nov 2026 |
| TC-064 | `TC-064_cart-qty-updated.png` | 21 Nov 2026 |
| TC-065 | `TC-065_cart-item-removed.png` | 21 Nov 2026 |
| TC-066 | `TC-066_cart-invalid-qty.png` | 21 Nov 2026 (restored state; message capture pending) |
| TC-067 | `TC-067_cart-invalid-codes.png` | 21 Nov 2026 (post-login state; error capture pending) |
