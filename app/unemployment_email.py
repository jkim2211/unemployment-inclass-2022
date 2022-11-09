from app.unemployment import fetch_unemployment_data
from app.email_service import send_email

if __name__ == "__main__":

    print("UNEMPLOYMENT EMAIL...")

    data = fetch_unemployment_data()

    # keeping the email content simple for example purposes, but
    # ... for an example of attaching the data as a CSV file
    # ... and attaching the chart as an image file
    # ... see: https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/codebase-cleanup/starter/app/unemployment_email.py#L56-L132
    # ... (you might need to create a more complex email sending function)

    html_content = f"""
        <h1>Unemployment Report Email</h1>

        <p>Latest rate: {data[0]['value']}% </p>
        <p>As of: {data[0]['date']} </p>
    """


    recipient_address = input("Please provide the recipient address: ")

    send_email(subject="[Daily Briefing] Unemployment Report", html=html_content, recipient_address=recipient_address)