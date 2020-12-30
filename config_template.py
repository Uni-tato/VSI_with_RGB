'''
Create a copy of this file named: "config.py".
You should then edit these values in the copy to best suit your use.

For example if you wanted your leds to only show cpu temp then you would only need to
check the cpu, and therefore should set CPU_ENABLED to True and set the others to False.

'''

# --- Monitor ---
MAINBOARD_ENABLED = True
CPU_ENABLED = True
RAM_ENABLED = True
GPU_ENABLED = True
HDD_ENABLED = True
FAN_CONTROLLER_ENABLED = True

# --- Update ---
UPDATES_PER_MINUTE = 1
# Note: to minimise the impact we don't compensate for the time it takes to
# actually preform the checks/communication, therefore the update frequecy will
# be slightly less than it should be.

# --- Communication ---
PORT = 'COM1' # You can check the port you're using in the arduino ide.
BAUDRATE = 9600 # Make sure that this matches the rate on the arduino side.
