from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/project.html')
def project():
    return render_template('project.html')

@app.route('/learn.html')
def learn():
    return render_template('learn.html')

@app.route('/blogs.html')
def blogs():
    return render_template('blogs.html')

@app.route('/feedback.html', methods=['GET', 'POST'])  # Route to handle form submission
def feedback():
    if request.method == 'POST':
        # Getting form data
        name = request.form['name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        stream = request.form['stream']
        message = request.form['message']

        # Creating dictionary with form data
        feedback_data = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'stream': stream,
            'message': message
        }

        # Writing data to file
        with open('feedback_data.json', 'a') as file:
            json.dump(feedback_data, file)
            file.write('\n')

        return render_template('index.html')
    else:
        # If it's a GET request, just render the feedback form
        return render_template('feedback.html')

@app.route('/index.html')
def custom_index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
