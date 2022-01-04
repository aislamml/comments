from flask import Flask, render_template, request

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://aislamml:12345@localhost/aislamml')
db = scoped_session(sessionmaker(bind=engine))


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': 

        email = request.form.get('email')
        comment = request.form.get('comment')

        db.execute('INSERT INTO comm (email, comment) VALUES (:email, :comment)',
                    {'email': email, 'comment': comment})
        db.commit()

    comments = db.execute('SELECT * FROM comm').fetchall()

    return render_template('index.html', comments = comments)

app.run(debug=True)