""" Вакансии """

jobs = [

    {"title": "Разработчик на Python", "cat": 'backend',
     "company": "staffingsmarter", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик в проект на Django", "cat": 'backend',
     "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик на Swift в аутсорс компанию", "cat": 'backend',
     "company": "swiftattack",
     "salary_from": "120000", "salary_to": "150000",
     "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Мидл программист на Python", "cat": 'backend',
     "company": "workiro", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Питонист в стартап", "cat": 'backend',
     "company": "primalassault", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"}

]

""" Компании """

companies = [

    {"title": "workiro",
     "location": "Москва",
     "description": "Дружная и многообещающая команда",
     "employee_count": 4},

    {"title": "rebelrage",
     "location": "Омск",
     "description": "Дружная и многообещающая команда",
     "employee_count": 75},

    {"title": "staffingsmarter",
     "location": "Москва",
     "description": "Дружная и многообещающая команда",
     "employee_count": 23},

    {"title": "evilthreath",
     "location": "Омск",
     "description": "Дружная и многообещающая команда",
     "employee_count": 15},

    {"title": "hirey",
     "location": "Рязань",
     "description": "Дружная и многообещающая команда",
     "employee_count": 37},

    {"title": "swiftattack",
     "location": "Москва",
     "description": "Дружная и многообещающая команда",
     "employee_count": 121},

    {"title": "troller",
     "location": "Рязань",
     "description": "Дружная и многообещающая команда",
     "employee_count": 45},

    {"title": "primalassault",
     "location": "Омск",
     "description": "Дружная и многообещающая команда",
     "employee_count": 1}

]

""" Категории """

specialties = [

    {"code": "frontend",
     "title": "Фронтенд",
     "pic": "https://raw.githubusercontent.com/kushedow/flask-html/master/Django%20Project%202/specialties/specty_frontend.png"},
    {"code": "backend",
     "title": "Бэкенд",
     "pic": "https://raw.githubusercontent.com/kushedow/flask-html/master/Django%20Project%202/specialties/specty_backend.png"},
    {"code": "gamedev",
     "title": "Геймдев",
     "pic": "https://raw.githubusercontent.com/kushedow/flask-html/master/Django%20Project%202/specialties/specty_gamedev.png"},
    {"code": "devops",
     "title": "Девопс",
     "pic": "https://raw.githubusercontent.com/kushedow/flask-html/master/Django%20Project%202/specialties/specty_devops.png"},
    {"code": "design",
     "title": "Дизайн",
     "pic": "https://raw.githubusercontent.com/kushedow/flask-html/master/Django%20Project%202/specialties/specty_design.png"},
    {"code": "products",
     "title": "Продукты",
     "pic": "https://raw.githubusercontent.com/kushedow/flask-html/master/Django%20Project%202/specialties/specty_products.png"},
    {"code": "management",
     "title": "Менеджмент",
     "pic": "https://raw.githubusercontent.com/kushedow/flask-html/master/Django%20Project%202/specialties/specty_management.png"},
    {"code": "testing",
     "title": "Тестирование",
     "pic": "https://raw.githubusercontent.com/kushedow/flask-html/master/Django%20Project%202/specialties/specty_testing.png"}

]

""" Статусы в формате Enum """

#
#
# class EducationChoices(Enum):
#     missing = 'Отсутствует'
#     secondary = 'Среднее'
#     vocational = 'Средне-специальное'
#     incomplete_higher = 'Неполное высшее'
#     higher = 'Высшее'
#
#
# class GradeChoices(Enum):
#     intern = 'intern'
#     junior = 'junior'
#     middle = 'middle'
#     senior = 'senior'
#     lead = 'lead'
#
#
# class SpecialtyChoices(Enum):
#     frontend = 'Фронтенд'
#     backend = 'Бэкенд'
#     gamedev = 'Геймдев'
#     devops = 'Девопс'
#     design = 'Дизайн'
#     products = 'Продукты'
#     management = 'Менеджмент'
#     testing = 'Тестирование'
#
#
# class WorkStatusChoices(Enum):
#     not_in_search = 'Не ищу работу'
#     consideration = 'Рассматриваю предложения'
#     in_search = 'Ищу работу'
