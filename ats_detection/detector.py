def detect_ats(url: str):
    url = url.lower()

    if "greenhouse" in url:
        return "greenhouse"

    if "lever.co" in url:
        return "lever"

    if "ashbyhq" in url:
        return "ashby"

    return "generic"