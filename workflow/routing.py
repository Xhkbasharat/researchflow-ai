from typing import Literal


def route_after_review(
    review: str,
    revision_count: int,
    max_revisions: int = 2
) -> Literal["approved", "revise", "rejected"]:
    """
    Decide the next workflow step using critic feedback.
    """

    if not review or not review.strip():
        return "rejected"

    decision = review.upper()

    if "NEEDS REVISION" in decision:
        if revision_count < max_revisions:
            return "revise"
        return "rejected"

    if "REJECTED" in decision:
        return "rejected"

    if "APPROVED" in decision:
        return "approved"

    return "rejected"


if __name__ == "__main__":

    result = route_after_review(
        review="APPROVED - Report quality is satisfactory.",
        revision_count=0
    )

    print("Supervisor decision:", result)
  
