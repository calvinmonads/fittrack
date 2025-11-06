import pandas as pd

# Create an empty DataFrame to store workouts
columns = ["Muscle Group", "Set #", "Movement", "Reps", "Equipment", "Weight", "Notes"]
workouts = pd.DataFrame(columns=columns)

print("🏋️ Welcome to FitTrack!")
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

print("\n✅ Workout complete!")
print(workouts)

# Save to CSV
workouts.to_csv("fittrack_log.csv", index=False)
print("\n💾 Saved to fittrack_log.csv")
