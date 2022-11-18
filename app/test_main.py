import pytest
from main import greeting

test_params = [('Никита', 'Привет, Никита'), ('Ольга', 'Привет, Ольга')]


@pytest.mark.parametrize('name,expected', test_params)
def test_greeting(name: str, expected: str):
    """Текст приветствия зависит от имени."""
    assert greeting(name) == expected


def test_capitalize():
    """Все слова в имени начинаются с большой буквы."""
    name = 'яндекс практикум'
    assert greeting(name) == 'Привет, Яндекс Практикум'
