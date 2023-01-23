from django.contrib import admin
from .models import *
from django.urls import re_path as url
from django.utils.html import format_html
from django.urls import reverse
from . import data_format, waybill_engine
from django.http import HttpResponse, HttpResponseRedirect
from slugify import slugify
import os

admin.site.site_header = 'Медицинский стационар'
admin.site.site_title = 'Медицинский стационар'
admin.site.index_title = 'Администрирование'

# Register your models here.
@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    model = Specialization

    list_display = ['name', ]
    search_fields = ['name', ]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    model = Service

    list_display = ['name', 'specialization', 'cost']
    list_display_links = ['name', ]
    search_fields = ['name', ]
    autocomplete_fields = ['specialization']
    ordering = ['id']

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    model = University

    list_display = ['full_name', 'short_name', ]
    search_fields = ['full_name', 'short_name', ]

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    model = Staff

    list_display = ['doctor', 'university', 'type', 'expirience', 'ext_staff', ]
    search_fields = ['doctor', 'type__name']
    autocomplete_fields = ['university', 'type']

@admin.register(Exempt)
class ExemptAdmin(admin.ModelAdmin):
    model = Exempt

    list_display = ['exempt_type', 'exempt', ]
    search_fields = ['exempt_type', ]

    class Media:
        js = ('//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
              'js/exempt.js',)

@admin.register(Underwriter)
class UnderwriterAdmin(admin.ModelAdmin):
    model = Underwriter

    list_display = ['company', 'comp_address', 'bank', 'inn', 'chief', ]
    search_fields = ['company', 'comp_address', ]

    class Media:
        js = ('//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
              'js/jquery.maskedinput.js',
              'js/jquery.maskedinput.min.js',
              'js/underwriter_masking.js',)

@admin.register(InsurancePolicy)
class InsurancePolicyAdmin(admin.ModelAdmin):
    model = InsurancePolicy

    InsurancePolicy.get_patient.short_description = 'Пациент'

    list_display = ['id', 'get_patient', 'underwriter', 'balance', ]
    search_fields = ['id', ]
    autocomplete_fields = ['underwriter', ]


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    model = Patient

    list_display = ['name', 'policy_number', 'address', 'district', ]
    search_fields = ['name', 'policy_number', ]
    autocomplete_fields = ['policy_number', ]

    class Media:
        js = ('//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
              'js/jquery.maskedinput.js',
              'js/jquery.maskedinput.min.js',
              'js/patient_masking.js',
              'js/patient.js',)


@admin.register(Placement)
class PlacementAdmin(admin.ModelAdmin):
    model = Placement

    Placement.get_patient.short_description = 'Пациент'

    list_display = ['get_patient', 'date_start', 'date_stop', 'summa', 'placement_actions', ]
    list_display_links = ['get_patient', ]
    # search_fields = ['patient', ]
    # autocomplete_fields = ['patient', 'exempt']

    class Media:
        js = ('//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
              'js/jquery.maskedinput.js',
              'js/jquery.maskedinput.min.js',
              'js/placement_masking.js',
              'js/placement.js',)

    def get_urls(self):
        urls = super(PlacementAdmin, self).get_urls()
        custom_urls = [
            url(
                r'^(?P<id>.+)/save_check/$',
                self.admin_site.admin_view(self.save_check),
                name='save_check',
            ),
        ]
        return custom_urls + urls

    def placement_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">&nbsp  Акт оказанных услуг &nbsp</a>'
            '<p></p>',
            reverse('admin:save_check', args=[obj.pk]),
        )
    placement_actions.short_description = 'Выписка'
    placement_actions.allow_tags = True

    def save_check(self, request, id,  *args, **kwargs):
        data = data_format.get_order_data(int(id))
        path = waybill_engine.waybill_generate(data)
        temp = slugify(path.split('/')[2], save_order=True, separator='.')
        if os.path.exists(path):
            with open(path, 'rb') as fh:
                response = HttpResponse(fh.read(),
                                        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = 'inline; filename=' + temp
                return response

