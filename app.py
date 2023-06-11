from flask import Flask, render_template, redirect
import datetime

today = datetime.datetime.now()
year = today.year

app = Flask(__name__)


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', year=year)


@app.route('/blog')
def blog():
    return render_template('blog.html', year=year)


@app.route('/cv')
def cv():
    return render_template('cv.html', year=year)


@app.errorhandler(404)
def handle_404(e):
    return redirect('about')


if __name__ == '__main__':
    app.run()
