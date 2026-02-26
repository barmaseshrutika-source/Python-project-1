import pandas as pd
import smtplib
import os

# Check if file exists
if not os.path.exists("students.csv"):
    print("Error: students.csv file not found!")
    exit()

# Read CSV file
df = pd.read_csv("students.csv")

# Your Gmail credentials
sender_email = "your_email@gmail.com"
app_password = "your_app_password"   # Use Gmail App Password

# Connect to Gmail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender_email, app_password)
    print("Login Successful!\n")

    for index, row in df.iterrows():
        name = row["Name"]
        receiver_email = row["Email"]

        subject = "Internship Update"
        message = f"""Hello {name},

Congratulations! You have been shortlisted.

Regards,
HR Team
"""

        full_email = f"Subject: {subject}\n\n{message}"

        server.sendmail(sender_email, receiver_email, full_email)
        print(f"Email sent to {name}")

    print("\nAll emails sent successfully!")

except Exception as e:
    print("Error:", e)

finally:
    server.quit()