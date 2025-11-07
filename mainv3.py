import pandas as pd
from datetime import datetime

def log_workout():
    workout_data = []
    print("🏋️ FITTRACK – Log Your Workout\n")

    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    notes = input("General notes for this session (optional): ")

    while True:
        muscle_group = input("\nEnter muscle group (or 'done' to finish): ").strip()
        if muscle_group.lower() == "done":
            break

        set_count = 1
        while True:
            print(f"\n--- {muscle_group} | Set {set_count} ---")
            movement = input("Movement: ")
            reps = input("Reps: ")
            weight = input("Weight: ")
            equipment = input("Equipment: ")
            set_notes = input("Notes for this set (optional): ")

            workout_data.append({
                "Date": date,
                "Muscle Group": muscle_group,
                "Set #": set_count,
                "Movement": movement,
                "Reps": reps,
                "Weight": weight,
                "Equipment": equipment,
                "Set Notes": set_notes,
                "Session Notes": notes
            })

            add_another_set = input("Add another set for this muscle group? (y/n): ").strip().lower()
            if add_another_set != "y":
                break
            set_count += 1

    if workout_data:
        df = pd.DataFrame(workout_data)
        try:
            existing = pd.read_csv("workout_log.csv")
            df = pd.concat([existing, df], ignore_index=True)
        except FileNotFoundError:
            pass

        df.to_csv("workout_log.csv", index=False)
        print("\n✅ Workout saved successfully!")
    else:
        print("No data entered. Nothing saved.")

import matplotlib.pyplot as plt

def analytics():
    """Display a simple analytics summary and bar chart."""
    try:
        df = pd.read_csv("workout_log.csv")
    except FileNotFoundError:
        print("⚠️ No workout log found yet! Run a workout first.")
        return

    if df.empty:
        print("⚠️ Log file is empty.")
        return

    # Group by muscle group and count sets
    summary = df.groupby("Muscle Group")["Set #"].count().reset_index()
    summary.rename(columns={"Set #": "Total Sets"}, inplace=True)

    print("\n📊 Workout Summary (Sets per Muscle Group):")
    print(summary)

    # Plot bar chart
    plt.figure(figsize=(8, 5))
    plt.bar(summary["Muscle Group"], summary["Total Sets"])
    plt.title("Total Sets per Muscle Group")
    plt.xlabel("Muscle Group")
    plt.ylabel("Total Sets")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    log_workout()
    see_analytics = input("\nWould you like to see analytics now? (y/n): ").strip().lower()
    if see_analytics == "y":
        analytics()
    else:
        print("👋 See you next time!")
