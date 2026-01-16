import re

def comprobar_ip(ip: str) -> bool:
    """Comprueba si ip es una dirección IP válida."""
    # p = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    p = re.compile(r'^\d{1,3}(\.\d{1,3}){3}$')
    if p.search(ip) is None:
        return False
    return all(n >= 0 and n <= 255 for n in map(int, ip.split('.')))

