import logging
import os

from src.network_device import NetworkDevice
from src.utils_parser import parse_csv, parse_json, parse_xml, parse_yaml


os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/lab.log", level=logging.INFO)


def main():
    """Parse the lab data, create device objects, and print required messages."""
    devices = parse_json("data/devices.json")
    yaml_data = parse_yaml("data/interfaces.yaml")
    vlans = parse_xml("data/vlans.xml")
    inventory = parse_csv("data/inventory.csv")

    for device_data in devices:
        device = NetworkDevice(
            device_data["hostname"],
            device_data["ip"],
            device_data["type"],
        )
        device.summarize()

    interfaces = yaml_data.get("interfaces", []) if isinstance(yaml_data, dict) else []
    for interface in interfaces:
        msg = f"Interface {interface['name']} is {interface['status']}"
        print(msg)
        logging.info("INTERFACE_MSG: %s", msg)

    for device in inventory:
        msg = f"Device {device['hostname']} is a {device['location']} {device['role']}"
        print(msg)
        logging.info("DEVICE_MSG: %s", msg)

    for vlan in vlans:
        msg = f"VLAN {vlan['id']} is the {vlan['name']}"
        print(msg)
        logging.info("VLAN_MSG: %s", msg)


if __name__ == "__main__":
    logging.info("LAB1_START")
    main()
    logging.info("LAB1_END")    