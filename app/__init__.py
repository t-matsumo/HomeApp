from flask import Flask, render_template, request
from app import config_development, config_production

# ENVIRONMENT is 'development' or 'production'
ENVIRONMENT = 'development'

app = Flask(__name__)

if ENVIRONMENT == 'development':
    app.config.from_object(config_development)
elif ENVIRONMENT == 'production':
    app.config.from_object(config_production)
else:
    print("error:ENVIRONMENT must be 'development' or 'production'!!")
    exit(1)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('root/index.html')

@app.route('/remote_controller/light', methods=['GET'])
def remote_controller_light():
    return render_template('remote_controller/light.html')

@app.route('/remote_controller/light', methods=['POST'])
def remote_controller_light_ajax():
    b = request.form['b']
    if b == 'brightest':
        pass
    elif b == 'darker':
        pass
    elif b == 'brighter':
        pass
    elif b == 'out':
        pass

    # 何も返さない
    return b
