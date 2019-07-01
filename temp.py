from sense_hat import SenseHat
from time import gmtime, localtime, strftime, time
import time

sense = SenseHat()
sense.set_rotation(180)

sense.low_light = True

while True:
    temp = sense.get_temperature() - 9 
    humidity = sense.get_humidity()
    message = "%sc - %s" % (int(temp), strftime("%H:%M", localtime()))
    print(message)
    sense.show_message(message)
    time.sleep(1)
 
    # for i in  chars:
    #     sense.show_letter("%s" % i)
    #     time.sleep(1)

#print("Temperature: %s C" % int(temp) )

#print("Temperature: %s C" % temp)

# alternatives
#print(sense.temp)
#print(sense.temperature)
