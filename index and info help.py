import vsirgb

print("For more info please run as administrator")
print("This may take a moment...")
HardwareHandle = vsirgb.initialize_openhardwaremonitor()
vsirgb.print_info(HardwareHandle)
input("Press enter to continue")
