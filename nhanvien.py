from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from enum import unique



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nhanvien.db'
db=SQLAlchemy(app)

class Nhanvien(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    numberphone = db.Column(db.String(length=20), nullable=False)
    datejoin = db.Column(db.String(length=30), nullable=False, unique=True)
    description = db.Column(db.String(length=200), nullable=False, unique=True)

    def __init__(self, name, numberphone, datejoin, description):
        self.name = name
        self.numberphone = numberphone
        self.datejoin = datejoin
        self.description = description

    
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

if __name__ == '__nhanvien__':
    app.run(debug=True)

@app.route('/qlnv')    
def nhanvien_page():
    dsnv = Nhanvien.query.all()
    return render_template('qlnv.html', dsnv=dsnv)


@app.route('/create', methods = ['GET', 'POST'] )
def add():
    if request.method == 'POST':
        NhanVien= Nhanvien(request.form['name'],
        request.form['numberphone'],
        request.form['datejoin'],
        request.form['description'])

        db.session.add(NhanVien)
        db.session.commit()

        return redirect(url_for('nhanvien_page'))
    return render_template('Create.html')


@app.route('/edit/<int:id>', methods = ['GET', 'POST'])
def edit(id):
   NhanVien = Nhanvien.query.filter_by(id = id).first()

   if request.method == 'POST':
      NhanVien.name = request.form['name']
      NhanVien.numberphone = request.form['numberphone']
      NhanVien.datejoin = request.form['datejoin']
      NhanVien.description = request.form['description']

      db.session.merge(NhanVien)
      db.session.commit()

      return redirect(url_for('nhanvien_page'))
   return render_template('edit.html')      


@app.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
   NhanVien = Nhanvien.query.filter_by(id = id).first()
   if request.method =='POST':
      db.session.delete(NhanVien)
      db.session.commit()
      return redirect(url_for('nhanvien_page'))
   return render_template('delete.html')




