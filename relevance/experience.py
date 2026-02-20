import re

def extract_years(text: str):
    text = text.lower()

    # patterns like "2+ years", "1-2 years", "0-1 year"
    patterns = [
        r'(\d+)\+?\s*years',
        r'(\d+)\s*-\s*(\d+)\s*years'
    ]

    for p in patterns:
        m = re.search(p, text)
        if m:
            nums = [int(x) for x in m.groups() if x]
            return max(nums)

    return None


def is_junior(job):
    years = extract_years(job.get("description", ""))

    if years is None:
        return True  

    return years <= 2