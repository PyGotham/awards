from __future__ import annotations

from decouple import config  # type: ignore[import]

from awards.settings.base import *  # NOQA

SECRET_KEY = config("SECRET_KEY")

DEBUG = False
