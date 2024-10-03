# Django CRUD with Signals

This project demonstrates about  Django signals with CRUD operations. It includes the creation, update, and deletion of employee records, with Django signals (`post_save` and `post_delete`) integrated to handle actions like logging and simulating transactional behavior.

## How Django Signals Are Integrated

1. **Synchronous Signal Execution**:
    - When an employee record is created or updated, the post_save signal is triggered **synchronously**, meaning it runs in the same flow as the main request

2. **Same Thread Execution**:
    - The signal handler runs in the same thread as the view. We print the thread name in both the view and the signal handler to demonstrate that they share the same thread.

3. **Transactional Rollback**:
    - If an exception is raised in the signal handler (as demonstrated in `signals.py` for the `post_save` signal), the database transaction is rolled back, and the employee record is not saved.

## Requirements

- Python 3.8+
- Django 3.x+
- SQLite 
## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Kunalkrsingh-10/Eventmanagment.git
    cd Eventmanagment
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv myenv
    source myenv/bin/activate  
    ```


