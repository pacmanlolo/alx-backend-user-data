#!/usr/bin/env python3
import re

def filter_datum(fields, redaction, message, separator):
    return re.sub(fr'({separator.join(fields)})(?={separator}|$)', redaction, message)
