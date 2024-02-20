class DbConnectionStub:
    def __init__(self):
        print("__init__ConnectionStub")


class DatabaseConnection:
    def __init__(self, database: str, user: str, password: str):
        self.database = database
        self.user = user
        self.password = password
        print(f"__init__Connection with database: {self.database}, user: {self.user}, password: {self.password}")


class DatabaseServer:
    def __init__(self, db_connection: DatabaseConnection):
        self.connection = db_connection
        print(f"__init__Service with {db_connection}")

