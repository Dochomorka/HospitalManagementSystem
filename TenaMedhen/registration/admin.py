from django.contrib import admin
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from reportlab.platypus import SimpleDocTemplate, PageBreak
from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.lib.pagesizes import landscape, A4

from .models import Patient, Credit
from .ethiopian_calander_converter import gc_to_ec
from . import calculator
from .MonthFilter import DateOfCreationFilter


class CreditInline(admin.TabularInline):
    exclude = ['created_by','created_date']
    model = Credit
    extra = 1


class PatientAdmin(admin.ModelAdmin):
    list_per_page = 15
    inlines = [CreditInline]
    exclude = ['created_by', 'created_date']
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

    def save_formset(self, request, form, formset, change):
        print(f'user {request.user} #####')
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, Credit):
                instance.created_by = str(request.user)
            instance.save()




class CreditAdmin(admin.ModelAdmin):
    exclude = ['created_by']
    actions = ['export_csv_for_print']
    search_fields = ['created_date']
    list_per_page = 15
    list_filter = ['rx_type', 'created_date', DateOfCreationFilter]
    list_display = ['get_full_name', 'card', 'lab', 'x_ray', 'others', 'bed', 'ultrasound', 'medication', 'rx_type',
                    'get_total', 'get_et_date', 'created_by']

    def get_full_name(self, obj):
        return obj.patient.full_name()

    def get_sept(self, obj):
        return Credit.objects.filter(date__range=["2011-01-01", "2011-01-31"])

    get_full_name.short_description = 'Full name'

    def get_et_date(self, obj):
        et_date = gc_to_ec(year=obj.created_date.year,
                           month=obj.created_date.month,
                           day=obj.created_date.day)
        return et_date

    def add_up(self, names, page_end=25):
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
                    if outerindex % page_end == 0 and innerindex == len(outerelement) - 1:
                        if outerindex == 0:
                            continue
                        if len_counter != len(names):
                            temp.append(("", "", "", "", "", "", "", "", str(round(float(card_sum), 2)),
                                         str(round(float(lab_sum), 2)), str(round(float(x_ray_sum), 2)),
                                         str(round(float(others_sum), 2)),
                                         str(round(float(bed_sum), 2)), str(round(float(ultrasound_sum), 2)),
                                         str(round(float(medication_sum), 2)), str(round(float(total_birr), 2))))

                            temp.append(("", "", "", "", "", "", "", "", str(round(float(card_sum), 2)),
                                         str(round(float(lab_sum), 2)), str(round(float(x_ray_sum), 2)),
                                         str(round(float(others_sum), 2)),
                                         str(round(float(bed_sum), 2)), str(round(float(ultrasound_sum), 2)),
                                         str(round(float(medication_sum), 2)), str(round(float(total_birr), 2))))

                if len_counter == len(names) and innerindex == len(outerelement) - 1:
                    temp.append(
                        ("*Total", "", "", "", "", "", "", "", str(round(card_sum, 2)), str(round(lab_sum, 2)),
                         str(round(x_ray_sum, 2)), str(round(others_sum, 2)), str(round(bed_sum, 2)),
                         str(round(ultrasound_sum, 2)), str(round(medication_sum, 2)), str(round(total_birr, 2))))

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
                             f'{p.card}', f'{p.lab}',
                             f'{p.x_ray}', f'{p.others}',
                             f'{p.bed}', f'{p.ultrasound}',
                             f'{p.medication}',
                             f'{p.get_total()}', f'{p.created_by}'))

            returned_value = self.add_up(data, 20)

            doc = SimpleDocTemplate('/tmp/somefilename.pdf', pagesize=landscape(A4))
            TABLE_STYLE = TableStyle([('SIZE', (0, 0), (-1, -1), 8), ('ALIGN', (0, 0), (-2, -2), 'RIGHT'),
                                      ('BOX', (0, 0), (-1, -1), 0.3, colors.blue),
                                      ('INNERGRID', (0, 0), (-1, -1), 0.9, colors.azure)])

            elements = self.break_to_pages(returned_value)

            doc.build(elements)
            fs = FileSystemStorage('/tmp')
            with fs.open('somefilename.pdf') as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
                return response
            return response

        except Exception as exc:
            raise exc

    def break_to_pages(self, twod_array):
        print(f'two d array size {twod_array} = {len(twod_array)}')
        tables = list()
        table = list()

        TABLE_STYLE = TableStyle([('SIZE', (0, 0), (-1, -1), 8), ('ALIGN', (0, 0), (-2, -2), 'RIGHT'),
                                  ('BOX', (0, 0), (-1, -1), 0.3, colors.black),
                                  ('INNERGRID', (0, 0), (-1, -1), 0.9, colors.red)])

        for (outerindex, outervalue) in enumerate(twod_array):

            if (outerindex % 21 == 0 and outerindex > 0):
                table.append(list(outervalue))
                t = Table(table)
                t.setStyle(TABLE_STYLE)
                tables.append(t)
                tables.append(PageBreak())
                table.clear()  # calling clear will eliminate all entries
                print(f'adding module block')
            else:
                table.append(list(outervalue))
                if(outerindex == (len(twod_array)-1)):
                    table.append(list(outervalue))
                    t = Table(table)
                    t.setStyle(TABLE_STYLE)
                    tables.append(t)

                    table.clear()
                print(f'adding else block {outervalue} out of {len(twod_array)}')
        print(f'tables ....')
        return tables

    def save_model(self, request, obj, form, change):
        print(f'CreaditAdmin save_model {request.user} ******')
        # if not change:
        #     obj.created_by = request.user
        # obj.save()
        if not change:
            obj.created_by = str(request.user)
            print(f'obj.created_by = {request.user}')
        super().save_model(request, obj, form, change)
        print(f'after calling super! obj = {obj}')



    export_csv_for_print.short_description = "Export for print"
    get_et_date.short_description = "Date"
    get_sept.short_description = "መስከረም ወር"


# Register your models here.
admin.site.register(Patient, PatientAdmin)
admin.site.register(Credit, CreditAdmin)
