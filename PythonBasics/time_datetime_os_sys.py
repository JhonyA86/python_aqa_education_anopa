import datetime
import time
import os
import sys


dt = datetime.datetime(1986, 4, 6, 4, 0)
print(dt)
print(dt.time())
print(dt.date())
print(datetime.datetime.now())


action = "to feed the dog"
current_time = time.asctime()
print(f"It's {current_time}. Time {action}")
print(time.timezone / 3600)


print(dir(os))
print(os.getcwd())
print(os.getlogin())
print(os.name)


print(sys.flags)
print(sys.float_info.dig)
print(sys.implementation)
print(sys.copyright)
print(sys.path)
