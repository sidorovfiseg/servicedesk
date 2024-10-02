from abc import ABC, abstractmethod

class FileReader(ABC):
    def __init__(self, file_path: str) :
        self.file_path = file_path
        
    @abstractmethod
    def read(self):
        pass