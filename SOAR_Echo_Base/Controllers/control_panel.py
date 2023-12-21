from Config import *
import Services.lora as lora
from flask import Flask, render_template, jsonify

@app.route('/')
def control_panel():
    return render_template('control_panel.html')

@app.route('/random_cmd')
def random_cmd():
    # Trigger deployment of the payload
    # Sending an RF signa
    lora.send_random()
    return "Hello from server"

@app.route('/start_serial/<port>')
def start_serial(port = "COM7"):
    try:
        lora.connect(port)
        print(f'Stablishing serial {port}')
    except Exception as e:
        print(f'Error connecting to serial: {e}')

@app.route('/serial_input/<message>')
def serial_input(message):
    try:
        lora.serial_input(message)
    except Exception as e:
        print(f'Exception with Serial Input')
        return jsonify
    return jsonify(message='OK'),200

def log_lora(message):
    socketio.emit('lora_log', {'message':message})

def log_serial(message):
    socketio.emit('serial_log', {'message', message})