# Convert Font Awesome Subsetter SVG icons to be compatible with Oxygen Builder.
#
# USAGE:
# python "/path/to/FixFontAwesomeSVG.py" "/path/to/fontawesome-subset/sprites/filename.svg" "/path/to/Desktop/output.svg"
# Home Brew users may have use /usr/local/bin/python3 "/path..."
#
# Tested with Python 3.7
#
# By Matthew Hamel
#

import sys
import os
import xml.etree.ElementTree as ET

input_file = sys.argv[1]
output_file = sys.argv[2]

tree = ET.parse(input_file)
ET.register_namespace("", "http://www.w3.org/2000/svg")
xmlRoot = tree.getroot()

# Loop to add title tag
for elem in xmlRoot:
    child = ET.Element("title")
    child.text = elem.attrib.get("id")
    elem.insert(0, child)

# Write file
tree.write(output_file)

# Open file as text
with open(output_file, 'r') as file:
    data = file.read()

# Replace strings to add <defs> tag
data = data.replace('<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">', '<svg xmlns="http://www.w3.org/2000/svg" style="display: none;"><defs>')
data = data.replace('</svg>', '</defs></svg>')

with open(output_file, 'w') as file:
    file.write(data)

## Cleanup
if os.path.isfile:
    os.remove(input_file)