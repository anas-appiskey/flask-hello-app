from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://hp@localhost:5432/example' 
# all config variable is set through this 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 
# to connect to database we set config var 

class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(),nullable=False)

    #dender reper method
    def __repr__(self):
        return f'<Person ID: {self.id} , name : {self.name}>'

db.create_all()

@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello'+person.name

if __name__ =='__main__':
    app.run()