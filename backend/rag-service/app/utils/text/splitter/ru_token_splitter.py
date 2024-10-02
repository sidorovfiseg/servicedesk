from utils.text.tokenizer.ru_tokenizer import RuTokenizer
from utils.text.splitter import TextSplitter



class RuTokenSplitter(TextSplitter):
    def __init__(self, chunk_overlap: int, tokens_per_chunk: int):
        super().__init__(chunk_overlap=chunk_overlap, tokens_per_chunk=tokens_per_chunk)
        self.tokenizer = RuTokenizer()

    def split_text(self, text: str) -> list[str]:
        tokens = self.tokenizer.encode(text)
        chunks = []
        for i in range(0, len(tokens), self.tokens_per_chunk - self.chunk_overlap):
            chunk = tokens[i:i + self.tokens_per_chunk]
            chunks.append(self.tokenizer.decode(chunk))
        return chunks
