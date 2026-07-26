def generate_learning_plan(missing_skills):

    plan = []

    week = 1

    for skill in missing_skills:

        plan.append(
            {
                "week": week,
                "learn": skill
            }
        )

        week += 1

    return plan