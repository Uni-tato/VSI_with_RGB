from time import sleep
import re

import clr # pythonnet package
import serial
import json

import characters as chars
import config

waittime = 60/config.UPDATES_PER_MINUTE

hwtypes = ['Mainboard','SuperIO','CPU','RAM','GpuNvidia','GpuAti','TBalancer','Heatmaster','HDD']
sensortypes = ['Voltage','Clock','Temperature','Load','Fan','Flow','Control','Level','Factor','Power','Data','SmallData']

def initialize_openhardwaremonitor():
    # https://stackoverflow.com/a/49909330
    file = r'OpenHardwareMonitorLib'
    clr.AddReference(file)

    from OpenHardwareMonitor import Hardware

    handle = Hardware.Computer()
    handle.MainboardEnabled = config.MAINBOARD_ENABLED
    handle.CPUEnabled = config.CPU_ENABLED
    handle.RAMEnabled = config.RAM_ENABLED
    handle.GPUEnabled = config.GPU_ENABLED
    handle.HDDEnabled = config.HDD_ENABLED
    handle.FanControllerEnabled = config.FAN_CONTROLLER_ENABLED
    handle.Open()
    return handle


def print_info(handle):
    '''
        Creates a nice little table of info.
        Very useful when editing the arduino code.
    '''
    for hardware in handle.Hardware:
        print(f"{hwtypes[hardware.HardwareType]} ({hardware.HardwareType}), {hardware.Name}:")
        hardware.Update()
        # Probably the first update, in some cases sensors will return none,
        # the user should know which sensors return none so they can plan accordingly or fix.

        # Print the sensor data.
        for sensor in hardware.Sensors:
            print("\t- %-24s%-24s%-24s" % (f"{sensortypes[sensor.SensorType]} ({sensor.SensorType})",
                                           f"{sensor.Name} ({sensor.Index})",
                                           sensor.Value))

        # Does the same thing with subhardware.
        # Note: subhardware is not yet sent to controller.
        for subHardware in hardware.SubHardware:
            print(f"\t{subHardware.Name}")
            subHardware.Update()
            for sensor in subHardware:
                print("\t\t- %-24s%-24s%-24s" % (f"{sensortypes[sensor.SensorType]} ({sensor.SensorType})",
                                                 f"{sensor.Name} ({sensor.Index})",
                                                 sensor.Value))
## Old stuff
##def get_data(handle):
##    '''
##        Updates the hardware and compiles the data into a simple packet.
##    '''
##    data_string = chars.SEQUENCE_START
##    for hardware in handle.Hardware:
##        hardware.Update()
##        # Nonetypes should be handled controller side to keep this as minimal as possible.
##        for sensor in hardware.Sensors:
##            data_string += (f"{hardware.HardwareType}{chars.SEPARATOR}"
##                            f"{sensor.SensorType}{chars.SEPARATOR}"
##                            f"{sensor.Index}{chars.SEPARATOR}"
##                            f"{sensor.Value}{chars.SEPARATOR}")
##    data_string = data_string[:-1] + chars.SEQUENCE_END # replaces last sep char with the end char.
##    return data_string
##        
##def send(data_string, serial):
##    '''
##        Uses serial communication to send the data string to the controller.
##    '''
##    raw = bytes(data_string, 'utf-8')
##    serial.write(raw)

def get_colour(colourmap, lower_bound, upper_bound, value):
    pass

def send(data):
    pass

def get_settings():
    with open("settings.json") as file:
        string = file.read()
    for sub_string in re.findall(r'(//[^\n]*)\n', string):
        string = string.replace(sub_string, '') # Gotta find a better way of doing this.
    settings = json.loads(string)
    return settings

def read_and_send(handle, serial):
    settings = get_settings()
    for hardware in handle.Hardware:
        hardware.Update()
        for sensor in hardware.Sensors:
            control_info = settings[hardware.HardwareType][sensor.SensorType]
            if control_info and control_info[sensor.Index]:
                send(get_colour(control_info[sensor.Index]["colourmap"],
                                control_info[sensor.Index]["lower_bound"],
                                control_info[sensor.Index]["upper_bound"],
                                sensor.Value))

def read(serial):
    data = serial.readline()
    return data if data else None
    
if __name__ == "__main__":
    HardwareHandle = initialize_openhardwaremonitor()
    #print_info(HardwareHandle)
    serial = serial.Serial(port = config.PORT, baudrate = config.BAUDRATE)
    sleep(1) # give it a little time to make sure it's connected
    print("ready")
    while True:
        sleep(waittime)
        read_and_send(HardwareHandle, serial)
        
    


