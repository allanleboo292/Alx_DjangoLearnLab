# Security Measures in LibraryProject

## 1. Secure Settings
- `DEBUG`: Set to `False` in production to disable detailed error pages.
- Browser security headers:
  - `SECURE_BROWSER_XSS_FILTER`: Enabled to prevent XSS attacks.
  - `X_FRAME_OPTIONS`: Set to `DENY` to prevent clickjacking.
  - `SECURE_CONTENT_TYPE_NOSNIFF`: Prevent MIME type sniffing.
- Cookies:
  - `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE`: Enforce HTTPS-only cookies.

## 2. CSRF Protection
- All forms include the `{% csrf_token %}` template tag.

## 3. Input Validation
- User inputs are validated using Django forms.

## 4. Content Security Policy (CSP)
- Configured `CSP_DEFAULT_SRC`, `CSP_SCRIPT_SRC`, and `CSP_STYLE_SRC` to restrict loading of content to trusted domains.

## 5. SQL Injection Prevention
- All database queries use Django’s ORM to prevent SQL injection.

## 6. Testing
- Manually tested for CSRF, XSS, and SQL injection vulnerabilities using test forms and inputs.
