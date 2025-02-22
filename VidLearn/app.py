from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import csv  

from jinja2 import Template

# Registering zip function to be used in Jinja2 templates



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

app.jinja_env.globals.update(zip=zip)

personas = ['Emily', 'Michael', 'Sarah', 'David', 'Alex', 'Carlos', 'Lisa', 'Brandon', 'Katie', 'Sean']

def read_ratings(file_path):
    ratings = {}
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row: 
                persona, rating = row
                ratings[persona] = rating
    return ratings

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the files part
        if 'files' not in request.files:
            return render_template('index.html', personas=personas, uploaded_files=[[] for _ in personas])

        files = request.files.getlist('files')
        uploaded_files = [[] for _ in personas]

        for i, file in enumerate(files):
            if file and file.filename:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # Assign the uploaded file to a persona
                persona_index = i % len(personas)
                uploaded_files[persona_index].append(filename)

        # Read overall ratings from the external file
        ratings = read_ratings('/Users/home/Documents/Programs/VidLearn/VidLearn/ratings.csv')

        return render_template('display.html', personas=personas, uploaded_files=uploaded_files, ratings=ratings)

    # For GET request, render the upload form with empty uploaded_files
    return render_template('index.html', personas=personas, uploaded_files=[[] for _ in personas])

if __name__ == '__main__':
    app.run(debug=True)
