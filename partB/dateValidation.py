# The Incorrect Regex is: r"^(1[1-9]|1[0-2])/(0[1-9][12][0-9]|3[01])/\w{4}$"
# There are three main problems with the original regex. 
# 1. Is that the month section doesn't allow months 01 through 09.
# 2. The day section incorrectly combines patterns, preventing most valid days from matching.
# 3. The year section uses \w{4}, 
#    which allows letters and underscores instead of requiring four digits.

import re

def validate_date(date_str):

    pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/[0-9]{4}$"

    if re.fullmatch(pattern, date_str):
        print("Valid date format.")
    else:
        print("Invalid date format. Please enter MM/DD/YYYY.")

date_input = input("Please enter a date in the format MM/DD/YYYY: ")

validate_date(date_input)

# The corrected regex only accepts months from 01 to 12, days from 01 to 31, 
# and years containing exactly four digits. It also uses re.fullmatch() to check the entire input. 
# This fixes the requested date format, although it does not check whether the date actually exists, 
# such as February 30.