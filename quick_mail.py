import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gmail SMTP server parameters
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Use port 465 if you prefer SSL over TLS
email_address = 'adresse@gmail.com' # Your sender email address 
password = 'token' # The token for mail -> more details on token_documentation

# Email subject and content
subject = 'Hack club'
content = "I'm currently testing"

def create_email(to_address, subject, content):
    #Create an email with the specified parameters.
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(content, 'plain'))
    return msg

def send_email(msg, to_address):
    #Send an email via Gmail SMTP server.
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS (encrypted) connection
        server.login(email_address, password)
        server.sendmail(email_address, to_address, msg.as_string())
        server.quit()
        print(f'Email sent to {to_address} successfully.')
    except Exception as e:
        print(f'Error sending email to {to_address}: {str(e)}')

def main():
    # Input email addresses separated by ';'
    participant_names = input("Enter email addresses separated by ';' : ")

    # Split email addresses using ';' as a separator
    email_list = participant_names.split(";")

    # Send an email to each address
    for email in email_list:
        email = email.strip()  # Remove any extra spaces around the email address
        msg = create_email(email, subject, content)
        send_email(msg, email)

if __name__ == "__main__":
    main()


