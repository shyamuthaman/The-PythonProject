# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 18:49:26 2018

@author: shyam
"""

import simplekml
longitude=input("Enter longitude: ")
latitude=input("Enter longitude: ")
kml=simplekml.Kml()
kml.newpoint(name="Sample",coords=[(longitude,latitude)])
kml.save("C:\\in\\Points.kml")
