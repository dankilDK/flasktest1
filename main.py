from PIL import Image
from flask import Flask, url_for, request

app = Flask(__name__)

def gen_alert(name, type):
    return f'''<div class="alert alert-{type}" role="alert">
                    {name}
                </div>'''


@app.route('/')
def begin():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def prom():
    return "Человечество вырастает из детства.<p>" \
           "Человечеству мала одна планета.<p>" \
           "Мы сделаем обитаемыми безжизненные пока планеты.<p>" \
           "И начнем с Марса!<p>" \
           "Присоединяйся!<p>"


@app.route('/image_mars')
def img():
    return f'''<h1> Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars.png')}"alt="тут должен быть Марс, но его стащили гномы">
    <p>Вот она какая, красная планета.</p>'''


@app.route('/promotion_image')
def ad():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.2.1/dist/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}"alt="тут должен быть Марс, но его стащили гномы">
                    {gen_alert("Человечество вырастает из детства.", "secondary")}
                    {gen_alert("Человечеству мала одна планета.", "success")}
                    {gen_alert("Мы сделаем обитаемыми безжизненные пока планеты.", "secondary")}
                    {gen_alert("И начнем с Марса!", "warning")}
                    {gen_alert("Присоединяйся!", "danger")}
                  </body>
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def choice(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.2.1/dist/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <h3>{gen_alert(f'Поздравляем! Ваш рейтинг после {level} этапа отбора', 'success')}</h3>
                    <h3>Составляет {rating}!</h3>
                    <h3>{gen_alert('Желаем удачи!', 'warning')}</h3>
                  </body>
                </html>
    '''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
