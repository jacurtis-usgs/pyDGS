"""
 Author:  Daniel Buscombe
           Grand Canyon Monitoring and Research Center
           United States Geological Survey
           Flagstaff, AZ 86001
           dbuscombe@usgs.gov
 Revision Sept 7, 2015
 First Revision January 18 2013

For more information visit https://github.com/dbuscombe-usgs/DGS-python

    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)
    
    This software is in the public domain because it contains materials that
    originally came from the United States Geological Survey, an agency of the
    United States Department of Interior. For more information, 
    see the official USGS copyright policy at
    http://www.usgs.gov/visual-id/credit_usgs.html#copyright
    Any use of trade, product, or firm names is for descriptive purposes only 
    and does not imply endorsement by the U.S. government.
"""

#python -c "import DGS; DGS.test.dotest()"
import DGS
import os

__all__ = [
    'dotest',
    'dotest_folder',
    'dotest_web',
    ]

def dotest():
   dotest_folder()
   dotest_web()

def dotest_folder():
   folder = DGS.__path__[0]+os.sep
   resolution = 1
   density = 10
   dofilter=1
   maxscale=8
   notes=8
   doplot = 1

   DGS.dgs(folder, density, resolution, dofilter, maxscale, notes, doplot)

def dotest_web():
   image= DGS.__path__[0]+os.sep+'IMG_0229.JPG'
   resolution = 1
   density = 10
   dofilter=1
   maxscale=8
   notes=8
   verbose=1

   DGS.dgs_web(image, density, resolution, dofilter, maxscale, notes, verbose)

if __name__ == '__main__':
   dotest()




