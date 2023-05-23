import hosts

class application:

    i = int(0)

    def someting (self):
        pass

    def create_cobalt_strike_host (self, new_cs_host):
        new_cs_host = hosts.cobalt_strike(i, )
        i += 1
    
if __name__ == "__main__":
    my = application()

    host01 = hosts.cobalt_strike(1, "94.232.46.229", "v10.5.org")
    
    print(f'host01 est numero {host01.id}, son IP est {host01.ip} et le FQDN associe est {host01.fqdn}. Il heberge {host01.type}. Le risque associe est {host01.risk}.\n')