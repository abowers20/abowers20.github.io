# from flask import Flask, render_template, request, redirect
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# app = Flask(__name__, static_folder='homepage')

# @app.route('/')
# def index():
#     return render_template('homepage/index.html')

# @app.route('/submit_form', methods=['POST'])

# def submit_form():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         subject = request.form['subject']
#         message = request.form['message']
        
#         email_content = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

#         if not name or not email or not subject or not message:
#             return 'Error: All fields are required.'
    
#         try:
#             server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#             server.login('username', 'password')

#             # Create the email message
#             msg = MIMEMultipart()
#             msg['From'] = email
#             msg['To'] = 'alexb01890@gmail.com'
#             msg['Subject'] = f"New Form Submission: {subject}"
#             msg.attach(MIMEText(email_content, 'plain'))

#             # Send the email
#             server.sendmail(email, 'alexb01890@gmail.com', msg.as_string())
#             server.quit()

#             return redirect('/', success_message='Form submitted successfully!')
#         except Exception as e:
#             print(f'Error sending email: {e}')
#             return 'Error sending email'

# if __name__ == '__main__':
#     app.run(debug=True)