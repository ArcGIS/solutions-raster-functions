##Copyright 2015 Esri
##
##Licensed under the Apache License, Version 2.0 (the "License");
##you may not use this file except in compliance with the License.
##You may obtain a copy of the License at
##
##   [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)
##
##Unless required by applicable law or agreed to in writing, software
##distributed under the License is distributed on an "AS IS" BASIS,
##WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##See the License for the specific language governing permissions and
##limitations under the License.
##
##A copy of the license is available in the repository's
##[license.txt](license.txt) file.
##
##[](Esri Tags: ArcGIS Defense Intelligence Situational Awareness Military)
##[](Esri Language: Python)

# Name: HeatIndex

# Description: Python raster function to calculate Heat Index 

# Date Edited: 24/03/2015

#----------------------------------------------------------------------------------------------------------------------

import numpy as np


class HeatIndex():

    def __init__(self):
        self.name = "Heat Index Function"
        self.description = "This function combines ambient air temperature and relative humidity to return apparent temperature in degrees Fahrenheit."
        #self.doConversion = False
        self.tempunits = "Fahrenheit"


    def getParameterInfo(self):
        return [
            {
                'name': 'tmpsfc', #To be changed by user to the name of their variable for temperature
                'dataType': 'raster',
                'value': None,
                'required': True,
                'displayName': "Temperature Raster",
                'description': "A single-band raster where pixel values represent ambient air temperature in Fahrenheit." # to be changed by user.
            },
            {
                'name': 'units',
                'dataType': 'string',
                'value': 'Kelvin', # To be changed by the user to match whatever there input parameter units are.
                'required': True,
                'domain': ('Celsius', 'Fahrenheit', 'Kelvin'),
                'displayName': "Temperature Measured In",
                'description': "The unit of measurement associated with the temperature raster."
            },
            {
                'name': 'rh2m', # To be changed by user to the name of their variable for relative humidity
                'dataType': 'raster',
                'value': None,
                'required': True,
                'displayName': "Relative Humidity Raster",
                'description': "A single-band raster where pixel values represent relative humidity as a percentage value between 0 and 100." # to be changed by user
            },
        ]

    def getConfiguration(self, **scalars):
        return {
          'inheritProperties': 4 | 8,               # inherit all but the pixel type and NoData from the input raster
          'invalidateProperties': 2 | 4 | 8,        # invalidate statistics & histogram on the parent dataset because we modify pixel values. 
          'inputMask': False                        # Don't need input raster mask in .updatePixels(). Simply use the inherited NoData. 
        }

    def updateRasterInfo(self, **kwargs):
        kwargs['output_info']['bandCount'] = 1      # output is a single band raster
        kwargs['output_info']['histogram'] = ()     # we know nothing about the histogram of the outgoing raster.
        kwargs['output_info']['pixelType'] = 'f4'   # bit-depth of the outgoing HeatIndex raster based on user-specified parameters

# Getting and then setting the Temprature Units for use later

        if kwargs.get('units').lower() == 'celsius':
            self.tempunits = 'celsius'
        elif kwargs.get('units').lower() == 'farenheit':
            self.tempunits = 'farenheit'
        elif kwargs.get('units').lower() == 'kelvin':
            self.tempunits = 'kelvin'
                           

        #self.doConversion = bool(kwargs.get('units', 'Fahrenheit').lower() == 'Celsius')
        return kwargs

    def updatePixels(self, tlc, shape, props, **pixelBlocks):
        t = np.array(pixelBlocks['tmpsfc_pixels'], dtype='f4')
        r = np.array(pixelBlocks['rh2m_pixels'], dtype='f4')

#  Using the temperature variable generated earlier to know if a calculation is needed to turn the temp into degrees F
        if self.tempunits.lower() == "celsius":
            t = (9.0/5.0 * t) + 32.0
        elif self.tempunits.lower() == "kelvin":
            t = ((((t)-273.15)*1.8000) +32.00)
        else:
            t = t

##        if self.doConversion:
##            t = (9.0/5.0 * t) + 32.0

        tr = t * r
        rr = r * r
        tt = t * t
        ttr = tt * r
        trr = t * rr
        ttrr = ttr * r

        outBlock = -42.379 + (2.04901523 * t) + (10.14333127 * r) - (0.22475541 * tr) - (0.00683783 * tt) - (0.05481717 * rr) + (0.00122874 * ttr) + (0.00085282 * trr) - (0.00000199 * ttrr)
        pixelBlocks['output_pixels'] = outBlock.astype(props['pixelType'])
        return pixelBlocks

    def updateKeyMetadata(self, names, bandIndex, **keyMetadata):
        if bandIndex == -1:                                     # update dataset-level key metadata
            keyMetadata['datatype'] = 'Scientific'
            keyMetadata['variable'] = 'HeatIndex'
        elif bandIndex == 0:
            keyMetadata['wavelengthmin'] = None                 # reset inapplicable band-specific key metadata 
            keyMetadata['wavelengthmax'] = None
            keyMetadata['bandname'] = 'HeatIndex'
        return keyMetadata



HeatIndex.updateRasterInfo()