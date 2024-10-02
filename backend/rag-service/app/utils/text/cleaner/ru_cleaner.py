from utils.text.cleaner import BaseTextCleaner
from cleantext import clean


class RuTextCleaner(BaseTextCleaner):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.args['lang'] = "ru"
        self.args['replace_with_url'] = "<ссылка>"
        self.args['replace_with_email'] = "<почта>"
        self.args['replace_with_phone_number'] = "<телефон>"
        self.args['replace_with_currency_symbol'] = "<валюта>"

    def clean_text(self, text: str) -> str:
        return clean(text, **self.args)
