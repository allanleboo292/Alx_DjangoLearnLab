# Django Permissions and Groups Setup

## Permissions
- **can_view**: Allows viewing books.
- **can_create**: Allows creating books.
- **can_edit**: Allows editing books.
- **can_delete**: Allows deleting books.

## Groups
- **Admins**: Full permissions (view, create, edit, delete).
- **Editors**: View, create, and edit permissions.
- **Viewers**: View-only permissions.

## Views Protection
- Each view is protected using `@permission_required` decorator.
- Example:
  ```python
  @permission_required('app_name.can_view', raise_exception=True)
# HTTPS and Security Configuration

This project has been configured to enforce HTTPS connections to ensure secure communication between the server and clients.

## Changes Made to settings.py
- `SECURE_SSL_REDIRECT`: Forces all HTTP traffic to be redirected to HTTPS.
- `SECURE_HSTS_SECONDS`: Ensures browsers only access the site via HTTPS for one year.
- `SESSION_COOKIE_SECURE` & `CSRF_COOKIE_SECURE`: Ensures that session and CSRF cookies are only sent over HTTPS.
- Security Headers: Configured headers to prevent clickjacking, MIME sniffing, and cross-site scripting (XSS).

## Web Server Configuration (Nginx/Apache)
- Configured SSL in Nginx (or Apache) to ensure all traffic is served over HTTPS.
- Set up 301 redirects from HTTP to HTTPS.

## Security Measures
These settings contribute to protecting the application by:
- Preventing data from being transmitted over insecure connections.
- Mitigating attacks such as XSS, clickjacking, and man-in-the-middle attacks.
