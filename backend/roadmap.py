from careers import CAREER_ROADMAPS


def generate_roadmap(goal):

    goal = goal.strip()

    return CAREER_ROADMAPS.get(
        goal,
        "No roadmap available for this role"
    )