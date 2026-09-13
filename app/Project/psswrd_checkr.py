MIN_PASSWORD_LENGTH = 8


def is_password_reliable(password: str) -> bool:
    if len(password) < MIN_PASSWORD_LENGTH:
        return False

    if " " in password:
        return False

    has_digit = False
    has_letter = False
    has_symbol = False

    for character in password:
        if character.isdigit():
            has_digit = True
        elif character.isalpha():
            has_letter = True
        else:
            has_symbol = True

    return has_digit and has_letter and has_symbol