# Nemching ChatBot 🤖💬

An intelligent AI-powered chatbot web application featuring a modern, responsive interface and real-time conversational capabilities powered by Meta's Llama 4 Scout model.

[![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge&logo=render)](https://nemching-chatbot.onrender.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/wealthyr7-cyber/nemching-chatbot)
[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)

## 🌐 Live Demo

**[Try Nemching ChatBot Live →](https://nemching-chatbot.onrender.com/)**

> Experience real-time AI conversations with context-aware responses. Works seamlessly on desktop and mobile devices.

## ✨ Key Features

- 🤖 **Advanced AI Model**: Powered by Meta's Llama 4 Scout (17B parameters)
- 💬 **Context-Aware Conversations**: Maintains conversation history for natural dialogue
- 📱 **Fully Responsive**: Beautiful mobile-first design with gradient UI
- 🔄 **Resilient Architecture**: Automatic retry logic with exponential backoff
- ⚡ **Real-Time Responses**: Fast, streaming-style responses
- 🎨 **Modern UI/UX**: Pink/purple gradient theme with smooth animations
- 🔒 **Secure**: Environment-based API key management
- 🚀 **Production-Ready**: Deployed with CI/CD pipeline

## 🛠️ Technology Stack

### Backend
- **Python 3.12** - Core programming language
- **Flask 3.0** - Lightweight web framework
- **Gunicorn** - Production WSGI server

### AI & APIs
- **Meta Llama 4 Scout** (17B parameters) - Language model
- **HuggingFace Inference Providers** - API gateway
- **Together AI** - Inference provider

### Frontend
- **HTML5/CSS3** - Semantic markup and modern styling
- **Vanilla JavaScript** - No framework dependencies
- **Responsive Design** - Mobile-first approach

### DevOps & Deployment
- **Git/GitHub** - Version control
- **Render** - Cloud hosting with auto-deployment
- **Environment Variables** - Secure configuration

## 📂 Project Structure
```
llama_project/
├── app.py                    # Flask application & API routes
├── templates/
│   └── index.html           # Frontend interface
├── requirements.txt          # Python dependencies
├── render.yaml              # Render deployment config
├── .gitignore               # Git ignore rules
└── README.md                # Documentation
```

## 🚀 Local Setup

### Prerequisites
- Python 3.12 or higher
- HuggingFace account with API token
- Git installed

### Installation Steps

1. **Clone the repository**
```bash
   git clone https://github.com/wealthyr7-cyber/nemching-chatbot.git
   cd nemching-chatbot
```

2. **Create virtual environment**
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Set environment variable**
```bash
   export HF_TOKEN="your_huggingface_token"
```

5. **Run the application**
```bash
   python app.py
```

6. **Access the app**
```
   http://localhost:5001
```

## 🌍 Deployment

### Deploy to Render

1. Fork this repository
2. Sign up at Render.com
3. Create new Web Service
4. Connect your GitHub repository
5. Add environment variable: HF_TOKEN
6. Deploy!

## 🔑 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| HF_TOKEN | HuggingFace API token | Yes |

## 💡 Key Technical Implementations

### Resilient API Integration
Automatic retry with exponential backoff for handling 503 errors

### Session-Based History
Maintains conversation context across multiple messages

### API Migration
Successfully migrated from deprecated endpoints to new Providers API

## 📊 Performance

- **Response Time**: < 3 seconds average
- **Concurrent Users**: 5-10 simultaneous users
- **Uptime**: 99%+
- **Context Window**: Last 20 messages

## 🎓 Learning Outcomes

### Skills Developed
- RESTful API integration and error handling
- Environment-based configuration management
- Cloud deployment with CI/CD pipelines
- Session management in web applications
- Responsive web design
- Git workflow and version control

### Challenges Overcome
1. API endpoint migration from deprecated infrastructure
2. Implemented retry logic for service errors
3. Secret management and GitHub security
4. Browser cache handling during development

## 🔮 Future Enhancements

- [ ] Image generation (Stable Diffusion)
- [ ] Voice input/output support
- [ ] Multi-language support
- [ ] User authentication
- [ ] Chat history export
- [ ] File upload capability
- [ ] PWA capabilities

## 👤 Author

**GitHub**: [@wealthyr7-cyber](https://github.com/wealthyr7-cyber)

**Email**: wealthyr7@gmail.com

## 🙏 Acknowledgments

- Meta AI for Llama 4 Scout model
- HuggingFace for Inference Providers
- Render for cloud hosting
- Flask community

## 📄 License

This project is open source and available under the MIT License.

---

⭐ **Star this repo if you found it helpful!**

*Last Updated: November 1, 2025*
