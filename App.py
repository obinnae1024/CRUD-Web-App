from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class instructors(db.Model):
    __tablename__ = 'instructors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    department = db.Column(db.String(100))

    def __int__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department


class courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    instructor_id = db.Column(db.Integer, db.ForeignKey("instructors.id"))

    def __int__(self, id, title, instructor_id):
        self.id = id
        self.title = title
        self.instructor_id = instructor_id


class student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    total_credits = db.Column(db.Integer)

    def __int__(self, id, name, total_credits):
        self.id = id
        self.name = name
        self.total_credits = total_credits


class enrollment(db.Model):
    __tablename__ = 'enrollment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    credits = db.Column(db.Integer)
    grade = db.Column(db.Integer)

    def __int__(self, id,student_id, course_id, credits, grade):
        self.id=id
        self.student_id = student_id
        self.course_id = course_id
        self.credits = credits
        self.grade = grade


@app.route('/')
def Index():
    all_data = instructors.query.all()
    all_data1 = courses.query.all()
    all_data2 = student.query.all()
    all_data3 = enrollment.query.all()

    return render_template("index.html", instructors=all_data, courses=all_data1, student=all_data2, enrollment=all_data3)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        # 'name' comes from the name of the inputs from index.html

        my_data = instructors(id=request.form['id'], name=request.form['name'], department=request.form['department'])
        db.session.add(my_data)
        db.session.commit()

        flash("Inserted Successfully")

        return redirect(url_for('Index'))


@app.route('/insert-course', methods=['POST'])
def insert_course():
    if request.method == 'POST':
        # 'name' comes from the name of the inputs from index.html

        my_data = courses(id=request.form['id'], title=request.form['title'],
                          instructor_id=request.form['instructor_id'])
        db.session.add(my_data)
        db.session.commit()

        flash("Inserted Successfully")

        return redirect(url_for('Index'))


@app.route('/insert-enroll', methods=['POST'])
def insert_enroll():
    if request.method == 'POST':
        # 'name' comes from the name of the inputs from index.html

        my_data = enrollment(student_id=request.form['student_id'],
                             course_id=request.form['course_id'], credits=request.form['credits'],
                             grade=request.form['grade'])
        db.session.add(my_data)
        db.session.commit()

        flash("Inserted Successfully")

        return redirect(url_for('Index'))


@app.route('/insert-student', methods=['POST'])
def insert_student():
    if request.method == 'POST':
        # 'name' comes from the name of the inputs from index.html

        my_data = student(id=request.form['id'], name=request.form['name'], total_credits=request.form['total_credits'])
        db.session.add(my_data)
        db.session.commit()

        flash("Inserted Successfully")

        return redirect(url_for('Index'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = instructors.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.department = request.form['department']

        db.session.commit()
        flash("Instructor Updated Succesfully ")

        return redirect(url_for('Index'))


@app.route('/update-course', methods=['GET', 'POST'])
def update_course():
    if request.method == 'POST':
        try:
            my_data = courses.query.get(request.form.get('id'))

            my_data.title = request.form['title']
            my_data.instructor_id = request.form['instructor_id']

            db.session.commit()
            flash("Updated Succesfully ")
        except:
            flash("You can't change the instructor id")

        return redirect(url_for('Index'))


@app.route('/update-enroll', methods=['GET', 'POST'])
def update_enroll():
    if request.method == 'POST':
        my_data = enrollment.query.get(request.form.get('id'))

        my_data.student_id = request.form['name']
        my_data.course_id = request.form['course_id']
        my_data.credits = request.form['credits']
        my_data.grade = request.form['grade']

        db.session.commit()
        flash("Updated Succesfully ")

        return redirect(url_for('Index'))


@app.route('/update-student', methods=['GET', 'POST'])
def update_student():
    if request.method == 'POST':
        my_data = student.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.total_credits = request.form['total_credits']

        db.session.commit()
        flash("Updated Succesfully ")

        return redirect(url_for('Index'))


@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    try:
        my_data = instructors.query.get(id)
        db.session.delete(my_data)
        db.session.commit()
        flash("Deleted Succesully")
    except:
        flash("Delete the courses this teacher teaches first")

    return redirect(url_for('Index'))


@app.route('/delete-course/<id>/', methods=['GET', 'POST'])
def delete_course(id):
    my_data = courses.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Deleted Succesully")

    return redirect(url_for('Index'))


@app.route('/delete-enroll/<id>/', methods=['GET', 'POST'])
def delete_enroll(id):
    my_data = enrollment.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Deleted Succesully")

    return redirect(url_for('Index'))


@app.route('/delete-student/<id>/', methods=['GET', 'POST'])
def delete_student(id):
    try:
        my_data = student.query.get(id)
        db.session.delete(my_data)
        db.session.commit()
        flash("Deleted Succesully")
    except:
        flash("You can't delete a student that is enrolled in a class")
    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
