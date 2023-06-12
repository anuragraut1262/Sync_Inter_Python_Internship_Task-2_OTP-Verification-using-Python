import random
import smtplib

# function to send OTP via email
def send_otp(email):
    # connect to Gmail SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # replace with your own Gmail account credentials
    email_address = 'amankumarjc@gmail.com'
    email_password = 'wedjoehumsqqxtcl'
    server.login(email_address, email_password)
    # generate a 6-digit OTP and send it via email
    otp = ''.join([str(random.randint(0, 9)) for i in range(6)])  # changed to 6 digits
    message = f'Your OTP is {otp}'
    server.sendmail(email_address, email, message)
    server.quit()
    # return the generated OTP
    return otp

# function to verify the OTP
def verify_otp():
    email = input("Enter your email address: ")
    # send OTP via email
    otp = send_otp(email)
    # get user input for OTP and verify it
    user_input = input("Enter the OTP sent to your email: ")
    if user_input == otp:
        print("OTP verified successfully!")
    else:
        print("Invalid OTP, please try again.")

# call the verify_otp function to start the OTP verification process
verify_otp()
