import sys

from cron_expression import CronExpression

if len(sys.argv) < 2:
    sys.exit("Pass a cron string to parse")

if len(sys.argv) > 2:
    sys.exit("Too many arguments. Pass a cron string as a single argument")

# Sample expression: "*/15 0 1,15 * 1-5 /usr/bin/find"
expression = CronExpression(sys.argv[1])
expression.printFormattedTable()

