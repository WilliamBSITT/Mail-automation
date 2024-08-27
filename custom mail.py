import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re

# Gmail SMTP server parameters
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Use port 465 if you prefer SSL over TLS
email_address = 'adresse@gmail.com'  # Your sender email address
password = 'token'  # The token for mail -> more details on token_documentation

# Email subject
subject = 'Hack club'

def create_email(to_address, subject, content):
    """Create an email with the specified parameters."""
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(content, 'plain'))
    return msg

def send_email(msg, to_address):
    """Send an email via Gmail SMTP server."""
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS (encrypted) connection
        server.login(email_address, password)
        server.sendmail(email_address, to_address, msg.as_string())
        server.quit()
        print(f'Email sent to {to_address} successfully.')
    except Exception as e:
        print(f'Error sending email to {to_address}: {str(e)}')

def is_valid_email(email):
    """Check if the email address is valid using a regular expression."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def main():
    participant_info = input("Enter names and email addresses separated by ';' (ex, 'Alice:alice@gmail.com,Bob:bob@gmail.com') : ")

    # Split participants into name-email pairs using ';' as the separator
    pairs = participant_info.split(';')

    for pair in pairs:
        # Split each pair into name and email
        name_email = pair.split(':')
        
        if len(name_email) != 2:
            print(f'Invalid format for pair: {pair}')
            continue
        
        name, email = name_email
        name = name.strip()
        email = email.strip()

        if is_valid_email(email):
            content = f"Hello {name},\nI'm currently testing this email.\nHack Club"
            print(content)
            print(email)
            msg = create_email(email, subject, content)
            send_email(msg, email)
        else:
            print(f'Invalid email address: {email}')

if __name__ == "__main__":
    main()
