from enum import Enum

class PHYSICS(Enum):
    CLASSICAL = 0
    ELECTROMAGNATISM = 1
    QUANTUM = 2

    def __init__(self, id):
        self.id = id
        self.subject = 'PHYSICS'

class CHEMISTRY(Enum):
    PHYSICAL = 0
    ORGANIC = 1
    INORGANIC = 2

    def __init__(self, id):
        self.id = id
        self.subject = 'CHEMISTRY'

class MATHS(Enum):
    ALGEBRA = 0
    TRIGONOMETRY = 1
    CALCULUS = 2
    VECTOR3D = 3

    def __init__(self, id):
        self.id = id
        self.subject = 'MATHS'

class CS(Enum):
    PYTHON = 0

    def __init__(self, id):
        self.id = id
        self.subject = 'CS'

class GK(Enum):
    GK = 0

    def __init__(self, id):
        self.id = id
        self.subject = 'GK'


SUBJECTS = {
    'PHYSICS': PHYSICS,
    'CHEMISTRY': CHEMISTRY,
    'MATHS': MATHS,
    'CS': CS,
    'GK': GK,
}