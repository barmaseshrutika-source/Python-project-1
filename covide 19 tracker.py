import pandas as pd
import matplotlib.pyplot as plt

# Create COVID dataset manually
data = {
    "Country": ["USA", "India", "Brazil", "Russia", "UK", "France", "Italy"],
    "TotalCases": [1000000, 900000, 850000, 600000, 550000, 500000, 480000]
}

# Convert into DataFrame
df = pd.DataFrame(data)

print("----- COVID-19 Dataset -----\n")
print(df)

# Sort and get Top 5 countries
top5 = df.sort_values(by="TotalCases", ascending=False).head(5)

print("\nTop 5 Countries by Total Cases:\n")
print(top5)

# Plot Bar Chart
plt.figure()
plt.bar(top5["Country"], top5["TotalCases"])
plt.title("Top 5 Countries by COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.show()