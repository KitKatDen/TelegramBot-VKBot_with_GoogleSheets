import gspread


def connect_and_get_data():
    gc = gspread.service_account(filename='credentials.json')
    sh = gc.open_by_key('TOKEN')
    worksheet = sh.sheet1
    res = worksheet.get_all_records()
    return res


def find_number(data):
    n = len(data)
    ans = []
    print('Привет! По какому ключу (буквы фамилиии, имени) мы ищем?')
    find_me = input('!!! Будь внимателен, я чувствителен к регистру!!! (заглавные буквы, с которых начинаются имя и'
                    ' фамилия)\n')
    print('Начинаю поиск по ключу "{}"!'.format(find_me))
    for i in range(0, n):
        if data[i]['имя'].find(find_me) != -1:
            ans.append(i)
            # print('Нашёл, это {}, её номер телефона: {}'.format(data[i]['имя'], data[i]['телефон']))
    if len(ans) == 1:
        print('Нашёл, это {}, её номер телефона: {}'.format(data[ans[0]]['имя'], data[ans[0]]['телефон']))
    elif len(ans) != 1 and len(ans) > 1:
        print('У меня есть {} вариантов, надеюсь, здесь есть то, что тебе нужно!'.format(len(ans)))
        for j in range(0, len(ans)):
            print('Вариант №{}, это {}, номер телефона: {}'.format(j + 1, data[ans[j]]['имя'], data[ans[j]]['телефон']))


find_number(connect_and_get_data())

# TODO Если ячейка 'телефон' пуста, то нужно это дополнительно предусмотреть при выводе
# TODO Добавить выбор листа в таблице и подумать, как подбирать столбцы для поиска
