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

if __name__ == "__main__":
    log_workout()
