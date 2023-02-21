#Lab Partners: Michelle Arredondo and Nayeli De Leon
#https://github.com/michellle1/lab-04

"""EE 250L Lab 04 Part 2 Code"""

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))


if __name__ == '__main__':
    #rpi IP address
    ip_address=0
    """your code here"""
    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python. For example:
    
    `client.connect("eclipse.usc.edu", 11000, 60)` 
    
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    time.sleep(1)

    while True:
        #replace user with your USC username in all subscriptions
        client.publish("mearredo/ipinfo", f"{ip_address}")
        print("Publishing ip address")
        time.sleep(4)

        #get date and time 
        """your code here """
        #getting date: (source: https://www.programiz.com/python-programming/datetime/current-datetime) 
        
        from datetime import date
        today = date.today()
        
        #getting time: (source https://www.programiz.com/python-programming/datetime/current-time) 
        
        import pytz
        
        #getting timezone object for California
        tz_LA = pytz.timezone('America/Los_Angeles')
        
        #getting current time in California
        datetime_LA = datetime.now(tz_LA)
        
        t = datetime_LA.strftime("%H: %M: %S") 
          
        #publish date and time in their own topics
        """your code here"""
        client.publish("mearredo/date", f"{today}")
        print("Publishing date")
        
        client.publish("mearredo/time", f"{t}")
        print("Publishing time")
