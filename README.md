# 🗳️ Online Polling System  

An interactive online polling system that allows users to create, vote on, and manage polls efficiently. Built with Django's Class-Based Views (CBVs) for a structured and maintainable backend.  

## 🚀 Features  

- **User Authentication** – Sign up, log in, and manage polls securely.  
- **Poll Creation** – Users can create polls with multiple choices and set the number of allowed selections.  
- **Voting System** – Users can vote on polls with at least one selection, ensuring valid participation.  
- **Poll Sharing** – Share poll links for external voting.  
- **Poll Management** – Poll creators can manually close polls or set an expiration timer.  
- **User Poll History** – Users can view their past polls and participation.  

## 🛠️ Tech Stack  

- **Backend:** Django, CBVs  
- **Database:** SQLite (default, but configurable)  
- **Frontend:** Basic HTML, CSS, and JavaScript  

## 🔧 Setup & Installation  

1. **Clone the Repository**  
   ```sh
   git clone https://github.com/alirezz2020/Online-Polling-System.git
   cd Online-Polling-System
2 **Create a Virtual Environment**
```sh
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**

  pip install -r requirements.txt

4. **Apply Migrations**

  python manage.py migrate
  
5. **Create a Superuser (Optional for Admin Access)**

  python manage.py createsuperuser
  
6. **Run the Development Server**

  python manage.py runserver

7**Access the App**
  Open http://127.0.0.1:8000/ in your browser.


  **🤝 Contributing**
    Feel free to fork this repository, open issues, and submit pull requests!


    **📜 License**
      This project is licensed under the MIT License.
