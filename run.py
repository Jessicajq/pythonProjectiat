#-*-coding:utf-8 -*-

from app import app,socketio
import subprocess ,sys

def runTimingCheck():
    subprocess.Popen('python runTimingCheck.py main',shell=True)
@app.route('/users', methods=['GET'])
def check():
    print('hello', sys.path)
    return "12345", sys.path

if __name__ == '__main__':
  runTimingCheck()
  check()
  socketio.run(app,host='0.0.0.0', port=5000, debug=True, use_reloader=False)
  #http://10.11.41.84:8000/
