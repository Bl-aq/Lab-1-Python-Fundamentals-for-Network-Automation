import logging  

class NetworkDevice:
    def __init__(self, hostname, ip, device_type):
        self.hostname = hostname
        self.ip = ip
        self.device = device_type

    def summarize(self):
        summary = f"[DEVICE_SUMMARY]: {self.hostname} ({self.device}) - {self.ip}"


        print(summary)
        logging.info(summary)


        return summary