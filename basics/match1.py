num=int(input('enter a num'))
match num:
    case 1:
        print('sunday')
    case 2:
        print('monday')
    case 3:
        print('tuesday')
    case 4:
        print('wednessday')
    case 5:
        print('thrusday')
    case 6:
        print('friday')
    case 7:
        print('saturday')
    case _ :# '_' acts as a defaulat
        print('invalid choice')
