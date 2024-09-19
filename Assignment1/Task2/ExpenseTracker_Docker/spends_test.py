import pytest
import json
import datetime
from spends_handler import SpendsHandler
from unittest.mock import patch


@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test_expenses.json"
    file.write_text("[]")
    return str(file)

@pytest.fixture
def handler(temp_file):
    return SpendsHandler(temp_file)

def test_create_expense(handler):
    expense_data = {
        'title': 'Test Expense',
        'amount': 100.50,
        'date': '2024-03-16',
        'description': 'This is a test expense'
    }
    result = handler.create_expense(expense_data)
    assert result['success'] is True
    assert result['message'] == 'Expense added successfully'
    
    expenses = handler.get_expenses()
    assert len(expenses) == 1
    assert expenses[0]['title'] == 'Test Expense'
    assert expenses[0]['amount'] == 100.50
    assert expenses[0]['date'] == '2024-03-16'
    assert expenses[0]['description'] == 'This is a test expense'

def test_update_expense(handler):
    # First, create an expense
    handler.create_expense({
        'title': 'Original Expense',
        'amount': 50.00,
        'date': '2024-03-15',
        'description': 'Original description'
    })
    
    # Now, update it
    update_data = {
        'id': 1,
        'title': 'Updated Expense',
        'amount': 75.00,
        'date': '2024-03-16',
        'description': 'Updated description'
    }
    result = handler.update_expense(update_data)
    assert result['success'] is True
    assert result['message'] == 'Expense updated successfully'
    
    expenses = handler.get_expenses()
    assert len(expenses) == 1
    assert expenses[0]['title'] == 'Updated Expense'
    assert expenses[0]['amount'] == 75.00
    assert expenses[0]['date'] == '2024-03-16'
    assert expenses[0]['description'] == 'Updated description'

def test_delete_expense(handler):
    # First, create an expense
    handler.create_expense({
        'title': 'Expense to Delete',
        'amount': 25.00,
        'date': '2024-03-17',
        'description': 'This expense will be deleted'
    })
    
    # Now, delete it
    result = handler.delete_expense(1)
    assert result['success'] is True
    assert result['message'] == 'Expense deleted successfully'
    
    expenses = handler.get_expenses()
    assert len(expenses) == 0

def test_get_expenses(handler):
    # Create multiple expenses
    handler.create_expense({
        'title': 'Expense 1',
        'amount': 100.00,
        'date': '2024-03-15',
        'description': 'First expense'
    })
    handler.create_expense({
        'title': 'Expense 2',
        'amount': 200.00,
        'date': '2024-03-16',
        'description': 'Second expense'
    })
    
    expenses = handler.get_expenses()
    assert len(expenses) == 2
    assert expenses[0]['title'] == 'Expense 1'
    assert expenses[1]['title'] == 'Expense 2'


def test_load_expenses(temp_file):
    # Prepare a file with some expenses
    expenses = [
        {
            'id': 1,
            'title': 'Test Expense',
            'amount': 100.50,
            'date': '2024-03-16',
            'description': 'This is a test expense'
        }
    ]
    with open(temp_file, 'w') as f:
        json.dump(expenses, f)
    
    # Create a new handler, which should load the expenses
    handler = SpendsHandler(temp_file)
    loaded_expenses = handler.get_expenses()
    
    assert len(loaded_expenses) == 1
    assert loaded_expenses[0]['title'] == 'Test Expense'
    assert loaded_expenses[0]['amount'] == 100.50

def test_save_expenses(handler, temp_file):
    # Create an expense
    handler.create_expense({
        'title': 'Expense to Save',
        'amount': 150.75,
        'date': '2024-03-18',
        'description': 'This expense should be saved to file'
    })
    
    # Create a new handler to load from the file
    new_handler = SpendsHandler(temp_file)
    loaded_expenses = new_handler.get_expenses()
    
    assert len(loaded_expenses) == 1
    assert loaded_expenses[0]['title'] == 'Expense to Save'
    assert loaded_expenses[0]['amount'] == 150.75