import dicom
import os
import numpy

dir = '../sample_data/DICOM/digest_article/'
lstFilesDCM = []  # create an empty list
for dirName, subdirList, fileList in os.walk(dir):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            lstFilesDCM.append(os.path.join(dirName,filename))

numFiles = len(lstFilesDCM)
print 'found {} DICOM files'.format(numFiles)

# get the dimensions from the 1st file
d0 = dicom.read_file(lstFilesDCM[0])
dims = (int(d0.Rows), int(d0.Columns), len(lstFilesDCM))

# allocate space
data = numpy.zeros(dims, dtype=d0.pixel_array.dtype)

# loop through all the DICOM files and read
for i in range(numFiles):
    filename = lstFilesDCM[i]
    # read the file
    ds = dicom.read_file(filename)
    # store the raw image data
    data[:, :, i] = ds.pixel_array