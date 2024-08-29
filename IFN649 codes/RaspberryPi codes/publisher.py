mport paho.mqtt.publish as publish
publish.single("ifn649", "Hello World", hostname="3.106.228.95")
print("Done")
