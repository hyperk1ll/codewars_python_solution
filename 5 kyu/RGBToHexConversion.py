# RGB To Hex Conversion

def rgb(r, g, b):
    return '%02X%02X%02X' % (max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b)))