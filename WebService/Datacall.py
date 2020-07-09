# -*- coding: utf-8-*-
import pymysql

Host = '127.0.0.1'
Port = 3306
User = 'LotusDream'
Password = '123456'
DBTable = 'fortest'

dbcon=0
cursor=0

def __init__():
    try:
        global dbcon,cursor
        dbcon = pymysql.connect(host = Host, port = Port, user = User, passwd = Password, db = DBTable, charset = 'utf8', cursorclass = pymysql.cursors.DictCursor)
        cursor = dbcon.cursor()
        return 0
    except Exception as e:
        return 1

def ExeSql(sqlstr):
    try:
        if(__init__()!=0):
            return 1
        global dbcon, cursor
        cursor.execute(sqlstr)
        dbcon.commit()
    except Exception as e:
        print(e)
        dbcon.rollback()
    finally:
        if dbcon:
            Dispose()

def GetData(sqlstr):
    data=""
    try:
        if(__init__()!=0):
            return data
        global dbcon, cursor
        cursor.execute(sqlstr)
        dbcon.commit()
        data=cursor.fetchall()

    except Exception as e:
        dbcon.rollback()
        print(e)
    finally:
        if dbcon:
            Dispose()
    return data


def Dispose():
    global dbcon, cursor
    cursor.close()
    dbcon.close()

# if __name__ == "__main__":
#     d =GetData('select * from detail')
#     for row in d:
#         #for cl in row:
#         #type(row)
#         print(row["f_carno"])
#     print("-------------------------")
#     print(d[1]["f_carno"])
    #dbtest.Dispose()