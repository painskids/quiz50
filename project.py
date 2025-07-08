from data import data
from quiz import questions, question, subjects
from ui.cli import colorize, Quiz50, Debug
import random
from pyfiglet import Figlet
import os

os.system('')

figlet = Figlet()

sub = {
    '0': subjects.SUBJECTS['PHYSICS'],
    '1': subjects.SUBJECTS['CHEMISTRY'],
    '2': subjects.SUBJECTS['MATHS'],
    '3': subjects.SUBJECTS['CS'],
    '4': subjects.SUBJECTS['GK'],
    '*': '__TEMP__',
}

lvl = {
    '0': question.QuestionLevel.EASY,
    '1': question.QuestionLevel.MEDIUM,
    '2': question.QuestionLevel.HARD,
    '3': question.QuestionLevel.ADV,
    '*': '__TEMP__',
}

def main():
    print(colorize(f'&[bold golden]{figlet.renderText("Quiz50")}'))
    print(colorize('&[bold pr]⚠ ANSI COLORS MAY NOT DISPLAY CORRECTLY AND MESS UP ON SOME TERMINALS ⚠'))
    print()
    data.load_data()
    questions.load_questions()

    # print(colorize(f'{question.qdata}'))

    ques = questions.QUES
    print(colorize('''
    &[bold green]Subjects
        0: Physics
        1: Chemistry
        2: Maths
        3: CS
        4: GK
        *: ALL
        '''))
    while True:
        subject = input(Quiz50('Select Subject: ', printing=False).msg + '\033[33m').strip().lower()
        if subject in sub.keys(): break

    if subject != '*': ques = [_ for _ in ques if isinstance(_.subject, sub[subject])]

    print(colorize('''
    &[bold cyan]Levels
        0: &[green]Easy&[cyan]
        1: &[yellow]Medium&[cyan]
        2: &[red]Hard&[cyan]
        3: &[magenta]ADVANCED&[cyan]
        *: &[blue]ANY&[reset]
    '''))
    while True:
        level = input(Quiz50('Select Level: ', printing=False).msg + '\033[33m').strip().lower()
        if level in lvl.keys(): break
    
    if level != '*': ques = [_ for _ in ques if _.level.marks == int(level) + 1]

    stats = {'correct': 0, 'wrong': 0, 'unattempted': 0}

    ques_mcq = [_ for _ in ques if _.questiontype == question.QuestionType.MCQ]
    ques_int = [_ for _ in ques if _.questiontype == question.QuestionType.INTTYPE]
    
    n_int = random.randint(2, min(len(ques_int)//2 + 1, 7))

    i = 0

    wrong_unattempted_ques = dict()

    print(colorize('&[bold yellow]Multiple Choice Question: Enter the correct answer from the given options'))
    for _ in range(12 - n_int if len(ques_mcq) > 10 else len(ques_mcq)):
        i += 1
        Q = random.choice(ques_mcq)
        ques_mcq.remove(Q)
        ans = Q.answer[0]

        c = dict()

        choices = Q.answer

        ans_letter = ''
        
        random.shuffle(choices)
        for _ in range(len(choices)):
            c[chr(ord('A') + _)] = choices[_]
            if choices[_] == ans: ans_letter = chr(ord('A') + _)

        
        print(colorize(f'&[bold red]Question {i}: &[green]{Q.question}'))
        for _ in c.keys():
            print(colorize(f'&[bold green] {_}. {c[_]}'))
        


        while True:
            user_answer = input(colorize('&[reset blue]Answer is: ')).strip().upper()
            if user_answer in ['A', 'B', 'C', 'D', '']: break

        if user_answer == '':
            stats['unattempted'] += 1
            wrong_unattempted_ques[i] = f'{ans_letter}. {ans}'
        elif c[user_answer].lower() == ans.lower():
            stats['correct'] += 1
        else:
            stats['wrong'] += 1
            wrong_unattempted_ques[i] = f'{ans_letter}. {ans}'
            Debug(f'wrong, answer is {ans}')

    
    print('')
    print(colorize('&[bold yellow]Interger Type: Answer must be an integer if not must be rounded to neartest integer'))
    for _ in range(n_int):
        i += 1
        Q = random.choice(ques_int)
        ques_int.remove(Q)
        print(colorize(f'&[bold red]Question {i}: &[green]{Q.question}'))

        while True:
            try:
                user_answer = input(colorize('&[reset blue]Answer is: ')).strip()
                if user_answer != '': user_answer = int(user_answer)
            except ValueError: 
                ...
            else: break
        
        if user_answer == '':
            stats['unattempted'] += 1
            wrong_unattempted_ques[i] = f'{Q.answer}'
        elif user_answer == Q.answer:
            stats['correct'] += 1
        else:
            stats['wrong'] += 1
            wrong_unattempted_ques[i] = f'{Q.answer}'
            Debug(f'wrong, answer is {Q.answer}')

    print()
    print(colorize(f'&[bold green]Correct: &[magenta]{stats["correct"]}, &[red]Wrong: &[magenta]{stats["wrong"]}, &[yellow]Unattempted: &[magenta]{stats["unattempted"]}'))

    if len(wrong_unattempted_ques) > 0:
        display_wrong_n_unattempted = input(Quiz50('\nDisplay unattempted and wrongly answered questions? (Y): ', printing=False).msg + '\033[33m').strip().lower()
        if display_wrong_n_unattempted.startswith('y'):
            for i in wrong_unattempted_ques.keys():
                print(colorize(f'&[bold yellow]Ques {i}: &[green]{wrong_unattempted_ques[i]}'))

if __name__ == '__main__':
    main()