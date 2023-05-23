from my_application import application

if __name__ == "__main__":
    host_01 = application.create_cobalt_strike_host("94.232.46.229", "v10.5.org")
    host_02 = application.create_cobalt_strike_host(input('Entrer IP:'), input('Entrer FQDN:'))
    print(f"host02 est un serveur {host_02.type} avec l'IP {host_02.ip}. {host_02.get_risk}. Le niveau de risque est de {host_02.risk}. L'identite est {host_02.identity}. Host01 a l'identite {host_01.identity}")