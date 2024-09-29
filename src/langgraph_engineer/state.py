from langgraph.graph import MessagesState
from typing import TypedDict, Literal
class AgentState(MessagesState):
    requirements: str
    code: str
    accepted: bool


class OutputState(TypedDict):
    code: str


class GraphConfig(TypedDict):
    gather_model: Literal['o1-mini', 'o1-preview','gpt-4o']
    draft_model: Literal['o1-mini', 'o1-preview','gpt-4o']
    critique_model: Literal['o1-mini', 'o1-preview','gpt-4o']
