#Welcome Branch

#Libraries Imported Here
import sys
import time

print("\nWelcome Branch - Developer: Kiera McKimmy")
print("\nWelcome to InfotechCenter V.1.0")


x = 0
ellipsis = 0

while x != 20:
    x += 1
    ellipsisMessage = ("InfotechCenter OS Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\nOperating System Booted Up - Retina Scanned - Access Granted")