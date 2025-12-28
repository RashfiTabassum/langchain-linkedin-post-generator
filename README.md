# 🚀 AI LinkedIn Post Generator

An intelligent AI agent built with LangChain that generates professional, engaging LinkedIn posts based on user-provided topics and languages. Uses **GitHub Models for FREE** LLM access!

## ✨ Features

- **Multi-language Support**: Generate posts in English, Spanish, Bengali, French, German, or any custom language
- **FREE LLM Access**: Uses GitHub Models - no credit card required!
- **Smart Content Generation**: Leverages powerful models like GPT-4o-mini to create engaging, professional LinkedIn content
- **Hashtag Generation**: Optionally generate relevant hashtags for your posts
- **Interactive CLI**: User-friendly command-line interface for easy interaction
- **Customizable**: Adjust model parameters and prompts to fit your needs

## 📋 Requirements

- Python 3.8 or higher
- GitHub Personal Access Token (free to create)

## 🔧 Installation

1. **Clone or download this project**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   - Copy `.env.example` to `.env`:
     ```bash
     copy .env.example .env
     ```
   - Get your GitHub Personal Access Token:
     1. Go to https://github.com/settings/tokens
     2. Click "Generate new token" → "Generate new token (classic)"
     3. Give it a name like "LinkedIn Post Generator"
     4. Select scopes: No special scopes needed for GitHub Models
     5. Click "Generate token" and copy it
   - Edit `.env` and add your GitHub token:
     ```
     GITHUB_TOKEN=your_github_token_here
     ```

## 🚀 Usage

### Option 1: Web Interface (Recommended)

Run the Streamlit web app:
```bash
streamlit run streamlit_app.py
```

This will open a beautiful web interface in your browser where you can:
- Enter topics and select languages from dropdowns
- Toggle hashtags on/off
- Copy generated posts with one click
- Download posts as text files

### Option 2: Interactive CLI Mode

Run the command-line application:
```bash
python main.py
```

Follow the prompts to:
1. Enter your topic (e.g., "AI in Healthcare", "Remote Work Productivity")
2. Select your preferred language
3. Choose whether to include hashtags
4. View your generated LinkedIn post!

### Programmatic Usage

You can also use the agent in your own Python scripts:

```python
from linkedin_agent import LinkedInPostAgent

# Initialize the agent
agent = LinkedInPostAgent()

# Generate a post with hashtags
post = agent.generate_post(
    topic="AI in Healthcare",
    language="English",
    include_hashtags=True,
    num_hashtags=5
)
print(post)

# Generate a post without hashtags
post = agent.generate_post(
    topic="Remote Work Productivity",
    language="Spanish",
    include_hashtags=False
)
print(post)
```

## 📁 Project Structure

```
ai_linkedin_agent/
├── linkedin_agent.py      # Core AI agent implementation
├── main.py                # Interactive CLI application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🎯 Features Breakdown

### LinkedIn Post Agent (`linkedin_agent.py`)

- **LinkedInPostAgent class**: Main agent implementation
  - `generate_post()`: Generates a LinkedIn post based on topic and language
  - `generate_post_with_hashtags()`: Generates post with relevant hashtags

### Interactive CLI (`main.py`)

- User-friendly interface with emoji indicators
- Input validation and error handling
- Support for multiple posts in one session
- Customizable hashtag count

## 🔐 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GITHUB_TOKEN` | Your GitHub Personal Access Token | Required |
| `MODEL_NAME` | GitHub model to use | `gpt-4o-mini` |
| `TEMPERATURE` | Generation temperature (0-1) | `0.7` |

### Available GitHub Models (FREE):
- `gpt-4o-mini` - Fast and efficient (recommended)
- `gpt-4o` - Most capable
- `Phi-3-medium-4k-instruct` - Microsoft's Phi-3 model
- `Phi-3-small-8k-instruct` - Smaller Phi-3 variant
- And many more!

## 💡 Example Output

**Topic**: AI in Healthcare  
**Language**: English

```
The healthcare industry is witnessing a remarkable transformation through artificial intelligence. 🏥✨

AI-powered diagnostic tools are now helping doctors detect diseases earlier and with greater accuracy than ever before. From analyzing medical images to predicting patient outcomes, these technologies are not just enhancing clinical decision-making—they're saving lives.

However, the real magic happens when we combine AI's analytical power with human empathy and expertise. Technology should augment healthcare professionals, not replace them. The future of healthcare lies in this harmonious collaboration.

What's your take on AI in healthcare? Are you optimistic about its potential, or do you have concerns? Let's discuss! 💭

#AI #Healthcare #MedicalInnovation #Di (all models are free via GitHub):
```
MODEL_NAME=gpt-4o
## 🛠️ Customization

### Adjust the Model

Modify temperature and model in `.env`:
```
MODEL_NAME=gpt-4
TEMPERATURE=0.8
```

### Customize Prompts

Edit the prompt template in `linkedin_agent.py` to change the style or structure of generated posts.

## 🤝 Contributing

Feel free to fork this project and customize it for your needs!

## 📝 License

This project is open source and available for personal and commercial use.

## ⚠️ Important Notes

- **FREE to use** with GitHub Models - no credit card required! 🎉
- Ensure your GitHub token is kept secure and never committed to version control
- GitHub Models has rate limits but they're generous for personal use
- Generated content should be reviewed before posting to LinkedIn
- Respect LinkedIn's content policies and guidelines

## 🐛 Troubleshooting
GITHUB_TOKEN not found"
- Solution: Make sure you've created a `.env` file with your GitHub token

**Issue**: "ModuleNotFoundError"
- Solution: Install dependencies with `pip install -r requirements.txt`

**Issue**: "API rate limit exceeded"
- Solution: GitHub Models has rate limits. Wait a few minutes and try again

**Issue**: "Model not found"
- Solution: Check available models at https://github.com/marketplace/models and update MODEL_NAME in `.env`
- Solution: Check your OpenAI account usage and billing settings

## 📧 Support

For issues or questions, please check the code comments or modify the agent to suit your specific needs.

---

**Happy posting! 🎉**
