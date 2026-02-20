from ats_detection.detector import detect_ats
from apply.greenhouse import apply_greenhouse
from apply.lever import apply_lever
from apply.generic_form import apply_generic


def route_apply(job):
    url = job["url"]

    ats = detect_ats(url)

    print("Detected ATS:", ats)

    if ats == "greenhouse":
        return apply_greenhouse(job)

    if ats == "lever":
        return apply_lever(job)

    return apply_generic(job)