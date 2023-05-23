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

        team_server = {"ip" : ip, "fqdn" : fqdn, "type" : ttype, "identity" : identity, "spawnto" : spawnto, "sleep_time" : sleeptime, "watermark" : watermark}
        team_server_set = team_server_set.add(team_server)

    def get_property(self, prop):
        return self.prop

    def build_dict(self):
        return team_

    """
    @property.setter
    def set_property(self, prop, value):
        self.prop = value
    """