def predict(subject, hours_per_day, days, weak_topic=""):
    try:
        subject = str(subject).strip().capitalize()
        hours_per_day = float(hours_per_day)
        days = int(days)
        weak_topic = str(weak_topic).strip()

        if not subject:
            return "Error: Please enter a subject"

        if hours_per_day <= 0 or days <= 0:
            return "Error: Invalid input values"

        plan = f"Study Plan for {subject}\n\n"

        topics = [subject]
        if weak_topic:
            topics = [weak_topic + " (Focus)", subject]

        for i in range(days):
            topic = topics[i % len(topics)]
            plan += f"Day {i+1}: {topic} ({hours_per_day} hrs)\n"

        return plan

    except Exception as e:
        return f"Error: {str(e)}"
