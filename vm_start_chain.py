#Lab Partners: Michelle Arredondo and Nayeli De Leon
#https://github.com/michellle1/lab-04

"""EE 250L Lab 04 Starter Code . This is Ping Publisher. 
Run vm_sub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    
    #replace user with your USC username in all subscriptions
    client.subscribe("mearredo/pong")
    
    #publish initial integer value to begin counter between VMs
    #initial number
    initialNum= int(0)
    client.publish("mearredo/ping", f"{initialNum}")
    print ("Publishing initial integer")
    
    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("mearredo/pong", on_message_from_pong)
    time.sleep(4)
	 
   
#Custom message callback. And then publish a new message to subscribers (i.e to pong)
def on_message_from_pong(client, userdata, message):
   print("Custom callback  - integer: "+ message.payload.decode())
   num=int(message.payload.decode()) #message from pong --> convert to int
   NUM = num + 1
   
   #replace user with your USC username in all subscriptions
   time.sleep(4)
   client.publish("mearredo/ping", f"{NUM}")
   print("Publishing integer: " + f"{NUM}")
   
   
   

if __name__ == '__main__':
    #get IP address
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

    client.connect(host="172.20.10.8", keepalive=60)
    
    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    time.sleep(1)
    
    while True:
    	pass
	    
    

	 
   

 
        
      
