import pytest

from psswrd_checkr import is_password_reliable


class TestPasswordChecker:

    @pytest.mark.parametrize(
        "password, expected",
        [
            ("Pass123!", True),
            ("MyP@ssw0rd#2024", True),
            ("Пароль1!", True),
            ("P1!", False),
            ("Password!", False),
            ("12345678!", False),
            ("Password1", False),
            ("Pass 123!", False),
            ("", False),
            ("        ", False),
            ("Ab1!def", False),
            ("!!!!1111", False),
        ],
    )
    def test_is_password_reliable(self, password: str, expected: bool):
        actual = is_password_reliable(password)
        assert expected is actual

    @pytest.mark.skip(reason="Test is not ready yet")
    def test_is_password_reliable_character_variety(self):
        pass