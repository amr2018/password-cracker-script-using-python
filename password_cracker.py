import random
import string


def crack_from_information(secret):
    guess = ''
    count = 0
    first_name = input('[+] first name : ')
    last_name = input('[+] last name : ')
    age = input('[+] age : ')
    sun_name = input('[+] (If he has) Son name : ')
    wife_name = input('[+]  (If he has) wife name : ')
    phone = input('[+] phone number : ')
    other1 = input('[+] other1 : ')
    other2 = input('[+] other2 : ')
    other3 = input('[+] other3 : ')
    other4 = input('[+] other4 : ')

    info_list = [first_name, last_name, age, sun_name, wife_name, phone, other1, other2, other3, other4,
    '@', '#', '&', '$', '*', '%', '/', '-', '_', '!', '~', '?', '.']

    while secret != guess:
        guess = ''.join(random.choice(info_list) for i in range(random.randint(0, len(info_list))))
        print(f'[+] count = {count}', f' Try =>  {guess}')
        count += 1

    print('-' * 100)
    print(' Password Is : ', guess)
    print('-' * 100)


#crack_from_information('')
#=================================================================================================
def crack_random(secret):
    guess = ''
    count = 0
    random_letters = list(string.printable + string.ascii_letters)
    while secret != guess:
        guess = ''.join(random.choice(random_letters) for i in range(random.randint(0, len(secret))))
        print(f'[+] count = {count}', f' Try =>  {guess}')
        count += 1

    print('-' * 100)
    print(' Password Is : ', guess)
    print('-' * 100)

#crack_random('')

#=================================================================================================
def crack_for_PIN_CODE(secret):
    guess = ''
    count = 0
    numbers = list(string.digits)
    while secret != guess:
        guess = ''.join(random.choice(numbers) for i in range(len(secret)))
        print(f'[+] count = {count}', f' Try =>  {guess}')
        count += 1

    print('-' * 100)
    print(' PIN-CODE IS : ', guess)
    print('-' * 100)

#crack_for_PIN_CODE('')

#=================================================================================================
