class Device:
    def __init__(self, name, protocol):
        self.name = name
        self.protocol = protocol

    def upgrade_to_dual_stack(self):
        self.protocol = "Dual Stack"

    def upgrade_to_ipv6(self):
        self.protocol = "IPv6"

class InstitutionNetwork:
    def __init__(self, name):
        self.name = name
        self.devices = []

    def add_device(self, name, protocol):
        self.devices.append(Device(name, protocol))

    def display_network_status(self):
        print(f"\nNetwork Status for {self.name}:")
        for d in self.devices:
            print(f" - {d.name}: {d.protocol}")
        print()
