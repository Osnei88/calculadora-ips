import ipaddress

def calcular_ip(ip_digitado):

    # Converte o endereço informado
    interface = ipaddress.ip_interface(ip_digitado)

    # Aceita somente IPv4
    if interface.version != 4:
        raise ValueError("Apenas IPv4 é permitido.")

    # Identifica a rede
    rede = interface.network

    # Identifica o broadcast
    broadcast = rede.broadcast_address

    # Calcula os hosts disponíveis
    if rede.prefixlen == 32:
        quantidade_hosts = 1
        primeiro_ip = str(rede.network_address)
        ultimo_ip = str(rede.network_address)

    elif rede.prefixlen == 31:
        quantidade_hosts = 2
        primeiro_ip = str(rede.network_address)
        ultimo_ip = str(broadcast)

    else:
        quantidade_hosts = rede.num_addresses - 2
        primeiro_ip = str(rede.network_address + 1)
        ultimo_ip = str(broadcast - 1)

    # Identifica a classe tradicional
    primeiro_octeto = int(str(interface.ip).split(".")[0])

    if primeiro_octeto < 128:
        classe = "A"
    elif primeiro_octeto < 192:
        classe = "B"
    elif primeiro_octeto < 224:
        classe = "C"
    elif primeiro_octeto < 240:
        classe = "D"
    else:
        classe = "E"

    # Converte IP e máscara para binário
    ip_binario = ".".join(
        f"{int(octeto):08b}"
        for octeto in str(interface.ip).split(".")
    )

    mascara_binaria = ".".join(
        f"{int(octeto):08b}"
        for octeto in str(rede.netmask).split(".")
    )

    # Organiza os resultados
    resultado = {
        "ip": str(interface.ip),
        "cidr": f"/{rede.prefixlen}",
        "classe": classe,
        "mascara": str(rede.netmask),
        "wildcard": str(rede.hostmask),
        "rede": str(rede.network_address),
        "primeiro_ip": primeiro_ip,
        "ultimo_ip": ultimo_ip,
        "broadcast": str(broadcast),
        "total_enderecos": rede.num_addresses,
        "hosts_disponiveis": quantidade_hosts,
        "ip_binario": ip_binario,
        "mascara_binaria": mascara_binaria
    }

    return resultado
