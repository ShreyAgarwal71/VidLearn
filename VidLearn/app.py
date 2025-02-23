
# app.py
import csv
from flask import Flask, render_template, request, redirect, url_for, jsonify
import threading
import os
import time
import response  # Import the refactored response module

app = Flask(__name__)

# Set paths for uploads and CSV output
#UPLOAD_FOLDER = '/Users/home/Documents/Programs/VidLearn/static/uploads'
#CSV_FOLDER = r'C:\Users\Shiven Saxena\Downloads\VidLearn\static\csv_reviews'
UPLOAD_FOLDER = r'C:\Users\Shiven Saxena\Downloads\VidLearn\static\uploads'
CSV_FOLDER = r'C:\Users\Shiven Saxena\Downloads\VidLearn\static\csv_reviews'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CSV_FOLDER'] = CSV_FOLDER

# Ensure the directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CSV_FOLDER, exist_ok=True)

# Global status to track processing
processing_status = {'done': False}

def process_files(file_paths):
    try:
        # Call the function in response.py that processes the PNGs and creates CSVs
        response.process_uploaded_files(file_paths, app.config['CSV_FOLDER'])
    except Exception as e:
        print("Error during processing:", e)
    processing_status['done'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('files')
        if len(files) != 4:
            message = "Please upload exactly 4 PNG files."
            return render_template('index.html', message=message)
        
        file_paths = []
        # Save files with sequential names (version1.png, version2.png, etc.)
        for i, file in enumerate(files, start=1):
            if file and file.filename.lower().endswith('.png'):
                filename = f"version{i}.png"
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                file_paths.append(file_path)
            else:
                message = "Only PNG files are allowed."
                return render_template('index.html', message=message)
        
        # Reset processing status and launch processing in a background thread
        processing_status['done'] = False
        thread = threading.Thread(target=process_files, args=(file_paths,))
        thread.start()
        
        # Redirect to the waiting/processing screen
        return redirect(url_for('processing'))
    
    return render_template('index.html')

@app.route('/processing')
def processing():
    return render_template('processing.html')

@app.route('/status')
def status():
    return jsonify(processing_status)

@app.route('/display')
def display():
    csv_data = []  # Will hold parsed CSV info for each file
    try:
        files = os.listdir(app.config['CSV_FOLDER'])
    except Exception as e:
        return render_template('display.html', csv_data=[], message=f"Error reading CSV folder: {str(e)}")
    
    # Process only CSV files (sorted to ensure consistent order)
    for file in sorted(files):
        if file.lower().endswith('.csv') and file != 'reviews1.csv' and file != 'reviews2.csv' and file != 'reviews3.csv' and file != 'reviews4.csv' and file != 'reviews_1_Books.csv' and file != 'reviews_1_Dress.csv' and file != 'reviews_1_Dresses.csv' and file != 'reviews_1_Medical_Care.csv' and file != 'reviews_1_Outerwear.csv' and file != 'reviews_1_Skincare.csv' and file != 'reviews_1_Sweater.csv':
            file_path = os.path.join(app.config['CSV_FOLDER'], file)
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                try:
                    header = next(reader)
                except StopIteration:
                    header = []
                rows = list(reader)
            csv_data.append({
                'filename': file[:-4],
                'header': header,
                'rows': rows
            })

    message = "Processing complete." if csv_data else "No CSV files were found."
    return render_template('display.html', csv_data=csv_data, message=message)

if __name__ == '__main__':
    app.run(debug=True)
