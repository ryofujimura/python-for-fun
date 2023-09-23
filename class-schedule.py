from collections import defaultdict

# Define the schedule calendar structure
schedule_calendar = defaultdict(lambda: defaultdict(str))

# Define the available time slots for each day (24 hours * 60 minutes / 15 minutes per slot)
available_time_slots = [
    '0000', '0015', '0030', '0045', '0100', '0115', '0130', '0145', '0200', '0215', '0230', '0245',
    '0300', '0315', '0330', '0345', '0400', '0415', '0430', '0445', '0500', '0515', '0530', '0545',
    '0600', '0615', '0630', '0645', '0700', '0715', '0730', '0745', '0800', '0815', '0830', '0845',
    '0900', '0915', '0930', '0945', '1000', '1015', '1030', '1045', '1100', '1115', '1130', '1145',
    '1200', '1215', '1230', '1245', '1300', '1315', '1330', '1345', '1400', '1415', '1430', '1445',
    '1500', '1515', '1530', '1545', '1600', '1615', '1630', '1645', '1700', '1715', '1730', '1745',
    '1800', '1815', '1830', '1845', '1900', '1915', '1930', '1945', '2000', '2015', '2030', '2045',
    '2100', '2115', '2130', '2145', '2200', '2215', '2230', '2245', '2300', '2315', '2330', '2345'
]

# Define the classes and their sections
classes = {
    "Class 351": [
        {"section": "Section 1", "time_slots": ["1500", "1515", "1530", "1545", "1600", "1615"], "days": ["Monday", "Wednesday"]},
        {"section": "Section 2", "time_slots": ["1500", "1515", "1530", "1545", "1600", "1615"], "days": ["Tuesday", "Thursday"]},
    ],
    "Class 361": [
        {"section": "Section 1", "time_slots": ["1500", "1515", "1530", "1545", "1600", "1615"], "days": ["Monday", "Wednesday"]},
        {"section": "Section 2", "time_slots": ["1500", "1515", "1530", "1545", "1600", "1615"], "days": ["Tuesday", "Thursday"]},
    ],
}

# Generate all possible schedules
def generate_schedules(classes, schedule_calendar, current_schedule=[]):
    if not classes:
        # All classes have been scheduled, add the current schedule to the list of possible schedules
        yield current_schedule
        return

    class_name, sections = classes.popitem()
    for section in sections:
        section_name = section["section"]
        days = section["days"]
        time_slots = section["time_slots"]

        # Check if any of the days have already been occupied
        if any(schedule_calendar[day][slot] for day in days for slot in time_slots):
            continue

        # Ensure that all days are occupied together
        available_slots = available_time_slots.copy()
        for slot in time_slots:
            if all(slot in available_slots for day in days):
                for day in days:
                    for slot in time_slots:
                        schedule_calendar[day][slot] = f"{class_name} - {section_name}"
                yield from generate_schedules(dict(classes), schedule_calendar, current_schedule + [(day, class_name, section_name)])
                for day in days:
                    for slot in time_slots:
                        schedule_calendar[day][slot] = ""

# Generate and print all possible schedules
for schedule in generate_schedules(dict(classes), schedule_calendar):
    print("Possible Schedule:")
    for day, class_name, section_name in schedule:
        print(f"{day}: {class_name} - {section_name}")
    print()
