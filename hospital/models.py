from django.db import models

# Create your models here.

def default_id():
    id_list = Placement.objects.values_list('id', flat=True).distinct()
    if not id_list:
        max_id = 0
    else:
        max_id = max(id_list)
    max_id += 1
    return max_id

class Patient(models.Model):
    id = models.CharField(verbose_name='Номер карточки пациента', max_length=10, primary_key=True)
    name = models.CharField(verbose_name='ФИО пациента', max_length=60)
    address = models.CharField(verbose_name='Адрес пациента', max_length=80)
    district = models.CharField(verbose_name='Район города, где проживает', max_length=20)
    policy_number = models.ForeignKey('InsurancePolicy', on_delete=models.CASCADE, verbose_name='Номер страхового полиса', null=True, blank=True)
    year = models.CharField(verbose_name='Год рождения пациента', max_length=4)
    sign = models.BooleanField(verbose_name='Работник предприятия (да/нет)', default=False)
    department = models.CharField(verbose_name='Отдел, в котором работает', max_length=40, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'


class Exempt(models.Model):
    id = models.BigAutoField(verbose_name='Идентификатор льготы', primary_key=True)
    # exempt_type_choices = [
    #     ('student', 'Студент'),
    #     ('disabled', 'Инвалид'),
    #     ('veteran', 'Ветеран'),
    # ]
    exempt_type = models.CharField(verbose_name='Название льготы', max_length=60)
    exempt = models.PositiveIntegerField(verbose_name='Сумма льготы(%)', default=0)

    def __str__(self):
        return self.exempt_type

    class Meta:
        verbose_name = 'Льготы'
        verbose_name_plural = 'Льготы'

class Placement(models.Model):
    id = models.BigAutoField(verbose_name='Идентификатор посещения', primary_key=True, default=default_id)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, verbose_name='Пациент')
    date_start = models.DateTimeField(verbose_name='Дата помещения в стационар')
    date_stop = models.DateTimeField(verbose_name='Дата выписки из стационара')
    services = models.ManyToManyField('Service', verbose_name='Услуги')
    cost = models.PositiveIntegerField(verbose_name='Стоимость лечения всего курса', default=0)
    exempt = models.ForeignKey(Exempt, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Льгота')
    summa = models.PositiveIntegerField(verbose_name='К оплате', default=0)
    comment = models.TextField(verbose_name='Расшфировка', max_length=200)

    def __str__(self):
        return str(self.id)

    def get_patient(self):
        return self.patient

    class Meta:
        verbose_name = 'Посещение стационара'
        verbose_name_plural = 'Посещения стационаров'

class Underwriter(models.Model):
    id = models.BigAutoField(verbose_name='Идентификатор страховой компании', primary_key=True)
    company = models.CharField(verbose_name='Название страховой компании', max_length=60)
    comp_address = models.CharField(verbose_name='Адрес страховой компании', max_length=150)
    bank = models.CharField(verbose_name='Банк страховой компании', max_length=40)
    inn = models.CharField(verbose_name='ИНН страховой компании', max_length=10)
    chief = models.CharField(verbose_name='ФИО директора страховой компании', max_length=60)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'Страховая компания'
        verbose_name_plural = 'Страховая компании'

class InsurancePolicy(models.Model):
    id = models.BigAutoField(verbose_name='ИД полиса', primary_key=True, default=1160000000)
    underwriter = models.ForeignKey(Underwriter, on_delete=models.CASCADE, verbose_name='Страхования компания')
    balance = models.BigIntegerField(verbose_name='Баланс страхового полиса', default=15000)

    def __str__(self):
        return str(self.id)

    def get_patient(self):
        return Patient.objects.get(policy_number=self.id).name

    class Meta:
        verbose_name = 'Страховой полис'
        verbose_name_plural = 'Страховые полисы'

class Specialization(models.Model):
    id = models.BigAutoField(verbose_name='Идентификатор специализации', primary_key=True)
    name = models.CharField(verbose_name='Название специализации', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

class Service(models.Model):
    id = models.BigAutoField(verbose_name='Идентификатор услуги', primary_key=True)
    name = models.CharField(verbose_name='Название услуги', max_length=100)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, verbose_name='Специализация')
    cost = models.PositiveIntegerField(verbose_name='Стоимость услуги', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Staff(models.Model):
    id = models.BigAutoField(verbose_name='Идентификационный номер врача', primary_key=True)
    doctor = models.CharField(verbose_name='ФИО лечащего врача', max_length=60)
    university = models.ForeignKey('University', on_delete=models.CASCADE, verbose_name='Университет')
    # type_choices = [
    #     ('pediatrics', 'Педиатрия'),
    #     ('vaccination', 'Вакцинация'),
    #     ('tuberculin', 'Туберкулинодиагностика'),
    #     ('neurology', 'Неврология'),
    #     ('dermatology', 'Дерматология'),
    #     ('therapy', 'Терапия'),
    #     ('cardiology', 'Кардиология'),
    # ]
    # type = models.CharField(verbose_name='Специализация', choices=type_choices, max_length=20)
    type = models.ForeignKey(Specialization, on_delete=models.CASCADE, verbose_name='Специализация')
    expirience = models.PositiveSmallIntegerField(verbose_name='Стаж работы')
    ext_staff = models.BooleanField(verbose_name='Приглашенный специалист', default=False)

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

# class ExtStaff(models.Model):
#     id = models.BigAutoField(verbose_name='Идентификационный номер специалиста', primary_key=True)
#     doctor = models.CharField(verbose_name='ФИО специалиста', max_length=60)
#     university = models.ForeignKey('University', on_delete=models.CASCADE, verbose_name='Университет')
#
#     class Meta:
#         verbose_name = 'Приглашенный специалист'
#         verbose_name_plural = 'Приглашенные специалисты'

class University(models.Model):
    id = models.BigAutoField(verbose_name='Идентификационный номер специалиста', primary_key=True)
    short_name = models.CharField(verbose_name='Аббревиатура', max_length=10)
    full_name = models.CharField(verbose_name='полное название', max_length=60)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural = 'Университеты'


