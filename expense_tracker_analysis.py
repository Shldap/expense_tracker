import matplotlib.pyplot as plt
import numpy as np

class ExpenseTrackerAnalysis:
    def __init__(self):
        self.categories = []
        self.expenses = []

    def initialize(self, categories, expenses):
        self.categories = categories
        self.expenses = expenses

    def plot_category_spending(self):
        category_spending = {}
        for category in self.categories:
            category_spending[category] = sum(amount for cat, amount in self.expenses if cat == category)

        categories = list(category_spending.keys())
        spending = list(category_spending.values())

        plt.bar(categories, spending)
        plt.xlabel("Categories")
        plt.ylabel("Spending")
        plt.title("Category Spending")
        plt.show()

    def analyze_spending(self):
        total_spending = sum(amount for _, amount in self.expenses)
        average_spending = np.mean([amount for _, amount in self.expenses])
        max_spending = max([amount for _, amount in self.expenses])
        min_spending = min([amount for _, amount in self.expenses])

        print("Total Spending:", total_spending)
        print("Average Spending:", average_spending)
        print("Max Spending:", max_spending)
        print("Min Spending:", min_spending)
