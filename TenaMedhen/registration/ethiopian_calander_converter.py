# YEAR CONVERTIONS
# 1. ACCEPT year in gc eg. 2020
# 2. if month > = 9 date = 12 = substruct 7 years from GC year
# 3. if month < = 8 = substruct  substruct 8 years from gc
def et_converted_year(year, month, day):
    _converted_year = year
    if month in [10, 11, 12]:
        _converted_year = year - 7
    elif month in [9]:
        if day >= 12:
            _converted_year = year - 7
        else:
            _converted_year = year - 8
    elif month in [1, 2, 3, 4, 5, 6, 7, 8]:
        _converted_year = year - 8
    return _converted_year


def is_leap_year(year):
    is_leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap = True
            else:
                is_leap = False
        else:
            is_leap = True
    else:
        is_leap = False

    return is_leap


def gc_to_ec(year=2020, month=1, day=1):
    ethiopian_month = 0
    ethiopian_day = 0
    ethiopian_year = year - 8

    ethiopian_month_in_number = {
        'Meskerem': 1,
        'Tikimt': 2,
        'Hidar': 3,
        'Tahisas': 4,
        'Tir': 5,
        'Yekatit': 6,
        'Megabit': 7,
        'Miaziya': 8,
        'Ginbot': 9,
        'Sene': 10,
        'Hamlea': 11,
        'Nehasea': 12,
        'Pagumea': 13
    }

    leap_year = is_leap_year(et_converted_year(year, month, day))
    if month == 1:
        ethiopian_month = "Tir"
        if leap_year:
            ethiopian_day = day - 9
            if ethiopian_day <= 0:
                ethiopian_month = "Tahisas"
                if ethiopian_day <= 0:
                    if ethiopian_day == 0:
                        ethiopian_day = 30
                    elif ethiopian_day == -1:
                        ethiopian_day = 29
                    elif ethiopian_day == -2:
                        ethiopian_day = 28
                    elif ethiopian_day == -3:
                        ethiopian_day = 27
                    elif ethiopian_day == -4:
                        ethiopian_day = 26
                    elif ethiopian_day == -5:
                        ethiopian_day = 25
                    elif ethiopian_day == -6:
                        ethiopian_day = 24
                    elif ethiopian_day == -7:
                        ethiopian_day = 23
                    elif ethiopian_day == -8:
                        ethiopian_day = 22

        else:
            ethiopian_day = day - 8
            if ethiopian_day <= 0:
                ethiopian_month = "Tahisas"
                if ethiopian_day <= 0:
                    if ethiopian_day == 0:
                        ethiopian_day = 30
                    elif ethiopian_day == -1:
                        ethiopian_day = 29
                    elif ethiopian_day == -2:
                        ethiopian_day = 28
                    elif ethiopian_day == -3:
                        ethiopian_day = 27
                    elif ethiopian_day == -4:
                        ethiopian_day = 26
                    elif ethiopian_day == -5:
                        ethiopian_day = 25
                    elif ethiopian_day == -6:
                        ethiopian_day = 24
                    elif ethiopian_day == -7:
                        ethiopian_day = 23
                    elif ethiopian_day == -8:
                        ethiopian_day = 22

    elif month == 2:
        ethiopian_month = "Yekatit"
        if leap_year:
            ethiopian_day = day - 8
            if ethiopian_day <= 0:
                ethiopian_month = "Tir"
                if ethiopian_day == 0:
                    ethiopian_day = 30

                elif ethiopian_day == -1:
                    ethiopian_day = 29

                elif ethiopian_day == -2:
                    ethiopian_day = 28

                elif ethiopian_day == -3:
                    ethiopian_day = 27

                elif ethiopian_day == -4:
                    ethiopian_day = 26

                elif ethiopian_day == -5:
                    ethiopian_day = 25

                elif ethiopian_day == -6:
                    ethiopian_day = 24

                elif ethiopian_day == -7:
                    ethiopian_day = 23

        else:
            ethiopian_day = day - 7
            if ethiopian_day <= 0:
                ethiopian_month = "Tir"
                if ethiopian_day == 0:
                    ethiopian_day = 30

                elif ethiopian_day == -1:
                    ethiopian_day = 29

                elif ethiopian_day == -2:
                    ethiopian_day = 28

                elif ethiopian_day == -3:
                    ethiopian_day = 27

                elif ethiopian_day == -4:
                    ethiopian_day = 26

                elif ethiopian_day == -5:
                    ethiopian_day = 25

                elif ethiopian_day == -6:
                    ethiopian_day = 24

                elif ethiopian_day == -7:
                    ethiopian_day = 23

    elif month == 3:
        ethiopian_month = "Megabit"
        ethiopian_day = day - 9
        if ethiopian_day <= 0:
            ethiopian_month = "Yekatit"
            if ethiopian_day == 0:
                ethiopian_day = 30
            elif ethiopian_day == -1:
                ethiopian_day = 29
            elif ethiopian_day == -2:
                ethiopian_day = 28
            elif ethiopian_day == -3:
                ethiopian_day = 27
            elif ethiopian_day == -4:
                ethiopian_day = 26
            elif ethiopian_day == -5:
                ethiopian_day = 25
            elif ethiopian_day == -6:
                ethiopian_day = 24
            elif ethiopian_day == -7:
                ethiopian_day = 23
            elif ethiopian_day == -8:
                ethiopian_day = 22

    elif month == 4:
        ethiopian_month = "Miaziya"
        ethiopian_day = day - 8
        if ethiopian_day <= 0:
            ethiopian_month = "Megabit"
            if ethiopian_day == 0:
                ethiopian_day = 30
            elif ethiopian_day == -1:
                ethiopian_day = 29
            elif ethiopian_day == -2:
                ethiopian_day = 28
            elif ethiopian_day == -3:
                ethiopian_day = 27
            elif ethiopian_day == -4:
                ethiopian_day = 26
            elif ethiopian_day == -5:
                ethiopian_day = 25
            elif ethiopian_day == -6:
                ethiopian_day = 24
            elif ethiopian_day == -7:
                ethiopian_day = 23


    elif month == 5:
        ethiopian_month = "Ginbot"
        ethiopian_day = day - 8
        if ethiopian_day <= 0:
            ethiopian_month = "Miaziya"
            if ethiopian_day == 0:
                ethiopian_day = 30
            elif ethiopian_day == -1:
                ethiopian_day = 29
            elif ethiopian_day == -2:
                ethiopian_day = 28
            elif ethiopian_day == -3:
                ethiopian_day = 27
            elif ethiopian_day == -4:
                ethiopian_day = 26
            elif ethiopian_day == -5:
                ethiopian_day = 25
            elif ethiopian_day == -6:
                ethiopian_day = 24
            elif ethiopian_day == -7:
                ethiopian_day = 23



    elif month == 6:
        ethiopian_month = "Sene"
        ethiopian_day = day - 7
        if ethiopian_day <= 0:
            ethiopian_month = "Ginbot"
            if ethiopian_day == 0:
                ethiopian_day = 30
            elif ethiopian_day == -1:
                ethiopian_day = 29
            elif ethiopian_day == -2:
                ethiopian_day = 28
            elif ethiopian_day == -3:
                ethiopian_day = 27
            elif ethiopian_day == -4:
                ethiopian_day = 26
            elif ethiopian_day == -5:
                ethiopian_day = 25
            elif ethiopian_day == -6:
                ethiopian_day = 24

    elif month == 7:
        ethiopian_month = "Hamlea"
        ethiopian_day = day - 7
        if ethiopian_day <= 0:
            ethiopian_month = "Sene"
            if ethiopian_day == 0:
                ethiopian_day = 30
            elif ethiopian_day == -1:
                ethiopian_day = 29
            elif ethiopian_day == -2:
                ethiopian_day = 28
            elif ethiopian_day == -3:
                ethiopian_day = 27
            elif ethiopian_day == -4:
                ethiopian_day = 26
            elif ethiopian_day == -5:
                ethiopian_day = 25
            elif ethiopian_day == -6:
                ethiopian_day = 24
            elif ethiopian_day == -7:
                ethiopian_day = 23

    elif month == 8:
        ethiopian_month = "Nehasea"
        ethiopian_day = day - 6
        if ethiopian_day <= 0:
            ethiopian_month = "Hamlea"
            if ethiopian_day == 0:
                ethiopian_day = 30
            elif ethiopian_day == -1:
                ethiopian_day = 29
            elif ethiopian_day == -2:
                ethiopian_day = 28
            elif ethiopian_day == -3:
                ethiopian_day = 27
            elif ethiopian_day == -4:
                ethiopian_day = 26
            elif ethiopian_day == -5:
                ethiopian_day = 25

    elif month == 9:
        ethiopian_month = "Meskerem"
        if leap_year:
            ethiopian_day = day - 11
            if ethiopian_day <= 0:
                ethiopian_month = "Pagumea"
                if ethiopian_day == 0:
                    ethiopian_day = 6
                elif ethiopian_day == -1:
                    ethiopian_day = 5
                elif ethiopian_day == -2:
                    ethiopian_day = 4
                elif ethiopian_day == -3:
                    ethiopian_day = 3
                elif ethiopian_day == -4:
                    ethiopian_day = 2
                elif ethiopian_day == -5:
                    ethiopian_day = 1
                if ethiopian_day < -5:
                    ethiopian_month = "Nehasea"
                    if ethiopian_day == -6:
                        ethiopian_day = 30
                    elif ethiopian_day == -7:
                        ethiopian_day = 29
                    elif ethiopian_day == -8:
                        ethiopian_day = 28
                    elif ethiopian_day == -9:
                        ethiopian_day = 27
                    elif ethiopian_day == -10:
                        ethiopian_day = 26

        else:
            ethiopian_day = day - 10
            if ethiopian_day <= 0:
                ethiopian_month = "Pagumea"
                if ethiopian_day == 0:
                    ethiopian_day = 5
                elif ethiopian_day == -1:
                    ethiopian_day = 4
                elif ethiopian_day == -2:
                    ethiopian_day = 3
                elif ethiopian_day == -3:
                    ethiopian_day = 2
                elif ethiopian_day == -4:
                    ethiopian_day = 1
                if ethiopian_day <= -5:
                    ethiopian_month = "Nehasea"
                    if ethiopian_day == -5:
                        ethiopian_day = 30
                    elif ethiopian_day == -6:
                        ethiopian_day = 29
                    elif ethiopian_day == -7:
                        ethiopian_day = 28
                    elif ethiopian_day == -8:
                        ethiopian_day = 27
                    elif ethiopian_day == -9:
                        ethiopian_day = 26


    elif month == 10:
        ethiopian_month = "Tikimt"
        if leap_year:
            ethiopian_day = day - 11
            if ethiopian_day <= 0:
                ethiopian_month = "Meskerem"
                if ethiopian_day == 0:
                    ethiopian_day = 30
                elif ethiopian_day == -1:
                    ethiopian_day = 29
                elif ethiopian_day == -2:
                    ethiopian_day = 28
                elif ethiopian_day == -3:
                    ethiopian_day = 27
                elif ethiopian_day == -4:
                    ethiopian_day = 26
                elif ethiopian_day == -5:
                    ethiopian_day = 25
                elif ethiopian_day == -6:
                    ethiopian_day = 24
                elif ethiopian_day == -7:
                    ethiopian_day = 23
                elif ethiopian_day == -8:
                    ethiopian_day = 22
                elif ethiopian_day == -9:
                    ethiopian_day = 21
                elif ethiopian_day == -10:
                    ethiopian_day = 20
        else:
            ethiopian_day = day - 10
            if ethiopian_day <= 0:
                ethiopian_month = "Meskerem"
                if ethiopian_day == 0:
                    ethiopian_day = 30
                elif ethiopian_day == -1:
                    ethiopian_day = 29
                elif ethiopian_day == -2:
                    ethiopian_day = 28
                elif ethiopian_day == -3:
                    ethiopian_day = 27
                elif ethiopian_day == -4:
                    ethiopian_day = 26
                elif ethiopian_day == -5:
                    ethiopian_day = 25
                elif ethiopian_day == -6:
                    ethiopian_day = 24
                elif ethiopian_day == -7:
                    ethiopian_day = 23
                elif ethiopian_day == -8:
                    ethiopian_day = 22
                elif ethiopian_day == -9:
                    ethiopian_day = 21





    elif month == 11:
        ethiopian_month = "Hidar"
        if leap_year:
            ethiopian_day = day - 10
            if ethiopian_day <= 0:
                ethiopian_month = "Tikimt"
                if ethiopian_day <= 0:
                    if ethiopian_day == 0:

                        ethiopian_day = 30
                    elif ethiopian_day == -1:
                        ethiopian_day = 29
                    elif ethiopian_day == -2:
                        ethiopian_day = 28
                    elif ethiopian_day == -3:
                        ethiopian_day = 27
                    elif ethiopian_day == -4:
                        ethiopian_day = 26
                    elif ethiopian_day == -5:
                        ethiopian_day = 25
                    elif ethiopian_day == -6:
                        ethiopian_day = 24
                    elif ethiopian_day == -7:
                        ethiopian_day = 23
                    elif ethiopian_day == -8:
                        ethiopian_day = 22
                    elif ethiopian_day == -9:
                        ethiopian_day = 21


        else:
            ethiopian_day = day - 9
            if ethiopian_day <= 0:
                ethiopian_month = "Tikimt"
                if ethiopian_day <= 0:
                    if ethiopian_day == 0:
                        ethiopian_day = 30
                    elif ethiopian_day == -1:
                        ethiopian_day = 29
                    elif ethiopian_day == -2:
                        ethiopian_day = 28
                    elif ethiopian_day == -3:
                        ethiopian_day = 27
                    elif ethiopian_day == -4:
                        ethiopian_day = 26
                    elif ethiopian_day == -5:
                        ethiopian_day = 25
                    elif ethiopian_day == -6:
                        ethiopian_day = 24
                    elif ethiopian_day == -7:
                        ethiopian_day = 23
                    elif ethiopian_day == -8:
                        ethiopian_day = 22


    elif month == 12:
        ethiopian_month = "Tahisas"
        if leap_year:
            ethiopian_day = day - 10
            if ethiopian_day <= 0:
                ethiopian_month = "Hidar"
                if ethiopian_day <= 0:
                    if ethiopian_day == 0:

                        ethiopian_day = 30
                    elif ethiopian_day == -1:
                        ethiopian_day = 29
                    elif ethiopian_day == -2:
                        ethiopian_day = 28
                    elif ethiopian_day == -3:
                        ethiopian_day = 27
                    elif ethiopian_day == -4:
                        ethiopian_day = 26
                    elif ethiopian_day == -5:
                        ethiopian_day = 25
                    elif ethiopian_day == -6:
                        ethiopian_day = 24
                    elif ethiopian_day == -7:
                        ethiopian_day = 23
                    elif ethiopian_day == -8:
                        ethiopian_day = 22
                    elif ethiopian_day == -9:
                        ethiopian_day = 21


        else:
            ethiopian_day = day - 9
            if ethiopian_day <= 0:
                ethiopian_month = "Hidar"
                if ethiopian_day <= 0:
                    if ethiopian_day == 0:
                        ethiopian_day = 30
                    elif ethiopian_day == -1:
                        ethiopian_day = 29
                    elif ethiopian_day == -2:
                        ethiopian_day = 28
                    elif ethiopian_day == -3:
                        ethiopian_day = 27
                    elif ethiopian_day == -4:
                        ethiopian_day = 26
                    elif ethiopian_day == -5:
                        ethiopian_day = 25
                    elif ethiopian_day == -6:
                        ethiopian_day = 24
                    elif ethiopian_day == -7:
                        ethiopian_day = 23
                    elif ethiopian_day == -8:
                        ethiopian_day = 22
    return f"{ethiopian_day} /{ethiopian_month_in_number[ethiopian_month]} /{ethiopian_year}"
