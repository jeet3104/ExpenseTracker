from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import TransactionManager, TransactionStack
from datetime import datetime

# Create Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'

# Initialize our transaction system
transaction_manager = TransactionManager()
expense_history = TransactionStack()
income_history = TransactionStack()

# Home page route
@app.route('/')
def home():
    # Get all transactions
    expenses = transaction_manager.expenses
    incomes = transaction_manager.incomes
    
    # Calculate totals
    total_expense = 0
    for expense in expenses:
        total_expense += expense.amount
        
    total_income = 0
    for income in incomes:
        total_income += income.amount
        
    # Calculate remaining balance
    balance = total_income - total_expense
    
    # Show the main page
    return render_template('index.html', 
                         expenses=expenses, 
                         incomes=incomes,
                         total_expense=total_expense,
                         total_income=total_income,
                         balance=balance)

# Add new expense
@app.route('/add_expense', methods=['POST'])
def add_expense():
    # Get form data
    amount = float(request.form['amount'])
    description = request.form['description']
    category = request.form['category']
    
    # Check if we have enough balance
    total_income = sum(income.amount for income in transaction_manager.incomes)
    total_expense = sum(expense.amount for expense in transaction_manager.expenses)
    available_balance = total_income - total_expense
    
    # Don't allow expense if no money available
    if available_balance < amount:
        return jsonify({
            'success': False,
            'message': 'Not enough balance! Please add income first.'
        }), 400
    
    # Add the expense
    expense = transaction_manager.add_expense(amount, description, category)
    expense_history.push(('add', expense))
    return redirect(url_for('home'))

# Add new income
@app.route('/add_income', methods=['POST'])
def add_income():
    # Get form data
    amount = float(request.form['amount'])
    description = request.form['description']
    category = request.form['category']
    
    # Add the income
    income = transaction_manager.add_income(amount, description, category)
    income_history.push(('add', income))
    return redirect(url_for('home'))

# Delete an expense
@app.route('/delete_expense/<int:id>')
def delete_expense(id):
    # Find the expense first
    expense = transaction_manager.get_expense(id)
    if expense:
        # Delete it and save to history
        transaction_manager.delete_expense(id)
        expense_history.push(('delete', expense))
    return redirect(url_for('home'))

# Delete an income
@app.route('/delete_income/<int:id>')
def delete_income(id):
    # Find the income first
    income = transaction_manager.get_income(id)
    if income:
        # Delete it and save to history
        transaction_manager.delete_income(id)
        income_history.push(('delete', income))
    return redirect(url_for('home'))

# Edit an expense
@app.route('/edit_expense/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = transaction_manager.get_expense(id)
    
    if request.method == 'POST':
        # Update expense details
        expense.amount = float(request.form['amount'])
        expense.description = request.form['description']
        expense.category = request.form['category']
        return redirect(url_for('home'))
        
    # Show edit form
    return render_template('edit_expense.html', expense=expense)

# Edit an income
@app.route('/edit_income/<int:id>', methods=['GET', 'POST'])
def edit_income(id):
    income = transaction_manager.get_income(id)
    
    if request.method == 'POST':
        # Update income details
        income.amount = float(request.form['amount'])
        income.description = request.form['description']
        income.category = request.form['category']
        return redirect(url_for('home'))
        
    # Show edit form
    return render_template('edit_income.html', income=income)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)