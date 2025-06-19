def collect_feedback(response):
    print("\nWas this response helpful? (y/n): ")
    feedback = input().strip().lower()
    return feedback == 'y'
