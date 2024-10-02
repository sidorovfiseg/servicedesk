# services/ru_en_translation.py

from external.service.translation import BaseTranslation
from external.prompts.translation import ru_en_translation_prompt

class RUENTranslation(BaseTranslation):
    def get_prompt(self, message: str) -> str:
        return ru_en_translation_prompt.format(text=message)
