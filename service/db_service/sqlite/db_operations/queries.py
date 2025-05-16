from interface.db_service import AQueriesAdapter


class QueriesAdapter(AQueriesAdapter):

    def __init__(self):
        self._connect = None
        self._cursor = None


    def add_query(self, *args) -> None:
        pass


    def get_query(self) -> tuple[str]:
        pass


    def del_query(self) -> tuple[str]:
        pass