from flask import Flask

FAI=Flask(__name__)

@FAI.route('/wish/<name>')
def wish(name):
    return f'hello world {name}'

@FAI.route('/greetings')
def greetings():
    return "all the best"


if __name__=='__main__':
    FAI.run(debug=True,port=5001,host='192.168.43.21')