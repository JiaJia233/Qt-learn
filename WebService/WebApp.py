from flask import Flask, session, redirect, request,render_template,make_response
from datetime import datetime
from io import BytesIO
from gevent.pywsgi import WSGIServer
import time
import xlwt
import Datacall
from threading import Thread
from gevent import monkey

app = Flask(__name__,
            static_url_path='/static',      # 访问静态资源的url前缀, 默认值是static
            static_folder='static',         # 静态文件的存放目录，默认就是static
            template_folder="templates",    # 模板文件的目录，默认是tjddddd
            #static_folder="static"
            #static_url_path="/static"
            )
Login_State = False
@app.route('/')
def Index():
    return redirect('/login')

@app.route('/login',methods=['POST','GET'])
def Login():
    global Login_State
    Login_State = False
    if request.method == 'POST':
        sql = "Select * From t_person Where f_number = '" + request.form["username"] + "'"
        bizdata = Datacall.GetData(sql)
        if bizdata != "":
            if bizdata[0]['f_password'] == request.form["password"]:
                if bizdata[0]['f_access'] == '管理员':
                    Login_State = True
                    return render_template('DataRequery.html')
                else:
                    return render_template('DataRequery2.html')
            else:
                err = "错误的密码"
                return render_template('login.html', errx=err)
        else:
            err = "错误的用户名"
            return render_template('login.html', errx=err)
    else:
        return redirect('/login')

@app.route('/datarequery', methods=['POST','GET'])
def DataRequery():
    global Login_State
    if Login_State:
        if request.method == 'POST':
            pass
        else:
            return render_template('DataRequery.html')
    else:
        return redirect('/login')

@app.route('/datarequery2', methods=['POST','GET'])
def DataRequery2():
    pass

@app.route('/management',methods=['POST','GET'])
def Management():
    global Login_State
    if Login_State:
        if request.method == 'POST':
            pass
        else:
            return render_template('Management.html')
    else:
        return redirect('/login')

@app.route('/fomular',methods=['POST','GET'])
def Fomular():
    global Login_State
    if Login_State:
        if request.method == 'POST':
            pass
        else:
            return render_template('Fomular.html')
    else:
        return redirect('/login')

@app.route('/material',methods=['POST','GET'])
def Material():
    global Login_State
    if Login_State:
        if request.method == 'POST':
            pass
        else:
            return render_template('Material.html')
    else:
        return redirect('/login')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)