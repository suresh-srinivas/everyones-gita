from flask import Flask, request, redirect, url_for, render_template
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uploads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    details = db.Column(db.String(200), nullable=False)
    chapter = db.Column(db.String(10), nullable=False)
    image_filename = db.Column(db.String(120), nullable=False)
    recording_filename = db.Column(db.String(120))
    youtube_url = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    uploads = Upload.query.all()
    chapters = {upload.chapter: [] for upload in uploads}
    for upload in uploads:
        chapters[upload.chapter].append(upload)
    return render_template('index.html', chapters=chapters)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        name = request.form['name']
        details = request.form['details']
        chapter = request.form['chapter']
        image = request.files['image']
        recording = request.files.get('recording')
        youtube_url = request.form.get('youtube_url')

        if image and (recording or youtube_url):
            image_filename = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_filename)
            
            recording_filename = None
            if recording:
                recording_filename = os.path.join(app.config['UPLOAD_FOLDER'], recording.filename)
                recording.save(recording_filename)
            
            upload_entry = Upload(name=name, details=details, chapter=chapter, image_filename=image_filename, recording_filename=recording_filename, youtube_url=youtube_url)
            db.session.add(upload_entry)
            db.session.commit()

            return redirect(url_for('index'))

        return 'File upload failed'
    return render_template('upload.html')

@app.route('/clear_db', methods=['POST'])
def clear_db():
    db.session.query(Upload).delete()
    db.session.commit()
    return 'Database cleared.'

if __name__ == '__main__':
    app.run(debug=True)


