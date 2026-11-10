# 🍽️ AI Restaurant Idea Generator

An AI-powered restaurant idea generator built using Python, Streamlit, LangChain, and Google's Gemini API.

## 🚀 Project Overview

The AI Restaurant Idea Generator helps users generate creative restaurant names and signature menu items based on their preferred cuisine.

Users can select from multiple cuisines, including:
- Indian
- Mexican
- American
- Russian
- Italian
- South Indian
- Arabic

The application uses Google's Gemini API to generate a unique restaurant name and five suggested menu items.

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini API
- python-dotenv

## 📁 Project Structure

```text
AI-Restaurant-Generator/
│
├── App.py
├── Langchain_helper.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd AI-Restaurant-Generator
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root directory.

Add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_actual_api_key
```

Get an API key from Google AI Studio:

https://aistudio.google.com/apikey

### 5. Run the application

```bash
streamlit run App.py
```

The application will open in your default browser.

## ✨ Features

- Cuisine selection through an interactive sidebar.
- AI-generated restaurant names.
- Five AI-generated signature menu items.
- Integration with Google Gemini.
- Simple and user-friendly interface.

## 👨‍💻 Developer

Developed as a Generative AI project using Python, LangChain, and Streamlit.