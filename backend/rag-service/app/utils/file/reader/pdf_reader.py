from utils.file.reader.base_reader import FileReader
from pypdf import PdfReader

class PdfFileReader(FileReader):
    def read(self):
        reader = PdfReader(self.file_path)
        return '\n'.join(p.extract_text() for p in reader.pages)