def sort(width, height, length, mass):
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise Exception(
            "Invalid input, cannot have measurement less than or equal to 0")

    is_bulky = False
    is_heavy = False

    if width >= 150 or height >= 150 or length >= 150:
        is_bulky = True
    if width * height * length >= 1000000:
        is_bulky = True

    if mass >= 20:
        is_heavy = True

    if is_heavy and is_bulky:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"
