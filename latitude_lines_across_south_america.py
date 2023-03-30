#Import the modules pandas, geopandas and shapely
import pandas as pd
import geopandas as gpd
import shapely as sh

#Read csv file containing the cities latitudes as a pandas dataframe
directory = "C:/Users/Azzla/Downloads/"
input_csv = "SouthernCities.csv"
df = pd.read_csv(directory + input_csv)

#Store each dataframe column values into an array
latitudes = df['LATITUDE']
cities = df['CITY']
countries = df['COUNTRY']

#Create the latitude lines
all_lines = []
for lat in latitudes:
    line = sh.geometry.LineString([[-180, lat], [0, lat], [180, lat]])
    all_lines.append(line)

#Create the dataframe to store the lines
latitude_lines = pd.DataFrame({'city': cities, 'country': countries, 'geometry': all_lines})

#Turn pandas dataframe into geopandas geodataframe
latitude_lines_gdf = gpd.GeoDataFrame(cities, geometry=latitude_lines.geometry)

#Make sure the columns are correctly named
latitude_lines_gdf.columns = ['city', 'geometry']

#Write geodataframe to shapefile (line)
output = "LatitudeLines_Across_SouthAmerica.shp"
latitude_lines_gdf.to_file(directory + output)
print('Complete')
