from flask import Flask, render_template, request
import string
import getpass

app = Flask(__name__)

def analyze_password(password):
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char.isspace():
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1
    
    if strength == 1:
        remarks = "Password is very weak and can be easily cracked."
    elif strength == 2:
        remarks = "Not a good password. Consider choosing a stronger one."
    elif strength == 3:
        remarks = "It's a weak password. You should consider changing it."
    elif strength == 4:
        remarks = "It's a strong password, but can be better."
    elif strength == 5:
        remarks = "A very strong password."

    return {
        'lower_count': lower_count,
        'upper_count': upper_count,
        'num_count': num_count,
        'wspace_count': wspace_count,
        'special_count': special_count,
        'strength': strength,
        'remarks': remarks
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        result = analyze_password(password)
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
