from wsgiref.simple_server import make_server
from funcs import *
import cgi

#головна сторінка
HTML_MAIN = """<html>
<title>Головна</title>
<body>
<h1>Головна</h1>
<br>
<form method=POST action="go_find_products">
<input type=submit value="Пошук продуктів">
</form>
<form method=POST action="go_to_basket">
<input type=submit value="Перейти до корзини">
</form>
<h3>Усі продукти в наявності:</h3>

<table style="width:50%">
{}
</table>
</body>
</html>
        """

#пошук продуктів (знайдені з'являються у таблиці на цій же сторінці разом з кнопками додавання до корзини та введення к-ті)
FIND_PROD_PAGE = """ <html>
<head>
    <meta charset="UTF-8">
    <title>Пошук продуктів</title>
</head>
<body>
<h3>Можливість пошуку за категорією товарів або за назвою(частиною назви) товару</h3>
<form method=POST action="find_by_categ">
Пошук за категорією: 
<select name="category">
  <option>Фрукти</option>
  <option>Овочі</option>
  <option>Ягоди</option>
  <option>Молочні продукти</option>
  <option>Напої</option>
  <option>Технології</option>
  <option>18+</option>
  <option>Розваги</option>
  <option>Інше</option>
</select>
<input type=submit value="Пошук">
</form>
<form method=POST action="find_by_name">
Пошук за назвою: <input type=text name=name value =""> 
<input type=submit value="Пошук">
</form>
     <table style="width:100%">
        {}
    </table>
<form method=POST action="go_to_main">
<input type=submit value="Повернутися на головну">
</form>
<form method=POST action="go_to_basket">
<input type=submit value="Перейти до корзини">
</form>
</body>
</html>"""

#корзина
BASKET_PAGE="""<html>
<head>
    <meta charset="UTF-8">
    <title>Ваша корзина</title>
</head>
<body>
<h1>Усі продукти у корзині</h1>
     <h2>Cписок товарів:</h2>>
     <table style="width:50%">
        {}
    </table>
<h2>Сума до сплати:{}</h2>
</form>
<form method=POST action="checkout">
<input type=submit value="Розрахуватися">
</form>
<form method=POST action="go_to_main">
<input type=submit value="Повернутися на головну">
</form>
</body>
</html>
        """

CHECKOUT_PAGE="""<html>
<head>
    <meta charset="UTF-8">
    <title>Дякуємо</title>
</head>
<body>
    <h1>Дякуємо за покупку!</h1>
    <h3>Якщо ви придбали товари з категорії 18+, підготуйте відповідні документи.</h3>
    <form method=POST action="go_to_main">
    <input type=submit value="На головну">
</form>
</body>
</html>
"""

##########################################################################################################################################

def return_finds(dct):
    res = f"<tr>  " \
          f"<th>НОМЕР</th>    " \
          f"<th>Назва</th>    " \
          f"<th>Опис</th>" \
          f"<th>Характеристики</th>" \
          f"<th>Ціна</th>" \
          f"<th>Фото</th>" \
          f"</tr>"
    i = 1
    try:
        for key,j in dct.items():
            booll = False
            res += f"<tr>" \
                   f"<td>{i}</td>"
            for k in range(len(j)-1):
                if k!= 1:
                    res += f"<td>{j[k]}</td>"
                if j[k] == 8:
                    print(1)
                    booll = True

            res += f'<td><img src={j[-1]} height=100 width=100 /></td>'
            res += f"<td><form method=POST action='add_to_basket'><input type=hidden name=id value={key}><input type=text name=amount value ='Введіть бажану кількість'> "

            if booll == True:
                print(2)
                res += f'<p>Чи є Вам 18 років?</p>'\
                          f'<input type="radio" id="yes" name="q" value="yes">'\
                          f'<label for="yes">yes</label><br>'\
                          f'<input type="radio" id="no" name="q" value="no">'\
                          f'<label for="no">no</label><br>'
            res += f"<input type=submit value='Додати до корзини'> </form></td>" \
                       f"</tr>"
            i += 1
            booll = False
    except AttributeError:
        return dct
    return res

def return_finds_for_main(dct):
    res = f"<tr>  " \
          f"<th>НОМЕР</th>    " \
          f"<th>Назва</th>    " \
          f"<th>Опис</th>" \
          f"<th>Характеристики</th>" \
          f"<th>Ціна</th>" \
          f"<th>Фото</th>" \
          f"</tr>"
    i = 1
    try:
        for key, j in dct.items():
            booll = False
            res += f"<tr>" \
                   f"<td>{i}</td>"
            for k in range(len(j) - 1):
                if k != 1:
                    res += f"<td>{j[k]}</td>"
                if j[k] == 8:
                    print(1)
                    booll = True
            res += f'<td><img src={j[-1]} height=100 width=100 /></td>'
            res += f"<td><form method=POST action='add_to_basket_to_main'><input type=hidden name=id value={key}><input type=text name=amount value ='Введіть бажану кількість'> "
            if booll == True:
                res += f'<p>Чи є Вам 18 років?</p>' \
                       f'<input type="radio" id="yes" name="q" value="yes">' \
                       f'<label for="yes">yes</label><br>' \
                       f'<input type="radio" id="no" name="q" value="no">' \
                       f'<label for="no">no</label><br>'
            res += f"<input type=submit value='Додати до корзини'> </form></td>" \
                    f"</tr>"
            i += 1
            booll = False
    except AttributeError:
        return dct
    return res

def basket_table(dct):
    res = f"<tr>  " \
          f"<th>НОМЕР</th>    " \
          f"<th>Назва</th>    " \
          f"<th>Ціна</th>" \
          f"<th>Кількість</th>" \
          f"<th>Фото</th>" \
          f"<th>Загальна ціна</th>" \
          f"</tr>"
    i = 1
    for key,j in dct.items():
        res += f"<tr>" \
               f"<td>{i}</td>"
        for k in range(len(j)-1):
            res += f"<td>{j[k]}</td>"
        res += f'<td><img src={j[-1]} height=100 width=100 /></td>'\
            f"<td> {j[-3]}*{j[-2]}={j[-2]*j[-3]}</td>" \
               f"<td><form method=POST action='change_amount'><input type=hidden name=id value={key}><input type=text name=amount value ='Введіть бажану кількість'> " \
               f"<input type=submit value='Змінити кількість'></form>" \
               f"<form method=POST action='delete_item'><input type=hidden name=id value={key}>" \
               f"<input type=submit value='Видалити позицію'></form></td>"\
            f"</tr>"
        i += 1
    return res

def basket_to_dct(filename):
    global prod_dct
    dct_res = {}
    conn = sqlite3.connect(filename)
    curs = conn.cursor()
    for key,ammount in prod_dct.items():
        curs.execute("""SELECT * FROM products
                            WHERE id=(?)""", (key,))
        res=curs.fetchone()
        dct_res[key]=[res[1],res[5],ammount, res[6]]
    return dct_res

##########################################################################################################################################

def application(environ, start_response):
    global prod_dct
    if environ.get('PATH_INFO', '').lstrip('/') == '' or environ.get('PATH_INFO', '').lstrip('/') == 'go_to_main':
        body = HTML_MAIN.format(return_finds_for_main(dct_for_main(file)))
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == "go_to_basket":
        body = BASKET_PAGE.format(basket_table(basket_to_dct(file)),get_total(basket_to_dct(file)))
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == "go_find_products":
        body = FIND_PROD_PAGE
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == "find_by_categ":
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        res = ''
        if 'category' in form:
            cat = str(form.getfirst('category'))
            print(cat)
            res = return_finds(search_cat(file, cat))
        else:
            print('None')
        body = FIND_PROD_PAGE.format(res)
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == "find_by_name":
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        res = ''
        if 'name' in form:
            name = str(form.getfirst('name'))
            res = return_finds(search_prod(file, name))
        body = FIND_PROD_PAGE.format(res)
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'add_to_basket':
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        prod_id=int(form['id'].value)
        prod_amount=int(form['amount'].value)
        if 'q' in form:
            if str(form.getfirst('q')) == 'yes':
                print(3)
                prod_dct[prod_id] = prod_amount
        elif prod_id not in prod_dct:
            prod_dct[prod_id]=prod_amount
        else:
            prod_dct[prod_id]+=prod_amount
        body = FIND_PROD_PAGE
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'add_to_basket_to_main':
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        prod_id = int(form['id'].value)
        prod_amount = int(form['amount'].value)
        if 'q' in form:
            if str(form.getfirst('q')) == 'yes':
                print(3)
                prod_dct[prod_id] = prod_amount
        elif prod_id not in prod_dct:
            prod_dct[prod_id] = prod_amount
        else:
            prod_dct[prod_id] += prod_amount
        body = HTML_MAIN.format(return_finds_for_main(dct_for_main(file)))
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'checkout':
        body = CHECKOUT_PAGE
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        prod_dct = {}

    elif environ.get('PATH_INFO', '').lstrip('/') == 'change_amount':
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        if 'id' in form:
            prod_id = int(form['id'].value)
            new_am = int(form['amount'].value)
            prod_dct[prod_id] = new_am
        body = BASKET_PAGE.format(basket_table(basket_to_dct(file)),get_total(basket_to_dct(file)))
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'delete_item':
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        if 'id' in form:
            item = int(form['id'].value)
            prod_dct.pop(item)
        body = BASKET_PAGE.format(basket_table(basket_to_dct(file)),get_total(basket_to_dct(file)))
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    else:
        start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
        body = 'Page not found'

    return [bytes(body, encoding='utf-8')]

if __name__ == "__main__":
    print("--------------- сервер інтернет-крамниця ------------------")
    file = 'products1.db'
    prod_dct={}
    httpd = make_server('', 8000, application)
    httpd.serve_forever()
