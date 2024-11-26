import matplotlib.pyplot as plt
import pandas as pd

# Sample data for Primary and Secondary lifts for Squat, Bench, and Deadlift over 5 weeks
data = {
    "Week": [1, 2, 3, 4, 5],
    "Squat Primary": [120, 130, 140, 150, 160],  # Primary Squat lifts
    "Squat Secondary": [110, 120, 125, 130, 135],  # Secondary Squat lifts
    "Bench Primary": [80, 85, 90, 95, 100],  # Primary Bench lifts
    "Bench Secondary": [70, 75, 80, 85, 90],  # Secondary Bench lifts
    "Deadlift Primary": [180, 190, 200, 210, 220],  # Primary Deadlift lifts
    "Deadlift Secondary": [160, 170, 180, 190, 200]  # Secondary Deadlift lifts
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Create a plot
plt.figure(figsize=(12, 8))

# Plot Primary and Secondary Squat Lifts (Red for Primary, Green for Secondary)
plt.plot(df["Week"], df["Squat Primary"], color="red", label="Squat Primary", marker='o')
plt.plot(df["Week"], df["Squat Secondary"], color="green", label="Squat Secondary", marker='o')

# Plot Primary and Secondary Bench Lifts (Red for Primary, Green for Secondary)
plt.plot(df["Week"], df["Bench Primary"], color="red", label="Bench Primary", marker='o')
plt.plot(df["Week"], df["Bench Secondary"], color="green", label="Bench Secondary", marker='o')

# Plot Primary and Secondary Deadlift Lifts (Red for Primary, Green for Secondary)
plt.plot(df["Week"], df["Deadlift Primary"], color="red", label="Deadlift Primary", marker='o')
plt.plot(df["Week"], df["Deadlift Secondary"], color="green", label="Deadlift Secondary", marker='o')

# Add labels and title
plt.xlabel('Week')
plt.ylabel('Lift Weight (kg)')
plt.title('Primary vs Secondary Lifts: Squat, Bench, Deadlift over Weeks')

# Add a legend
plt.legend()

# Display the plot with a grid
plt.grid(True)
plt.tight_layout()
plt.show()
