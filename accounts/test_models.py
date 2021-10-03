from __future__ import annotations

from django.db import IntegrityError
import pytest

from accounts.models import User


@pytest.mark.django_db
def test_cannot_create_without_email() -> None:
    with pytest.raises(IntegrityError):
        User.objects.create(email=None)


@pytest.mark.django_db
def test_email_is_case_insensitive() -> None:
    user1, _ = User.objects.get_or_create(email="user@example.org")
    user2, _ = User.objects.get_or_create(email="USER@EXAMPLE.ORG")
    assert user1 == user2


@pytest.mark.parametrize("number_of_characters", range(10))
def test_email_is_redacted_when_converting_to_string(number_of_characters: int) -> None:
    user = User(email=f"a{'b' * number_of_characters}@example.org")
    assert str(user) == f"a{'*' * number_of_characters}@example.org"
