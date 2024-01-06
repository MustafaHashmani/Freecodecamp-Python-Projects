def add_time(start, duration, today=None):
    time, unit = start.split()
    hour_start, minutes_start = time.split(":")
    hour_duration, minutes_duration = duration.split(":")

    hour_start = int(hour_start)
    minutes_start = int(minutes_start)
    minutes_duration = int(minutes_duration)
    hour_duration = int(hour_duration)

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    num_days = 0

    minutes_start += minutes_duration
    minutes_duration = 0
    if minutes_start >= 60:
        minutes_start = minutes_start % 60
        hour_start += 1

    # if only minutes were input
    if hour_duration == 0 and hour_start == 12:
        if unit == "AM":
            unit = "PM"
        else:
            unit = "AM"
            num_days += 1

    while hour_duration != 0:
        # resolve hours
        hour_start += 1
        hour_duration -= 1

        if hour_start >= 12:
            hour_start = hour_start % 12
            if unit == "AM":
                unit = "PM"
            else:
                unit = "AM"
                num_days += 1

    if hour_start == 0:
        hour_start = 12

    result_day = 0

    # if today is passed
    if today is not None:
        result_day = days[(days.index(today.capitalize()) + num_days) % 6]

        # resolve days case
        if num_days == 1:
            return f"{hour_start}:{minutes_start:02} {unit} (next day)"
        elif num_days > 1:
            return f"{hour_start}:{minutes_start:02} {unit}, {result_day} ({num_days} days later)"
        else:
            return f"{hour_start}:{minutes_start:02} {unit}, {result_day}"
    else:
        # resolve days case
        if num_days == 1:
            return f"{hour_start}:{minutes_start:02} {unit} (next day)"
        elif num_days > 1:
            return f"{hour_start}:{minutes_start:02} {unit} ({num_days} days later)"
        else:
            return f"{hour_start}:{minutes_start:02} {unit}"


print(add_time("6:30 PM", "205:12"))
