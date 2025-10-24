class IPv6Transition:
    def __init__(self, network):
        self.network = network

    def apply_dual_stack(self):
        print("🔄 Applying Dual-Stack Transition...")
        for device in self.network.devices:
            if device.protocol == "IPv4":
                device.upgrade_to_dual_stack()
        print("✅ Dual-Stack applied successfully.\n")

    def apply_tunneling(self):
        print("🌉 Establishing Tunneling Mechanism...")
        print("Tunneling IPv6 packets through IPv4 networks...")
        print("✅ Tunnel established successfully.\n")

    def finalize_transition(self):
        print("🚀 Migrating all devices to full IPv6 support...")
        for device in self.network.devices:
            device.upgrade_to_ipv6()
        print("✅ Transition to IPv6 completed!\n")
