def add_time(start, duration, day=None):
    start_time, meridian = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if meridian == 'PM':
        start_hour += 12

    duration_hour, duration_minute = map(int, duration.split(':'))

    end_hour = (start_hour + duration_hour) % 24
    end_minute = start_minute + duration_minute
    if end_minute >= 60:
        end_hour += 1
        end_minute -= 60
    end_meridian = 'AM' if end_hour < 12 else 'PM'
    end_hour = end_hour % 12
    if end_hour == 0:
        end_hour = 12

    days_later = (start_hour + duration_hour) // 24

    if day:
        day = day.capitalize()
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_weekday = weekdays.index(day)
        end_weekday = (start_weekday + days_later) % 7

    result = f'{end_hour:02}:{end_minute:02} {end_meridian}'
    if day:
        result += f', {weekdays[end_weekday]}'
    if days_later == 1:
        result += ' (next day)'
    elif days_later > 1:
        result += f' ({days_later} days later)'

    return result

    