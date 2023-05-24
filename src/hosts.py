from abc import ABC, abstractmethod
import conf

class hosts(ABC):
    Desc = str("Host")

    i = int(0)

    def __init__(self, ip:str, fqdn:str):
        self.ip = ip
        self.fqdn = fqdn
        self.id = hosts.i
        hosts.i += 1


    @abstractmethod
    def get_ip(self):
        return self.ip

    @abstractmethod
    def get_type(self):
        return self.type

    @abstractmethod
    def get_risk(self):
        pass

    @abstractmethod
    def get_fqdn(self):
        return self.fqdn

class cobalt_strike(hosts):
    def __init__(self, ip:str, fqdn:str, ttype:str="cobalt_strike",identity:int=hosts.i , spawnto:str=None, sleeptime:int=None, watermark:int=None):
        self.ip = ip
        self.fqdn = fqdn
        self.id = identity
        self.ttype = ttype #str("cobalt_strike")
        self.spawnto = spawnto #str("%windir%\sysnative\dllhost.exe -o enable")
        self.sleeptime = sleeptime #int(62248)
        self.watermark = watermark #int(987654321)
        #conf.cobalt_strike(ip, fqdn, ttype, identity, spawnto, sleeptime, watermark)

    @property
    def type(self):
        return str("Cobalt Strike")

    def get_ip(self):
        return self.ip

    def get_type(self):
        return self.type

    def get_fqdn(self):
        return self.fqdn

    @property
    def risk(self):
        return int(5)

    def get_risk(self):
        match self.risk:
            case 1:
                return "Risk is very low"
            case 2:
                return "Risk is low"
            case 3:
                return "Risk is elevated"
            case 4:
                return "Risk is high"
            case 5:
                return "Risk is very high"


class gophish(hosts):   
    def get_ip(self):
        return self.ip