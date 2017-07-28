from utils import search_employee, post_servicecall
import constants

# функции создания тикетов на основании команды из командной строки
def run_call(namespace):
    '''
    Функция создания заявки на основе данных из пропущенного звонка из Астериска
    '''
    client = search_employee(search=namespace.phone, title='cityPhoneNumber')
    shortDescr = 'Вы звонили на 333, но мы не смогли ответить. Мы свяжемся с вами в ближайшее время.'
    post = post_servicecall(client=client, shortDescr=shortDescr)
    print(post)
    pass

def run_av_check(namespace):
    '''
    Функция создания заявки на регулярной заявки для проверки переговорных комнат
    '''
    descriptionRTF = 'Необходимо провести проверку переговорных комнат и внести данные в файл.  ' \
                     'Проверить подключение HDMI кабеля  ' \
                     'проверить работоспособность всех переходников  ' \
                     'Проверить работоспособность LifeSize(перезагрузить устройства)  '
    shortDescr = 'Регулярная проверка переговорных комнат'
    post = post_servicecall(client=constants.SUPPORT_LEAD, shortDescr=shortDescr, service=constants.AGREEMENT_AV, descriptionRTF=descriptionRTF)
    print(post)
    pass

def run_new_task(namespace):
    client = search_employee(search=namespace.email, title='email')
    post = post_servicecall(client=client, shortDescr=namespace.title)
    print(post)
    pass

def run_fired(namespace):
    '''
    Функция создания заявки на основе csv с уволенными сотрудниками
    '''
    # TODO
    pass