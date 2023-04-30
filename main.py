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


@app.route('/load_photo', methods=['POST', 'GET'])
def selection():
    if request.method == 'GET':
        return f"""
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet"
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                <title>Отбор астровнавтов</title>
            </head>
            <body>
                <h1>Загрузка фотографии</h1>
                <h2>для участия в миссии</h2>
                <div>
                    <form class="login_form" method="post" enctype="multipart/form-data">
                        <div class="form-group">
                            <label for="photo">Приложите фотографию</label>
                            <input type="file" class="form-control-file" id="photo" name="file">
                        </div>
                        <div class="form-group">
                            <img src="{url_for('static', filename='img/avatar.jpg')}" 
                            alt="Здесь должно быть Ваше фото">
                        </div>
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
                </div>
            </body>
        </html>
        """
    elif request.method == "POST":
        im = Image.open(request.files['file'])
        try:
            im.save("static/img/avatar.jpg")
        except Exception:
            im.load()
            res = Image.new("RGB", im.size, (255, 255, 255))
            res.paste(im, mask=im.split()[3])
            res.save("static/img/avatar.jpg")
        print(request.files['file'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
