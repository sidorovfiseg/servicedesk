from utils.file.reader.base_reader import FileReader
import pandas as pd

class XlsxFileReader(FileReader):
    def read(self):
        df = pd.read_excel(self.file_path, sheet_name='Sheet1')
        return df.to_dict('records')