import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.config(bg="lightgray")

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Password Generator", font=("Helvetica", 24, "bold"), bg="lightgray")
        self.title_label.pack(pady=20)

        self.length_frame = tk.Frame(self.root, bg="lightgray")
        self.length_frame.pack(pady=10)

        self.length_label = tk.Label(self.length_frame, text="Password Length:", font=("Helvetica", 14), bg="lightgray")
        self.length_label.grid(row=0, column=0, padx=10)

        self.length_entry = tk.Entry(self.length_frame, font=("Helvetica", 14), width=5)
        self.length_entry.grid(row=0, column=1, padx=10)

        self.generate_button = tk.Button(self.root, text="Generate Password", font=("Helvetica", 14), command=self.generate_password)
        self.generate_button.pack(pady=20)

        self.password_label = tk.Label(self.root, text="", font=("Helvetica", 18, "bold"), bg="lightgray", wraplength=350)
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be positive")

            # Create the pool of characters
            characters = string.ascii_letters + string.digits + string.punctuation

            # Generate the password
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
