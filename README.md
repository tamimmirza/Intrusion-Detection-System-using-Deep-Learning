# Intrusion Detection System using Deep Learning

VGG-19 deep learning model trained using ISCX 2012 IDS Dataset

# Framework & API's 

* Tensorflow-GPU
* Keras
* NVIDIA CUDA Toolkit 9.0
* NVIDIA cuDNN 7.0

# Tools

* Anaconda (Python 3.6)
* PyCharm


# How to use
Download the ISCX 2012 data set from the link

http://www.unb.ca/cic/datasets/ids.html

Then run the Java program known as ISCX FlowMeter which is found here on GitHub. You can use any IDE for that

https://github.com/ISCX/CICFlowMeter (if this doesnt convert .PCAP to .XML then try below)

https://github.com/ISCX/ISCXFlowMeter

Next I want you to make sure that your system is capable of running deep learning software. To check you can follow this guide that I have created:

https://towardsdatascience.com/python-environment-setup-for-deep-learning-on-windows-10-c373786e36d1

#### Note: If your system is inadequate then I humbly request you to stop here as the program will not perform efficiently and a great deal of time will be wasted.

Next run the program on the pre-processed data (change the location of the save file in the code). This will take out the relevant data fields in XML format for each file and process the data into Numpy Arrays by running the following python file:

    Data_Extraction_Revised.py

When completed you can now run (assuming you have Jupyter Notebook) the program.
You have to change the location of the save file, in the code, to the save file from the revised data extraction program

    FYP-Revised.ipynb

And you can begin training

## GOOD LUCK :)
