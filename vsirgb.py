from time import sleep

import clr #package pythonnet, not clr

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
    handle.MainboardEnabled = True
    handle.CPUEnabled = True
    handle.RAMEnabled = True
    handle.GPUEnabled = True
    handle.HDDEnabled = True
    handle.Open()
    return handle


def print_info(handle):
    for hardware in HardwareHandle.Hardware:
        print(f"{hwtypes[hardware.HardwareType]} ({hardware.HardwareType}), {hardware.Name}:")
        hardware.Update()
        for sensor in hardware.Sensors:
            print("\t- %-24s%-24s%-24s" % (f"{sensortypes[sensor.SensorType]} ({sensor.SensorType})",
                                           f"{sensor.Name} ({sensor.Index})",
                                           sensor.Value))

        for subHardware in hardware.SubHardware:
            print(f"\t{subHardware.Name}")
            subHardware.Update()
            for sensor in subHardware:
                print("\t\t- %-24s%-24s%-24s" % (f"{sensortypes[sensor.SensorType]} ({sensor.SensorType})",
                                                 f"{sensor.Name} ({sensor.Index})",
                                                 sensor.Value))

def get_data(handle):
    data_string = chars.SEQUENCE_START
    for hardware in handle.Hardware:
        hardware.Update()
        for sensor in hardware.Sensors:
            data_string += (f"{hardware.HardwareType}{chars.SEPARATOR}"
                            f"{sensor.Index}{chars.SEPARATOR}"
                            f"{sensor.Name}{chars.SEPARATOR}"
                            f"{sensor.Value}{chars.SEPARATOR}")
    data_string = data_string[:-1] + chars.SEQUENCE_END
    return data_string
        
    

    
if __name__ == "__main__":
    HardwareHandle = initialize_openhardwaremonitor()
    print_info(HardwareHandle)
    while True:
        sleep(waittime)
        #send(get_data(HardwareHandle))
        print("hello")
    


