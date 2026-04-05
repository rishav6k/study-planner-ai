from app import generate_plan

def predict(subject, hours_per_day, days, weak_topic=""):
    return generate_plan(subject, hours_per_day, days, weak_topic)
