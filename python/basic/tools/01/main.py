from abc import ABC, abstractmethod
import sys
import logging

logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
logger = logging.getLogger(__name__)


class CreateConfig(object):
    def __init__(self, _template_file: str, _devices_file: str):
        self.template_file = _template_file
        self.devices_file = _devices_file
        self.template_config = []
        self.created_config = []
        self.devices_list = []

    def import_template(self):
        with open(self.template_file, 'r', encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                # print(line)
                self.template_config.append(line)

    def import_input_list(self):
        with open(self.devices_file, 'r', encoding="utf-8") as f:
            # header = f.readline().strip().split(",")
            headers = []
            device = {}
            lines = f.readlines()
            for cnt, line in enumerate(lines):
                line = line.rstrip("\n")
                items = line.split(",")
                if cnt == 0:
                    for item in items:
                        print(item)
                        headers.append(item)
                else:
                    for idx, item in enumerate(items):
                        device[headers[idx]] = item
                if not line:
                    continue
                self.devices_list.append(device)

    def create_new_config(self):
        key1 = 'hostname SW-2960L-8TS'
        key2 = 'vlan 10,247'
        key3 = 'switchport access vlan '
        key4 = 'ip address 192.168.99.2 255.255.255.0'

        for device in self.devices_list:
            for item in self.template_config:
                if key1 in item:
                    self.created_config.append(f"hostname {device['HOSTNAME']}")
                    continue
                if key2 in item:
                    self.created_config.append(f"vlan {device['DVLAN']} {device['MVLAN']}")
                    continue
                if key3 in item:
                    self.created_config.append(f"switchport access vlan {device['DVLAN']}")
                    continue
                if key4 in item:
                    self.created_config.append(f"ip address {device['IP']} 255.255.255.0")
                    continue
                self.created_config.append(item)
            print(self.created_config)

    def run(self):
        self.import_template()
        self.import_input_list()
        self.create_new_config()


if __name__ == '__main__':
    template_file = 'template/2960L.txt'
    devices_file = 'config/devices_file.txt'

    create_config = CreateConfig(template_file, devices_file)
    create_config.run()
    # print(create_config.template_config)
    print(create_config.devices_list)



