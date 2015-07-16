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

xmin, xmax, ymin, ymax, zmin, zmax = imageData.GetBounds()
print 'xmin, xmax = ', xmin, xmax
print 'ymin, ymax = ', ymin, ymax
print 'zmin, zmax = ', zmin, zmax

print 'minVal, maxVal = ', minVal, maxVal
nx, ny, nz = imageData.GetDimensions()
print 'nx, ny, nz = ', nx, ny, nz

smooth = vtk.vtkImageGaussianSmooth()
npx, npy, npz = int(0.01*nx), int(0.01*ny), int(0.05*nz)
print 'npx, npy, npz = ', npx, npy, npz
smooth.SetStandardDeviation(npx, npy, npz)
#smooth.SetRadiusFactors(10, 10, 10)
if vtk.VTK_MAJOR_VERSION <= 5:
  smooth.SetInput(imageData)
else:
  smooth.SetInputData(imageData)
smooth.Update()

print smooth.GetOutput()
print smooth.GetOutput().GetPointData().GetArray(0).GetRange()


contour = vtk.vtkContourFilter()
contour.SetNumberOfContours(1)
contour.SetValue(0, 200.0) # 0.5*(minVal + maxVal))
contour.SetArrayComponent(0) # scalar
contour.ComputeNormalsOn()

#contour.SetInputConnection(reader.GetOutputPort())
#contour.SetInputConnection(smooth.GetOutputPort())
if vtk.VTK_MAJOR_VERSION <= 5:
  contour.SetInput(smooth.GetOutput())
else:
  contour.SetInputData(smooth.GetOutput())

mapper = vtk.vtkPolyDataMapper()
mapper.ScalarVisibilityOff()
mapper.SetInputConnection(contour.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(222/256., 184/256., 135/256.)

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
