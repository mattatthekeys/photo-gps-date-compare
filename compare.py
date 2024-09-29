from pathlib import Path
from geopy.distance import geodesic
from datetime import datetime
from GPSPhoto import gpsphoto


# Function to get metadata from an image file
def get_image_metadata(filepath):
    data = gpsphoto.getGPSData(filepath)
    return (data['Latitude'], data['Longitude'])


# Function to check if two photos were taken within 1 mile
def are_within_one_mile(coords1, coords2):
    if coords1 and coords2:
        distance = geodesic(coords1, coords2).miles
        return distance <= 1
    return False

# Function to compare files in two directories
def compare_directories(dir1, dir2, distance):
    files_dir1 = list(Path(dir1).glob('*.jpg'))
    files_dir2 = list(Path(dir2).glob('*.jpg'))

    for file1 in files_dir1:
        metadata1 = gpsphoto.getGPSData(str(file1))
        created_date1 = datetime.strptime(metadata1['Date'] + " " + metadata1['UTC-Time'], '%m/%d/%Y %H:%M:%S')
        gps = metadata1['Latitude'], metadata1['Longitude']

        # Find files in files_dir2 with the same date
        for file2 in files_dir2:
            metadata2 = gpsphoto.getGPSData(str(file2))
            created_date2 = datetime.strptime(metadata2['Date'] + " " + metadata2['UTC-Time'], '%m/%d/%Y %H:%M:%S')

            if (abs((created_date2 - created_date1).days <= 1)):
                gps2 = metadata2['Latitude'], metadata2['Longitude']
                distance_delta = geodesic(gps, gps2).miles
                if created_date1 > created_date2:
                    timedelta = (created_date1 - created_date2)
                else:
                    timedelta = (created_date2 - created_date1)
   
                if distance_delta <= distance:
                    print(f"** FOUND A MATCH - {created_date1}, {distance_delta} miles, {timedelta} hours")
                    print(f"  File: {file1}")
                    print(f"  File: {file2}")

# Usage example
DIR1 = 'photos1'
DIR2 = 'photos2'
DISTANCE_MILES = 2

compare_directories(DIR1, DIR2, DISTANCE_MILES)
