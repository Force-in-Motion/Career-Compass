from abc import ABC, abstractmethod



class ADBInit(ABC):

    @abstractmethod
    def __init__(self):
        self._connect = None
        self._cursor = None



    @abstractmethod
    def _create_table(self, request):
        pass


    @abstractmethod
    def _init_db(self):
        pass