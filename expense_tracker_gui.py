from tkinter import Tk, Label, Entry, Button, Listbox, END

class ExpenseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.categories = []
        self.expenses = []

        self.category_label = Label(root, text="Category:")
        self.category_label.pack()
        self.category_entry = Entry(root)
        self.category_entry.pack()

        self.amount_label = Label(root, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = Entry(root)
        self.amount_entry.pack()

        self.add_button = Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

        self.expenses_listbox = Listbox(root)
        self.expenses_listbox.pack()

    def add_expense(self):
        category = self.category_entry.get()
        amount = float(self.amount_entry.get())

        self.categories.append(category)
        self.expenses.append((category, amount))

        self.expenses_listbox.insert(END, f"{category}: ${amount}")

        self.category_entry.delete(0, END)
        self.amount_entry.delete(0, END)

    def set_analysis(self, analysis):
        self.analysis = analysis
        self.analysis.initialize(self.categories, self.expenses)
