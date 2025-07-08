from quiz.question import Question, QuestionType, QuestionLevel
from quiz import subjects 
from ui.cli import Raise
from utils.loader import Loader
import time
import json

QUES = list()
QUES_JSON = [
    'physics/classical.json',
    'physics/electromagnatism.json',
    'physics/quantum.json',
    'chemistry/physical.json',
    'chemistry/organic.json',
    'chemistry/inorganic.json',
    'maths/algebra.json',
    'maths/calculus.json',
    'maths/trigonometry.json',
    'maths/vector.json',
    'cs/python.json',
    'gk/gk.json',
]
# Type[0:MCQ, 1:INT TYPE] Level[1: Easy, 2: Medium, 3:HARD, 4:ADV] SUB['PHYSICS', 'CHEMISTRY', 'MATHS', 'CS', 'GK']
# Branches: Physics: CLASSICAL(0), ELECTROMAGNATISM(1), QUANTUM(2)
#           CHEMISTRY: PHYSICAL(0), ORGANIC(1), INORGANIC(2)
#           MATHS: MATRIX(0), ALGEBRA(1), TRIGONOMETRY(2), CALCULUS(3), VECTOR3D(4)
#           CS: C(0), PYTHON(1), JAVA(2)
#           GK: GK(0)
def load_questions():
    with Loader('Loading Questions!', 'Questions Loaded!') as l:
        for jsons in QUES_JSON:
            with open(f'data/questions/{jsons}',  encoding="utf-8") as f:
                data = json.load(f)
                for q in data:
                    reg(q['code'], q['question'], q['answer'])  
                time.sleep(0.075)     

def reg(code: str, question: str, answer):
    if code[2:-1] not in subjects.SUBJECTS.keys():
        Raise(f'Invalid Subject ID, {question[:25].strip()}')
        return
    qtype = QuestionType(int(code[0]))
    qlevel = QuestionLevel.get(int(code[1]))
    qtopic = subjects.SUBJECTS[code[2:-1].upper()](int(code[-1]))
    QUES.append(Question(qtype, qlevel, qtopic, question, answer))