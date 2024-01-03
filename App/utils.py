# Convert a hex color to rgba
def hex_to_rgba(hex : str):
    return "rgba(" + str(int(hex[1:3], 16)) + "," + str(int(hex[3:5], 16)) + "," + str(int(hex[5:7], 16)) + ", 0.7)"

# Converts a RGB color in form of a tuple (r,g,b) to a hex color
def rgb_to_hex(rgb : tuple):
    return '#%02x%02x%02x' % rgb