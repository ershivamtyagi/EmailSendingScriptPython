import smtplib
import pymysql
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

# Database connection parameters
db_host = "your_mysql_host"
db_user = "your_mysql_user"
db_password = "your_mysql_password"
db_name = "your_database_name"

# Connect to the database
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
cursor = connection.cursor()

# Get today's date
current_date = datetime.now().date()

# Query to fetch users and their questions based on the criteria
query = """
SELECT u.id, u.email, u.preferredLanguage, q.day_id, q.question, q.intuition, q.brute_force, q.complexitybf, q.better1, q.complexity_b, q.optimal, q.complexity_o
FROM user u
JOIN daily_questions q ON DATEDIFF(%s, u.creationDate) = q.dayid
"""

# Execute the query
cursor.execute(query, (current_date,))

# Fetch the results
results = cursor.fetchall()

# Close database connection
connection.close()

# Email configuration
email_host = "your_smtp_host"
email_port = 587
email_user = "your_email_address"
email_password = "your_email_password"

# Iterate through the results and send emails
for row in results:
    user_id, email, preferred_language, day_id, question, intuition, brute_force, complexitybf, better1, complexity_b, optimal, complexity_o = row

    # Compose the email subject and body based on user preferences with embedded CSS styles
    subject = f"Daily Question - Day {day_id}"
    username = email.split('@')[0]  # Extracting username from email address

    body = f"""
        <html>
            <head>
                <style>
                    /* Add your CSS styles here */
                    body {{
                        font-family: 'Arial', sans-serif;
                        color: #333;
                    }}
                    .question {{
                        font-weight: bold;
                        font-size: 16px;
                    }}
                    .solution {{
                        margin-left: 20px;
                    }}
                </style>
            </head>
            <body>
                <p>Hello {username},</p>
                <p class="question">Here is your daily question (Day {day_id}):</p>
                <p>{question}</p>
    """

    if preferred_language.lower() == "true":  # If the user wants to get answers
        body += f"""
                <p>Intuition: {intuition}</p>
                <div class="solution">
                    <p>Solution 1 (Brute Force):</p>
                    <p>{brute_force}</p>
                    <p>Complexity: {complexitybf}</p>
                </div>
        """
        if better1:
            body += f"""
                <div class="solution">
                    <p>Solution 2 (Better):</p>
                    <p>{better1}</p>
                    <p>Complexity: {complexity_b}</p>
                </div>
            """
        body += f"""
                <div class="solution">
                    <p>Optimal Solution:</p>
                    <p>{optimal}</p>
                    <p>Complexity: {complexity_o}</p>
                </div>
            """

    body += """
            </body>
        </html>
    """

    # Set up the email
    message = MIMEMultipart()
    message['From'] = email_user
    message['To'] = email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'html'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(email_host, email_port) as server:
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, email, message.as_string())

print("Emails sent successfully.")
