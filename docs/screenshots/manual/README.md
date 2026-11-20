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
