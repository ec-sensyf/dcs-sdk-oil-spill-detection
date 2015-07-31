#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from xml.dom import minidom

def main(args):

  kml = minidom.parse(args[1])
  placemarks = kml.getElementsByTagName("Placemark")
  num_placemarks = len(placemarks)
  if num_placemarks == 0:
    os.system("rm " + args[1])
  else:
    coords = kml.getElementsByTagName("coordinates")
    coordinates = coords[0].firstChild.nodeValue.split(' ')
    with open(args[2], "w") as text_file:
      text_file.write(coordinates[0])


if __name__ == '__main__':

  main(sys.argv)
