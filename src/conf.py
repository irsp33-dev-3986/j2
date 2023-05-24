from abc import ABC

class config(ABC):
    def __init__(self, ip:str, fqdn:str, ttype:str, identity:int):
        self.ip = ip
        self.fqdn = fqdn
        self.type = ttype
        self.id = identity

class cobalt_strike(config):
    def __init__(self, ip:str, fqdn:str, ttype:str, identity:int, spawnto:str, sleeptime:int, watermark:int):
        self.ip = ip
        self.fqdn = fqdn
        self.type = ttype
        self.id = identity
        self.spawnto = spawnto
        self.sleeptime = sleeptime
        self.watermark = watermark
        config.build_ts_set()

    @property
    def get_property(self, prop):
        return self.prop

    def build_ts_set(self):
        team_server = config.build_dict()
        team_server_set = team_server_set.add(team_server)
        return team_server_set

    def build_dict(self):
        team_server = {"ip" : self.ip, "fqdn" : self.fqdn, "type" : self.ttype, "identity" : self.identity, "spawnto" : self.spawnto, "sleep_time" : self.sleeptime, "watermark" : self.watermark}
        return team_server

    """
    @property.setter
    def set_property(self, prop, value):
        self.prop = value
    """