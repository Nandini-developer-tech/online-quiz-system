# Online Quiz System
 
## Project Overview         
       
The Online Quiz System is a web-based application developed using **Python Flask, MySQL, HTML, and CSS**. The system allows users to register, log in, select a subject, attempt quizzes, and view their results. The application supports multiple subjects such as Python, Java, DBMS, Operating Systems, and Computer Networks. Questions are stored in a MySQL database and are displayed dynamically based on the subject selected by the user.         

The system automatically evaluates answers, calculates scores, stores quiz results, and maintains a history of quiz attempts for each user.                                     

---

# Technologies Used                 
    
### Frontend

* HTML5
* CSS3

### Backend          

* Python
* Flask Framework

### Database

* MySQL

---
  
# Project Structure  

```text          
online_quiz_system/    
│
├── app.py
│
├── templates/
│   ├── register.html
│   ├── login.html
│   ├── subjects.html
│   ├── quiz.html
│   ├── result.html           
│   └── history.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

# File Description

## 1. app.py

This is the main file of the project. It contains all the Flask routes and application logic.                    

### Responsibilities     

* Establishes database connection
* Handles user registration
* Handles user login
* Displays available subjects
* Loads questions based on selected subject
* Evaluates quiz answers
* Calculates score
* Stores results in the database
* Displays quiz history
* Manages user sessions
* Handles logout functionality

### Routes Used

| Route     | Purpose                                |
| --------- | -------------------------------------- |
| /         | Redirects user to login page           |
| /register | User Registration                      |
| /login    | User Login                             |
| /subjects | Displays available subjects            |
| /quiz     | Displays quiz questions                |
| /submit   | Evaluates answers and calculates score |
| /history  | Displays previous quiz results         |
| /logout   | Logs out the user                      |

---
   
## 2. templates/register.html

This page allows new users to create an account.

### Fields

* Username
* Email       
* Password

### Functionality

When the user clicks the Register button, the entered information is stored in the `users` table of the database.            

---

## 3. templates/login.html

This page allows registered users to log in.

### Fields

* Username
* Password

### Functionality

The entered credentials are verified against the database. If valid, the user is redirected to the subject selection page.

---

## 4. templates/subjects.html

This page displays all available quiz subjects.

### Example Subjects

* Python
* Java
* DBMS
* Operating System     
* Computer Networks          

### Functionality

The user selects a subject and clicks the "Start Quiz" button. The selected subject ID is sent to the server, which loads the corresponding questions.

---

## 5. templates/quiz.html

This page displays quiz questions and answer options.
         
### Functionality

* Retrieves questions from the database.
* Displays questions dynamically.
* Allows users to select answers using radio buttons.      
* Submits answers for evaluation.

### Example

Question:

What is Python?

Options:

* Programming Language
* Browser
* Database
* Operating System

The user selects one answer and proceeds.

---

## 6. templates/result.html

This page displays the user's quiz score after submission.

### Information Displayed

* Total Questions
* Correct Answers
* Final Score

### Example

```text
Quiz Result

Score: 8 / 10
```

---

## 7. templates/history.html

This page displays the user's previous quiz attempts.

### Information Displayed

* Subject Name
* Score
* Date of Attempt

### Example

| Subject | Score | Date       |
| ------- | ----- | ---------- |
| Python  | 8     | 2026-06-05 |
| Java    | 7     | 2026-06-06 |

---

## 8. static/style.css

This file contains the styling for all web pages.

### Responsibilities

* Page layout
* Form styling
* Button styling
* Table styling
* Responsive design
* Color schemes
* Typography

The CSS file ensures a professional and user-friendly interface throughout the application.

---

# Database Design

The project uses four tables.

## users Table

Stores user information.

| Column Name | Description    |
| ----------- | -------------- |
| user_id     | Unique user ID |
| username    | User name      |
| email       | User email     |
| password    | User password  |

---

## subjects Table

Stores available quiz subjects.

| Column Name  | Description       |
| ------------ | ----------------- |
| subject_id   | Unique subject ID |
| subject_name | Subject name      |

---

## questions Table

Stores quiz questions and answer options.

| Column Name    | Description        |
| -------------- | ------------------ |
| question_id    | Unique question ID |
| subject_id     | Subject reference  |
| question       | Question text      |
| option1        | First option       |
| option2        | Second option      |
| option3        | Third option       |
| option4        | Fourth option      |
| correct_answer | Correct answer     |

---

## results Table

Stores quiz results.

| Column Name | Description          |
| ----------- | -------------------- |
| result_id   | Unique result ID     |
| user_id     | User reference       |
| subject_id  | Subject reference    |
| score       | Quiz score           |
| quiz_date   | Date of quiz attempt |

---

# Application Workflow

```text
User Opens Application
          │
          ▼
      Register
          │
          ▼
        Login
          │
          ▼
   Select Subject
          │
          ▼
      Start Quiz
          │
          ▼
   Answer Questions
          │
          ▼
     Submit Quiz
          │
          ▼
   Score Calculation
          │
          ▼
    Result Display
          │
          ▼
    Save to Database
          │
          ▼
     View History
```

---

# How Score Calculation Works

When a user submits a quiz:

1. The system retrieves the correct answers from the database.
2. User-selected answers are collected from the form.
3. Each answer is compared with the corresponding correct answer.
4. For every correct answer, the score is increased by one.
5. The final score is calculated and displayed.
6. The result is stored in the database.

### Example

```text
Total Questions : 10

Correct Answers : 8

Wrong Answers : 2

Final Score : 8/10
```

---

# Features Implemented

### User Features

* Registration
* Login
* Subject Selection
* Quiz Attempt
* Result Viewing
* Quiz History
* Logout

### System Features

* Dynamic Question Loading
* Automatic Evaluation
* Result Storage
* Session Management
* Multi-Subject Support

---

# Future Enhancements

The project can be extended with:

* Admin Dashboard
* Add/Edit/Delete Questions
* Timer-Based Quiz
* Leaderboard
* Random Question Selection
* Password Encryption
* Email Verification
* Certificate Generation
* PDF Report Download
* Difficulty Levels (Easy, Medium, Hard)

---

# Learning Outcomes

This project helped in understanding:

* Flask Web Development
* Routing and Templates
* MySQL Database Integration
* Session Handling
* CRUD Operations
* User Authentication
* Dynamic Content Rendering
* Frontend Design using HTML and CSS

---

# Conclusion

The Online Quiz System is a complete web application that demonstrates the integration of Flask, MySQL, HTML, and CSS to create an interactive learning platform. The project provides hands-on experience with backend development, database management, user authentication, and frontend design. It serves as an excellent academic and portfolio project for students learning full-stack web development.

**Developed By:** Nandini
**Technology Stack:** Python, Flask, MySQL, HTML, CSS
**Project Type:** Web Application / Academic Mini Project
