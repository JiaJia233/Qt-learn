# -*- coding: utf-8-*-
import pymssql

Server = "192.134.2.139\SQL2008"
User = "sa"
Password = "sa123"
Database = "Test"

dbcon = 0
cursor = 0


def __init__():
    try:
        global dbcon, cursor
        dbcon = pymssql.connect(server=Server, user=User, password=Password, database=Database, charset="utf8", as_dict=True)
        cursor = dbcon.cursor()
        return 0

    except Exception as e:
        print(e)
        return -1


def ExqSql(sqlstr):
    global dbcon, cursor
    try:
        if __init__() != 0:
            return -1
        cursor.execute(sqlstr)
        dbcon.commit()

    except Exception as e:
        print(e)
        dbcon.rollback()
        return -1

    finally:
        if dbcon:
            Dispose()


def GetData(sqlstr):
    data=""
    global dbcon, cursor
    try:
        if __init__()!=0:
            return data
        cursor.execute(sqlstr)
        data=cursor.fetchall()

    except Exception as e:
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
#     d =GetData('Select * from t_member')
#     for row in d:
#         #for cl in row:
#         #type(row)
#         print(row["f_name"])
#         # print("-------------------------")
#         # print(d[1]["f_name"])