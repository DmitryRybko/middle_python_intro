"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Return greeting line.

    Args:
        name: User name.

    Returns:
        Greeting text with name capitalized.
    """
    name_capitalized = name.title()

    return 'Привет, {0}'.format(name_capitalized)
