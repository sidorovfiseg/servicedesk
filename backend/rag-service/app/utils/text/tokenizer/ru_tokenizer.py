from razdel import tokenize
from typing import List
from utils.text.tokenizer import BaseTokenizer

class RuTokenizer(BaseTokenizer):
    
    @staticmethod
    def token_function(text: str) -> List[str]:
        tokens = list(tokenize(text))
        return [_.text for _ in tokens]

    def encode(self, text: str) -> List[str]:
        return self.token_function(text)  
    
    def decode(self, token_ids: List[str]) -> str:
        return ' '.join(token_ids)

    def length(self, text: str) -> int:
        return len(self.token_function(text))  