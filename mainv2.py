import pandas as pd
import os

# File name for saved workouts
file_name = "fittrack_log.csv"

# Check if the file already exists — if it does, load it
if os.path.exists(file_name):
    workouts = pd.read_csv(file_name)
    print(f"📂 Loaded existing log with {len(workouts)} entries.")
else:
    # If not, start a new DataFrame
    columns = ["Muscle Group", "Set #", "Movement", "Reps", "Equipment", "Weight", "Notes"]
    workouts = pd.DataFrame(columns=columns)
    print("🆕 No existing log found. Starting a new one.")

print("\n🏋️ Welcome to FitTrack!")
print("Type 'q' anytime to finish logging.\n")

while True:
    muscle = input("Enter muscle group (or 'q' to quit): ").strip()
    if muscle.lower() == 'q':
        break

    set_number = 1
    while True:
        print(f"\n--- {muscle.upper()} | Set {set_number} ---")
        movement = input("Movement: ")
        if movement.lower() == 'q':
            break
        reps = input("Reps: ")
        equipment = input("Equipment: ")
        weight = input("Weight (kg): ")
        notes = input("Notes: ")

        workouts.loc[len(workouts)] = [muscle, set_number, movement, reps, equipment, weight, notes]
        set_number += 1

        add_more = input("\nAdd another set for this muscle group? (y/n): ").strip().lower()
        if add_more != 'y':
            break

# Save (append mode)
w
