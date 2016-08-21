from datetime import datetime
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy

from database import init_db, db_session
from forms import BoardInsertForm
from models import Board

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
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
    form = BoardInsertForm(csrf_enabled=False)
    return render_template('board/board_form.html', form=form)


@app.route("/board/update/<int:id>", methods=['GET'])
def board_update_form(id):
    board = Board.query.get(id)
    form = BoardInsertForm(csrf_enabled=False, obj=board)
    return render_template('board/board_form.html', form=form)


@app.route("/board", methods=['POST'])
def board_save():
    form = BoardInsertForm(csrf_enabled=False)
    if form.validate():
        id = form.id.data
        if not id:
            b = Board(title=form.title.data, content=form.content.data)
            db_session.add(b)
            db_session.commit()
            id = b.id
            flash('게시물을 생성 하였습니다.')
        else:
            board = Board.query.get(id)
            board.title = form.title.data
            board.content = form.content.data
            db_session.commit()
            flash('게시물을 수정 하였습니다.')

        return redirect(url_for('board_view', id=id))
    else:
        return render_template('board/board_form.html', form=form)


@app.route("/board/<id>", methods=['GET'])
def board_view(id):
    board = Board.query.get(id)
    return render_template('board/board_view.html', board=board)


if __name__ == '__main__':
    app.run()
