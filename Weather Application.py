# --------------------------------------------------------------------------------------
# File: Final_Project.py
# Name: Amie Davis
# Date: 8/5/2019
# Course: DSC510 - Introduction to Programming
# Assignment Number: 10.2
#
# Purpose: Gets weather for a given city or zip code.
#
# Usage: Uses API at https://openweathermap.org
#
# Functions: retrieveWeatherByZip(), retrieveWeatherByCity(), parseWeather(), main()
#
# --------------------------------------------------------------------------------------
# Retrieves weather from Open Weather API Given Zip Code
def retrieveWeatherByZip(zipCode):

    # Call API for weather
    url = 'https://api.openweathermap.org/data/2.5/weather'

    querystring = {'zip':zipCode, 'APPID':'f544bf2e6d99eb544466563f46c7fce2', 'units':'imperial'}
    headers = {'cache-control':'no-cache'}

    try:
        response = requests.request('GET',url, headers=headers, params=querystring)

    except:
        print('Web service is unavailable.  Try again later.')

    else:
        print('Web service connection successful.')

        # Parse and display results
        parseWeather(response)

# --------------------------------------------------------------------------------------
# Retrieves weather from Open Weather API Given US City
def retrieveWeatherByCity(city):

    # Call API for weather
    url = 'https://api.openweathermap.org/data/2.5/weather'
    us_city = city + ',US'

    querystring = {'q':us_city, 'APPID':'f544bf2e6d99eb544466563f46c7fce2', 'units':'imperial'}
    headers = {'cache-control':'no-cache'}

    try:
        response = requests.request('GET',url, headers=headers, params=querystring)

    except:
        print('Web service is unavailable.  Try again later')

    else:
        print('Web service connection successful.')


    # Parse and display results
    parseWeather(response)

# --------------------------------------------------------------------------------------
# Parses and displays results from weather API.
def parseWeather(response):

    # Parse JSON data
    data = json.loads(response.text)

    # Format and display weather
    if data['cod'] == '404':
        print('Location not found.  Please try again.')

    else:
        # Gets data fields to display
        city_name = data['name']
        hi_temp = int(round(data['main']['temp_max'],0))
        low_temp = int(round(data['main']['temp_min'],0))
        cur_temp = int(round(data['main']['temp'],0))

        # Since weather condition is a list, need to loop to set value
        for weather_item in data['weather']:
            condition = weather_item['description']


        # FOR TESTING - Displays full API response
        # print(json.dumps(data, indent=4, sort_keys=True))

        # Display weather in user-friendly format
        print('\n')
        print('Today in {}, there will be {} '.format(city_name, condition))
        print('with a high of {} degrees and a low of {} degrees.'.format(hi_temp, low_temp))
        print('Currently, the temperature is {} degrees.'.format(cur_temp))

# --------------------------------------------------------------------------------------
def main():

    # Display welcome message
    print('\n')
    print('Welcome to my Weather app.')
    weather_prompt = input('Would you like to look up weather for a US location?  If so, enter Y. ')

    # Prompt user for location
    while weather_prompt.upper() == 'Y':

        print('\n')
        print('You can look up weather by US city or zip code.')
        city_zip = input('Enter C for City or Z for Zip Code.')

        # Obtain and validate zip code
        if city_zip.upper() == 'Z':

            zipCode = input('Enter a 5-digit zip code. ')
            try:
                int(zipCode)

            except:
                print('\n')
                print('Zip code must contain digits only.')

            else:
                zip_length = len(zipCode)
                if zip_length == 5:
                    retrieveWeatherByZip(zipCode)
                else:
                    print('Zip code must contain 5 digits.')


        # Obtain city
        elif city_zip.upper() == 'C':
            city = input('Enter a US city. ')
            retrieveWeatherByCity(city)

        # Start over if invalid response entered
        else:
            print('You must enter a C or Z.  Please try again.')

        print('\n')
        weather_prompt = input('Would you like to look up weather for another US location?  If so, enter Y. ')

# --------------------------------------------------------------------------------------
# Runs program
import requests, json

main()