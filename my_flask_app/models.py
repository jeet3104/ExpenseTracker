from datetime import datetime

# Simple class to store transaction details
class Transaction:
    def __init__(self, amount, description, category):
        # Using a simple counter would be more human-like than id()
        self.id = Transaction.get_next_id()
        self.amount = amount
        self.description = description
        self.category = category
        self.date = datetime.now()
    
    # Simple counter for IDs (more intuitive than using id())
    _id_counter = 0
    
    @classmethod
    def get_next_id(cls):
        cls._id_counter += 1
        return cls._id_counter

# Simple manager to handle all transactions
class TransactionManager:
    def __init__(self):
        # Simple lists to store transactions
        self.expenses = []
        self.incomes = []
    
    # Basic expense operations
    def add_expense(self, amount, description, category):
        new_expense = Transaction(amount, description, category)
        self.expenses.append(new_expense)
        return new_expense
    
    def delete_expense(self, id):
        # Simple loop to find and remove expense
        for expense in self.expenses:
            if expense.id == id:
                self.expenses.remove(expense)
                break
    
    def get_expense(self, id):
        # Simple loop to find expense
        for expense in self.expenses:
            if expense.id == id:
                return expense
        return None
    
    # Basic income operations
    def add_income(self, amount, description, category):
        new_income = Transaction(amount, description, category)
        self.incomes.append(new_income)
        return new_income
    
    def delete_income(self, id):
        # Simple loop to find and remove income
        for income in self.incomes:
            if income.id == id:
                self.incomes.remove(income)
                break
    
    def get_income(self, id):
        # Simple loop to find income
        for income in self.incomes:
            if income.id == id:
                return income
        return None

# Basic stack implementation for transaction history
class TransactionStack:
    def __init__(self):
        # Using a simple list as stack
        self.transactions = []
    
    def push(self, transaction):
        # Add transaction to top of stack
        self.transactions.append(transaction)
    
    def pop(self):
        # Remove and return top transaction
        if not self.is_empty():
            return self.transactions.pop()
        return None
    
    def is_empty(self):
        # Check if stack is empty
        return len(self.transactions) == 0 