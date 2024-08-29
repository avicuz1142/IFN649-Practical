import paho.mqtt.publish as publish
publish.single("ifn649", "LED_OFF", hostname="3.106.228.95")
print("Turned off LED")
