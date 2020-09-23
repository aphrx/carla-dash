from django.shortcuts import render
from django.http import HttpResponse
from time import gmtime, strftime
import threading
import json
import cantools
import can

db = cantools.database.load_file("honda.dbc")
can_bus = can.interface.Bus('vcan0', bustype='socketcan')

context = {
        'speed': 0,
        'gear': 'P',
        'steering': 0,
        'time': strftime("%I:%M %p", gmtime())
    }

def update():
    while True:
        message = can_bus.recv()
        if(message.arbitration_id == 777):
            speed = int(db.decode_message(message.arbitration_id, message.data)['CAR_SPEED'])
            context.update(speed = speed)
        elif(message.arbitration_id == 419):
            gear = db.decode_message(message.arbitration_id, message.data)['GEAR']
            context.update(gear = gear)
        elif(message.arbitration_id == 330):
            steer = db.decode_message(message.arbitration_id, message.data)['STEER_WHEEL_ANGLE']
            context.update(steering = steer/1.3)
        time = strftime("%I:%M %p", gmtime())
        context.update(time = time)

def home(request):
    return render(request, 'dash/dash.html', context)

def canbus(request):
    
    return HttpResponse(json.dumps(context), content_type='application/json')

b = threading.Thread(name='update', target=update)
b.start()