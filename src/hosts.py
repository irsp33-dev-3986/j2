from abc import ABC, abstractmethod

class hosts(ABC):
    Desc = str("Host")

    def __init__(self, identity:int, ip:str, fqdn:str):
        self.id = identity
        self.ip = ip
        self.fqdn = fqdn

    @abstractmethod
    def get_ip(self):
        return self.ip

    @abstractmethod
    def get_type(self):
        return self.ttype

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
        return str("Very high")

    def get_risk(self):
        return self.risk

class gophish(hosts):
    
    def get_ip(self):
        return self.ip