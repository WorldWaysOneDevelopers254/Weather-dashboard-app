import requests  
import matplotlib.pyplot as plt  
import plotly.graph_objects as go  
api_key = 'ad385a20db1293eb6cfb4ace6b8e0880'  
base_url = 'http://api.openweathermap.org/data/2.5/weather?'  

def get_weather_data(city_name): 


    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric" 
    
    
    response = requests.get(complete_url)
    
    
    if response.status_code == 200:
        return response.json()  
    else:
        print("Error: Unable to fetch data. Please check the city name or API key.")
        return None  
def extract_weather_info(data):
    if data:
        main = data['main']
        weather_description = data['weather'][0]['description']
        wind = data['wind']
        sys = data['sys']
        
        weather_info = {
            'Temperature': main['temp'],
            'Feels Like': main['feels_like'],
            'Humidity': main['humidity'],
            'Pressure': main['pressure'],
            'Weather Description': weather_description,
            'Wind Speed': wind['speed'],
            'Sunrise': sys['sunrise'],
            'Sunset': sys['sunset']
        }
        return weather_info
    else:
        return {}
  




def display_weather_info(weather_info, city): 
    if weather_info:
        print(f"\nWeather in {city}:")
        print(f"Temperature: {weather_info['Temperature']}°C")
        print(f"Feels Like: {weather_info['Feels Like']}°C")
        print(f"Humidity: {weather_info['Humidity']}%")
        print(f"Description: {weather_info['Weather Description']}")
    else:
        print("No weather information available.")


def plot_weather_data(weather_info, city):
    if weather_info: 
        labels = list(weather_info.keys()) 
        values = list(weather_info.values())  
        fig = go.Figure([go.Bar(x=labels, y=values)])  
        fig.update_layout(
            title=f"Weather Data for {city}",  
            xaxis_title="Metrics",  
            yaxis_title="Values", 
        )
        fig.show() 

def main():
    city_name = input("Enter the city name: ") 
    weather_data = get_weather_data(city_name) 
    weather_info = extract_weather_info(weather_data) 
    display_weather_info(weather_info, city_name) 
    plot_weather_data(weather_info, city_name)
if __name__ == "__main__":
    main()
    