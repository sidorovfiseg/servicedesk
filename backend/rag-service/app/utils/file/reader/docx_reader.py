from utils.file.reader.base_reader import FileReader
from docx import Document

class DocxFileReader(FileReader):
    def read(self):
        document = Document(self.file_path)
        return '\n'.join([p.text for p in document.paragraphs])