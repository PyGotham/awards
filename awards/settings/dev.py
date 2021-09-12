from __future__ import annotations

from awards.settings.base import *  # NOQA

SECRET_KEY = "django-insecure-@a*u0tmk#a@+3h4#sxhv2za+vm+hlei(bu685cw&t05gf6620n"

DEBUG = True

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

INTERNAL_IPS = ["127.0.0.1"]
