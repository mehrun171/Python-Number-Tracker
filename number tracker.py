import phonenumbers
import folium
from phonenumbers import timezone, geocoder, carrier
from opencage.geocoder import OpenCageGeocode

number = input("Enter phone number with country code: ")

try:
    phoneNumber = phonenumbers.parse(number)
    
    timeZone = timezone.time_zones_for_number(phoneNumber)
    print("Timezone:", str(timeZone))
    
    geolocation = geocoder.description_for_number(phoneNumber, "en")
    print("Location:", geolocation)
    
    if geolocation:
        Key = "3deb8184527c4cada1dc2510d417ec17"
        geocoder = OpenCageGeocode(Key)
        result = geocoder.geocode(geolocation)
        
        if result and len(result) > 0:
            lat = result[0]['geometry']['lat']
            lng = result[0]['geometry']['lng']
            print("Latitude:", lat)
            print("Longitude:", lng)
            
            map = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=geolocation).add_to(map)
            map.save("location.html")
        else:
            print("Geocoding failed. No results found.")
    
    service = carrier.name_for_number(phoneNumber, "en")
    print("Service provider:", service)

except phonenumbers.phonenumberutil.NumberParseException:
    print("Error: Invalid phone number format.")
except Exception as e:
    print(f"An error occurred: {e}")
