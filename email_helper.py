import smtplib


def send_email(to_address, subject, body):
    # Define your SMTP email server details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    # Define your email address and password
    from_address = 'your-email@gmail.com'
    password = 'your-password'

    # Create the email header
    header = 'To:' + to_address + '\n' + 'From:' + from_address + '\n' + 'Subject:' + subject + '\n'
    msg = header + '\n' + body + '\n\n'

    # Start the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Login to your email account
    server.login(from_address, password)

    # Send the email
    server.sendmail(from_address, to_address, msg)
    server.quit()