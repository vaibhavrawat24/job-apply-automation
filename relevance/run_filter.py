from relevance.filter import is_relevant
from relevance.experience import is_junior
from relevance.stack import has_stack


def run(jobs):
    final = []

    for j in jobs:

        # 1 title
        if not is_relevant(j):
            continue

        # 2 experience
        if not is_junior(j):
            continue

        # 3 stack
        if not has_stack(j):
            continue

        final.append(j)

    return final