# book_review_platform
Here’s a step-by-step guide to run the **Book Review Platform**:

---

### **Step-by-Step Command Guide**

#### **1. Setup the Virtual Environment**
Before running the project, create and activate a virtual environment to isolate your project dependencies.

- **Create a virtual environment**:
  ```bash
  python -m venv envname
  ```
  
- **Activate the virtual environment**:
  - On Windows:
    ```bash
    envname\Scripts\activate
    ```
  - On macOS/Linux:
    ```bash
    source envname/bin/activate
    ```

#### **2. Install Required Dependencies**
Ensure that you have the required packages installed. Use the `requirements.txt` file if available.

- Install Django and other dependencies:
  ```bash
  pip install -r requirements.txt
  ```
  *If there’s no `requirements.txt`, install Django manually*:
  ```bash
  pip install django
  ```

#### **3. Navigate to the Project Directory**
Move into the project folder where the `manage.py` file is located.

```bash
cd book_review_platform
```

#### **4. Apply Migrations**
Django uses migrations to set up the database schema.

- **Make migrations**:
  ```bash
  python manage.py makemigrations
  ```

- **Apply migrations**:
  ```bash
  python manage.py migrate
  ```

#### **5. Create a Superuser**
To access the Django admin panel, create a superuser account.

```bash
python manage.py createsuperuser
```

Follow the prompts to enter a username, email, and password.

#### **6. Run the Development Server**
Start the Django development server to test the application.

```bash
python manage.py runserver
```

#### **7. Access the Application**
- Open your web browser and go to:
  ```
  http://127.0.0.1:8000/
  ```
- To access the admin panel, visit:
  ```
  http://127.0.0.1:8000/admin/
  ```

#### **8. Test the Application**
- View the list of books on the homepage.
- Click on a book to see its details and submit a review.
- Use the admin panel to manage books and reviews.

#### **Optional: Collect Static Files for Deployment**
If you’re deploying the project, collect all static files using:
```bash
python manage.py collectstatic
```

---

### **Troubleshooting Tips**
1. **Dependency Issues**:
   If any library is missing or you encounter an error, install the required package using `pip install <package-name>`.

2. **Database Issues**:
   If migrations fail, delete the `db.sqlite3` file and the migrations folder, then recreate migrations:
   ```bash
   rm db.sqlite3
   rm -rf appname/migrations
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Virtual Environment Not Activating**:
   Ensure you’ve created the virtual environment in the correct directory and are running the correct activation command for your OS.

---

This command guide should help you set up and run your project seamlessly!


Screenshots
Here are some screenshots showcasing the key parts of the platform:

Homepage: Displays the list of all books available for review.
 ![image](https://github.com/user-attachments/assets/08e189b2-0f9c-4dd9-8190-f1458060cf76)

Book Detail Page: Shows detailed information about a specific book, along with a form for submitting reviews.
 ![image](https://github.com/user-attachments/assets/9ed6213b-cb76-4e63-8083-13ba0cd7e30d)

Add New Book: New Books are added.
 ![image](https://github.com/user-attachments/assets/d3423940-4842-4657-8040-c202d2e32901)

