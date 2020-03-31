from django.contrib import admin
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.lib.pagesizes import landscape, A4

from .models import Patient, Credit
from .ethiopian_calander_converter import gc_to_ec
from . import calculator


class PatientAdmin(admin.ModelAdmin):
    list_filter = ['patient_address', 'patient_gender']
    search_fields = ['mrn']
    list_display = ['mrn', 'patient_first_name', 'patient_father_name', 'patient_grand_father_name', 'patient_gender',
                    'patient_age']
    fieldsets = [
        ('Patient Information', {
            'fields': ['mrn', 'patient_first_name', 'patient_father_name', 'patient_grand_father_name',
                       'patient_gender']}),
        ('advanced',
         {'fields': ['patient_age', 'h_in_id', 'patient_address'], 'classes': ('collapse',)}),
    ]


class CreditAdmin(admin.ModelAdmin):
    exclude = ['created_by']
    actions = ['export_csv_for_print']
    list_per_page = 50
    list_filter = ['rx_type', 'created_date']
    list_display = ['get_full_name', 'card', 'lab', 'x_ray', 'others', 'bed', 'ultrasound', 'medication', 'rx_type',
                    'get_total', 'get_et_date','created_by']

    def get_full_name(self, obj):
        return obj.patient.full_name()

    get_full_name.short_description = 'Full name'

    def get_et_date(self, obj):
        et_date = gc_to_ec(year=obj.created_date.year,
                           month=obj.created_date.month,
                           day=obj.created_date.day)
        return et_date

    def add_up(self, names):
        card_sum = 0.0
        lab_sum = 0.0
        x_ray_sum = 0.0
        others_sum = 0.0
        bed_sum = 0.0
        ultrasound_sum = 0.0
        medication_sum = 0.0

        total_birr = 0;

        temp = list()
        names_len = len(names)
        len_counter = 0
        try:
            for (outerindex, outerelement) in enumerate(names):
                len_counter += 1
                temp.append(outerelement)
                if outerindex == 0:
                    print(f'outer element {outerelement}')
                    print(f'outer index {outerindex}')
                    print("skip")
                    continue

                for (innerindex, innerelement) in enumerate(outerelement):
                    if innerindex == 8:
                        card_sum += float(innerelement)
                    elif innerindex == 9:
                        lab_sum += float(innerelement)
                    elif innerindex == 10:
                        x_ray_sum += float(innerelement)
                    elif innerindex == 11:
                        others_sum += float(innerelement)
                    elif innerindex == 12:
                        bed_sum += float(innerelement)
                    elif innerindex == 13:
                        ultrasound_sum += float(innerelement)
                    elif innerindex == 14:
                        medication_sum += float(innerelement)

                    total_birr = card_sum + lab_sum + x_ray_sum + others_sum + bed_sum + ultrasound_sum + medication_sum
                    if outerindex % 7 == 0 and innerindex == len(outerelement) - 1:
                        if outerindex == 0:
                            continue
                        if len_counter != len(names):
                            temp.append(("Yezore Demer","","","","","","","",round(float(card_sum),2), round(float(lab_sum),2), round(float(x_ray_sum),2), round(float(others_sum),2),
                    round(float(bed_sum),2), round(float(ultrasound_sum),2), round(float(medication_sum),2),round(float(total_birr),2)))
                if len_counter == len(names) and innerindex == len(outerelement) - 1:
                    # number two (2) should be dynamic. it represents length of column
                    temp.append(
                    ("Total","","","","","","","",round(card_sum,2), round(lab_sum,2), round(x_ray_sum,2), round(others_sum,2), round(bed_sum,2), round(ultrasound_sum,2), round(medication_sum,2),round(total_birr,2)))
                    # temp.append(float(card_sum) + float(lab_sum) + float(x_ray_sum) + float(others_sum) + float(
                    # bed_sum) + float(ultrasound_sum) + float(medication_sum))
            # print(f'Type of temp {type(temp)}')
            return temp
        except IndexError as err:
            print(f"hey, you list index out of range {len(names)}")


    def export_csv_for_print(self, request, queryset):
        try:
            elements = []
            data = [('Date', 'Full Name', 'AGE', 'Gender', 'Address', 'H/in/ID', 'MRN', 'RX-Type', 'CARD', 'Lab',
                     'X-Ray', 'others', 'Bed', 'U/S', 'Medication', 'Total', 'by')]

            for p in queryset:
                et_date = gc_to_ec(year=p.created_date.year,
                                   month=p.created_date.month,
                                   day=p.created_date.day)

                data.append((et_date, f'{p.patient.full_name()}',
                             f'{p.patient.patient_age}', f'{p.patient.patient_gender}',
                             f'{p.patient.patient_address}',
                             f'{p.patient.h_in_id}', f'{p.patient.mrn}', f'{p.rx_type}',
                             p.card, p.lab,
                             p.x_ray, p.others,
                             p.bed, p.ultrasound,
                             p.medication,
                             p.get_total(),p.created_by))

            returned_value = self.add_up(data)
            # print(returned_value)
            doc = SimpleDocTemplate('/tmp/somefilename.pdf', pagesize=landscape(A4))
            table = Table(returned_value)
            TABLE_STYLE = TableStyle([('SIZE', (0, 0), (-1, -1), 8), ('ALIGN', (0, 0), (-2, -2), 'RIGHT'),
                                      ('BOX', (0, 0), (-1, -1), 0.3, colors.black),
                                      ('INNERGRID', (0, 0), (-1, -1), 0.9, colors.red)])
            table.setStyle(TABLE_STYLE)
            elements.append(table)
            doc.build(elements)
            fs = FileSystemStorage('/tmp')
            with fs.open('somefilename.pdf') as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
                return response
            return response

        except Exception as exc:
            self.message_user(request, f'Failed to Export {exc} ')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()

    export_csv_for_print.short_description = "Export for print"
    get_et_date.short_description = "Date"


# Register your models here.
admin.site.register(Patient, PatientAdmin)
admin.site.register(Credit, CreditAdmin)
