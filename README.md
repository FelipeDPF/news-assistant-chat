# 📰 News Assistant Chat App

This is a simple conversational web app built with FastAPI and vanilla JavaScript that lets users interact with a chatbot-style news assistant. It fetches real-time news using the NewsAPI and presents it in a friendly chat interface styled with Bootstrap 5.

---

## ✨ Features

- Conversational chat UI with typing effect
- Light/Dark mode toggle 🌞🌙
- Responsive layout and clean design
- API integration with NewsAPI for live headlines
- **FastAPI backend** for secure API handling and key management
- Graceful message formatting with titles, images, and links
- Follow-up conversation flow ("Looking for anything else?")
- Restart conversation with "Hey"
- Friendly closing message when the session ends

---

![News Assistant Demo](./demo1.gif)

## 🗂 Project Structure

```
NEWS_APP/
├── main.py               # FastAPI backend
├── templates/
│   └── index.html        # Main frontend template
└── README.md
```

## 🛠 Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

## 🚀 Getting Started

1. Clone the Repository

```
git clone https://github.com/your-username/news-assistant-chat.git
cd news-assistant-chat
```

2. Install Dependencies

```
pip install fastapi uvicorn jinja2 requests
```

3. Get a NewsAPI Key

- Sign up at https://newsapi.org/

- Copy your API key and paste it into main.py:

```
API_KEY = "your-api-key-here"
```

4. Run the App

```
uvicorn main:app --reload
```

Visit: http://localhost:8000

## 📖 Usage
- Open your browser and navigate to `http://127.0.0.1:8000`.
- Type your queries into the chatbox to fetch news.
- Use "Hey" to restart the conversation.

## 🔧 To-Do / Improvements

Here are some ideas to improve and expand the project:
- [ ] **Add error handling** for API request failures (e.g. network issues, invalid responses)
- [ ] **Make chat responsive/resizable**, especially for mobile devices
- [ ] **Improve assistant responses** to handle a wider range of user inputs (e.g. greetings, thanks, confusion)
- [ ] **Support follow-up questions** or multi-step queries
- [ ] **Add loading indicator or typing animation** when waiting for news results
- [ ] **Allow user to select news country or category** (e.g. sports, tech, etc.)
- [ ] **Add a "Clear Chat" button** to reset the conversation
- [ ] **Use local storage or session** to remember previous conversations
- [ ] **Add deployment instructions** for hosting on platforms like Vercel or Render
- [ ] **Write unit tests** for backend (FastAPI) logic

## 🤖 Technologies Used

- FastAPI: Backend framework

- Jinja2 Templating

- Bootstrap 5 + Font Awesome: Frontend styling

- Vanilla JavaScript: Client-side interactivity

- NewsAPI for fetching articles: Real-time news data

## 🙌 Acknowledgments

- NewsAPI for their awesome free news API

- Bootstrap for making styling a breeze