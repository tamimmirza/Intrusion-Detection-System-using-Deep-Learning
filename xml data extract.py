import numpy as np
import sys
import os
import xml.etree.ElementTree as ET

path = 'labeled_flows_xml'

main = []

i = 0 #Indicate the File that has been access i.e 1 is 1st file, 2 is 2nd file, etc

for filename in os.listdir(path):
    if not filename.endswith('.xml'):
        continue
    fullname = os.path.join(path, filename)
    tree = ET.parse(fullname)

    doc = tree.getroot()

    i = i + 1

    main.append(i)

    source = []
    destination = []
    tag = []

    x = os.path.splitext(filename)[0]

    for elem in doc.findall(x):
        y = elem.find('sourcePayloadAsUTF')

        if(y == None):
            source.append("N/A")
        else:
            source.append(y)

    for elem1 in doc.findall(x):
        y = elem1.find('destinationPayloadAsUTF').text

        if (y == None):
            destination.append("N/A")
        else:
            destination.append(y)

    for elem2 in doc.findall(x):
        tag.append(elem2.find('Tag').text)

    print(destination)
    break