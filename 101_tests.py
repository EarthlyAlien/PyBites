from driving import allowed_driving
from driving import allowed_driving2


def test_not_allowed_to_drive(capfd):
    allowed_driving('tim', 17)
    output = capfd.readouterr()[0].strip()
    assert output == 'tim is not allowed to drive'


def test_allowed_to_drive(capfd):
    allowed_driving('bob', 18)
    output = capfd.readouterr()[0].strip()
    assert output == 'bob is allowed to drive'

    allowed_driving('julian', 19)
    output = capfd.readouterr()[0].strip()
    assert output == 'julian is allowed to drive'

def test_not_allowed_to_drive2(capfd):
    allowed_driving2('tim', 17)
    output = capfd.readouterr()[0].strip()
    assert output == 'tim is not allowed to drive'


def test_allowed_to_drive2(capfd):
    allowed_driving2('bob', 18)
    output = capfd.readouterr()[0].strip()
    assert output == 'bob is allowed to drive'

    allowed_driving2('julian', 19)
    output = capfd.readouterr()[0].strip()
    assert output == 'julian is allowed to drive'