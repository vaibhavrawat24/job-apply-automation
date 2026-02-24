import re

def extract_years(text: str):
    text = text.lower()

    patterns = [
        r'(\d+)\s*-\s*(\d+)\s*years?',     
        r'(\d+)\s*years?'                
    ]

    matches = []

    for p in patterns:
        for m in re.finditer(p, text):
            nums = [int(x) for x in m.groups() if x]
            if nums:
                matches.append(min(nums))  

    if not matches:
        return None

    return min(matches)

JUNIOR_HINTS = ["new grad", "entry level", "intern", "graduate", "fresher"]

def is_junior(job):
    desc = job.get("description", "").lower()

    if any(k in desc for k in JUNIOR_HINTS):
        return True

    years = extract_years(desc)

    if years is None:
        return True

    return years <= 2