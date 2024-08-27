import random

class DeviceController:
    """
    DeviceController class is where all devices are
    stored and managed/controlled.
    """
    devices = []

    def __init__(self, devices=None):
        """
        this is the constructor of the DeviceController class.
        it takes a list of devices as a parameter and sets
        the devices to the given list or an empty list.
        """
        if devices is None:
            self.devices = []
        else:
            self.devices = devices

    def add_device(self, device):
        """
        this method adds a device to the list of devices.
        """
        self.devices.append(device)

    def get_devices(self):
        """
        this method returns the list of devices.
        """
        return self.devices
    
    def get_device(self, name):
        """
        this method returns the device with the given name.
        """
        for device in self.devices:
            if device.id == name:
                return device
        return None
    
    def randomizer(self):
        """
        this method randomizes all devices that 
        are in the list of current class
        """
        for device in self.devices:
            if random.choice([1,1,1, 0]):
                device.randomize()
    