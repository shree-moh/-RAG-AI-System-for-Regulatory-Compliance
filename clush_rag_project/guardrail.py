def apply_guardrail(response):
    risky_phrases = ["ignore the law", "bypass", "fake"]
    for phrase in risky_phrases:
        if phrase in response.lower():
            return "[REDACTED: Potential non-compliance detected]"
    return response
