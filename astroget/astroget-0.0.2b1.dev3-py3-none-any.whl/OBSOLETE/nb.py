#!/usr/bin/env python

from pprint import pformat as pf
from importlib import reload

import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS              # !!!
from astropy.nddata import Cutout2D      # !!!
from astropy.coordinates import SkyCoord
from astropy import units as u
import numpy as np
import pandas as pd

#!import astroget.client
import astroget.client
#reload(astroget.client)
#astroget.__version__

# Server must support client.cutout() method !!!
#server='https://astroarchive.noirlab.edu'
server='https://marsnat1-pat.csdc.noirlab.edu' #!!!
client = astroget.client.CsdcClient(url=server)
print(f'Client: {client}')

def tt():
    limit=20
    #fname='/net/archive/pipe/20170803/ct4m/2017B-0951/c4d_170804_050615_oow_r_v1.fits.fz'
    fname='/net/archive/pipe/20170803/ct4m/2017B-0951/c4d_170804_075609_ooi_Y_v1.fits.fz'
    obj_name = 'M2'
    obj_coord = SkyCoord.from_name(obj_name)
    ra = obj_coord.ra.degree
    dec = obj_coord.dec.degree
    search_size = 0.01 # radius in degrees
    print(f'Target ra,dec={(ra,dec)} search_size={search_size}')

    print(f'\n##########\nRunning client.find(limit={limit})\n')
    found = client.find(
          outfields=['md5sum', 'hdu:hdu_idx',
                     'hdu:ra_center', 'hdu:dec_center',
                     'archive_filename', 'hdu:updated'],
          constraints={
              'archive_filename': [fname],
              'instrument': ['decam'],
              'obs_type': ['object'],
              'proc_type': ['instcal'],
              'hdu:ra_center': [ra - search_size, ra + search_size],
              'hdu:dec_center': [dec - search_size, dec + search_size],
          },
        limit=limit)

    print(f'Found {found.count} matches of object {obj_name} '
          f'at position: ra,dec={(ra,dec)} using client.vohdu()')
    recidx = 0
    rec = found.records[recidx]
    print(f'Show 1 of {found.count} records. rec[{recidx}] = \n{pf(rec)}\n')

    # ID of chosen HDU
    md5 = rec['md5sum']
    hduidx = rec['hdu:hdu_idx']
    #!hduurl = rec['url']
    hduurl = f'{server}/api/retrieve/{md5}/?hdus=0,{hduidx}'
    print(f'hduurl = {hduurl}')

    # Verify
    print('call client.hdu_bounds({(md5, hduidx)}')
    bounds = client.hdu_bounds(md5, hduidx, vet=1, verbose=True)
    print(f'\nbounds=\n{pf(bounds)}\n')

    # END tt()

##############################################################################

def tt1():
    header0 = fits.getheader(hduurl, 0) # hdu0=Primary, hdu1=image
    image_data1, header1 = fits.getdata(hduurl, ext=1, header=True) # hdu0=Primary, hdu1=image
    print(f'HDU size in pixels = {image_data1.shape}')



    cornerkeys = ['CENRA1',   'CENDEC1',
                  'COR1RA1', 'COR1DEC1',
                  'COR2RA1', 'COR2DEC1',
                  'COR3RA1', 'COR3DEC1',
                  'COR4RA1', 'COR4DEC1']
    hducornerkeys = [f'hdu:{k}' for k in cornerkeys] # rename for use in find()

    dbboundskeys = ['ra_min', 'ra_max',
                    'dec_min', 'dec_max', 'ra_center', 'dec_center']
    hdudbboundskeys = [f'hdu:{k}' for k in dbboundskeys] # rename for use in find()


    hducornerkeys = ['CENRA1',   'CENDEC1',
                     'COR1RA1', 'COR1DEC1',
                     'COR2RA1', 'COR2DEC1',
                     'COR3RA1', 'COR3DEC1',
                     'COR4RA1', 'COR4DEC1']
    h0 = {k: header0.get(k,None) for k in ['INSTRUME', 'OBSTYPE', 'PROCTYPE','PRODTYPE']}
    h1 = {k: header1.get(k,None) for k in hducornerkeys}
    print(f'header0={h0}')
    print(f'header1={h1}')


    # DEBUG.  Why do we get error: "NoOverlapError: Arrays do not overlap"
    print(f'ra,dec={(ra,dec)} chip_size={chip_size}')  # cutout parameters
    client.hdu_bounds(md5, hduidx, verbose=Trtue)


    chip_size = 100
    print(f'Get chip centered at ra,dec={(ra,dec)} size {chip_size}. From image md5,hduidx=({md5}, {hduidx})')
    # get in memory FITS file
    chip = client.cutout(ra, dec, chip_size, md5, hduidx, verbose=True)
    print(f'Cutout chip into local FITS file: {chip}')


    # Look at HDU values stored in DB
    recidx = 5
    rec = found.records[recidx]
    [f'{k} = {rec[k]}' for k in sorted(rec.keys())]



def all_messier():
    objs = dict()
    for n in range(1,110+1):
        name = f'M{n}'
        obj_coord = SkyCoord.from_name(name)
        ra = obj_coord.ra.degree
        dec = obj_coord.dec.degree

        # Search HDUs (not files).  There are a lot more of these than there are of files.
        # The Astro Data Archive has over 390 million HDUs that can be searched.
        # (contained in over 18 million files)
        try:
            found = client.vohdu(
                (ra,dec), 0.000001,  # position=(ra,dec), size(in decimal degrees)
                instrument='decam',
                obs_type='object',
                proc_type='instcal',
                limit=None, VERB=3, verbose=False)
        except:
            continue
        #! print(f'name={name}  found.count={found.count}')
        objs[name] = found.count
    found_objects = {k:v for (k,v) in objs.items() if v > 0}
    print(found_objects)

def tt2():
    obj_name = 'M2'
    instrument = 'decam'
    obs_type = 'object'
    proc_type = 'instcal'
    limit = 25

    obj_coord = SkyCoord.from_name(obj_name)
    ra = obj_coord.ra.degree
    dec = obj_coord.dec.degree
    print(f'obj_name={obj_name} at position: ra,dec={(ra,dec)}')

    cornerkeys = ['CENRA1',   'CENDEC1',
                  'COR1RA1', 'COR1DEC1',
                  'COR2RA1', 'COR2DEC1',
                  'COR3RA1', 'COR3DEC1',
                  'COR4RA1', 'COR4DEC1']
    hducornerkeys = [f'hdu:{k}' for k in cornerkeys] # rename for use in find()

    dbboundskeys = ['ra_min', 'ra_max',
                    'dec_min', 'dec_max', 'ra_center', 'dec_center']
    hdudbboundskeys = [f'hdu:{k}' for k in dbboundskeys] # rename for use in find()


    search_size = 0.01  # diameter in degrees
    out = ['md5sum', 'hdu:hdu_idx']  + hducornerkeys + hdudbboundskeys
    cons = {'instrument': [instrument],
            'obs_type': [obs_type],
            'proc_type': [proc_type],
            'hdu:ra_center': [ra - search_size/2, ra + search_size/2],
            'hdu:dec_center': [dec - search_size/2, dec + search_size/2],
            }
    found = client.find(outfields=out, constraints=cons, limit=limit)
    print(f'Found {found.count} matches of object {obj_name} using client.find()')
    found


    # In[ ]:


    found.records[0]
    #chip = client.cutout(ra, dec, size, md5, hduidx)
    chip = client.cutout(ra, dec, 5000, md5, hduidx)
    print(f'chip={chip}')


if __name__ == "__main__":
    tt()
