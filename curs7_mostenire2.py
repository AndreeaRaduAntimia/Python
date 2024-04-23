class Device:
    power = "off"
    operating_system = None
    device_type = None
    processor = None
    size = "Mare"

    def change_power_state(self, power_change):
        self.power = power_change

    def connect_wireless(self):
        print('You are now connected to the network')

class Tablet(Device):
    size = None

ios_tablet = Tablet()
print(ios_tablet.power)
ios_tablet.change_power_state("on")
print(f"Starea tabletei: {ios_tablet.power}")
ios_tablet.operating_system = "android"
print(f"Sistemul de operare al tabletei: {ios_tablet.operating_system}")
ios_tablet.device_type = "tablet"
print(f"Tipul de device: {ios_tablet.device_type}")
ios_tablet.processor = "i7"
print(f"Procesorul tabletei: {ios_tablet.processor}")
ios_tablet.connect_wireless()
print(ios_tablet.size)

