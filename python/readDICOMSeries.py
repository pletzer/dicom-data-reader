#
# This example demonstrates how to read a series of dicom images
# and how to scroll with the mousewheel or the up/down keys
# through all slices
#
# some standard vtk headers
import vtk
import sys 
 
def main():

   argc = len(sys.argv)

   # Verify input arguments
   if argc != 2:
      print "Usage: ", sys.argv[0], " FolderName"
      return sys.exit(1)
 
   folder = sys.argv[1]
 
   # Read all the DICOM files in the specified directory.
   reader = vtk.vtkDICOMImageReader()
   reader.SetDirectoryName(folder)
   reader.Update()
 
   # Visualize
   imageViewer = vtk.vtkImageViewer2()
   imageViewer.SetInputConnection(reader.GetOutputPort())
 
   # slice status message
   sliceTextProp = vtk.vtkTextProperty()
   sliceTextProp.SetFontFamilyToCourier()
   sliceTextProp.SetFontSize(20)
   sliceTextProp.SetVerticalJustificationToBottom()
   sliceTextProp.SetJustificationToLeft()
 
   sliceTextMapper = vtk.vtkTextMapper()
   msg = "Slice {} out of {}".format(imageViewer.GetSliceMin() + 1, \
                                     imageViewer.GetSliceMax() + 1)
   sliceTextMapper.SetInput(msg)
   sliceTextMapper.SetTextProperty(sliceTextProp)
 
   sliceTextActor = vtk.vtkActor2D()
   sliceTextActor.SetMapper(sliceTextMapper)
   sliceTextActor.SetPosition(15, 10)
 
   # usage hint message
   usageTextProp = vtk.vtkTextProperty()
   usageTextProp.SetFontFamilyToCourier()
   usageTextProp.SetFontSize(14)
   usageTextProp.SetVerticalJustificationToTop()
   usageTextProp.SetJustificationToLeft()
 
   usageTextMapper = vtk.vtkTextMapper()
   usageTextMapper.SetInput("- Slice with mouse wheel\n  or Up/Down-Key\n- Zoom with pressed right\n  mouse button while dragging")
   usageTextMapper.SetTextProperty(usageTextProp)
 
   usageTextActor = vtk.vtkActor2D()
   usageTextActor.SetMapper(usageTextMapper)
   usageTextActor.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
   usageTextActor.GetPositionCoordinate().SetValue( 0.05, 0.95)

   interactor = vtk.vtkInteractorStyleImage()
   #interactor.SetImageViewer(imageViewer)
   #interactor.SetStatusMapper(sliceTextMapper)
 
   #imageViewer.SetupInteractor(renWin)
   #renderWindowInteractor.SetInteractorStyle(myInteractorStyle)
   # add slice status message and usage hint message to the renderer
   imageViewer.GetRenderer().AddActor2D(sliceTextActor)
   imageViewer.GetRenderer().AddActor2D(usageTextActor)
 
   # initialize rendering and interaction
   #imageViewer.GetRenderWindow().SetSize(400, 300)
   #imageViewer.GetRenderer().SetBackground(0.2, 0.3, 0.4)
   #imageViewer.Render()
   #imageViewer.GetRenderer().ResetCamera()
   #imageViewer.Render()
   #renderWindowInteractor.Start()


if __name__ == '__main__': main()

