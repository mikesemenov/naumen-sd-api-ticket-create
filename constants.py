ACCESS_KEY = ''

ITSM_URL = ''

# Значения по умолчанию,если не выбрано другое - Вставлены жесткие данные из системы для удосбва. Можно находить поиском
# сотрудник "служебный" для регистрации заявки если контрагент не найден
DEFAULT_CLIENT = 'employee$2241003'
# соглашение по обслуживанию по умолчанию, если не выбрано при создании
DEFAULT_AGREEMENT = 'agreement$605301'
# Услуга по умолчанию
DEFAULT_SERVICE = 'slmService$605005'
# Тип обьекта по умолчанию(в системе это "обращение")
DEFAULT_METACLASS = 'serviceCall$call'
# Лидер поддержки, для создания и контроля регулярных запросов
SUPPORT_LEAD = 'employee$2494151'

# по умолчанию статические значения в системе в зависимости от услуги и пр.
# вынесены сюда для удобства изменения и отсутствия необходимости поиска мест использования в коде
# в моих задачах выполняется для создания регламентных работ с использованием Cron

AGREEMENT_AV = 'slmService$4162216'
AGREEMENT_USER_DATA = 'slmService$605002'

METACLASS_REQUEST = 'serviceCall$request'
