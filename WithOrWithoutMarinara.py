# Welcome Branch
# Libraries Imported Here
import sys
import time

# ===== ANSI Color Codes =====
CYAN = "\033[96m"
GREEN = "\033[92m"
RESET = "\033[0m"

# ===== Welcome Messages (UNCHANGED) =====
print("\nWelcome Branch - Developer: Kiera McKimmy")
print("\nWelcome to InfotechCenter V.1.0")

# ===== Variable Initialization =====
x = 0                 # Loop counter to control boot duration
ellipsis = 0          # Controls number of dots in animation

# ===== Boot Animation Loop =====
while x != 20:
    x += 1  # Increment loop counter

    # Build boot message with animated ellipsis
    ellipsisMessage = (
        CYAN + "InfotechCenter OS Booting" + "." * ellipsis + RESET
    )

    ellipsis += 1  # Increase dots each cycle

    # Overwrite the current terminal line with updated message
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()

    # Pause to simulate boot processing
    time.sleep(.5)

    # Reset ellipsis after 3 dots
    if ellipsis == 4:
        ellipsis = 0

    # Final boot confirmation message
    if x == 20:
        print(
            GREEN
            + "\nOperating System Booted Up - Retina Scanned - Access Granted"
            + RESET
        )