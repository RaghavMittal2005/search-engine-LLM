# 🔎 LangChain Search Chatbot

A powerful AI chatbot built with LangChain and Streamlit that can search across Wikipedia, arXiv, and the web using DuckDuckGo to provide comprehensive answers to your questions.

## Features

- **Multi-Source Search**: Integrates Wikipedia, arXiv (academic papers), and DuckDuckGo web search
- **Interactive UI**: Built with Streamlit for a clean, user-friendly chat interface
- **Real-time Agent Actions**: View the agent's thought process and tool usage in real-time
- **Powered by Groq**: Uses Groq's fast LLM inference with the Gemma2-9b-it model
- **Persistent Chat History**: Maintains conversation context throughout the session

## Prerequisites

- Python 3.8+
- Groq API Key (get one from [console.groq.com](https://console.groq.com))

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd <your-repo-name>
```

2. **Install required packages**
```bash
pip install streamlit langchain langchain-groq langchain-community python-dotenv
```

3. **Set up environment variables** (Optional)

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

Or enter your API key directly in the sidebar when running the app.

## Usage

1. **Run the application**
```bash
streamlit run app.py
```

2. **Enter your Groq API Key** in the sidebar

3. **Start chatting!** Ask questions and watch the agent search across multiple sources:
   - "What is quantum computing?"
   - "Find recent papers about machine learning"
   - "Who won the Nobel Prize in Physics in 2023?"

## How It Works

The chatbot uses LangChain's agent framework with three specialized tools:

1. **Wikipedia Tool**: Searches Wikipedia for general knowledge
2. **arXiv Tool**: Searches academic papers and research
3. **DuckDuckGo Search**: Falls back to web search when other tools don't provide useful results

The agent intelligently decides which tool to use based on your question and combines information from multiple sources when needed.

## Project Structure

```
.
├── app.py              # Main application file
├── .env               # Environment variables (create this)
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Configuration

You can modify the following parameters in the code:

- **Model**: Change `model="gemma2-9b-it"` to use different Groq models
- **Character Limits**: Adjust `doc_content_chars_max` for Wikipedia and arXiv results
- **Agent Type**: Modify `AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION` for different agent behaviors

## Dependencies

```txt
streamlit
langchain
langchain-groq
langchain-community
python-dotenv
wikipedia
arxiv
duckduckgo-search
```

## Troubleshooting

**Issue**: "Invalid API Key" error
- **Solution**: Make sure you've entered a valid Groq API key in the sidebar

**Issue**: Search results are too long
- **Solution**: Adjust `doc_content_chars_max` parameter to reduce content length

**Issue**: Agent is slow
- **Solution**: Try a different Groq model or reduce the conversation history

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Acknowledgments

- Built with [LangChain](https://langchain.com/)
- UI powered by [Streamlit](https://streamlit.io/)
- LLM inference by [Groq](https://groq.com/)

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Happy Searching! 🚀**
