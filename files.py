name = input('what is your name?').title().strip()
age = int(input('how old are you?'))
sex = input('what is your gender?').strip()

with open('names.csv', 'a') as read_csv:
    read_csv.write(f'{name}, {age}, {sex},\n')
