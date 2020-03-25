def add_up(names):
    print("Calling names ...")
    # names = [(11, 22, 1, 33),
    #          (4, 52, 1, 6),
    #          (38, 34, 1, 38),
    #          (10, 383, 1, 38),
    #          (25, 28, 1, 39),
    #          (92, 83, 1, 29),
    #          (10, 10, 1, 10),
    #          (10, 10, 1, 10),
    #          (290, 83, 1, 28)
    #          ]
    card_sum = 0
    lab_sum = 0
    x_ray_sum = 0
    others_sum = 0
    bed_sum = 0
    ultrasound_sum = 0
    medication_sum = 0


    # temp = list()
    temp = []
    names_len = len(names)
    len_counter = 0
    try:
        for (outerindex, outerelement) in enumerate(names):
            len_counter += 1
            temp.append(outerelement)
            if outerindex == 0:
                continue

            for (innerindex, innerelement) in enumerate(outerelement):
                if innerindex == 9:
                    card_sum += innerelement
                elif innerindex == 10:
                    lab_sum += innerelement
                elif innerindex == 11:
                    x_ray_sum += innerelement
                elif innerindex == 12:
                    others_sum += innerelement
                elif innerindex == 13:
                    bed_sum += innerelement
                elif innerindex == 14:
                    ultrasound_sum += innerelement
                elif innerindex == 15:
                    medication_sum += innerelement

                if outerindex % 7 == 0 and innerindex == len(outerelement) - 1:
                    # number two (2) should be dynamic. it represents length of column
                    if outerindex == 0:
                        continue
                    if len_counter != len(names):
                        temp.append((float(card_sum), float(lab_sum), float(x_ray_sum), float(others_sum),float(bed_sum),float(ultrasound_sum),float(medication_sum)))
                if len_counter == len(names) and innerindex == len(outerelement) - 1:
                    # number two (2) should be dynamic. it represents length of column
                    temp.append((card_sum,lab_sum,x_ray_sum,others_sum,bed_sum,ultrasound_sum,medication_sum))
                    temp.append(float(card_sum )+ float(lab_sum) + float(x_ray_sum) + float(others_sum) + float(bed_sum) + float(ultrasound_sum) + float(medication_sum))
        print(f'Type of temp {type(temp)}')
        return temp
    except IndexError as err:
        print(f"hey, you list index out of range {len(names)}")


def add_sum(values):
    newValues = list()
    try:
        for (index, element) in enumerate(values):
            if isinstance(element, int):
                continue
            newValues.append(element)
            newValues.append(sum(element))
        return newValues
    except Exception as exec:
        print(exec)


# returned_values = add_up()
# print(add_sum(returned_values))