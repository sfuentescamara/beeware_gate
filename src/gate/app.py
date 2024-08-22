"""
The gate application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class gate(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        button = toga.Button(
            "Abrir / Cerrar",
            on_press=self.toggle,
            style=Pack(padding=5),
        )

        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def toggle(self, widget):
        print(f"Funciona")


def main():
    return gate()
