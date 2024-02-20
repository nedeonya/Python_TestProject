from unittest import mock
from container import DatabaseConnectionContainer
from database_service import DbConnectionStub, DatabaseServer
from dependency_injector.wiring import inject, Provide


@inject
def db_inject(db_server: DatabaseServer = Provide[DatabaseConnectionContainer.create_db_server]):
    return inject


#Testing
if __name__ == "__main__":
    db_container = DatabaseConnectionContainer()
    db_container.config.from_ini("./config.ini")
    db_container.wire(modules=[__name__])

    db_inject()

    with db_container.create_db_connection.override(mock.Mock()):
        db_inject()

    with db_container.create_db_connection.override(DbConnectionStub()):
        db_inject()
