# !python3
# randomquizegenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.


import random

# The quize data. Keys are states and values are their capitals.
# 字典capitals，州为key, 首府为values.
capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phonix',
    'Arkansas': 'Little Rock',
    'California': 'Sacremento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kientucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Main': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'Mew York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

# Gernerate 35 quiz files. 分别生成35个问卷和35个答案的文件。
for quiznumber in range(35):

    # TODO: create quiz and answer key files.
    quizefile = open(f'capitalquize{quiznumber}.txt', 'w')
    answerkeyfile = open(f'answerkey{quiznumber}.txt', 'w')

# TODO: Write out the header for the quiz
    quizefile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizefile.write(f"{' '*20} State Capitals Quiz {quiznumber+1}")
    quizefile.write('\n\n')

# TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

# TODO: Loop through all 50 states, making a question for each.
    for question_num in range(50):
        # Get right and wrong answers.
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        # TODO: Write the question and answer options to the quiz file.
        quizefile.write(f'\n{question_num+1}. Whate is the Capital of {states[question_num]}?\n')
        for i in range(4):
            quizefile.write(f"{'ABCD'[i]}. {answer_options[i]}\n")
    quizefile.write('\n')

    # TODO: Write the answer key to the file.
    answerkeyfile.write(f"{question_num+1}.  {'ABCD'[answer_options.index(correct_answer)]}")

quizefile.close()
answerkeyfile.close()
