from utils.file.reader.txt_reader import TxtFileReader
from utils.file.reader.pdf_reader import PdfFileReader
from utils.file.reader.docx_reader import DocxFileReader
from utils.file.reader.xlsx_reader import XlsxFileReader

class FileReaderFactory:
    @staticmethod
    def get_file_reader(file_path: str):
        if file_path.endswith('txt'):
            return TxtFileReader(file_path)
        elif file_path.endswith('pdf'):
            return PdfFileReader(file_path)
        elif file_path.endswith('docx'):
            return DocxFileReader(file_path)
        elif file_path.endswith('xlsx'):
            return XlsxFileReader(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_path}")