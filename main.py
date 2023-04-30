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


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Пейзажи Марса</title>
                </head>
                <body>
                    <h1>Пейзажи Марса</h1>
                    <div id="carouselExample" class="carousel slide" data-ride="carousel">
                        <ol class="carousel-indicators">
                            <li data-target="#carouselExample" data-slide-to="0" class="active"></li>
                            <li data-target="#carouselExample" data-slide-to="1"></li>
                            <li data-target="#carouselExample" data-slide-to="2"></li>
                        </ol>
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                                <img src="{url_for('static', filename='img/landscape1.jpg')}" class="d-block w-100" alt="First Slide">
                            </div>
                            <div class="carousel-item">
                                <img src="{url_for('static', filename='img/landscape2.jpg')}" class="d-block w-100" alt="Second Slide">
                            </div>
                            <div class="carousel-item">
                                <img src="{url_for('static', filename='img/landscape3.jpg')}" class="d-block w-100" alt="Third Slide">
                            </div>
                        </div>
                        <a class="carousel-control-prev" role="button" href="#carouselExample" data-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        </a>
                        <a class="carousel-control-next" role="button" href="#carouselExample" data-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        </a>
                    </div>
                </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
