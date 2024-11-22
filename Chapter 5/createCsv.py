import pandas as pd

# Data
data = {
    'Area (sqft)': [2000, 1500, 3000, 1800, 2500, 1200, 2700, 3200],
    'Bedrooms': [3, 2, 4, 3, 4, 2, 4, 5],
    'Bathrooms': [2, 1, 3, 2, 3, 1, 3, 4],
    'Location': ['Downtown', 'Suburbs', 'Uptown', 'Downtown', 'Uptown', 'Suburbs', 'Uptown', 'Downtown'],
    'Price ($)': [250000, 150000, 400000, 200000, 300000, 120000, 350000, 450000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_file = 'house_data.csv'
df.to_csv(csv_file, index=True)

print(f"CSV file '{csv_file}' has been created successfully.")

