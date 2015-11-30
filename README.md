# solutions-raster-functions

Raster functions can be applied to raster datasets and mosaic datasets for fast, accurate analytic capabilities.  The raster functions published within this repo are for weather data and are for use with NAM CONUS 12km data in the NetCDF format which can be obtained from here http://nomads.ncep.noaa.gov/.  The raster functions enable the user to take a multi variable meteorological data raster and extract and display single variables.  Examples would be extracting Temperature or Relative Humidity so that they can be viewed within ArcMAP.  Also included are some Python raster function which utilise Python scripts, which are provided, to calculate derived weather variable such as wind chill and heat index. The user can then by inputting parameters make predictions as to the impact these weather conditions may have on Military Operations.  These parameters can be changed to suit not just Military operations but any activity that may be influenced by the weather.

![Raster functions graphic](GenericFunctionsGraphic.png)

## Features

* What is included in this repo is:
  * Military Aspects of Weather Raster Functions
  
  Raster Functions included and what they do
 
| Raster Function | What it does |
|----- |-----|
| DeriveHeatIndex.rft.xml | Raster function to calculate Heat Index using Relative Humidity and Temperature. |
| DeriveWindChillNonUV.rft.xml | Raster function to display windchill but not using u and v components of wind. Uses a single variable for wind speed and single variable for temperature. |
| DeriveWindChillUV.rft.xml | Raster function to display windchill using u and v components of wind. Uses a single variable for temperature. |
| ExtractCloudCeiling.rft.xml | Raster function to display cloud ceiling height from data. |
| ExtractCloudCover.rft.xml | Raster function to display percentage cloud cover from data. |
| ExtractGust.rft.xml | Raster function to display wind gust derived from u and v values of wind. |
| ExtractPrecipitationRate.rft.xml | Raster functions to display precipitation rate from data. |
| ExtractRelativeHumidity.rft.xml | Raster function to display relative humidity from data. |
| ExtractTemperature.rft.xml | Raster function to display temperature readings from data. |
| ExtractTemperatureDegC.rft.xml | Raster function to extract temperature from data and change from Degrees Kelvin to Degrees Centigrade. |
| ExtractVisibility.rft.xml | Raster function to display visibility values from data. |
| ExtractWindDirection.rft.xml | Raster function to display wind direction using u and v components of wind. |
| ExtractWindDirectionNonUV.rft.xml | Raster function display wind direction but not using u and v components of wind. Uses a single variable for wind speed. |
| OpImpactAirDefenseCloudCeiling.rft.xml | Raster function to display the operational impact of cloud ceiling values on air defense operations. |
| OpImpactAirDefenseTemperature.rft.xml | Raster function to display the operational impact of temperature values on air defense operations. |
| OpImpactAirDefenseVisibility.rft.xml | Raster function to display the operational impact of visibility values on air defense operations. |
| OpImpactAirDefenseWindSpeed.rft.xml | Raster function to display the operational impact of wind speed derived from u and v values on air defense operations. |
| OpImpactArtilleryCloudCeiling.rft.xml | Raster function to display the operational impact of cloud ceiling values on artillery operations. |
| OpImpactArtilleryVisibility.rft.xml | Raster function to display the operational impact of visibility values on artillery operations. |
| OpImpactArtilleryWindSpeed.rft.xml | Raster function to display the operational impact of wind speed derived from u and v values on artillery operations. |
| OpImpactBridgeCrossingWindSpeed.rft.xml | Raster function to display the operational impact of wind speed derived from u and v values on bridge crossing. |
| OpImpactCrossCountryManoevresCloudCeiling.rft.xml | Raster function to display the operational impact of cloud ceiling values on cross country manoeuvres. |
| OpImpactCrossCountryManoevresTemperature.rft.xml | Raster function to display the operational impact of temperature values on cross country manoeuvres. |
| OpImpactCrossCountryManoevresVisibility.rft.xml | Raster function to display the operational impact of visibility values on cross country manoeuvres. |
| OpImpactCrossCountryManoevresWindSpeed.rft.xml | Raster function to display the operational impact of wind speed values derived from u and v values on cross country manoeuvres. |
| OpImpactParachuteCloudCeiling.rft.xml | Raster function to display the operational impact of cloud ceiling values on parachute operations. |
| OpImpactParachuteWindSpeed.rft.xml | Raster function to display the operational impact of wind speed values on parachute operations. |
| OpImpactPersonnelHeatIndex.rft.xml | Raster function to display the operational impact of heat index values on personnel. |
| OpImpactPersonnelTemp.rft.xml | Raster function to display the operational impact of temperature values on personnel. |
| OpImpactPersonnelWindChill.rft.xm | Raster function to display the operational impact of wind chill values on personnel.
| OpImpactUAVCloudCeiling.rft.xml | Raster function to display the operational impact of cloud ceiling values on UAV operations. |
| OpImpactUAVVisibility.rft.xml | Raster function to display the operational impact of visibility values on UAV operations. |
| OpImpactUAVWindSpeed.rft.xml | Raster function to display the operational impact of wind speed values on UAV operations. |
| TacticalAirliftCloudCeiling.rft.xml | Raster function to display the impact of cloud ceiling values on tactical airlifts. |
| TacticalAirliftVisibility.rft.xml | Raster function to display the impact of visibility values on tactical airlifts. |

  * Python Scripts for use within the Raster Functions
	
	Python Scripts included and what they do

	All of the scripts need to be checked by the user especially if it is intended to use them with different data as parameters may need to be changed to suit.
	
|Python Script Name | What script does |
|-----|-----| 
| GustWindSpeedFromUV.py | Python script used by the ExtractGust raster function which uses U and V components of wind. |
| HeatIndex.py | Python script used by the DeriveHeatIndex raster function. |
| NAMDownload.py | Python script that automates the download of the most up to date NAM data. |
| WindChillNonUV.py | Python script used by the DeriveWindChillnonuv raster function for data that does not contain the U and V components of wind. |
| WindchillUV.py | Python script used by the DeriveWindChilluv raster function for data that does contain the U and V components of wind. | 
| WindDirectionFromUV.py | Python script used by the WindDirectionFromUV raster function. |
| WindSpeedFromUV.py | Python script used by the OpImpact wind speed raster functions. |

  * Variables extracted in sample data.
  
    These are 12 of a potential 139 that are available from the NAM CONUS 12km data downloaded from the NOAA site.  The sample data supplied covers the area of the state of California in the United States of America.

| Variable Name | Description |
| ------ | ----- |	
| rh2m | Relative Humidity 2m (%) |
| tcdcclm | Total cloud cover (%) |
| tmpsfc | Surface Temperature (k) |
| hgtclb | Cloud Base geopotential height (GPM) |
| vissfc | Surface Visibility (m) |
| ugrd10m | u component of wind 10m above ground |
| vgrd10m | v component of wind 10m above ground |
| ugrdmwl | Max wind u component (m/s) |
| vgrdmwl | Max wind v component (m/s) |
| snodsfc | Snow depth surface (m) |
| gustsfc | Wind gust surface (m/s) |
| apcpsfc | surface total precipitation (kg/m2) |

  * Sample data
	
| File Name | Description |
| ----- | ----- |
| nam201509181hr00z.nc | All the above variables for the State of California. |
| nam201509181hr00zWind.nc |Just U and V components of wind for the State of California. |


## Sections

* [Requirements](#requirements)
* [Instructions](#instructions)
* [Resources](#resources)
* [Issues](#issues)
* [Contributing](#contributing)
* [Licensing](#licensing)

## Requirements

* ArcGIS Desktop 10.3 or later
* ArcGIS Pro v1 or later
* Multidimension Supplemental Tools for ArcGIS (http://www.arcgis.com/home/item.html?id=9f963f362fe5417f87d44618796db938)
* Pywin build 219 or later or similar ide. (Optional)

## Instructions

### General Help

* [New to Github? Get started here.](http://htmlpreview.github.com/?https://github.com/Esri/esri.github.com/blob/master/help/esri-getting-to-know-github.html)
* [Getting started with image and raster processing](http://pro.arcgis.com/en/pro-app/help/data/imagery/get-started-with-image-and-raster-processing.htm)
* [Apply functions to a dataset](http://pro.arcgis.com/en/pro-app/help/data/imagery/apply-functions-to-a-dataset.htm)


### Getting Started

* Download the solutions-raster-functions repo to your local computer and unzip it to a local drive location preferably route of C:
* Read information on building raster functions which can be found  here (https://github.com/Esri/raster-functions/wiki) and here (https://github.com/Esri/raster-functions) and here for Python raster functions (https://github.com/Esri/raster-functions/wiki/PythonRasterFunction)
* Information on how to build / modify raster functions within ArcMap can be found here (https://desktop.arcgis.com/en/desktop/latest/manage-data/raster-and-images/accessing-the-raster-function-template-editor.htm) and information for ArcGIS Pro can be found here (http://pro.arcgis.com/en/pro-app/help/data/imagery/apply-functions-to-a-dataset.htm)


* These raster functions are designed to work with mosaic datasets only and only with NAM data in the NetCDF format.  If the user wants to use other data formats then the raster functions and associated python scripts will have to be edited. 
* The raster functions have been built with NAM CONUS (12km) downloaded in the OpeNDAP format obtained from here (http://nomads.ncep.noaa.gov/)  and then converted to NetCDF format using the OpeNDAP to NetCDF tool within the Multidimension Supplemental tools which can be downloaded from here (http://www.arcgis.com/home/item.html?id=9f963f362fe5417f87d44618796db938) For more information on the data downloaded please refer to here (http://nomads.ncep.noaa.gov/txt_descriptions/WRF_NMM_doc.shtml)
* Raster functions should be applied as follows;
    * With ArcGIS Desktop 10.3
        * Add the raster functions to the mosaic dataset as a processing templates.
        * Add the mosaic dataset to a project and then apply relevant processing template.
    * With ArcGIS Pro:
        * The Mosaic dataset needs to be within a database within the databases section.
        * The Set Mosaic Dataset Properties geoprocessing tool then needs to be run.
        * Under the Image Processing tab the Raster Functions should be added as Processing templates one by one.
        * To run them within ArcGIS Pro 1st select the layer you want apply it to from the table of contents then select Mosaic Layer - Data from the ribbon bar at the top and select the relevant Raster Function from the processing templates drop down.
					
* It is likely that you will want to use your own data and thresholds within these raster functions this can be done as follows;

    * To edit the thresholds open the raster function within the raster function editor and change the parameters within the remap function.  If you want to add more levels of operational impact for an activity then also open and edit the statistics and histogram function.

    * To use your own data in a standard raster function the Definition Query within the Function Chain will have to edited to suit your data.  The function chain is accessed through the raster function editor.

    * To use your own data within a Python raster function the .py file has to be edited so the correct names are within the getParameterInfo function. Also within the raster function itself the variable names need to be corrected within the Variable Manager section of the Python Raster Function function.  Within the Function Chain section "Type" needs to be set to Item Group and the "Group Field Name" and "Tag Field Name" need to be set to appropriate values.  For more information on how to make your own Python Raster Functions please refer to (https://github.com/Esri/raster-functions/wiki/PythonRasterFunction)

* For further information on how to set up the test data / raster functions please refer to the Military Aspects of Weather (MAoW) template located here (URL OF MAoW TEMPLATE WHEN AVAILABLE)
					
## Resources

* [ArcGIS Pro](https://pro.arcgis.com/en/pro-app/community/)
* [MAoW v2 Template](http://www.arcgis.com/home/item.html?id=2bd5ab673e5d4374bca6343cc80df414)  - This may be of use as it is fully working example of the above raster functions with sample Map Packages.  Uses all the same functions are as presented in this repo. Also contains more detailed instructions on how the raster functions can be set up and changed to suit the users needs.
* [noaa NOMADS data](http://nomads.ncep.noaa.gov/)
* [Multidimension Supplemental Tools](http://www.arcgis.com/home/item.html?id=9f963f362fe5417f87d44618796db938)
* [Information on Raster Functions](https://github.com/Esri/raster-functions)
* [Information on Python Raster Functions](https://github.com/Esri/raster-functions/wiki/PythonRasterFunction)
* [Modifying raster functions] (https://desktop.arcgis.com/en/desktop/latest/manage-data/raster-and-images/accessing-the-raster-function-template-editor.htm)
* [Test Data](http://nomads.ncep.noaa.gov/txt_descriptions/WRF_NMM_doc.shtml)

## Issues

Find a bug or want to request a new function?  Please let us know by submitting an issue.

## Contributing

Esri welcomes contributions from anyone and everyone. Please see our [guidelines for contributing](https://github.com/esri/contributing).

## Licensing

For information on licensing around the meteorological data used please see - http://www.weather.gov/disclaimer

Copyright 2015 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's
[license.txt](license.txt) file.

[](Esri Tags: ArcGIS Defense Intelligence Military ArcGISSolutions )
[](Esri Language: Python)

