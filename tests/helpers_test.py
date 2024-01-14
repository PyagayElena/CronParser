import unittest

from helpers import *

class TestHelpers(unittest.TestCase):
    def test_validate_cron_expression(self):
        correctExpression = "*/15 0 1,15 * 1-5 /usr/bin/find"
        wrongTypeExpression = 12
        incorrectExpression = "1 2 3 4 5"

        # Validate correct cron expression
        self.assertEqual(validate_cron_expression(correctExpression), correctExpression)

        # Validate cron expression with numeric argument passed
        with self.assertRaises(ValueError):
            validate_cron_expression(wrongTypeExpression)

        # Validate cron expression without all fields passed
        with self.assertRaises(ValueError):
            validate_cron_expression(incorrectExpression)
    
    def test_parse_time_unit(self):
        # Parse correct day of month
        self.assertEqual(parse_time_unit("23", 1, 32), [23])

        # Parse correct day of week with "*" (all option)
        self.assertEqual(parse_time_unit("*", 1, 8), [1,2,3,4,5,6,7])

        # Parse correct month time interval, custom options and removed duplicate
        self.assertEqual(parse_time_unit("1-3,2,12", 1, 13), [1,2,3,12])

        # Parse correct minute with time interval
        self.assertEqual(parse_time_unit("0-30/15", 0, 60), [0,15,30])

        # Parse correct hour with all option
        self.assertEqual(parse_time_unit("*/12", 0, 24), [0,12])

        # Raise error for incorrect day of month (out of acceptable range)
        with self.assertRaises(ValueError):
            parse_time_unit("32", 1, 32)

        # Raise error for incorrect day of week (incorrect interval)
        with self.assertRaises(ValueError):
            parse_time_unit("5-3", 1, 8)

        # Raise error for incorrect month (out of range interval)
        with self.assertRaises(ValueError):
            parse_time_unit("0-3", 1, 13)

        # Raise error for incorrect hour (incorrect recurring period)
        with self.assertRaises(ValueError):
            parse_time_unit("*//15", 0, 24)

if __name__ == "__main__":
  unittest.main()
