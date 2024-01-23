import requests
class Sender():
    def __init__(self,ipadr_):
        global ipadresself_
        ipadresself_= ipadr_
    def send(self,npin_):
        res = requests.get('http://'+ipadresself_+'/'+str(npin_))#192.168.43.47