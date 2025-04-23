class SmartLight:

    def __init__(self, location, brightness = 100):
        """
                1) Constructor: set up a new light with
                   - location (e.g. "kitchen")
                   - brightness (0–100 scale, default 100)
                   - on/off state (starts off)
                """
        self.location = location
        self.on = False
        self.brightness = brightness

    def toggle(self):
        if  not self.on:
            self.on = True
        else:
            self.on = False
        state = "on" if self.on else "off"
        print(f"💡 The '{self.location}' lamp is now {state}.")

    def dim(self, new_brightness):
        """
        brightness changes only if the light is on
        :param new_brightness:
        :return:
        """
        if not self.on:
            print(f"⚠️  Cannot dim '{self.location}' because it’s off.")
            return

        old= self.brightness
        self.brightness = max(0, min(100, new_brightness)) #set the brightness level (0-100)
        print(f"🕯 Brightness for the '{self.location}' lamp changed from {old}% to {self.brightness}%.")

    def info(self):
        print(f"----- SmartLight Information -----")
        print(f"Location: {self.location}")
        print(f"Brightness: {self.brightness}")
        print(f"Turned on: {'Yes' if self.on else 'No'}")
        print("--------------------------------------")


bulb = SmartLight("kitchen", 40)

# View the initial state
bulb.info()

# Turn it on
bulb.toggle()

# Dim it to 20%
bulb.dim(20)

#Show the updated info
bulb.info()



