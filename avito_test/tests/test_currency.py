from ..app.services.currency import get_currency


def test_get_currency():
    assert type(get_currency("R01235")) == float
