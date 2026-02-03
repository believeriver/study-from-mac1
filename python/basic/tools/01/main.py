from abc import ABC, abstractmethod


class CreateConfig(object):
    def __init__(self, template_file: str, devices_file: str):
        self.template_file = template_file
        self.devices_file = devices_file
        self.template_config = []
        self.devices_list = {}

    def import_template(self):
        with open(self.template_file, encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                print(line)
                self.template_config.append(line)

    def import_input_list(self):
        with open(self.devices_file, encoding="utf-8") as f:
            cnt = 0
            for line in f:
                line = line.rstrip("\n")
                if cnt == 0:
                    items = line.split(",")
                    for item in items:
                        print(item)
                if not line:
                    continue

    def run(self):
        self.import_template()
        self.import_input_list()


