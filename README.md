# 🚀 AI Career Roadmap Generator

An AI-powered career guidance application that generates structured learning roadmaps for different career paths.

The application helps students and professionals understand the skills, technologies, tools, and projects required to achieve their desired career goals.

Currently supports multiple IT and non-IT career roles such as:

- AI Engineer
- Machine Learning Engineer
- Data Scientist
- Data Analyst
- Software Developer
- Frontend Developer
- Backend Developer
- DevOps Engineer
- Cloud Engineer
- Cyber Security Analyst
- UI/UX Designer
- Business Analyst
- Digital Marketing Specialist
- Financial Analyst
- HR Manager


## 🌟 Features

✅ Career role selection  
✅ Generates structured learning roadmap  
✅ Covers required skills and technologies  
✅ Includes project recommendations  
✅ FastAPI backend API  
✅ Streamlit interactive frontend  
✅ Easy to extend with new career paths  


## 🏗️ Project Architecture

```
AI-Roadmap-Generator/

│
├── backend/
│   ├── main.py
│   ├── roadmap.py
│   └── careers.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
├── .env
└── README.md
```

## 🔄 Application Workflow

```
User
 |
 |
Select Career Goal
 |
 |
Streamlit Frontend
 |
 |
FastAPI Backend
 |
 |
Roadmap Generator
 |
 |
Career Roadmap Response
 |
 |
Display Learning Path
```


# 🛠️ Tech Stack

## Backend
- Python
- FastAPI
- REST API

## Frontend
- Streamlit

## Development Tools
- VS Code
- Git
- GitHub


# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/AI-Roadmap-Generator.git
```

Move into project folder:

```bash
cd AI-Roadmap-Generator
```


## 2. Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```


## 3. Install Dependencies

```bash
pip install -r requirements.txt
```


# ▶️ How to Run the Project


## Start Backend (FastAPI)

Open Terminal 1:

```bash
uvicorn backend.main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```


## Start Frontend (Streamlit)

Open Terminal 2:

```bash
cd frontend
```

Run:

```bash
streamlit run app.py
```

Frontend will open at:

```
http://localhost:8501
```


# 📌 Example Output

Input:

```
Career Goal:
AI Engineer
```

Output:

```
AI Engineer Roadmap

Skills:
- Python
- Machine Learning
- Deep Learning
- NLP
- Generative AI
- LLMs

Projects:
- AI Chatbot
- Recommendation System
- RAG Assistant
```


# 🚀 Future Enhancements

- Integration with Gemini/OpenAI API
- Personalized roadmap generation
- Resume-based career recommendations
- Skill gap analysis
- Job role recommendations
- LinkedIn/Job portal integration
- User authentication
- Progress tracking dashboard

# 📄 License

This project is open-source and available for learning and development purposes.