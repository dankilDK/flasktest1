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

@app.route('/astronaut_selection', methods=['POST', 'GET'])
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
                <h1>Анкета претендента</h1>
                <h2>на участие в миссии</h2>
                <div>
                    <form class="login_form" method="post">
                        <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                        <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                        <div class="form-group">
                            <label for="eduSelect">Какое у Вас образование?</label>
                            <select class="form-control" id="eduSelect" name="edu">
                                <option>Начальное</option>
                                <option>Среднее</option>
                                <option>Высшее</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="form-check">Какие у Вас есть профессии?</label>
                            <div class="form-check">
                                <input type="checkbox" class="form-check-input" name = "job" id="explorer" name="explorer">
                                <label class="form-check-label" for="explorer">Инженер-исследователь</label>
                            </div>
                            <div class="form-check">
                                <input type="checkbox" class="form-check-input" name = "job" id="builder" name="builder">
                                <label class="form-check-label" for="builder">Инженер-строитель</label>
                            </div>
                            <div class="form-check">
                                <input type="checkbox" class="form-check-input" name = "job" id="pilot" name="pilot">
                                <label class="form-check-label" for="pilot">Пилот</label>
                            </div>
                            <div class="form-check">
                                <input type="checkbox" class="form-check-input" name = "job" id="meteorologist" name="meteorologist">
                                <label class="form-check-label" for="meteorologist">Метеоролог</label>
                            </div>
                            <div class="form-check">
                                <input type="checkbox" class="form-check-input" name = "job" id="lifesupport" name="lifesupport">
                                <label class="form-check-label" for="lifesupport">Инженер по жизнеобеспечению</label>
                            </div>
                            <div class="form-check">
                                <input type="checkbox" class="form-check-input" name = "job" id="radiation" name="radiation">
                                <label class="form-check-label" for="radiation">Инженер по радиационной защите</label>
                            </div>
                            <div class="form-check">
                                <input type="checkbox" class="form-check-input" name = "job" id="medic" name="medic">
                                <label class="form-check-label" for="medic">Врач</label>
                            </div>
                            <div class="form-check">
                                <input type="checkbox" class="form-check-input" name = "job" id="exobiologist" name="exobiologist">
                                <label class="form-check-label" for="exobiologist">Экзобиолог</label>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="form-check">Укажите пол</label>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                <label class="form-check-label" for="male">
                                    Мужской
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                <label class="form-check-label" for="female">
                                    Женский
                                </label>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="about">Почему вы хотите принять участие в миссии?</label>
                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                        </div>
                        <div class="form-group">
                            <label for="photo">Приложите фотографию</label>
                            <input type="file" class="form-control-file" id="photo" name="file">
                        </div>
                        <div class="form-group form-check">
                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                        </div>
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
                </div>
            </body>
        </html>
        """
    elif request.method == "POST":
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['edu'])
        print(request.form.get('job'))
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form.get('accept'))
        return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')