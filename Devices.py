import random

class Device:
    """
    Device class is the parent class of all devices.
    """
    def __init__(self, id):
        """
        this is the constructor of the Device class.
        it takes an id as a parameter and sets the mode to Off.
        """
        self.mode = "Off"
        self.id = id
        self.values = []

    def turn_on(self):
        """
        this method sets the mode to On.
        """
        self.mode = "On"

    def turn_off(self):
        """
        this method sets the mode to Off.
        """
        self.mode = "Off"
        
    def set_mode(self, isOn):
        """
        this method sets the mode to On or Off.
        """
        self.mode = "On" if isOn else "Off"

    def get_mode(self):
        """
        this method returns the mode of the device.
        """
        return self.mode

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class CCTV (Device):
    """
    CCTV class is a child class of Device.
    It has a motion sensor and infrared sensor.
    """
    def __init__(self):
        super().__init__("CCTV")
        self.infrared = "Off"
        self.motion = "Off"
        self.values = ["On", "Off"]

    def set_motion(self, motion):
        """
        this method sets the motion sensor to On or Off.
        """
        self.motion = "On" if motion else "Off"

    def get_motion(self):
        """
        this method returns the motion sensor state.
        """
        return self.motion

    def set_infrared(self, infrared):
        """
        this method sets the infrared sensor to On or Off.
        """
        self.infrared = "On" if infrared else "Off"

    def get_infrared(self):
        """
        this method returns the infrared sensor state.
        """
        return self.infrared

    def toggle_infrared(self):
        """
        this method toggles the infrared sensor state.
        """
        self.infrared = "On" if self.infrared == "Off" else "Off"
    
    def toggle_motion(self):
        """
        this method toggles the motion sensor state.
        """
        self.motion = "On" if self.motion == "Off" else "Off"
        self.mode = "On" if self.motion == "On" else "Off"

    def randomize(self):
        """
        this method randomizes the motion and infrared sensors.
        new values are generated randomly in the range [0, 1]
        where 0 is Off and 1 is On.
        """
        new_mode_motion = random.randint(0, 1)
        new_mode_infrared = random.randint(0, 1)

        self.set_motion(new_mode_motion)
        self.set_infrared(new_mode_infrared)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Light (Device):
    """
    Light class is a child class of Device.
    It has a brightness sensor.
    """
    def __init__(self):
        super().__init__("Light")
        self.brightness = 0
        self.values = [i for i in range(0, 101)]

    def set_brightness(self, brightness):
        """
        this method sets the brightness of the light.
        """
        self.brightness = brightness
    
    def get_brightness(self):
        """
        this method returns the brightness of the light.
        """
        return self.brightness
    
    def increase_brightness(self):
        """
        this method increases the brightness of the light.
        """
        if self.brightness < 100:
            self.brightness += 1
    
    def decrease_brightness(self):
        """
        this method decreases the brightness of the light.
        """
        if self.brightness > 0:
            self.brightness -= 1

    def randomize(self):
        """
        this method randomizes the brightness of the light.
        """
        new_mode = random.randint(0, 1)
        new_bright = random.randint(0, 1)
        
        if new_bright == 0:
            self.increase_brightness()
        else:
            self.decrease_brightness()
        
        self.set_mode(new_mode)
            
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Thermostat (Device):
    """
    Thermostat class is a child class of Device.
    It has a temperature sensor.
    """
    def __init__(self):
        """
        this is the constructor of the Thermostat class.
        it sets the temperature to 20 (default)
        """
        super().__init__("Thermostat")
        self.temperature = 20
        self.values = [i for i in range(-40, 41)]

    def set_temperature(self, temperature):
        """
        this method sets the temperature of the thermostat.
        """
        self.temperature = temperature

    def get_temperature(self):
        """
        this method returns the temperature of the thermostat.
        """
        return self.temperature

    def increase_temperature(self):
        """
        this method increases the temperature of the thermostat.
        """
        if self.temperature < 100:
            self.temperature += 1

    def decrease_temperature(self):
        """
        this method decreases the temperature of the thermostat.
        """
        if self.temperature > 0:
            self.temperature -= 1

    def randomize(self):
        """
        this method randomizes the temperature of the thermostat.
        new values are generated randomly in range [0, 1]
        where 0 is decrease and 1 is increase.
        """
        new_temp = random.choice([1,1,0])
        if new_temp == 1:
            self.increase_temperature()
        else:
            self.decrease_temperature()

        new_mode = random.randint(0, 1)
        self.set_mode(new_mode)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Window (Device):
    """
    Window class is a child class of Device.
    It has a mode state (Open or Closed).
    """
    def __init__(self):
        """
        this is the constructor of the Window class.
        it sets the mode to Closed (default)
        """
        super().__init__("Window")
        self.mode = "Closed"

    def window_close(self):
        """
        this method sets the mode to Closed.
        """
        self.mode = "Closed"

    def window_open(self):
        """
        this method sets the mode to Open.
        """
        self.mode = "Open"

    def set_mode(self, mode):
        """
        this method sets the mode to Open or Closed.
        """
        self.mode = mode

    def randomize(self):
        """
        this method randomizes the mode of the window.
        new values are generated randomly in the list
        with proper values.
        """
        new_mode = random.choice(["Open", "Closed"])
        self.set_mode(new_mode)