import pandas as pd

# Create Employee Data
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Arjun", "Kavya", "Rohan"],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance"],
    "Salary": [60000, 45000, 75000, 50000, 90000, 40000, 65000],
    "Age": [25, 28, 30, 26, 35, 24, 29]
}

# Convert into DataFrame
df = pd.DataFrame(data)

print("----- Employee Data -----\n")
print(df)

# Calculate Average Salary
average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)

# Count Employees by Department
department_count = df["Department"].value_counts()
print("\nEmployee Count by Department:\n")
print(department_count)

# Filter Employees with Salary > 60000
high_salary = df[df["Salary"] > 60000]
print("\nEmployees with Salary > 60000:\n")
print(high_salary)
