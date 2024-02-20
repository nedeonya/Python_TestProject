from injector import Module, provider, Injector, inject, singleton
import sqlite3


class RequestHandler:
    @inject
    def __init__(self, db: sqlite3.Connection):
        self._db = db
        print(f"init RequestHandler: {self}")


class Configuration:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        print(f"init Configuration: {self}")


def configure_for_testing(binder):
    print("configure_for_testing...")
    configuration = Configuration('ololo_configuration')
    binder.bind(Configuration, to=configuration, scope=singleton)


class DatabaseModule(Module):
    @inject
    @singleton
    @provider
    def provide_sqlite_connection(self, configuration: Configuration) -> sqlite3.Connection:
        conn = sqlite3.connect(configuration.connection_string)
        print(f"DatabaseModule with connection: {configuration.connection_string}")
        return conn


#Testing
injector = Injector([configure_for_testing, DatabaseModule()])

print(f"get from injector...")
print(f"injector.get: {injector.get(Configuration)}")
print(f"injector.get: {injector.get(RequestHandler)}")


