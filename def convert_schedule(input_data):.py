def convert_schedule(input_data):
    class_schedule = {}

    for item in input_data:
        class_number = item[0]
        section = "Section " + str(item[1])
        time_slots = [str(slot) for slot in range(item[2], item[3] + 1, 15)]
        time_slots = [slot.zfill(4) for slot in time_slots]
        days = [day.capitalize() for day in item[4:]]

        class_name = "Class " + str(class_number)
        if class_name not in class_schedule:
            class_schedule[class_name] = []

        class_schedule[class_name].append({
            "section": section,
            "time_slots": time_slots,
            "days": days
        })

    return class_schedule

input_data = [
    [341, 1, 1500, 1615, "monday", "wednesday"],
    [341, 2, 1400, 1500, "tuesday", "thursday"],
    [353, 1, 800, 915, "tuesday", "thursday"],
    [353, 2, 1000, 1115, "tuesday", "thursday"],
]

result = convert_schedule(input_data)

print(result)
print("--------------------")
for class_name, sections in result.items():
    print(class_name + ":")
    for section in sections:
        print(section)
