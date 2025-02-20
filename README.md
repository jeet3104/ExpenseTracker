# ExpenseTracker

## Overview

ExpenseTracker is a simple web application that helps users manage their income and expenses efficiently. It allows users to add, categorize, and track their expenses and income, providing a clear view of their financial balance.

## Features

- Add Income with categories
- Add Expenses with categories
- View total income, total expenses, and balance
- Recent transactions history
- User-friendly UI for easy expense management

## Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Data Structures & Algorithms:** Used for efficient transaction handling and categorization

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ExpenseTracker.git
   cd ExpenseTracker
   ```
2. Set up a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```sh
   python app.py
   ```
5. Open the browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Usage

1. Enter your income details (amount, description, category) and click "Add Income".
2. Enter your expense details (amount, description, category) and click "Add Expense".
3. View the summary of total income, total expenses, and balance at the top.
4. Check recent transactions in the "Recent Expenses" and "Recent Income" sections.

## Contributing

Feel free to fork the repository and submit pull requests for improvements and new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



Thank you for using the Expense Tracker with Stack DS! If you have any questions or feedback, feel free to open an issue or contact us.
