# Quick Setup Guide for GitHub Models

## Step 1: Get Your GitHub Token

1. Go to https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Give it a name like "LinkedIn Post Generator"
4. **No scopes needed** for GitHub Models
5. Click **"Generate token"**
6. **Copy the token immediately** (you won't see it again!)

## Step 2: Configure Environment

1. Copy the example file:
   ```bash
   copy .env.example .env
   ```

2. Edit `.env` and paste your token:
   ```
   GITHUB_TOKEN=ghp_YOUR_TOKEN_HERE
   MODEL_NAME=gpt-4o-mini
   TEMPERATURE=0.7
   ```

## Step 3: Run the Application

```bash
python main.py
```

## Available Free Models

- **gpt-4o-mini** (recommended) - Fast and efficient
- **gpt-4o** - Most capable
- **Phi-3-medium-4k-instruct** - Microsoft's model
- **Phi-3-small-8k-instruct** - Smaller variant

To use a different model, update `MODEL_NAME` in `.env`

## Troubleshooting

**Error: "GITHUB_TOKEN not found"**
- Make sure you created `.env` file (not `.env.example`)
- Check that your token is correctly pasted in `.env`

**Error: "Module not found"**
- Run: `pip install -r requirements.txt`

**Rate Limit**
- GitHub Models has generous limits for personal use
- Wait a few minutes if you hit the limit

## Testing

To test if everything works:
```bash
python linkedin_agent.py
```

This will run two example generations to verify the setup.
