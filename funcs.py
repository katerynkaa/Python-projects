import sqlite3
import re

# ---------------------------------------------------developers------------------------------------------------------------------

def add_product(filename):  # filename - db file photo - photo file
    conn = sqlite3.connect(filename)
    curs = conn.cursor()
    name = input("enter name: ")
    category = input("enter category: ")
    #curs.execute("""SELECT id FROM categories
     #                           WHERE categ_name=(?)""", (category,))
    #res = curs.fetchone()[0]
    #print(res)
    #if res == None:
    #    return -1
    desc = input("enter desc: ")
    charst = input("enter charst: ")
    price = input("enter price: ")
    photo = input("enter фото: ")
    curs.execute("""INSERT INTO
            products(name,category,description,characteristics,price,photo)
                        VALUES (?,?,?,?,?,?)""", (name, category, desc, charst, price, photo,))
    conn.commit()
    conn.close()
    return 1

def add_category(filename):
    conn = sqlite3.connect(filename)
    curs = conn.cursor()
    categ = input("enter categ name: ")
    curs.execute("""INSERT INTO categories(categ_name)
                                        VALUES (?)""", (categ,))
    conn.commit()
    conn.close()

# ------------------------------------------------------users--------------------------------------------------------------------

def search_cat1(filename, cat):
    conn = sqlite3.connect(filename)
    curs = conn.cursor()
    curs.execute("""SELECT id FROM categories
                                WHERE categ_name=(?)""", (cat,))
    cat_id = curs.fetchone()[0]
    if cat_id == None:
        return None
    curs.execute("""SELECT * FROM products
                            WHERE category=(?)""", (cat_id,))
    res = curs.fetchall()
    return res

def search_cat(filename, cat):
    conn = sqlite3.connect(filename)
    curs = conn.cursor()
    curs.execute("""SELECT id FROM categories
                                WHERE categ_name=(?)""", (cat,))
    try:
        cat_id = curs.fetchone()[0]
    except TypeError:
        print(1)
        res = f"<tr>  " \
              f"<th>Такої категорії {cat} немає</th>    " \
              f"</tr>"
        return res
    curs.execute("""SELECT * FROM products
                            WHERE category=(?)""", (cat_id,))
    res = curs.fetchall()
    dct = {}
    for elem in res:
        dct[elem[0]] = (elem[1], elem[2], elem[3], elem[4],elem[5], elem[6])
    return dct

def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

def search_prod(filename, prod):
    conn = sqlite3.connect(filename)
    curs = conn.cursor()
    conn.create_function("REGEXP", 2, regexp)
    curs.execute('SELECT * FROM products WHERE name REGEXP ?', [f'(\w+{prod}\w+)|({prod}\w+)|(\w+{prod})|({prod})'])
    f = curs.fetchall()
    if len(f)==0:
        res = f"<tr>  " \
              f"<th>Такого продукту {prod} немає</th>    " \
              f"</tr>"
        return res
    dct = {}
    for elem in f:
        dct[elem[0]] = (elem[1], elem[2], elem[3], elem[4], elem[5], elem[6])
    return dct

def get_total(dct):
    res_sum=0
    print(dct)
    for key,values in dct.items():
        res_sum+=values[-3]*values[-2]
    return res_sum

def dct_for_main(filename):
    dct_res = {}
    conn = sqlite3.connect(filename)
    curs = conn.cursor()
    curs.execute("SELECT * FROM products")
    res = curs.fetchall()
    for item in res:
        dct_res[item[0]] = [*item[1:]]
    print(dct_res)
    return dct_res

if __name__ == '__main__':
    #add_category("products.db")
    add_product("products1.db")
    #print(search_prod("products.db", "Apple"))