from flask import Flask
from flask import render_template, redirect,request


app = Flask(__name__)
notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_notes():
    note = request.form.get('note')
    notes.append(note)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_notes():
    note_index = int(request.form.get('note_index'))
    if 0 <= note_index <len(notes):
        del notes[note_index]
    return redirect('/')

if __name__ == '__main__':
    app.run(port=5000)
