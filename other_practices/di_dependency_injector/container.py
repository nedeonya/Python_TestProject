from dependency_injector import containers, providers
from database_service import DatabaseConnection, DatabaseServer


class DatabaseConnectionContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    create_db_connection = providers.Singleton(
        DatabaseConnection,
        database=config.connection.db,
        user=config.connection.user,
        password=config.connection.password,
    )

    create_db_server = providers.Factory(
        DatabaseServer,
        db_connection=create_db_connection,
    )
