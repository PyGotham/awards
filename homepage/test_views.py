from __future__ import annotations

from django.test import Client


def test_login_link_is_shown_to_guests(client: Client) -> None:
    response = client.get("/")
    assert b"log in" in response.content.lower()
