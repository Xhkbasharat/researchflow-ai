
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.research_agent import research_topic
from agents.analyst_agent import analyze_research
from agents.writer_agent import generate_report
from agents.fact_checker import fact_check_report


# Shared data passed between agents
class ResearchState(TypedDict):
    topic: str
    source_text: str
    research: str
    analysis: str
    report: str
    fact_check: str


# Agent 1: Research
def research_node(state: ResearchState):
    result = research_topic(
        state["topic"],
        state["source_text"]
    )

    return {"research": result}


# Agent 2: Analysis
def analyst_node(state: ResearchState):
    result = analyze_research(state["research"])

    return {"analysis": result}


# Agent 3: Report writing
def writer_node(state: ResearchState):
    result = generate_report(
        state["research"],
        state["analysis"]
    )

    return {"report": result}


# Agent 4: Fact checking
def fact_checker_node(state: ResearchState):
    result = fact_check_report(
        state["report"],
        state["source_text"]
    )

    return {"fact_check": result}


# Build the workflow
workflow = StateGraph(ResearchState)

workflow.add_node("researcher", research_node)
workflow.add_node("analyst", analyst_node)
workflow.add_node("writer", writer_node)
workflow.add_node("fact_checker", fact_checker_node)

# Define execution order
workflow.add_edge(START, "researcher")
workflow.add_edge("researcher", "analyst")
workflow.add_edge("analyst", "writer")
workflow.add_edge("writer", "fact_checker")
workflow.add_edge("fact_checker", END)

# Compile the workflow
researchflow = workflow.compile()


# Run the complete system
if __name__ == "__main__":

    result = researchflow.invoke({
        "topic": "Artificial Intelligence in Education",
        "source_text": """
        AI is used in education for personalized
        learning, automated assessment, and
        student support.
        """,
        "research": "",
        "analysis": "",
        "report": "",
        "fact_check": ""
    })

    print("\n===== RESEARCH =====")
    print(result["research"])

    print("\n===== ANALYSIS =====")
    print(result["analysis"])

    print("\n===== FINAL REPORT =====")
    print(result["report"])

    print("\n===== FACT CHECK =====")
    print(result["fact_check"])
  
