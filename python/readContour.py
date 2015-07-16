import vtk
import os
import numpy

dir = '../sample_data/DICOM/digest_article/'

reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName(dir)
reader.Update()

# vtkImageData
imageData = reader.GetOutput()
pointData = imageData.GetPointData()
dataArray = pointData.GetArray(0)
minVal, maxVal = dataArray.GetRange()

print dataArray
print 'minVal, maxVal = ', minVal, maxVal 

contour = vtk.vtkContourFilter()
contour.SetNumberOfContours(1)
contour.SetValue(0, 0.5*(minVal + maxVal))
contour.SetArrayComponent(0) # scalar
contour.ComputeNormalsOn()

contour.SetInputConnection(reader.GetOutputPort())

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(contour.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

renWin = vtk.vtkRenderWindow()
ren = vtk.vtkRenderer()
ren.AddActor(actor)
ren.SetBackground(0, 0, 0)

renWin.AddRenderer(ren)
renWin.SetSize(800, 800)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

iren.Initialize()
renWin.Render()
iren.Start()
