import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "n8g2zz",
        "typeId": "firstDevice",
        "deviceId":"00001"
    },
    "auth": {
        "token": "kP82(YEkB9IsKgEW!J"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['BookedTickets'])
    m=cmd.data['BookedTickets']
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
