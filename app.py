from flask import Flask, request, render_template_string
import random

app = Flask(__name__)
secret_number = random.randint(1, 10)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Guess the Number 🎯</title>
</head>
<body style="text-align:center; font-family:sans-serif;">
    <h1>🎮 Guess the Number (1 to 10)</h1>
    <form method="post">
        <input type="number" name="guess" min="1" max="10" required>
        <button type="submit">Submit Guess</button>
    </form>
    {% if message %}
        <h2>{{ message }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def game():
    global secret_number
    message = None
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            if guess == secret_number:
                message = f"🎉 Correct! The number was {secret_number}. Let's play again!"
                #secret_number = random.randint(1, 10)  # Reset game
            else:
                message = "❌ Wrong guess! Try again."
        except ValueError:
            message = "🚫 Invalid input."
    return render_template_string(html_template, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
