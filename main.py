from dotenv import load_dotenv

# Load API keys before importing agents
load_dotenv()

from workflow.graph import run_research


def main():
    print("=" * 60)
    print("          RESEARCHFLOW AI")
    print("  Multi-Agent Research & Reporting System")
    print("=" * 60)

    topic = input("\nEnter your research topic: ").strip()

    if not topic:
        print("Error: Please enter a research topic.")
        return

    try:
        print("\n[1] Starting multi-agent research workflow...")
        print("[2] Creating research plan...")
        print("[3] Collecting web evidence...")
        print("[4] Analyzing research...")
        print("[5] Generating research report...")
        print("[6] Checking factual accuracy...")
        print("[7] Reviewing report quality...")

        result = run_research(topic)

        print("\n" + "=" * 60)
        print("              RESEARCH PLAN")
        print("=" * 60)
        print(result["plan"])

        print("\n" + "=" * 60)
        print("             RESEARCH FINDINGS")
        print("=" * 60)
        print(result["research"]["summary"])

        print("\n" + "=" * 60)
        print("              ANALYSIS")
        print("=" * 60)
        print(result["analysis"])

        print("\n" + "=" * 60)
        print("              FINAL REPORT")
        print("=" * 60)
        print(result["report"])

        print("\n" + "=" * 60)
        print("              FACT CHECK")
        print("=" * 60)
        print(result["fact_check"])

        print("\n" + "=" * 60)
        print("              QUALITY REVIEW")
        print("=" * 60)
        print(result["review"])

        print("\nResearchFlow AI completed successfully!")

    except Exception as error:
        print(f"\nWorkflow failed: {error}")


if __name__ == "__main__":
    main()
      
