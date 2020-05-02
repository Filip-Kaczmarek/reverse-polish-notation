expressions = []

not_operators = ["NOT", "~", "¬"]

pre_operators = ["FORALL", "∀", "EXISTS", "∃"]

compare_operators = [ "AND", "&", "∧", "OR", "|", "∨",
                     "IMPLIES", "→", "IFF", "↔", "XOR", "⊕" ]

functions = ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

symbols = ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ONP(expression):
    stack = []
    for val in expression.split():
        result=''

        if val in pre_operators:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = '(' + val + ' ' + arg1 + ' ' + arg2 + ')'
            stack.append(result)

        elif val in compare_operators:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = '(' + arg1 + ' ' + val + ' ' + arg2 + ')'
            stack.append(result)

        elif val in not_operators:
            arg = stack.pop()
            result = '(' + val + arg + ')'
            stack.append(result)

        elif val[0] in functions:
            no_of_arguments = int(val[2])
            result = '(' + val[0] + '('
            arg = stack.pop()
            result = result + arg
            no_of_arguments -= 1
            while (no_of_arguments >= 1):
                arg = stack.pop()
                result = result + ', ' + arg
                no_of_arguments -= 1
            result = result + ')' + ')'
            stack.append(result)

        elif val[0] in symbols:
            no_of_arguments = int(val[2])
            result = '(' + val[0] + '('
            arg = stack.pop()
            result = result + arg
            no_of_arguments -= 1
            while (no_of_arguments >= 1):
                arg = stack.pop()
                result = result + ', ' + arg
                no_of_arguments -= 1
            result = result + ')' + ')'
            stack.append(result)

        else:
            stack.append(val)
    return stack.pop()

print ('1. Enter the expressions in reverse polish notation', '\n2. Exit')
choice = input('Enter number 1 or 2: ')
while (choice != '1') and (choice != '2'):
    print ('1. Enter the expressions in reverse polish notation', '\n2. Exit')
    choice = input('Enter number 1 or 2: ')

while choice != '2':
    while choice == '1':
        line = input('Enter the expression: ')
        print('Expression in standard bracket notation: ', ONP(line), '\n')
        print ('1. Enter the expression in reverse polish notation', '\n2. Exit')
        choice = input('Enter number 1 or 2: ')
        while (choice != '1') and (choice != '2'):
            print ('1. Enter the expressions in reverse polish notation', '\n2. Exit')
            choice = input('Enter number 1 or 2: ')
