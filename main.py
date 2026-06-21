from tkinter import Tk

from config import (
    APP_NAME,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    BACKGROUND_COLOR
)

from app import MotoCareApp


def main():

    root = Tk()

    root.title(APP_NAME)

    root.geometry(
        f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
    )

    root.configure(
        bg=BACKGROUND_COLOR
    )

    root.minsize(
        WINDOW_WIDTH,
        WINDOW_HEIGHT
    )

    app = MotoCareApp(root)

    app.run()


if __name__ == "__main__":

    main()