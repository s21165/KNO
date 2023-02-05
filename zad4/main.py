import logging

from app import MainApp

logging.basicConfig(
    filename="app.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)


if __name__ == "__main__":

    main_app = MainApp()
    main_app.menu()
