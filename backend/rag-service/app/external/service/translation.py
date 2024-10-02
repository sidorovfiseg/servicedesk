# services/translation_service.py

from external.service import BaseService
from external.api import BaseAPI
from external.service.translation.ru_en import RUENTranslation
from external.service.translation.en_ru import ENRUTranslation

class TranslationService(BaseService):
    def __init__(self, api: BaseAPI):
        self.api = api
        self.translations = {
            "ru_en": RUENTranslation(),
            "en_ru": ENRUTranslation(),
        }

    async def execute(self, message: str, lang: str) -> str:
        translation_strategy = self.translations.get(lang)
        if not translation_strategy:
            raise ValueError(f"Unsupported language: {lang}")
        
        prompt = translation_strategy.get_prompt(message)
        return await self.api.send_message(prompt)
