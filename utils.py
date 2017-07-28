import constants
import requests
import argparse

def create_parser():
    '''
    Обрабатывает входящие команды серии python3 app.py newticket -e petrov@ya.ru -t 'Ticket for test'
    :return значение с заданными полями: 
    '''
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    phone_call_parser = subparsers.add_parser('phonecall')
    phone_call_parser.add_argument('-p', '--phone')

    av_check_parser = subparsers.add_parser('avcheck')
    av_check_parser.add_argument('--day', '-d', default='1')

    fired_parser = subparsers.add_parser('fired')
    fired_parser.add_argument('--file', '-f')

    new_task_parser = subparsers.add_parser('newticket')
    new_task_parser.add_argument('-e', '--email')
    new_task_parser.add_argument('-t', '--title', default='Обращение')


    return parser

def search_request_employee(email):
    pass


def search_employee(search, title='email'):
    '''
    Функция поиска пользователя в системе.
    !!! Не реализована обработка ошибки если ищется по неправильному полю :) !!!
    поиск происходит по JSON в формате key : value (пример 'email' : 'petrov@ya.ru' )
    :param search - какое значение ищем: 
    :param title - значение чего ищем(из JSON): 
    :return - ID пользователя которого искали или ID 'Служебного'(безымянного) пользователя если не найдено : 
    '''
    search_data = {title : search}
    #    search_data = {'cityPhoneNumber': search_email}
    r = requests.get(
        '{}find/employee/{}?accessKey={}'.format(constants.ITSM_URL, search_data, constants.ACCESS_KEY))
    if r.text == '[]':
        print('nothing find')
        return constants.DEFAULT_CLIENT
    else:
        employee_id = [each['UUID'] for each in r.json()]
        return employee_id[0]



def post_servicecall(
        metaClass=constants.DEFAULT_METACLASS,
        agreement=constants.DEFAULT_AGREEMENT,
        service=constants.DEFAULT_SERVICE,
        client=constants.DEFAULT_CLIENT,
        shortDescr='Ticket',
        descriptionRTF='Описание не указана'
):
    '''
    Постит заявку в SD Naumen(itsm365) при помощи API этой системы
    :param metaClass - Тип заявки(default=обращение): 
    :param agreement - Тип соглашения(default=базовое): 
    :param service - Тип услуги(default=Прочее): 
    :param client - Контрагент(default=Служебный): 
    :param shortDescr - Тема обращения(defaule='Ticket'): 
    :return - возвращает статус поста, дает возможность контроллировать ответ от сервера: 
    '''
    # Создание json для передачи в данных в ITSM
    json = {
        "metaClass": metaClass,
        "agreement": agreement,
        "service": service,
        "client": client,
        "shortDescr": shortDescr,
        "descriptionRTF": descriptionRTF,
    }
    post = requests.post(
        '{}create/serviceCall/{}?accessKey={}'.format(constants.ITSM_URL, json, constants.ACCESS_KEY))
    return post
