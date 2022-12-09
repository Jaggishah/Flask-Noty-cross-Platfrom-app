from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default = True)

@app.route('/')
def main():
    todo = Todo.query.all()
    total_task = Todo.query.count()
    completed = Todo.query.filter_by(complete  =True).count()
    uncompleted = total_task - completed
    return render_template('index.html',**locals())

@app.route('/add',methods = ['POST','GET'])
def add():
    title = request.form.get('task')
    new_todo = Todo(title = title , complete = False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('main'))

@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('main'))

@app.route('/update/<int:id>')
def update(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.complete = not todo.complete
    
    db.session.commit()
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)