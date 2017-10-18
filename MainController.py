# coding: utf-8
import DBController as DBC
import streaming as st
from flask import Flask, render_template, request, jsonify, Response

app = Flask(__name__)

db = DBC.DBManager()

def dataSelectID(id):
    print(id, "조회")

def dataInsert(id, name, phone):
    print(id, name, phone, "삽입")
    
def dataUpdate(id, name, phone):
    print(id, name, phone, "수정")
    
def dataDelete(id):
    print(id, "삭제")
    
def dataSelectAll():
    print("모든 데이터 조회")

@app.route('/chkpw', methods=["GET"])
def chkpw():

    pw = request.args.get('pw')

    print(pw)
    result = jsonify( {"result" : db.comparePW( pw )})
    return result

@app.route('/GET/ID', methods=["GET"])
def get_id():

    id = request.args.get('id')
    rs = dataSelectID(id)

    try:
        result = jsonify( {"result" : "success", "id" : rs[0], "name" : rs[1], "phone" : rs[2]} )
    except:
        result = jsonify({"result": "fail"})
    return result

@app.route("/POST/CREATEID", methods=["POST"])
def create_id():
    id = request.form['id']
    name = request.form['name']
    phone = request.form['phone']

    result = dataInsert(id, name, phone)
    return jsonify({"result" : result})

@app.route("/PUT/UPDATEID", methods=["POST"])
def update_id():
    id = request.form['id']
    name = request.form['name']
    phone = request.form['phone']

    result = dataUpdate(id, name, phone)
    return jsonify({"result" : result})

@app.route("/DELETE/DELETEID", methods=["POST"])
def delete_id():
    id = request.form['id']

    result = dataDelete(id)
    return jsonify({"result" : result})

@app.route("/GET/ALLID", methods=["POST"])
def get_allid():
    #result = jsonify( {"result" : "success", "id" : rs[0], "name" : rs[1], "phone" : rs[2]} )

    result = []

    data = dataSelectAll()
    for item in data:
        result.append({"id" : item[0], "name" : item[1], "phone" : item[2]})

    print(result)

    return jsonify(result)

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route("/video")
def video():
    return render_template('video.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/config')
def config():
    return render_template('config.html')

@app.route('/control')
def control():
    return render_template('control.html')

@app.route('/cctv')
def cctv():
    return render_template('cctv.html')

@app.route('/streaming')
def streming():
    return render_template('streaming.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/video_feed')
def video_feed():
    img = st.gen()

    try:
        #result = Response(img, mimetype='multipart/x-mixed-replace; boundary=frame')
        result = Response(img, mimetype='video/mp4; boundary=frame')
    except:
        print("error")
        result = None

    return result

@app.route('/')
def init():
    return render_template('init.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888, threaded = True)
    print("Server shutdown..")
