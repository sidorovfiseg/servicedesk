from cleantext import clean
from abc import ABC, abstractmethod


class BaseTextCleaner(ABC):
    def __init__(self, **kwargs):
        self.args = {
            'fix_unicode': True,
            'to_ascii': False,
            'lower': True,
            'normalize_whitespace': True,
            'no_line_breaks': True,
            'strip_lines': True,
            'keep_two_line_breaks': False,
            'no_urls': True,
            'no_emails': True,
            'no_phone_numbers': True,
            'no_numbers': False,
            'no_digits': False,
            'no_currency_symbols': True,
            'no_punct': False,
            'no_emoji': True,
            'replace_with_url': "<URL>",
            'replace_with_email': "<EMAIL>",
            'replace_with_phone_number': "<PHONE>",
            'replace_with_number': "",
            'replace_with_digit': "",
            'replace_with_currency_symbol': "<CUR>",
            'replace_with_punct': "",
        }
        self.args.update(kwargs)

    @abstractmethod
    def clean_text(self, text: str) -> str:
        pass

    def validate_args(self, kwargs):
        for key in kwargs:
            if key not in self.args:
                raise ValueError(f"Недопустимый аргумент: {key}")
        self.args.update(kwargs)
