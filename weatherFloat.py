from kivy.app import App
import re, string
import urllib
import json
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
from urllib import urlopen
class AddLocationForm(FloatLayout):
        country_input = ObjectProperty()
        city_input = ObjectProperty()
        search_results = ObjectProperty()

        def Info(self):
                famous = {'INDIA':'Food, Relegion, Spirtiuality and Cricket'}
                info = famous[self.country_input.text]
                self.ids.info.text = 'Famous for'+" " +info
                
                
                
                

        """def validate_city(self):
                city = ('CHENNAI')
                if self.city_input.text == city:
                        self.search_location()
                elif self.city_input.text == "":
                        warning = "City should not be empty"
                else:
                        warning2= "City" + '{}'.format(self.city_input.text)+ " " + "does not exist"
                        self.ids.weather.text = warning2"""

        
        def validate_country(self):
                global url2
                global url3
                country =('Afghanistan',
    'Aland Islands',
    'Albania',
    'Algeria',
    'American Samoa',
    'Andorra',
    'Angola',
    'Anguilla',
    'Antarctica',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Aruba',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bermuda',
    'Bhutan',
    'Bolivia',
    'Bonaire',
    'Bosnia Herzegovina',
    'Botswana',
    'Bouvet-Island',
    'Brazil',
    'British Indian Ocean Territory',
    'Brunei',
    'Bulgaria',
    'burkina-faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape verde',
    'Cayman Islands',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Christmas Island',
    'Cocos Islands',
    'Colombia',
    'Comoros',
    'Congo',
    'Congo',
    'Cook Islands',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Curacao',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Falkland Islands (Malvinas)',
    'Faroe Islands',
    'Fiji',
    'Finland',
    'France',
    'French Guiana',
    'French Polynesia',
    'French Southern Territories',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Gibraltar',
    'Greece',
    'Greenland',
    'Grenada',
    'Guadeloupe',
    'Guam',
    'Guatemala',
    'Guernsey',
    'Guinea',
    'Guinea Bissau',
    'Guyana',
    'Haiti',
    'Heard Island and McDonald Islands',
    'Holy See',
    'Honduras',
    'Hong Kong',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Isle of Man',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jersey',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'South Korea',
    'North Korea',
    'Kuwait',
    'Kyrgyzstan',
    "Laos",
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macao',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Martinique',
    'Mauritania',
    'Mauritius',
    'Mayotte',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Montserrat',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Caledonia',
    'NewZealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Niue',
    'Norfolk Island',
    'Northern Mariana Islands',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Palestine',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Pitcairn',
    'Poland',
    'Portugal',
    'Puerto Rico',
    'Qatar',
    'Reunion',
    'Romania',
    'Russian Federation',
    'Rwanda',
    'Saint Barthelemy',
    'Saint Helena',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Martin',
    'Saint Pierre and Miquelon',
    'Saint Vincent and Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Sint Maarten',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'South Georgia',
    'South Sudan',
    'Spain',
    'Srilanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Timor-Leste',
    'Togo',
    'Tokelau',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Turks Caicos',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'UK',
    'USA',
    'United States Minor Outlying Islands',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Venezuela',
    'Vietnam',
    'British Virgin Islands',
    'US Virgin Islands',
    'Wallis and Futuna',
    'Western Sahara',
    'Yemen',
    'Zambia',
    'Zimbabwe',
)
                
                countries = [element.upper() for element in country]
                country = tuple(countries)
                self.country_input.text = self.country_input.text.upper()
                self.city_input.text = self.city_input.text.upper()
                print self.city_input.text
                city = ('CHENNAI',
                        'MUMBAI',
                        'Bangalore',
                        'Kolkata',
                        'Pune',
                        'Hyderabad',
                        'Delhi'
                        )
                cities = [element.upper() for element in city]
                city = tuple(cities)
                if self.country_input.text in country:
                        cityname = "Enter the city name"
                        self.ids.weather.text = cityname
                        if self.city_input.text in city:
                                url = 'https://www.timeanddate.com/weather/'
                                global url3
                                url2 = string.replace('{}'.format(self.country_input.text), ' ', '-')
                                url3 = '{}'.format(self.city_input.text)
                                full_url = url+url2+"/"+url3
                                print full_url
                                data = urllib.urlopen(full_url).read()
                                m = re.search('width=80 height=80><div class=h2>',data)
                                start = m.end()
                                end  = start + 2
                                data2 = data[start:end]
                                result = "Current Temperature in "+'{}'.format(self.city_input.text)+" "+  "is"+""  +data2
                                output = "Current Temperature in "+'{}'.format(self.city_input.text) + " " + "is" + " " +data2
                                self.ids.weather.text = output
                        elif self.city_input.text == "":
                                warning = "City should not be empty"
                        else:
                                warning2= "City" + " " + '{}'.format(self.city_input.text)+ " " + "does not exist"
                                self.ids.weather.text = warning2

                        
                        
                elif self.country_input.text == "":
                        warning = "Country Name should not be empty"
                        self.ids.weather.text = warning
                else:
                        warning= "Country" + " " + '{}'.format(self.country_input.text)+ " " + "does not exist"
                        self.ids.weather.text = warning
                        
        """def search_location(self):
            url = 'https://www.timeanddate.com/weather/'
            global url2
            url2 = '{}'.format(self.country_input.text)
            global url3
            url3 = url2+"/"'{}'.format(self.city_input.text)
            data = urllib.urlopen(url3).read()
            m = re.search('width=80 height=80><div class=h2>',data)
            start = m.end()
            end  = start + 2
            data2 = data[start:end]
            result = "Current Temperature in "+'{}'.format(self.city_input.text)+" "+  "is"+""  +data2
            output = "Current Temperature in "+'{}'.format(self.city_input.text) + " " + "is" + " " +data2
            self.ids.weather.text = output"""

            

class WeatherMan(App):
        pass
if __name__ == '__main__':
	WeatherMan().run()



