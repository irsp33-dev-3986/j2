from my_application import application

if __name__ == "__main__":
    host01 = application.create_cobalt_strike_host("94.232.46.229", "v10.5.org")
    host02 = application.create_cobalt_strike_host(input('Entrer IP:'), input('Entrer FQDN:'))
    print(f"host02 est un serveur {host02.type} avec l'IP {host02.ip}. {host02.get_risk}. Le niveau de risque est de {host02.risk}. L'identite est {host02.id}. Host01 a l'identite {host01.id}")

    print(f"{host02.get_risk}")

    print(application.get_set(host02))
    
    """
    host02_risk = application.get_host_property(risk)
    print(host02_risk)
    """