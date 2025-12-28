"""
Streamlit Web Interface for LinkedIn Post Generator
"""
import streamlit as st
from linkedin_agent import LinkedInPostAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Helper function to get configuration from either .env or Streamlit secrets
def get_config(key, default=None):
    """Get config from Streamlit secrets first, then .env, then default"""
    # Try Streamlit secrets first (for cloud deployment)
    if hasattr(st, 'secrets') and key in st.secrets:
        return st.secrets[key]
    # Fall back to environment variables (for local development)
    return os.getenv(key, default)

# Page configuration
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #0077B5;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .generated-post {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #0077B5;
        margin-top: 1rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #0077B5;
        color: white;
        font-weight: bold;
        padding: 0.5rem;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #005885;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🚀 LinkedIn Post Generator</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Create professional LinkedIn posts with AI - Powered by GitHub Models (FREE!)</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Check for GitHub token from either source
    github_token = get_config("GITHUB_TOKEN")
    if github_token:
        st.success("✅ GitHub Token configured")
    else:
        st.error("❌ GitHub Token not found!")
        st.info("""
        **For local development:** Set GITHUB_TOKEN in your .env file
        
        **For Streamlit Cloud:** Add secrets in app settings
        """)
        st.stop()
    
    st.markdown("---")
    
    # Model settings
    with st.expander("🤖 Model Settings"):
        model_name = st.selectbox(
            "Model",
            ["gpt-4o-mini", "gpt-4o", "Phi-3-medium-4k-instruct", "Phi-3-small-8k-instruct"],
            index=0
        )
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    
    st.markdown("---")
    st.markdown("### 📚 About")
    st.markdown("""
    This tool uses **LangChain** and **GitHub Models** to generate 
    professional LinkedIn posts in multiple languages.
    
    **Features:**
    - 🌍 Multi-language support
    - 🏷️ Optional hashtags
    - 🆓 Completely FREE
    - ⚡ Powered by GPT-4
    """)

# Initialize session state
if 'agent' not in st.session_state:
    try:
        # Temporarily set environment variable for LinkedInPostAgent
        os.environ['GITHUB_TOKEN'] = github_token
        st.session_state.agent = LinkedInPostAgent(model_name=model_name, temperature=temperature)
    except Exception as e:
        st.error(f"Error initializing agent: {str(e)}")
        st.stop()

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input(
        "📝 Post Topic",
        placeholder="e.g., AI in Healthcare, Remote Work Productivity",
        help="Enter the main topic for your LinkedIn post"
    )

with col2:
    language = st.selectbox(
        "🌍 Language",
        ["English", "Spanish", "Bengali", "French", "German", "Hindi", "Portuguese", "Chinese"],
        index=0
    )

# Hashtag options
col3, col4 = st.columns([1, 1])

with col3:
    include_hashtags = st.checkbox("🏷️ Include Hashtags", value=True)

with col4:
    if include_hashtags:
        num_hashtags = st.number_input("Number of Hashtags", min_value=1, max_value=10, value=5)
    else:
        num_hashtags = 5

# Generate button
st.markdown("---")
generate_button = st.button("✨ Generate LinkedIn Post", use_container_width=True)

# Generation logic
if generate_button:
    if not topic:
        st.warning("⚠️ Please enter a topic first!")
    else:
        with st.spinner(f"🤖 Generating post about '{topic}' in {language}..."):
            try:
                # Generate the post
                post = st.session_state.agent.generate_post(
                    topic=topic,
                    language=language,
                    include_hashtags=include_hashtags,
                    num_hashtags=num_hashtags
                )
                
                # Display the post
                st.markdown("---")
                st.markdown("### ✨ Generated LinkedIn Post")
                st.markdown(f'<div class="generated-post">{post}</div>', unsafe_allow_html=True)
                
                # Copy button
                st.text_area(
                    "Copy the post below:",
                    post,
                    height=200,
                    help="Select all and copy to your clipboard"
                )
                
                st.success("✅ Post generated successfully!")
                
                # Download button
                st.download_button(
                    label="📥 Download as Text File",
                    data=post,
                    file_name=f"linkedin_post_{topic.replace(' ', '_')}.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"❌ Error generating post: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9rem;'>
    Made with ❤️ using LangChain & GitHub Models | 
    <a href='https://github.com' target='_blank'>View on GitHub</a>
</div>
""", unsafe_allow_html=True)
