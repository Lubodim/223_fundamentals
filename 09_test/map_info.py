import folium
from phone_info import length, high
map_address = folium.Map(location=[high, length])

map_address.save("save_data.html")
