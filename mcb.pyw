#! /anaconda3/bin/python
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py mcb.pyw <keyword> - Loads keyword to clipboard.
#        py mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys, pyperclip

mcb_shelf = shelve.open('mcb')

# TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # TODO: list keywords and load content.
    if sys.argv[1].lower == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))

mcb_shelf.close()
