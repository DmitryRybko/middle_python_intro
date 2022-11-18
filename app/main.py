"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Return greeting line.

    Args:
        name: User name.

    Returns:
        Greeting text with name capitalized.
    """
    name_capitalized = name.title()

    return f'Привет, {name_capitalized}'
