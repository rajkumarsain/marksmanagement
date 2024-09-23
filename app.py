from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store for students and their marks (For demo purposes, use a database for real-world apps)
students = []

# Home route to display all students and marks
@app.route('/')
def index():
    return render_template('index.html', students=students)

# Route to add a new student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        marks = request.form['marks']
        students.append({'name': name, 'marks': marks})
        return redirect(url_for('index'))
    return render_template('add_student.html')

# Route to edit student marks
@app.route('/edit/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    student = students[student_id]
    if request.method == 'POST':
        student['name'] = request.form['name']
        student['marks'] = request.form['marks']
        return redirect(url_for('index'))
    return render_template('edit_student.html', student=student, student_id=student_id)

# Route to delete a student
@app.route('/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    students.pop(student_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
