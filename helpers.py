def validate_cron_expression(expression):
    if type(expression) != str or len(expression.split(" ")) != 6:
        raise ValueError("Invalid expression")
    
    return expression

"""
A function that parses a cron expression time unit for a given range
and returns an array of options
    unit - time unit from cron expression
    min - value for the acceptable time range to start (included)
    max - value for the acceptable time range to stop (not included)

Example for dayOfMonth with a custom value:
    Input: parse_time_unit("23", 1, 32)
    Output: [23]

Example for dayOfWeek with "*" (all option):
    Input: parse_time_unit("*", 1, 8)
    Output: [1,2,3,4,5,6,7]

Example for month with time interval and custom options:
    Input: parse_time_unit("1-3,2,12", 1, 13)
    Output: [1,2,3,12]
"""

def parse_time_unit(unit, min, max):
    if unit.isdigit():
        unitValue = int(unit)

        if unitValue < min or unitValue >= max:
            raise ValueError(f'Value {unit} is out of range: {min} - {max -1}')

        return [unitValue]
    
    if unit == "*":
        return list(range(min, max))
    
    values = []

    if "," in unit:
        parts = unit.split(",")

        for item in parts:
            values += parse_time_unit(item, min, max)

        return sorted(list(set(values)))

    if "/" in unit:
        values += _parse_recurring_period(unit, min, max)
        return sorted(list(set(values)))

    if "-" in unit:
        values += _parse_interval(unit, min, max)
    
    return sorted(list(set(values)))

"""
A function that parses a time interval and returns an array of options
    interval - time interval string to parse
    min - value for the acceptable time range to start (included)
    max - value for the acceptable time range to stop (not included)

Example:
    Input: _parse_interval("1-3", 1, 13)
    Output: [1,2,3]
"""
def _parse_interval(interval, min, max):
    values = interval.split("-")

    # Check if the interval has a valid format
    if (
        len(values) != 2 or
        not values[0].isdigit() or
        not values[1].isdigit()
    ):
        raise ValueError(f'Invalid range format: {interval}')
    
    start = int(values[0])
    end = int(values[1])

     # Check if the interval is in the defined range
    if (
        start > end or
        start < min or
        end >= max
    ):
        raise ValueError(f'{interval} is out of range: {min} - {max -1}. Or start time > end time')
    
    return list(range(start, end + 1))

"""
A function that parses a recurring period and returns an array of options
    recurringPeriod - recurring period string to parse
    min - value for the acceptable time range to start (included)
    max - value for the acceptable time range to stop (not included)

Example with time interval:
    Input: _parse_recurring_period("0-30/15", 0, 60)
    Output: [0,15,30]

Example with "*" (all option):
    Input: _parse_recurring_period("*/12", 0, 24)
    Output: [0,12]    
"""
def _parse_recurring_period(recurringPeriod, min, max):
    values = recurringPeriod.split("/")

    if len(values) != 2 or not values[1].isdigit():
        raise ValueError(f'Invalid recurring period: {recurringPeriod}')
    
    period = []

    if values[0] == "*":
        period = list(range(min, max))
    
    if "-" in values[0]:
        period = _parse_interval(values[0], min, max)

    if not period:
        raise ValueError(f'Invalid range for recurring period: {recurringPeriod}')

    return period[::int(values[1])]
    