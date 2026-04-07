def predict(subject, hours_per_day, days, weak_topic=""):
    try:
        # Clean inputs
        subject = str(subject).strip().capitalize()
        hours_per_day = float(hours_per_day)
        days = int(days)
        weak_topic = str(weak_topic).strip()

        # Basic validation
        if not subject:
            return "Error: Please enter a subject"
        if hours_per_day <= 0 or days <= 0:
            return "Error: Hours and days must be greater than 0"

        # Plan generation
        plan = f"Study Plan for {subject}\n\n"

        for i in range(1, days + 1):
            plan += f"Day {i}: {subject} ({hours_per_day} hrs)\n"

        # Weak topic focus
        if weak_topic:
            plan += f"\nFocus more on: {weak_topic}"

        return plan

    except Exception as e:
        return f"Error: {str(e)}"
