import telnetlib

class RelayController:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.tn = telnetlib.Telnet(ip, port)

    def onOne(self, relay_num):
        self.tn.write(str(relay_num).encode('ascii'))

    def onMassive(self, relay_states):
        self.tn.write(str(relay_states).encode('ascii'))

    def close(self):
        self.tn.close()