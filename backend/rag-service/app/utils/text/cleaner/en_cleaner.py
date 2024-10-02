from utils.text.cleaner import BaseTextCleaner
from cleantext import clean


class EnTextCleaner(BaseTextCleaner):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.args['lang'] = "en"
        self.args['replace_with_url'] = "<URL>"
        self.args['replace_with_email'] = "<EMAIL>"
        self.args['replace_with_phone_number'] = "<PHONE>"
        self.args['replace_with_currency_symbol'] = "<CUR>"

    def clean_text(self, text: str) -> str:
        return clean(text, **self.args)
