# core/state.py
from pydantic import BaseModel

class LayoutState(BaseModel):
    user_prompt: str
    layout_response: str | None = None
