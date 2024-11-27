import re
from collections import defaultdict
from datetime import datetime, timedelta


def extract_periods_by_day():
    time_pattern = r'\b\d{2}h\d{2} - \d{2}h\d{2}\b'
    day_pattern = r'([a-zA-Zéû]+ \d{2}):'

    periods_by_day = defaultdict(list)
    current_day = None

    with open('work_hours.txt') as file:
        for line in file:
            day_match = re.search(day_pattern, line)
            if day_match:
                current_day = day_match.group(1).lower() # extract the day and store it

            time_matches = re.findall(time_pattern, line)
            if time_matches and current_day:
                periods_by_day[current_day].extend(time_matches)

        return dict(periods_by_day)

def calculate_total_time(extracted_hours: dict):
    time_format = "%Hh%M"
    total_time_per_day = {}
    total_time = 0

    for day, periods in extracted_hours.items():
        for period in periods:
            period = period.split(' - ')
            start = datetime.strptime(period[0], time_format)
            end = datetime.strptime(period[1], time_format)

            if end < start:
                # If the worked hours span on two days, add 1 day to 
                # the end time
                end = end + timedelta(days=1)

            total_day_time = end - start

            if day in total_time_per_day:
                total_time_per_day[day] += total_day_time
            else:
                total_time_per_day[day] = total_day_time

    for day, time in total_time_per_day.items():
        time_in_hours = time.total_seconds() / 3600
        rounded_time = round(time_in_hours * 4) / 4
        total_time_per_day[day] = rounded_time
        total_time += rounded_time

    total_time_per_day['total'] = total_time

    return total_time_per_day


def write_result(converted_hours: dict):
    with open("result.txt", "w") as file:
        for day, hours in converted_hours.items():
            if day == 'total':
                day = '\n' + day + '  ->\t'
            else:
                day = day + ':\t'
            file.write(f'{day}{hours}\n')


if __name__ == '__main__':
    try:
        extracted_hours = extract_periods_by_day()
        converted_hours = calculate_total_time(extracted_hours)
        write_result(converted_hours)
    except Exception as e:
        with open("error.txt", "w") as file:
            file.write(e)