"""
Interactive CLI for LinkedIn Post Generator
"""
from linkedin_agent import LinkedInPostAgent
import sys


def print_banner():
    """Print the application banner""" # Displays app name and makes it look nice
    print("\n" + "=" * 80)
    print("🚀 AI LinkedIn Post Generator 🚀".center(80)) # it aligns text nicely
    print("=" * 80 + "\n") 


def get_user_input(prompt: str, default: str = None) -> str: # 
    """Get input from user with optional default value"""
    if default:
        user_input = input(f"{prompt} (default: {default}): ").strip()
        return user_input if user_input else default
    return input(f"{prompt}: ").strip()


def main():
    """Main CLI application"""
    print_banner()
    
    try:
        # Initialize the agent
        print("🔧 Initializing AI Agent...\n")
        agent = LinkedInPostAgent()
        
        while True: # Main loop to generate posts without restarting
            print("\n" + "-" * 80)
            print("📝 New LinkedIn Post Generation")
            print("-" * 80 + "\n")
            
            # Get topic from user
            topic = get_user_input("Enter the topic for your LinkedIn post")
            
            if not topic:
                print("❌ Topic cannot be empty. Please try again.") # Validate topic input
                continue
            
            # Get language from user
            print("\n🌍 Select language:")
            print("1. English")
            print("2. Spanish")
            print("3. Bengali")
            print("4. French")
            print("5. German")
            print("6. Other (custom)")
            
            language_choice = get_user_input("\nEnter your choice (1-6)", "1")
            
            language_map = {
                "1": "English",
                "2": "Spanish",
                "3": "Bengali",
                "4": "French",
                "5": "German"
            }
            
            if language_choice == "6":
                language = get_user_input("Enter the language name")
            else:
                language = language_map.get(language_choice, "English")
            
            # Ask if user wants hashtags
            include_hashtags = get_user_input("\n🏷️  Include hashtags? (y/n)", "y").lower()
            
            # Get number of hashtags if user wants them
            num_hashtags = 5
            if include_hashtags == 'y':
                num_hashtags = int(get_user_input("How many hashtags?", "5"))
            
            # Generate the post
            print(f"\n⏳ Generating LinkedIn post about '{topic}' in {language}...\n")
            
            try:
                # Use the unified generate_post method
                post = agent.generate_post(
                    topic=topic,
                    language=language,
                    include_hashtags=(include_hashtags == 'y'),
                    num_hashtags=num_hashtags
                )
                
                print("\n" + "=" * 80)
                print("✨ Generated LinkedIn Post:")
                print("=" * 80 + "\n")
                print(post)
                print("\n" + "=" * 80)
                
            except Exception as e:
                print(f"\n❌ Error generating post: {str(e)}")
            
            # Ask if user wants to generate another post
            continue_choice = get_user_input("\n🔄 Generate another post? (y/n)", "y").lower()
            
            if continue_choice != 'y':
                print("\n👋 Thank you for using AI LinkedIn Post Generator!")
                print("=" * 80 + "\n")
                break
                
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
