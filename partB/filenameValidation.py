# The Incorrect Regex would be: r"^[\s]+\\.(java,py,cs,txt)$"
# There are four main problems with this expression.
# 1. [\s]+ requires whitespace instead of a filename.
# 2. \\ matches a literal backslash, which is not needed before the extension.
# 3. The period is not properly escaped as \. to represent a literal dot.
# 4. (java,py,cs,txt) treats the extensions as one combined string instead of separate choices.

import re

def validate_filename(filename):

    pattern = r"^[a-zA-Z0-9_-]+\.(java|py|cs|txt)$"

    if re.fullmatch(pattern, filename):
        print("Valid filename format.")
    else:
        print("Invalid filename format.")

filename_input = input(
    "Enter a filename with a java, py, cs, or txt extension: "
)

validate_filename(filename_input)

# The corrected regex requires a filename containing letters, numbers, underscores, or hyphens, 
# followed by a period and one of the four allowed extensions. 
# The | symbol separates the extension choices, so the program can recognize each one individually. 
# It also prevents spaces and other unsupported characters from being accepted.