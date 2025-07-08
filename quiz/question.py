from enum import Enum, auto
from ui.cli import Debug, Error, Raise

class QuestionType(Enum):
    MCQ = 0
    INTTYPE = 1

    def __init__(self, index):
        self.index = index

class QuestionLevel(Enum):

    EASY = (1, 'green')
    MEDIUM = (2, 'yellow')
    HARD = (3, 'red')
    ADV = (4, 'magenta')

    def __init__(self, marks, color):
        self.marks = marks
        self.color = color
    
    @classmethod
    def get(cls, marks):
        for level in cls:
            if level.marks == marks:
                return level
        Raise(f"No level with marks = {marks}")

qdata = {'logged': 0, 'failed': 0, 'total': 0}

class Question:
    def __init__(self, questiontype: QuestionType, level: QuestionLevel, subject, question: str, *answer):

        if question is None or question.strip() == '':
            Raise(f'Invalid Formated question was Provided! {questiontype}, {level}')
            qdata['failed'] += 1
            return
        
        self.question = question
        display_q = self.question[:35] + '........'if len(self.question) > 40 else self.question

        if type(questiontype) != QuestionType: questiontype = QuestionType.MCQ
        if type(level) != QuestionLevel: level = QuestionLevel.EASY
        
        if len(answer) != 1 or answer == None or answer[0] is None or answer[0] == '': 
            Raise(f'Invalid Formated Answer was Provided for question &[underline]{display_q}!')
            qdata['failed'] += 1
            return
        
        self.subject = subject
        self.questiontype = questiontype
        self.level = level
        self.setAnswer(*answer)
        
        Debug(f'Resgitered question &[underline blue]{display_q}&[reset green] Type: &[underline yellow]{self.questiontype.name} &[reset green]Level: &[bold underline {self.level.color}]{self.level.name}&[reset green] Feild: &[underline red]{self.subject.name}, {self.subject.subject}')
        qdata['logged'] += 1


    
    def setAnswer(self, *answer):
        try:
            if self.questiontype == QuestionType.INTTYPE:
                self.answer = answer[0]
            elif self.questiontype == QuestionType.MCQ:
                self.answer = answer[0]
                self.choices = answer[1:]
            else: raise ValueError
        except IndexError:
            qdata['failed'] += 1
            Error('Invalid Index is Provided!')