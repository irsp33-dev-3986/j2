from abc import ABC, abstractmethod

class hosts(ABC):
    Desc = str("Host")

    i = []

    def __init__(self, ip:str, fqdn:str):
        self.ip = ip
        self.fqdn = fqdn
        i += 1

    @abstractmethod
    def get_ip(self):
        return self.ip

    @property
    def identity(self):
        return int(self.i)

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
                return("Risk is very low")
            case 2:
                return("Risk is low")
            case 3:
                return("Risk is elevated")
            case 4:
                return("Risk is high")
            case 5:
                return("Risk is very high")


class gophish(hosts):
    
    def get_ip(self):
        return self.ip