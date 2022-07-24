__author__ = "Benjamin Mickler"
__copyright__ = "Copyright 2022, Benjamin Mickler"
__credits__ = ["Benjamin Mickler"]
__license__ = "GPLv3 or later"
__version__ = "240720222"
__maintainer__ = "Benjamin Mickler"
__email__ = "ben@benmickler.com"

"""
Scissors, Paper, Rock is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

Scissors, Paper, Rock is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
Scissors, Paper, Rock. If not, see <https://www.gnu.org/licenses/>.
"""

import random
import sys
import tkinter as tk
import tkinter.messagebox
from help_message import HELP_MESSAGE

class cli_game:
    def pick_choice(self) -> str:
        return input("> ").lower(), random.randint(1, 3)
    def start(self):
        while True:
            user_choice, random_choice = self.pick_choice()
            if user_choice not in ["rock", "paper", "scissors"]:
                print("\033[91mInvalid choice. You must pick either 'scissors', 'paper' or 'rock'\033[0m")
                break
            print(f"The computer chose {str(random_choice).replace('1', 'rock').replace('2', 'paper').replace('3', 'scissors')}")
            if user_choice == "rock" and random_choice ==  1 or user_choice == "paper" and random_choice ==  2 or user_choice == "scissors" and random_choice ==  3:
                continue
            elif user_choice == "rock" and random_choice ==  3:
                print("You win!")
            elif user_choice == "scissors" and random_choice ==  2:
                print("You win!")
            elif user_choice == "paper" and random_choice ==  1:
                print("You win!")
            else:
                print("You lose")
            break

class gui_game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Scissors, Paper, Rock")
        self.window.tk.call('wm', 'iconphoto', self.window._w, tk.PhotoImage(file='logo.png'))
        self.window.minsize(400, 200)
        self.window.bind('<Return>', self.go)
        entry_label = tk.Label(text="Enter 'scissors', 'paper' or 'rock':")
        self.entry = tk.Entry()
        entry_label.pack()
        self.entry.pack()
        self.go_button = tk.Button(text="Go")
        self.go_button.pack()
        self.help_button = tk.Button(text="Help", command=self.show_help_dialog)
        self.help_button.pack()
        self.go_button.bind("<Button-1>", self.go)
        self.label = tk.Label()
        self.label.pack()
        self.entry.focus()
        self.window.mainloop()
    def go(self, event):
        user_choice = self.entry.get()
        random_choice = random.randint(1, 3)
        lbl_txt = ""
        if user_choice not in ["rock", "paper", "scissors"]:
            tkinter.messagebox.showerror("Invalid choice", "You must pick either 'scissors', 'paper' or 'rock'")
        else:
            lbl_txt += f"The computer chose {str(random_choice).replace('1', 'rock').replace('2', 'paper').replace('3', 'scissors')}\n"
            if user_choice == "rock" and random_choice ==  1 or user_choice == "paper" and random_choice ==  2 or user_choice == "scissors" and random_choice ==  3:
                lbl_txt += "It was a draw. Go again."
            elif user_choice == "rock" and random_choice ==  3:
                lbl_txt += "You win!"
            elif user_choice == "scissors" and random_choice ==  2:
                lbl_txt += "You win!"
            elif user_choice == "paper" and random_choice ==  1:
                lbl_txt += "You win!"
            else:
                lbl_txt += "You lose"
        self.label.config(text=lbl_txt)
        self.entry.delete(0, 'end')
    def show_help_dialog(self):
        aboutdialog = AboutDialog(self.window)
        self.window.wait_window(aboutdialog.top)

class AboutDialog:
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        self.about_text = tk.Text(top)
        self.about_text.pack()
        self.about_text.config(state='normal')
        self.about_text.insert('end', HELP_MESSAGE)
        self.about_text.config(state='disabled')
        self.close_button = tk.Button(top, text='Close', command=self.top.destroy)
        self.close_button.pack()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1].lower() in ["-h", "--help", "help"]:
            print(HELP_MESSAGE)
            raise SystemExit
        elif sys.argv[1].lower() in ["-g", "--gui", "gui"]:
            gui_game()
        elif sys.argv[1].lower() in ["-c", "--cli", "cli"]:
            cli_game().start()
        else:
            print("Invalid arguments, use --help for help")
    else:
        print("Not enough arguments, use --help for help")