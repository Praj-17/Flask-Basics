from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# def create_app():
app = Flask(__name__)

#     with app.app_context():
#         init_db()

#     return app
# app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class TODO(db.Model):
    
    sno = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String, nullable = False)
    desc = db.Column(db.String, nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    
    #How should we represent the class object
    def __repr__(self)->str:
        return f'{self.sno} {self.Title}'
@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello, world'


@app.route('/products')
def products():
    return 'This is products page'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)
    
    
