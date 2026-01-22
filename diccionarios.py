
def assign_person_to_job(names: list[str], jobs: list[str]) -> dict[str, str]:
    """Asigna personas a profesiones."""
    res = {}
    for n, j in zip(names, jobs):
        res[n] = j
    return res

    return {n: j for n, j in zip(names, jobs)}

    return dict(zip(names, jobs))

names = ["Dennis", "Vera", "Mabel", "Annette", "Sussan"]
jobs = ["Butcher", "Programmer", "Doctor", "Teacher", "Lecturer"]

print(assign_person_to_job(names, jobs))


def calculate_losses(inventario: dict[str, int]) -> str|int:
    """Calcula el total de unidades perdidas."""
    if len(inventario) == 0:
        return "Lucky you!"
    res = 0
    for v in inventario.values():
        res += v
    return res

print(calculate_losses({
    "tv" : 30,
    "skate" : 20,
    "stereo" : 50,
}) == 100)

print(calculate_losses({
    "painting" : 20000,
}) == 20000)

print(calculate_losses({}) == "Lucky you!")