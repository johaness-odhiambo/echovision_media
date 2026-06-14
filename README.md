# Echovision Media

A Django-based booking platform for media services with a gallery and Mpesa Daraja payments.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run migrations:

```
python echovision/manage.py migrate
```

4. Create a superuser:

```
python echovision/manage.py createsuperuser
```

5. Run the server:

```
python echovision/manage.py runserver
```

## Environment variables

Set these for production:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG` (True/False)
- `DJANGO_ALLOWED_HOSTS` (comma-separated)
- `DJANGO_CSRF_TRUSTED_ORIGINS` (comma-separated)
- `DJANGO_SESSION_COOKIE_SECURE` (True/False)
- `DJANGO_CSRF_COOKIE_SECURE` (True/False)
- `DJANGO_HSTS_SECONDS`
- `DJANGO_HSTS_INCLUDE_SUBDOMAINS` (True/False)
- `DJANGO_HSTS_PRELOAD` (True/False)

Email:

- `DJANGO_EMAIL_BACKEND`
- `DJANGO_EMAIL_HOST`
- `DJANGO_EMAIL_PORT`
- `DJANGO_EMAIL_USE_TLS`
- `DJANGO_EMAIL_HOST_USER`
- `DJANGO_EMAIL_HOST_PASSWORD`
- `DJANGO_DEFAULT_FROM_EMAIL`
- `BOOKING_NOTIFICATION_EMAIL`

Mpesa Daraja:

- `DARAJA_CONSUMER_KEY`
- `DARAJA_CONSUMER_SECRET`
- `DARAJA_SHORTCODE`
- `DARAJA_PASSKEY`
- `DARAJA_CALLBACK_URL`
- `DARAJA_STK_PUSH_URL`
- `DARAJA_TOKEN_URL`

## Notes

- Add services from the Django admin before bookings can be created.
- Gallery items can be added in the admin and linked to services.
- Mpesa callback URL must be publicly accessible when testing STK push.
