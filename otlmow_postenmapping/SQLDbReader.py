import os
import sqlite3
from pathlib import Path


class SQLDbReader:
    """SQLDbReader performs read query's. It first checks if the provided path has a file. Provides an easy way to override querying for testing purposes. """

    def __init__(self, path: Path = None):
        if path is None or path == '':
            self.file_exists = False
        else:
            self.path = path.resolve()
            self.file_exists = os.path.isfile(self.path)
            if not self.file_exists:
                raise FileNotFoundError(f"{str(self.path)} is not a valid path. File does not exist.")

    def perform_read_query(self, query: str, params: dict):
        self.file_exists = os.path.isfile(self.path)
        if not self.file_exists:
            raise FileNotFoundError(f"{self.path} is not a valid path. File does not exist.")

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        data = list(cur.execute(query, params))
        con.close()
        return data
