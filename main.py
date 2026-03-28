import random

class StudyPlanner:

    def __init__(self):
        # subjects with priority and time needed
        self.subjects = {
            "maths": {"priority": 2, "time": 45},
            "science": {"priority": 3, "time": 30},
            "english": {"priority": 1, "time": 15},
            "history": {"priority": 2, "time": 30}
        }

        # memory to track past performance
        self.history = {sub: 0 for sub in self.subjects}

    def choose_subject(self, energy, last_subject):
        best_subject = None
        best_score = -999
        reason = ""

        for sub, data in self.subjects.items():

            # base score from priority
            score = data["priority"] * 3

            # energy effect
            if energy < 40:
                score -= 4
                energy_reason = "low energy"
            else:
                energy_reason = "energy ok"

            # repeat penalty (strong)
            score -= self.history[sub] * 2

            # avoid same subject again
            if sub == last_subject:
                score -= 5

            # store best
            if score > best_score:
                best_score = score
                best_subject = sub
                reason = f"{energy_reason}, priority={data['priority']}, history={self.history[sub]}"

        return best_subject, best_score, reason

    def run(self):
        energy = int(input("Enter your energy (1-100): "))
        time_available = int(input("Enter time (minutes): "))

        print("\n--- Study Planner Started ---\n")

        plan = []
        last_subject = None
        total_score = 0

        while time_available > 0:
            subject, score, reason = self.choose_subject(energy, last_subject)

            subject_time = self.subjects[subject]["time"]

            if time_available < subject_time:
                break

            print(f"Selected: {subject} | Score: {score}")
            print(f"Reason: {reason}\n")

            plan.append((subject, subject_time))
            time_available -= subject_time
            total_score += score

            # update memory
            self.history[subject] += 1
            last_subject = subject

            # energy reduces over time
            energy -= 5
            if energy < 0:
                energy = 0

        print("\n--- Final Study Plan ---")
        for sub, t in plan:
            print(f"{sub} -> {t} mins")

        print("\nTotal Score:", total_score)

        print("\n--- Performance Memory ---")
        for sub, val in self.history.items():
            print(sub, ":", val)

        # suggestion
        weakest = min(self.history, key=self.history.get)
        print("\nFocus more on:", weakest)

        print("\nSystem avoids repetition to maintain balance.")
        print("This system helps students make better study decisions based on their condition.")

        print("\n--- System Ended ---")
        print("study smart, not hard")


# run
planner = StudyPlanner()
planner.run()
