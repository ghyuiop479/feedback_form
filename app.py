from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Email config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'dhoniashwin18@gmail.com'
app.config['MAIL_PASSWORD'] = 'kpyp avbn gncx fykm'  # Use Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'dhoniashwin18@gmail.com'

mail = Mail(app)

# Show the form
@app.route('/')
def index():
    return render_template('index.html')  # this looks inside templates/

# Send feedback email
@app.route('/send_feedback', methods=['POST'])
def send_feedback():
    data = request.get_json()

    msg = Message(
        subject="New Feedback",
        recipients=['dhoniashwin18@gmail.com'],
        body=f"""Name: {data['name']}
Age: {data['age']}
Gender: {data['gender']}
Message: {data['message']}"""
    )

    try:
        mail.send(msg)
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

