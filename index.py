from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"

@app.route('/index')
def page():
    return "И на Марсе будут яблони цвести!"

@app.route("/promotion")
def promotion():
    text=['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
          'Мы сделаем обитаемыми безжизненные пока планеты.','И начнем с Марса!'
'Присоединяйся!']
    return "<br>".join(text)

@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}"
           alt="здесь должна была быть картинка, но не нашлась">
            <p> Вот она какая красная планета!</p>
                             
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style.css')}" />
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}"
           alt="здесь должна была быть картинка, но не нашлась">
<div class="alert alert-primary" role="alert">
  Человечество вырастает из детства.
</div>
<div class="alert alert-secondary" role="alert">
  Человечеству мала одна планета.
</div>
<div class="alert alert-success" role="alert">
  Мы сделаем обитаемыми безжизненные пока планеты.
</div>
<div class="alert alert-danger" role="alert">
  И начнем с Марса!
</div>
<div class="alert alert-warning" role="alert">
  присоединяйтесь!
</div>
</body>
                </html>"""


@app.route('/choice/<planet>')
def choice(planet):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style.css')}" />
                  </head>
                  <body>
                    <h1>Жди нас, {planet}!</h1>
                    
<div class="alert alert-primary" role="alert">
 Эта планета близка к Земле.
</div>
<div class="alert alert-secondary" role="alert">
  На ней много ресурсов.
</div>
<div class="alert alert-success" role="alert">
  На ней есть вода и атмосфера
</div>

</body>
</html>"""


@app.route('/otbor', methods=['POST', 'GET'])
def otbor():
    if request.method == 'GET':
        return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style.css')}" />
                    </head>
                  <body>
                    <h1>Анкета претендента</h1>
                    <h2> на участие в миссии </h2>
                    <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="lastname" placeholder="Введите фамилию" name="lastname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>высшее</option>
                                          <option>начальное</option>
                                          <option>среднее</option>
                                          <option>никакого</option>
                                          </select>
                                     </div>
                                    <br>
                                    <div class="form-group">
                                    
                                        <label for="about">Какие у вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер</label>
                                        
                                        <br><input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                        
                                        <br><input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                        
                                        <br><input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Врач</label>
                                                                       
                                    </div>
                                    <br>
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
                                    <br>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    </div>
                                    <br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>

                  </body>
                </html>"""
    elif request.method == 'POST':
        pass
        return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')