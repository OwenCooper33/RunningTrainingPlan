import os
def round_to_half(x):
    return round(x * 2) / 2

def generate_training_plan(starting_mileage, goal_distance, weeks, taper_weeks=3):
    plan = []
    weekly_mileage = starting_mileage
    taper_start = weeks - taper_weeks


    for week in range(1, weeks + 1):
        # Apply taper for the last `taper_weeks` weeks
        # Apply taper for the last `taper_weeks` weeks
        if week > taper_start:
            weekly_mileage *= 0.8  # Reduce mileage by 20% each taper week
        elif weekly_mileage < goal_distance:
            weekly_mileage *= 1.10  # Increase by 10% each week until taper
            if weekly_mileage > goal_distance:
                weekly_mileage = goal_distance # Increase by 10% each week until taper

        long_run = weekly_mileage * 0.4    # Long run is 40% of weekly mileage
        tempo_run = weekly_mileage * 0.2   # Tempo run is 20% of weekly mileage
        easy_runs_total = weekly_mileage - (long_run + tempo_run)
        easy_run = easy_runs_total / 3     #
        # Add the weekly plan, rounding to the nearest 0.5
        plan.append({
            "week": week,
            "weekly_mileage": round_to_half(weekly_mileage),
            "long_run": round_to_half(long_run),
            "tempo_run": round_to_half(tempo_run),
            "easy_runs": [round_to_half(easy_run)] * 3
        })

    return plan


def save_plan_to_file(plan, filename="training_plan.txt"):
    with open(filename, "w") as file:
        for week_plan in plan:
            file.write(f"Week {week_plan['week']}, {week_plan['weekly_mileage']} miles:\n")
            file.write(f"  Long run: {week_plan['long_run']} miles\n")
            file.write(f"  Tempo run: {week_plan['tempo_run']} miles\n")
            file.write(f"  Easy runs: {week_plan['easy_runs'][0]} miles each\n\n")
    print(f"Training plan saved to {filename}")


def main():

    starting_mileage = float(input("Enter starting weekly mileage (in miles): "))
    goal_distance = float(input("Enter goal distance (in miles): "))
    weeks = int(input("Enter the number of weeks for the training plan: "))

    training_plan = generate_training_plan(starting_mileage, goal_distance, weeks)
    save_plan_to_file(training_plan)


if __name__ == "__main__":
    main()
