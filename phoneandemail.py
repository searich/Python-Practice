#! Python 3
# phoneandemail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phone_regex = re.compile(r'''(
    (\d{3})|(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|\.)\s*(\d{2, 5}))?
    )''', re.VERBOSE)

# TODO: Create email regex.

# TODO: Find matches in clipboard text.

# TODO: Copy results to clipboard.
