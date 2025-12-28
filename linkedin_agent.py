"""
LinkedIn Post Generator AI Agent using LangChain with GitHub Models
"""
import os
from typing import Optional
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# GitHub Models endpoint
GITHUB_MODELS_ENDPOINT = "https://models.inference.ai.azure.com"


class LinkedInPostAgent:
    """AI Agent for generating professional LinkedIn posts using GitHub Models"""
    
    def __init__(self, model_name: Optional[str] = None, temperature: Optional[float] = None):
        """
        Initialize the LinkedIn Post Generator Agent
        
        Args:
            model_name: GitHub model to use (default: gpt-4o-mini)
            temperature: Temperature for generation (default: 0.7)
        """
        self.model_name = model_name or os.getenv("MODEL_NAME", "gpt-4o-mini")
        self.temperature = temperature or float(os.getenv("TEMPERATURE", "0.7"))
        
        # Get GitHub token
        github_token = os.getenv("GITHUB_TOKEN")
        if not github_token:
            raise ValueError(
                "GITHUB_TOKEN not found in environment variables. "
                "Please set your GitHub Personal Access Token in the .env file."
            )
        
        # Initialize the LLM with GitHub Models
        self.llm = ChatOpenAI(
            model=self.model_name,
            temperature=self.temperature,
            api_key=github_token,
            base_url=GITHUB_MODELS_ENDPOINT
        )
        
# Create the prompt template for posts WITHOUT hashtags
        self.prompt_template = PromptTemplate(
            input_variables=["topic", "language"],
            template="""You are a professional LinkedIn content creator. Your task is to create an engaging, 
            professional LinkedIn post on the given topic in the specified language.

            The post should:
            - Be 2-4 paragraphs long
            - Include relevant insights or perspectives
            - Use a professional yet approachable tone
            - Include emojis where appropriate (but not excessive)
            - Be engaging and likely to generate discussion
            - Follow LinkedIn best practices
            - Be written entirely in {language}
            - DO NOT include hashtags at the end (they will be added separately if needed)

            Topic: {topic}
            Language: {language}

            Generate a professional LinkedIn post WITHOUT hashtags:"""
        )
        
        # Create the chain using LCEL
        self.chain = self.prompt_template | self.llm | StrOutputParser()
    
    def generate_post(self, topic: str, language: str = "English", include_hashtags: bool = True, num_hashtags: int = 5) -> str:
        """
        Generate a LinkedIn post based on the given topic and language
        
        Args:
            topic: The topic for the LinkedIn post
            language: The language for the post (default: English)
            include_hashtags: Whether to include hashtags (default: True)
            num_hashtags: Number of hashtags if included (default: 5)
            
        Returns:
            Generated LinkedIn post as a string
        """
        try:
            # Generate the main post
            result = self.chain.invoke({"topic": topic, "language": language})
            post = result.strip()
            
            # Add separate hashtags if requested
            if include_hashtags:
                hashtag_prompt = PromptTemplate(
                    input_variables=["topic", "num_hashtags"],
                    template="""Generate {num_hashtags} relevant hashtags for a LinkedIn post about: {topic}

                    Return only the hashtags separated by spaces, each starting with #.
                    Example: #AI #Technology #Innovation

                    Hashtags:"""
                )
                hashtag_chain = hashtag_prompt | self.llm | StrOutputParser()
                hashtags = hashtag_chain.invoke({"topic": topic, "num_hashtags": num_hashtags}).strip()
                
                # Combine post and hashtags
                return f"{post}\n\n{hashtags}"
            
            return post
        except Exception as e:
            raise Exception(f"Error generating post: {str(e)}")
def main():
    """Example usage of the LinkedIn Post Agent"""
    # Create an instance of the agent
    agent = LinkedInPostAgent()
    
    print("=" * 80)
    print("Example 1: AI in Healthcare")
    print("=" * 80)
    post1 = agent.generate_post(
        topic="AI in Healthcare",
        language="English"
    )
    print(post1)
    print("\n")
    
    print("=" * 80)
    print("Example 2: Remote Work Productivity")
    print("=" * 80)
    post2 = agent.generate_post(
        topic="Remote Work Productivity",
        language="English"
    )
    print(post2)
    print("\n")


if __name__ == "__main__":
    main()
