
from dotenv import load_dotenv
from workflow.supervisor import researchflow

load_dotenv()


def main():
    print("=" * 50)
    print("       RESEARCHFLOW AI")
    print(" Multi-Agent Research System")
    print("=" * 50)

    topic = input("\nEnter your research topic: ")

    if not topic.strip():
        print("Please enter a valid research topic.")
        return

    print("\nStarting ResearchFlow AI...")
    print("Running Research, Analysis, Writing and Fact-Checking Agents.")

    result = researchflow.invoke({
        "topic": topic,
        "source_text": "",
        "research": "",
        "analysis": "",
        "report": "",
        "fact_check": ""
    })

    print("\n========== RESEARCH ==========")
    print(result["research"])

    print("\n========== ANALYSIS ==========")
    print(result["analysis"])

    print("\n========== FINAL REPORT ==========")
    print(result["report"])

    print("\n========== FACT CHECK ==========")
    print(result["fact_check"])


if __name__ == "__main__":
    main()
  
