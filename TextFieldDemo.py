"""
Program: TextFieldDemo.py
GUI template file
8/14/2025

NOTE: the Python module breezypythongui.py must be in the same directory as this file for the app to run properly!

Template code for ANY GUI-based application in chapter 9.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font

class TextFieldDemo(EasyFrame):

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Text Field Demo", width=240, height=160, background="orange2", resizable=False)

        # Title label with custom font
        titleFont = Font(family="Comic Sans MS", size=14)
        self.addLabel(text="Text converter", row=0, column=0, columnspan=2, sticky="SNWE",background="orange2", font=titleFont)

        # Input label + text field
        self.addLabel(text="Input", row=1, column=0, background="orange2")
        self.inputField = self.addTextField(text="", row=1, column=1)
        self.inputField.focus_set()
        self.inputField.bind("<Return>", lambda event: self.convert())

        # Output label + text field
        self.addLabel(text="Output", row=2, column=0, background="orange2")
        self.outputField = self.addTextField(text="", row=2, column=1, state="readonly")

        # Convert button
        self.button = self.addButton(text="Convert", row=3, column=0, columnspan=2, command=self.convert)
        self.button["background"] = "plum1"

    def convert(self):
        """Grab input, convert to uppercase, show in output."""
        text = self.inputField.getText()
        result = text.upper()
        self.outputField.setText(result)
        self.inputField.setText("")


def main():
    TextFieldDemo().mainloop()

if __name__ == '__main__':
    main()

