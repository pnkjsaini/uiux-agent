# agents/layout_agent.py

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv


class LayoutAgent:
    def __init__(self):
        self.prompt_template = ChatPromptTemplate.from_messages([
            SystemMessage(content="You are a UI/UX expert who suggests high-quality layout ideas."),
            HumanMessage(content="{user_prompt}")
        ])
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",api_key = os.getenv("GEMINI_API_KEY"))

    def generate_layout(self, prompt: str) -> str:
        chain = self.prompt_template | self.llm
        return chain.invoke({"user_prompt": prompt}).content

    def handle_state(self, state: dict) -> dict:
        user_prompt = state.user_prompt
        layout_response = self.generate_layout(user_prompt)
        return {
            "user_prompt": user_prompt,
            "layout_response": layout_response
        }
