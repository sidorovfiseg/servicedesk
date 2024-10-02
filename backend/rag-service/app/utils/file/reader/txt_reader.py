from utils.file.reader.base_reader import FileReader


class TxtFileReader(FileReader):
    def read(self):
        with open(self.file_path, encoding='utf-8', mode='r') as f:
            return f.read()