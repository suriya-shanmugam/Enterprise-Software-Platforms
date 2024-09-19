<h1>Auto Expense Tracker - Prototype</h1>

<p> This is protype of the application that helps you track the monthly expenses .  



## Features

- Monthly expense report
- List of recent expenses
- Add, update, and delete expenses
- Extract expense details from receipt images - [This will not work because need to learn how to bundle the API credentials in docket image]


## Prerequisites

- Docker

## Setup

1. Pull the image

```
docker pull suriyashanmugam/expensemanage:v1
```

2. Run

```
docker run -p 12345:5001 suriyashanmugam/expensemanage:v1
```

3. Open a web browser and navigate to `http://localhost:12345`

## Project Structure

- `app.py`: Main Flask application file
- `spends_handler.py`: Handles expense-related operations
- `image_processor.py`: Processes receipt images using Gemini API
- `templates/index.html`: HTML template for the web interface
- `static/script.js`: JavaScript file for client-side logic
- `static/styles.css`: CSS file for styling
- `expenses.json`: JSON file for storing expense data

## Usage

1. **Adding an Expense**: 
   - Fill out the expense form with details (amount, title, date, description)
   - Optionally upload a receipt image to auto-fill the form
   - Click "Add Expense" to save

2. **Viewing Expenses**: 
   - The monthly total is displayed at the top
   - The list of expenses is shown below the form

3. **Editing an Expense**: 
   - Click the "Edit" button next to an expense
   - Update the details in the form
   - Click "Update Expense" to save changes

4. **Deleting an Expense**: 
   - Click the "Delete" button next to an expense
   - Confirm the deletion when prompted

