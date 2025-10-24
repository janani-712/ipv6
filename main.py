from network import InstitutionNetwork
from transition_model import IPv6Transition

def main():
    print("🌐 IPv6 Transition and Implementation Model for Smart Institutions\n")

    # Create institutional network
    institution = InstitutionNetwork("Smart University")

    # Add IPv4 devices
    institution.add_device("Library Server", "IPv4")
    institution.add_device("IoT Sensor 1", "IPv4")
    institution.add_device("Admin PC", "IPv4")

    # Add IPv6-ready devices
    institution.add_device("Smart Classroom", "IPv6")
    institution.add_device("IPv6 Gateway", "IPv6")

    # Display initial status
    institution.display_network_status()

    # Start transition
    transition = IPv6Transition(institution)
    transition.apply_dual_stack()
    transition.apply_tunneling()
    transition.finalize_transition()

    # Display final status
    institution.display_network_status()

if __name__ == "__main__":
    main()
