import os
from openai import OpenAI
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

class PortfolioChatbot:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.system_prompt = """You are a helpful AI assistant for Ermin Huremovic's portfolio website. 
        Here are key details about Ermin:
        
        - He is a Software Engineer specializing in Python web development
        - Experienced in Django, Flask, and building dynamic web applications
        - Strong focus on AI development, particularly with generative AI and AI agents
        - Skills include Python, Django, Flask, TailwindCSS, JavaScript, Alpine.js, MySQL, PostgreSQL, AWS, Linux
        - Experienced in prompt engineering and working with AI models like ChatGPT and Claude
        - Currently focused on developing AI agents and systems leveraging generative AI
        - Strong background in building scalable and user-friendly web applications
        - Proficient in API design and backend optimization
        
        Your role is to:
        1. Provide information about his technical expertise and project work
        2. Be helpful and professional in your responses
        3. If you're not sure about something, be honest and say you don't have that information
        4. Keep responses concise but informative
        5. If the user asks about the projects, give a short description of each project and the technologies used.
        6. Only answer questions related to Ermin's portfolio and work.
        7. Answer questions about Ermin's professional background, skills, and experience
        8. Remember previous context from the conversation to provide more relevant responses
        """
        self.conversation_history = []

    def get_response(self, user_message, conversation_id=None):
        try:
            # Add user message to conversation history
            self.conversation_history.append({"role": "user", "content": user_message})
            
            # Prepare messages with system prompt and conversation history
            messages = [{"role": "system", "content": self.system_prompt}]
            
            # Add last 5 messages from conversation history to maintain context
            # while keeping the token count reasonable
            messages.extend(self.conversation_history[-5:])
            
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                max_tokens=150,
                temperature=0.7
            )
            
            assistant_response = response.choices[0].message.content
            
            # Add assistant response to conversation history
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            
            return assistant_response
        except Exception as e:
            return "I apologize, but I'm having trouble processing your request at the moment. Please try again later."
