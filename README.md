# Cron Expression Parser

## Description
This application parses a cron string and expands each field to show the times at which it will run.
It handles the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command.

### Input
The cron string should be passed as a single argument.

```
% python3 cron-parser.py ＂*/15 0 1,15 * 1-5 /usr/bin/find＂
```

### Output
The output will be formatted as a table with the field name taking the first 14 columns and the times as a space-separated list following it. And will look like this:

```
minute 0 15 30 45 
hour 0 
day of month 1 15 
month 1 2 3 4 5 6 7 8 9 10 11 12 
day of week 1 2 3 4 5 
command /usr/bin/find
```

## Preparation
To run this application install python:
- [Detailed Instructions for Window, Mac, and Linux](https://python.land/installing-python)

## Run tests
To run unit tests run:

```
% python3 -m unittest tests/helpers_test.py
```
