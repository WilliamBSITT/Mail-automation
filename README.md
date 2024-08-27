# Python Email Sending Project

This Python project allows you to send emails to a list of recipients using Gmail's SMTP server. It includes two scripts:

- **`quick_mail.py`**: Sends an email to a list of recipients.
- **`custom_mail.py`**: Sends personalized emails to each recipient using their name.

## Prerequisites

- Python 3
- A Gmail account for sending emails

## Configuration

Before running the scripts, you need to configure the SMTP settings and the sender's information in the scripts:

- **Sender's Email Address**: Replace `'adresse@gmail.com'` with your Gmail email address.
- **App Password**: Replace `'token'` with the app password generated for your Gmail account. See the [Google documentation on app passwords](https://support.google.com/accounts/answer/185833?hl=en) for more details.

## Scripts

### 1. `quick_mail.py`

This script sends an email to a list of email addresses specified by the user. The addresses should be provided in the format `email@domain.com;anotheremail@domain.com`.

#### Usage

1. Run the script with the following command:

    ```bash
    python quick_mail.py email@domain.com;anotheremail@domain.com
    ```

#### Example

The content of the email will be customized for each recipient using the provided name.

### 2. `custom_mail.py`

This script is similar to the first one but allows for personalized emails to each recipient using their name. The addresses should be provided in the format `Name:email@domain.com;AnotherName:anotheremail@domain.com`.

#### Usage

1. Run the script with the following command:

    ```bash
    python send_email_custom.py Name:email@domain.com;AnotherName:anotheremail@domain.com
    ```

## Features

- **Email Validation**: Email addresses are checked using a regular expression to ensure they are valid.
- **Error Handling**: Errors in sending emails are captured and displayed, letting you know if the email failed.

## Notes

- Ensure that your SMTP connection details are correct to avoid sending errors.
- App passwords are necessary to allow scripts to connect to your Gmail account securely.

## License

This project is licensed under the [License Name] - see the [LICENSE](LICENSE) file for details.


