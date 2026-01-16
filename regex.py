import re
import datetime

def comprobar_ip(ip: str) -> bool:
    """Comprueba si ip es una dirección IP válida."""
    # p = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    p = re.compile(r'^\d{1,3}(\.\d{1,3}){3}$')
    if p.fullmatch(ip) is None:
        return False
    return all(n >= 0 and n <= 255 for n in map(int, ip.split('.')))

def comprobar_numero_entero_positivo_o_negativo(n: str) -> bool:
    """Comprueba si n es un número entero, positivo o negativo."""
    p = re.compile(r'^[+-]?\d+$')
    return p.fullmatch(n) is not None

def comprobar_fecha(f: str) -> bool:
    """Comprueba si f es una fecha válida."""
    p = re.compile(r'^\d\d/\d\d/\d{4}$')
    if p.fullmatch(f) is None:
        return False
    try:
        dia, mes, anyo = map(int, f.split('/'))
        datetime.date(anyo, mes, dia)
        return True
    except ValueError:
        return False
