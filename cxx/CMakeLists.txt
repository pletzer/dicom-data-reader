cmake_minimum_required(VERSION 2.8)
 
PROJECT(ReadDICOMSeries)
 
find_package(VTK REQUIRED)
include(${VTK_USE_FILE})
 
add_executable(ReadDICOMSeries MACOSX_BUNDLE ReadDICOMSeries)
 
if(VTK_LIBRARIES)
  target_link_libraries(ReadDICOMSeries ${VTK_LIBRARIES})
else()
  target_link_libraries(ReadDICOMSeries vtkHybrid vtkWidgets)
endif()

