from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

from database import init_db, db_session
from models import Board

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

init_db()


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route("/board/list", methods=['GET', 'POST'])
def board_list():
    boards = Board.query.all()
    return render_template('board/board_list.html', boards=boards)


@app.route("/board/add", methods=['GET'])
def board_add_form():
    b = Board(title='제목', content='내용')
    db_session.add(b)
    db_session.commit()
    return render_template('board/board_form.html')


@app.route("/board/update/<id>", methods=['GET'])
def board_update_form(id):
    return render_template('board/board_form.html')


@app.route("/board", methods=['POST'])
def board_save():
    return render_template(url_for('board_view'))


@app.route("/board/<id>", methods=['GET'])
def board_view(id):
    return render_template('board/board_view.html')


if __name__ == '__main__':
    app.run()
