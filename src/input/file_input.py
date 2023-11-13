import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = ["png", "jpg"]
# TODO: This should be stored in a DB
UPLOAD_FOLDER = "/tmp/"

app = Flask(__name__, template_folder="static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_filename(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route("/", methods=["GET", "POST"])
def file_input():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        
        if file and allowed_filename(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return "<p>Successfully uploaded a file!</p>"#redirect(url_for('download_file', name=filename))
        
    return render_template("file_input.html")


