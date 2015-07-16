import vtk
import os
import numpy

dir = '../sample_data/DICOM/digest_article/'

reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName(dir)
reader.Update()

imageData = reader.GetOutput()

volumeMapper = vtk.vtkSmartVolumeMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
  volumeMapper.SetInputConnection(imageData.GetProducerPort())
else:
  volumeMapper.SetInputData(imageData)

volumeProperty = vtk.vtkVolumeProperty()
volumeProperty.ShadeOff()
volumeProperty.SetInterpolationType(vtk.VTK_LINEAR_INTERPOLATION)

compositeOpacity = vtk.vtkPiecewiseFunction()
compositeOpacity.AddPoint(0.0,0.0)
compositeOpacity.AddPoint(80.0,1.0)
compositeOpacity.AddPoint(80.1,0.0)
compositeOpacity.AddPoint(255.0,0.0)
volumeProperty.SetScalarOpacity(compositeOpacity)

color = vtk.vtkColorTransferFunction()
color.AddRGBPoint(0.0  ,0.0,0.0,1.0)
color.AddRGBPoint(80.0  ,1.0,0.0,0.0)
color.AddRGBPoint(255.0,1.0,1.0,1.0)
volumeProperty.SetColor(color)

volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)

renWin = vtk.vtkRenderWindow();
ren1 = vtk.vtkRenderer();
ren1.SetBackground(0, 0, 0);

renWin.AddRenderer(ren1);
renWin.SetSize(800, 800);

iren = vtk.vtkRenderWindowInteractor();
iren.SetRenderWindow(renWin);


ren1.AddViewProp(volume)
ren1.ResetCamera()

# Render composite. In default mode. For coverage.
renWin.Render()

# 3D texture mode. For coverage.
volumeMapper.SetRequestedRenderModeToRayCastAndTexture()
renWin.Render()

# Software mode, for coverage. It also makes sure we will get the same
# regression image on all platforms.
volumeMapper.SetRequestedRenderModeToRayCast()
renWin.Render()

iren.Start()
