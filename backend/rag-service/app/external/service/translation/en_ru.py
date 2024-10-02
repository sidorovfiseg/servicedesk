# services/en_ru_translation.py

from external.service.translation import BaseTranslation
from external.prompts.translation import en_ru_translation_prompt

class ENRUTranslation(BaseTranslation):
    def get_prompt(self, message: str) -> str:
        return en_ru_translation_prompt.format(text=message)
