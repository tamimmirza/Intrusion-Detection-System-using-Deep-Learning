import xml.etree.ElementTree as ET
import numpy as np
import os
import time

import_directory = 'C:\\Users\Tamim Mirza\Documents\ISCX\labeled_flows_xml\\'

files = os.listdir(import_directory)

errors = []

start_time = time.time()
i = -1
data_array = np.empty((0, 2))
counter = 0
actual = (50**2) * 3
for file in files:
    print(file)
    try:
        tree = ET.parse(import_directory + file)
        print('Reading File ', file)
        root = tree.getroot()
    except:
        errors += file
        continue
    for child in root:
        for next_child in child:
            if next_child.tag == 'destinationPayloadAsUTF':
                if next_child.text is not None:
                    x = next_child.text
                    if len(x) > actual:
                        x = x[: actual]
                    else:
                        while len(x) < actual:
                            x += x
                        x = x[:actual]
                    if child.find('Tag').text == 'Normal':
                        data_array = np.vstack((data_array, np.array([np.fromstring(x, dtype=np.uint8), 0])))
                    else:
                        data_array = np.vstack((data_array, np.array([np.fromstring(x, dtype=np.uint8), 1])))
                    counter += 1
    print('Time taken: {}'.format(time.time() - start_time))
    start_time = time.time()
    np.save('Database2\destinationPayload_' + file, np.array(data_array))
    data_array = np.empty((0, 2))

print('Error in Opening Files = ', errors)
print('Counter = ', counter)
print('DONE!')