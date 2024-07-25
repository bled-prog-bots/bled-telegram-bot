

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def telegram_markdown_escaping(s1: str) -> str:
    """ экранирование символов для markdown v1 """
    make_escape_symbols = [
        '*'
    ]

    for symbol in make_escape_symbols:
        s1 = s1.replace(symbol, '\N{REVERSE SOLIDUS}' + symbol)

    return s1
