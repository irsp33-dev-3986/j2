import hosts

class application:

    def create_cobalt_strike_host (ip:str, fqdn:str):
        return hosts.cobalt_strike(ip, fqdn)
    
if __name__ == "__main__":
    my = application()

    host01 = hosts.cobalt_strike(1, "94.232.46.229", "v10.5.org")
    
    print(f'host01 est numero {host01.id}, son IP est {host01.ip} et le FQDN associe est {host01.fqdn}. Il heberge {host01.type}. Le risque associe est {host01.get_risk}.\n')