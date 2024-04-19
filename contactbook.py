import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contacts = []

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label_name = tk.Label(self.frame, text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.frame)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_phone = tk.Label(self.frame, text="Phone:")
        self.label_phone.grid(row=1, column=0, padx=5, pady=5)
        self.entry_phone = tk.Entry(self.frame)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)

        self.button_add = tk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=2, column=0, padx=5, pady=5)
        self.button_view = tk.Button(self.frame, text="View Contacts", command=self.show_contacts)
        self.button_view.grid(row=2, column=1, padx=5, pady=5)

        self.label_search = tk.Label(self.frame, text="Search:")
        self.label_search.grid(row=3, column=0, padx=5, pady=5)
        self.entry_search = tk.Entry(self.frame)
        self.entry_search.grid(row=3, column=1, padx=5, pady=5)
        self.button_search = tk.Button(self.frame, text="Search", command=self.search_contact)
        self.button_search.grid(row=3, column=2, padx=5, pady=5)

        self.label_output = tk.Label(self.frame, text="Contacts:")
        self.label_output.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.text_output = tk.Text(self.frame, height=10, width=40)
        self.text_output.grid(row=5, columnspan=2, padx=5, pady=5)

        self.label_update = tk.Label(self.frame, text="Update Index:")
        self.label_update.grid(row=6, column=0, padx=5, pady=5)
        self.entry_update = tk.Entry(self.frame)
        self.entry_update.grid(row=6, column=1, padx=5, pady=5)
        self.button_update = tk.Button(self.frame, text="Update", command=self.update_contact)
        self.button_update.grid(row=6, column=2, padx=5, pady=5)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        if name and phone:
            self.contacts.append((name, phone))
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter both name and phone number.")

    def show_contacts(self):
        self.text_output.delete(1.0, tk.END)
        for i, contact in enumerate(self.contacts, start=1):
            self.text_output.insert(tk.END, f"{i}. Name: {contact[0]}, Phone: {contact[1]}\n")

    def search_contact(self):
        query = self.entry_search.get().lower()
        results = [contact for contact in self.contacts if query in contact[0].lower() or query in contact[1]]
        self.text_output.delete(1.0, tk.END)
        if results:
            for i, contact in enumerate(results, start=1):
                self.text_output.insert(tk.END, f"{i}. Name: {contact[0]}, Phone: {contact[1]}\n")
        else:
            self.text_output.insert(tk.END, "No matching contacts found.")

    def update_contact(self):
        try:
            index = int(self.entry_update.get()) - 1
            if index < 0 or index >= len(self.contacts):
                raise ValueError
            name = self.entry_name.get()
            phone = self.entry_phone.get()
            if name and phone:
                self.contacts[index] = (name, phone)
                self.clear_entries()
                self.show_contacts()
            else:
                messagebox.showerror("Error", "Please enter both name and phone number.")
        except ValueError:
            messagebox.showerror("Error", "Invalid index.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_search.delete(0, tk.END)
        self.entry_update.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
