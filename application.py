from server.server import run_server
from database.database_api import Database


def start_application(db_obj):
    run_server(db_obj)


if __name__ == "__main__":
    db_object = Database()
    db_object.create_table()
    start_application(db_object)
