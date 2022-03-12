from . import models
from django.db.models.functions import datetime
from datetime import datetime, timedelta
from num2words import num2words


def get_order_data(id):
    placement = models.Placement.objects.filter(id=id).values()[0]
    patient = models.Patient.objects.filter(id=placement['patient_id']).values()[0]
    services = models.Service.objects.filter(placement=id).values()

    obj = obj_container(placement, patient, services)
    # print(obj)
    return obj

def obj_container(placement, patient, services):
    obj = []

    service_list = []
    for item in services:
        item.pop('id', None)
        item.pop('specialization_id', None)
        service_list.append(item)

    obj.extend([placement, patient, service_list])
    return obj

def format(data):
    dict = {}

    placement = data[0]
    dict['id'] = placement['id']
    dict['date_start'] = datetime.strftime(placement['date_start'], "%d.%m.%Y")
    dict['date_start_word'] = date2word(dict['date_start'])
    dict['summa'] = placement['summa']

    patient = data[1]
    patient_name = patient['name']
    dict['patient_name'] = patient_name
    temp = patient_name.split(' ')
    dict['patient_name_output'] = temp[0] + ' ' + temp[1][:1] + '.' + temp[2][:1] + '.'
    dict['address'] = patient['address']
    dict['year'] = patient['year']
    dict['path'] = f'{temp[0]}{temp[1][:1]}.{temp[2][:1]}_{dict["id"]}'

    service = data[2]
    service_name = []
    cost = []
    for item in service:
        service_name.append(item['name'])
        cost.append(item['cost'])
    dict['service_name'] = service_name
    dict['cost'] = cost


    return dict

def date2word(date):
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = date.split('.')
    date_list[1] = month_list[int(date_list[1]) - 1]
    return date_list


def n2w(num):
    return num2words(num, lang='ru')