"""
Šiame faile galime kaupti pagalbines funkcijas
"""

def check_pasword(password):
    """
    Slaptažodžio tikrinimas, pagal
    stringo ilgį, jei daugiau
    nei 5 simboliai - tinkamas
    :param password: slaptažodis
    :return: bool
    """
    if len(password) > 5:
        return True
    else:
        return False
