from flask import Flask, render_template, request, redirect
from models import db, StudentModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/data/create', methods=['GET', 'POST'])
def create_record():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        age = request.form['age']
        program = request.form['program']
        student = StudentModel(student_id=student_id, name=name, age=age, program=program)
        db.session.add(student)
        db.session.commit()
        return redirect('/data')

@app.route('/data')
def get_records():
    students = StudentModel.query.all()
    return render_template('datalist.html', students=students)


@app.route('/data/<int:id>')
def get_record(id):
    student = StudentModel.query.filter_by(student_id=id).first()
    if student:
        return render_template('data.html', student=student)
    return f"Student with id ={id} Doesn't exist"


@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def update_record(id):
    student = StudentModel.query.filter_by(student_id=id).first()
    if request.method == 'POST':
        if student:
            db.session.delete(student)
            db.session.commit()

            name = request.form['name']
            age = request.form['age']
            program = request.form['program']
            student = StudentModel(student_id=id, name=name, age=age, program=program)

            db.session.add(student)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Employee with id = {id} Does nit exist"

    return render_template('update.html', student=student)


app.run(host='localhost', port=5000)