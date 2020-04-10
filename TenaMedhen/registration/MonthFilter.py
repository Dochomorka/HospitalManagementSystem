from django.contrib import admin
import datetime
from .ethiopian_calander_converter import et_converted_year
from .ethiopian_calander_converter import is_leap_year


# filter queryset based on date interval
# return different queryset based on leap year
# if leap year

class DateOfCreationFilter(admin.SimpleListFilter):
    # here is how you implement filter
    # declare two date variable one for start date one for end date
    # pass year daynamicaly

    title = "Month"
    parameter_name = "month"

    def lookups(self, request, model_admin):
        today = datetime.date.today()
        ethiopian_year = et_converted_year(today.year, today.month, today.day)
        return (("sep", f"መስከረም {ethiopian_year}"), ("tik", f"ጥቅምት {ethiopian_year}"), ("hid", f"ህዳር {ethiopian_year}"),
                ("tah", f"ታህሳስ {ethiopian_year}"), ("tir", f"ጥር {ethiopian_year}"), ("yek", f"የካቲት {ethiopian_year}"),
                ("meg", f"መጋቢት {ethiopian_year}"), ("mia", f"ሚያዚያ {ethiopian_year}"), ("gin", f"ግንቦት {ethiopian_year}"),
                ("sene", f"ሰኔ {ethiopian_year}"), ("ham", f"ሃምሌ {ethiopian_year}"),
                ("neh", f"ነሃሴ ና ጳጉሜ {ethiopian_year}"))

    def queryset(self, request, queryset):
        leap_year = is_leap_year(datetime.date.today().year)
        today = datetime.date.today()
        if self.value() == "gin":
            if leap_year:
                start_date = datetime.date(year=today.year, month=5, day=9)
                end_date = datetime.date(year=today.year, month=6, day=7)
            else:
                start_date = datetime.date(year=today.year, month=5, day=9)
                end_date = datetime.date(year=today.year, month=6, day=7)

            return queryset.filter(created_date__gte=start_date, created_date__lte=end_date)

        if self.value() == "sene":
            if leap_year:
                start_date = datetime.date(year=today.year, month=6, day=8)
                end_date = datetime.date(year=today.year, month=7, day=7)
            else:
                start_date = datetime.date(year=today.year, month=6, day=8)
                end_date = datetime.date(year=today.year, month=7, day=7)

            return queryset.filter(created_date__gte=start_date, created_date__lte=end_date)

        if self.value() == "ham":
            if leap_year:
                start_date = datetime.date(year=today.year, month=7, day=8)
                end_date = datetime.date(year=today.year, month=8, day=6)
            else:
                start_date = datetime.date(year=today.year, month=7, day=8)
                end_date = datetime.date(year=today.year, month=8, day=6)

            return queryset.filter(created_date__gte=start_date, created_date__lte=end_date)

        if self.value() == "neh":
            if leap_year:
                start_date = datetime.date(year=today.year, month=8, day=7)
                end_date = datetime.date(year=today.year, month=9, day=11)
            else:
                start_date = datetime.date(year=today.year, month=8, day=7)
                end_date = datetime.date(year=today.year, month=9, day=10)

            return queryset.filter(created_date__gte=start_date, created_date__lte=end_date)

        if self.value() == "yek":
            if leap_year:
                start_date = datetime.date(year=today.year, month=2, day=9)
                end_date = datetime.date(year=today.year, month=3, day=9)
            else:
                start_date = datetime.date(year=today.year, month=2, day=8)
                end_date = datetime.date(year=today.year, month=3, day=9)

            return queryset.filter(created_date__gte=start_date, created_date__lte=end_date)

        if self.value() == "meg":
            if leap_year:
                start_date = datetime.date(year=today.year, month=3, day=10)
                end_date = datetime.date(year=today.year, month=4, day=8)
            else:
                start_date = datetime.date(year=today.year, month=3, day=10)
                end_date = datetime.date(year=today.year, month=4, day=8)

            return queryset.filter(created_date__gte=start_date, created_date__lte=end_date)

        if self.value() == "mia":
            if leap_year:
                start_date = datetime.date(year=today.year, month=4, day=9)
                end_date = datetime.date(year=today.year, month=5, day=8)
            else:
                start_date = datetime.date(year=today.year, month=4, day=9)
                end_date = datetime.date(year=today.year, month=5, day=8)

            return queryset.filter(created_date__gte=start_date, created_date__lte=end_date)

        if self.value() == "sep":
            if leap_year:
                start_date = datetime.date(year=today.year, month=9, day=11)
                end_date = datetime.date(year=today.year, month=10, day=11)
            else:
                start_date = datetime.date(year=today.year, month=9, day=10)
                end_date = datetime.date(year=today.year, month=10, day=10)

            return queryset.filter(created_date__gte=start_date, created_date__lte=end_date)

        if self.value() == "tik":
            if leap_year:
                start_date = datetime.date(year=today.year, month=10, day=11)
                end_date = datetime.date(year=today.year, month=11, day=10)
            else:
                start_date = datetime.date(year=today.year, month=10, day=10)
                end_date = datetime.date(year=today.year, month=11, day=10)

            return queryset.filter(created_date__gte=start_date, created_date__lte=end_date)

        if self.value() == "hid":
            if leap_year:
                start_date = datetime.date(year=today.year, month=11, day=11)
                end_date = datetime.date(year=today.year, month=12, day=10)
            else:
                start_date = datetime.date(year=today.year, month=11, day=10)
                end_date = datetime.date(year=today.year, month=12, day=9)

            return queryset.filter(created_date__gte=start_date, created_date__lte=end_date)

        if self.value() == "tah":
            if leap_year:
                start_date = datetime.date(year=today.year, month=12, day=11)
                end_date = datetime.date(year=today.year, month=1, day=9)
            else:
                start_date = datetime.date(year=today.year, month=12, day=10)
                end_date = datetime.date(year=today.year, month=1, day=8)

            return queryset.filter(created_date__gte=start_date, created_date__lte=end_date)

        if self.value() == "tir":
            if leap_year:
                start_date = datetime.date(year=today.year, month=1, day=10)
                end_date = datetime.date(year=today.year, month=2, day=9)
            else:
                start_date = datetime.date(year=today.year, month=1, day=9)
                end_date = datetime.date(year=today.year, month=2, day=8)

            return queryset.filter(created_date__gte=start_date, created_date__lte=end_date)
