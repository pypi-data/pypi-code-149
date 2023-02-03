from astropy.nddata import Cutout2D
import astropy.units as u
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
from .LoFAR_cat_search import LoFAR_Cat_Search
import math
import numpy as np

def truncate(number, digits):
    # Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
    nbDecimals = len(str(number).split('.')[1]) 
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def format_num(num):
    return str(math.trunc(num)).rjust(2,'0')

class cutout_2d:

    def __init__(self,RA,DEC,cutout_size=(28,28)):
        self.RA = RA
        self.DEC = DEC
        self.size = cutout_size
        self.find_pointing()
        self.load_pointing()
        self.preform_cutout()

    def load_pointing(self):
        url_base = 'https://lofar-surveys.org/public/DR2/mosaics/'+str(self.mosaic_id)+'/mosaic-blanked.fits'
        pointingfile = fits.open(url_base)
        self.mosaic_data = np.copy(pointingfile[0].data)
        pointingfile.close()
        self.wcs = WCS(pointingfile[0].header)

    def find_pointing(self):
        Source_Coord = SkyCoord(ra=self.RA*u.deg,dec=self.DEC*u.deg,frame='icrs')
        RA = Source_Coord.ra.to(u.hourangle).hms
        DEC = Source_Coord.dec.dms        
        RAhms = {'h':format_num(RA.h),'m':format_num(RA.m),'s':truncate(RA.s,1)}
        DEChms = {'h':format_num(DEC.d),'m':format_num(DEC.m),'s':format_num((DEC.s))}
        cat_search = LoFAR_Cat_Search(RAhms,DEChms,sr=1)
        self.mosaic_id = cat_search.Mosaic_id

    def preform_cutout(self):
        self.cutout = Cutout2D(data=self.mosaic_data,position=SkyCoord(ra=self.RA*u.deg,dec=self.DEC*u.deg,frame='icrs'),wcs=self.wcs,size=self.size)
        