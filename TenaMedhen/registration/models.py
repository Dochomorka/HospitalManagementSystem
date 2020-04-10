from django.db import models
from django.utils import timezone


class Patient(models.Model):
    GENDER = [('female', 'female'), ('male', 'male')]
    patient_first_name = models.CharField(max_length=255, default='')
    patient_father_name = models.CharField(max_length=255, default='')
    patient_grand_father_name = models.CharField(max_length=255, default='')
    patient_gender = models.CharField(choices=GENDER, max_length=255, default='')
    patient_age = models.IntegerField(default=1)
    h_in_id = models.CharField(max_length=255, default='', verbose_name='H/IN/ID')
    mrn = models.CharField(max_length=255, default='')
    patient_address = models.CharField(max_length=255, default='')

    # patient_credit = models.ForeignKey(Credit, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.mrn}] {self.full_name()} '

    def full_name(self):
        return f'{self.patient_first_name} {self.patient_father_name} {self.patient_grand_father_name}'


# Create your models here.

class Credit(models.Model):
    # rx_type weather the patient is in/out patient
    PATIENT_TYPE = [('in patient', 'in Patient'), ('out patient', 'out patient')]
    rx_type = models.CharField(choices=PATIENT_TYPE, max_length=255)
    card = models.FloatField(default=0.0)
    lab = models.FloatField(default=0.0)
    x_ray = models.FloatField(default=0.0)
    others = models.FloatField(default=0.0)
    bed = models.FloatField(default=0.0)
    ultrasound = models.FloatField(default=0.0)
    medication = models.FloatField(default=0.0)
    created_by = models.CharField(max_length=255, default='Unknown')
    created_date = models.DateField(max_length=255, default=timezone.now)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False)

    def get_total(self):
        try:
            total = [float(self.card), float(self.lab), float(self.x_ray), float(self.others), float(self.bed),
                     float(self.ultrasound), float(self.medication)]
            return str(sum(total))
        except Exception as exc:
            raise ValueError('Please enter only numbers in you entries')

    def formatted_date(self):
        return f'{self.created_date.day}-{self.created_date.month}-{self.created_date.year} '

    def __str__(self):
        return f'Total in {self.formatted_date()} is {self.get_total()} '
