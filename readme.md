# Lab 2: JSON, APIs, and Flask
## COP-4814 U03 - Fall 2019
This lab consists of API requests, Python programming, and reading & writing JSON documents.

## Steps to Recreate
### Preliminaries
1. Preliminaries: to get the API key for this part, please follow the following steps:
  * Visit *https://www.airvisual.com/air-pollution-data-api*.
  * Scroll down to *Community Free* and click on *START NOW*.
  * Sign up with your FIU email.
  * Visit *https://www.airvisual.com/dashboard/api*.
  * Click in +*New key*.
  * Under *Create your API Key*, select the *Community plan*.
  * Click on Create.
  * Visit *https://www.airvisual.com/dashboard/api* again and get your key, which is a string that contains only upper and lowercase letters and numbers.

2. Create a new project in PyCharm named `aqi` (stands for air quality index) - remember to use Python 3 - and create a new file named `aqiP roject.py` in the main folder. In this Python file, define the following functions for now:
```python
def save_to_file(data,file_name):
  with open(file_name,’w’) as write_file:
    json.dump(data,write_file,indent=4)
    print("The file {0} was successfully created.".format(file_name))
    
def read_from_file(file_name):
  with open(file_name,’r’) as read_file:
    file=json.load(read_file)
    print("You successfully read from {0}.".format(file_name))
    return file
```

3. Within the same folder, create a new file named `api_key.json` that contains the following structure:
```python
{
"aqi_api_key":"your_key_goes_here"
}
```
Substitute *your_key_goes_here* with the key you got at the Preliminaries step.

4. In `aqiProject.py`, read your API key from the JSON file you created above and assign it to a variable named `my_aqi_api_key`. Remember that the API key is a value which is accessed through a dictionary key.

5. Continuing `aqiProject.py`, define the following variables:
```python
url="http://api.airvisual.com/v2/nearest_city?key="
url_aqi=url+my_aqi_api_key
```

6. Now make a request to this API and save the output to variable `aqi_json`.

7. Save this data into a JSON file. For this, create a name for the JSON file:
```python
aqi_json_file_name="aqi.json"
```

8. At this point, you should be able to see your JSON file in the folder of this project. Exciting!

9. Read the data from the json file that we just created and save to a variable:
```python
air_quality_index=read_from_file(aqi_json_file_name)
```

10. It is pointless to deny that at this point you already know that Python reads the JSON file as a dictionary type, so to confirm this assertion, print the type of `air_quality_index`.

11. The following codes may appear in your json file and these are their definitions:
* `ts` : timestamp
* `aqius` : AQI value based on US EPA standard
* `aqicn` : AQI value based on China MEP standard
* `mainus` : main pollutant for US AQI
* `maincn` : main pollutant for Chinese AQI
* `tp` : temperature in Celsius
* `tp` : min minimum temperature in Celsius
* `pr` : atmospheric pressure in hPa
* `hu` : humidity
* `ws` : wind speed (m/s)
* `wd` : wind direction, as an angle of 360 (N=0, E=90, S=180, W=270)
* `p2` : pm2.5
* `p1` : pm10
* `o3` : Ozone O3
* `n2` : Nitrogen dioxide NO2
* `s2` : Sulfur dioxide SO2
* `co` : Carbon monoxide CO
* `ic` : weather icon code, see Figure 1 for icon index and get the images from the assignment folder

12. In the JSON file that you saved, you have the latitude and longitude of the location from which you
collected the air quality information. Save these values in two variables: *latitude* and *longitude* in
`aqiProject.py`. Hint: access these data through regular dictionary access.

13. Copy these values of latitude and longitude; visit Google Maps; paste and search this exact location;
take a screen shot of the location. Save this image in the PyCharm’s project folder with name `city.png`
(you might use other image formats).
