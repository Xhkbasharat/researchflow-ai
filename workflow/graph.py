
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.planner import create_research_plan
from agents.researcher import conduct_research
from agents.analyst import analyze_research
from agents.writer import generate_report
from agents.fact_checker import fact_check_report
from agents.critic import review_report


# Shared state for all agents
class ResearchState(TypedDict):
    topic: str
    plan: str
    research: dict
    analysis: str
    report: str
    fact_check: str
    review: str


# 1. Planner Agent
def planner_node(state: ResearchState):
    plan = create_research_plan(state["topic"])
    return {"plan": plan}


# 2. Research Agent
def researcher_node(state: ResearchState):
    research = conduct_research(
        state["topic"],
        state["plan"]
    )
    return {"research": research}


# 3. Analyst Agent
def analyst_node(state: ResearchState):
    analysis = analyze_research(
        state["topic"],
        state["research"]
    )
    return {"analysis": analysis}


# 4. Writer Agent
def writer_node(state: ResearchState):
    report = generate_report(
        state["topic"],
        state["research"],
        state["analysis"]
    )
    return {"report": report}


# 5. Fact-Checker Agent
def fact_checker_node(state: ResearchState):
    result = fact_check_report(
        state["report"],
        state["research"]
    )
    return {"fact_check": result}


# 6. Critic Agent
def critic_node(state: ResearchState):
    review = review_report(
        state["topic"],
        state["report"],
        state["fact_check"]
    )
    return {"review": review}


# Build LangGraph workflow
builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)
builder.add_node("researcher", researcher_node)
builder.add_node("analyst", analyst_node)
builder.add_node("writer", writer_node)
builder.add_node("fact_checker", fact_checker_node)
builder.add_node("critic", critic_node)


# Define execution sequence
builder.add_edge(START, "planner")
builder.add_edge("planner", "researcher")
builder.add_edge("researcher", "analyst")
builder.add_edge("analyst", "writer")
builder.add_edge("writer", "fact_checker")
builder.add_edge("fact_checker", "critic")
builder.add_edge("critic", END)


# Compile the workflow
researchflow = builder.compile()


def run_research(topic: str):
    """Execute the complete multi-agent workflow."""

    if not topic.strip():
        raise ValueError("Research topic cannot be empty.")

    initial_state = {
        "topic": topic,
        "plan": "",
        "research": {},
        "analysis": "",
        "report": "",
        "fact_check": "",
        "review": ""
    }

    return researchflow.invoke(initial_state)
  
