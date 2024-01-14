import sys
from helpers import *

class CronExpression:
    def __init__(self, expression):
        try:
            self.expression = validate_cron_expression(expression)
            [minute, hour, dayOfMonth, month, dayOfWeek, command] = expression.split(" ")
            self.minute = parse_time_unit(minute, 0, 60)
            self.hour = parse_time_unit(hour, 0, 24)
            self.dayOfMonth = parse_time_unit(dayOfMonth, 1, 32)
            self.month = parse_time_unit(month, 1, 13)
            self.dayOfWeek = parse_time_unit(dayOfWeek, 1, 8)
            self.command = command
        except ValueError as e:
            sys.exit(e)

    def printFormattedTable(self):
        CRON_PARTS = {
            "minute": self.minute,
            "hour": self.hour,
            "day of month": self.dayOfMonth,
            "month": self.month,
            "day of week": self.dayOfWeek,
            "command": self.command,
        }

        table = ""
        firstColLength = 14

        for name, value in CRON_PARTS.items():
            formattedValue = value
            formattedName = name + " " * (firstColLength - len(name))

            if type(value) == list:
                formattedValue = " ".join([str(option) for option in value])

            row = f"{formattedName} {formattedValue}\n"
            table += row

        return print(table)
