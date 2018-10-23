from .File import File
from .FileFormats import FileFormat
# User defined formats
from .FASTInFile import FASTInFile
from .FASTOutFile import FASTOutFile
from .FASTWndFile import FASTWndFile
from .CSVFile import CSVFile
from .HAWC2PCFile import HAWC2PCFile
from .HAWC2AEFile import HAWC2AEFile
import os

def fileFormats():
    formats = []
    formats.append(FileFormat(FASTInFile))
    formats.append(FileFormat(FASTOutFile))
    formats.append(FileFormat(FASTWndFile))
    formats.append(FileFormat(HAWC2PCFile))
    formats.append(FileFormat(HAWC2AEFile))
    formats.append(FileFormat(CSVFile))
    return formats


def detectFormat(filename):
    """ Detect the file formats by looping through the known list. 
        The method may simply try to open the file, if that's the case
        the read file is returned. """
    formats=fileFormats()
    ext = os.path.splitext(filename.lower())[1]
    detected = False
    i = 0 
    while not detected and i<len(formats):
        myformat = formats[i]
        if ext in myformat.extensions:
            valid, F = myformat.isValid(filename)
            if valid:
                #print('File detected as :',myformat)
                detected=True
                return myformat,F

        i += 1

    if not detected:
        raise Exception('The file was not detected by detectFormat():'+filename)

def read(filename,fileformat=None):
    F = None
    # Detecting format if necessary
    if fileformat is None:
        fileformat,F = detectFormat(filename)
    # Reading the file with the appropriate class if necessary
    if not isinstance(F,fileformat.constructor):
        F=fileformat.constructor(filename=filename)
    return F
