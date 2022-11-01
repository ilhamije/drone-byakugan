import os
import json
import ast
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from datetime import datetime


def get_exif(filename):
    exif_data = {}
    image = Image.open(filename)
    info = image._getexif()
    gps_info = {}

    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif_data[decoded] = value

    for key in exif_data['GPSInfo'].keys():
        sub_decoded = GPSTAGS.get(key, key)
        gps_info[sub_decoded] = exif_data['GPSInfo'][key]

    gps_info.pop('GPSVersionID')
    gps_info.pop('GPSAltitudeRef')
    return str(gps_info)


def _convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates stored
    in the EXIF to degress in float format
    """
    degree_val = value[0]
    minute_val = value[1]
    second_val = value[2]

    return degree_val + (minute_val / 60.0) + (second_val / 3600.0)


def get_parsed(filename, exif_json):
    """
    Returns the latitude and longitude, if available,
    from the provided exif_data (obtained through get_exif_data above)
    """

    result = {}
    lat = None
    lon = None

    if "GPSLatitude" in exif_json:
        gps_latitude = exif_json.get("GPSLatitude", None)
        gps_latitude_ref = exif_json.get("GPSLatitudeRef", None)
        gps_longitude = exif_json.get("GPSLongitude", None)
        gps_longitude_ref = exif_json.get("GPSLongitudeRef", None)

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":
                lat = 0 - lat

            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon


    result = {
        filename : {
            "latitude": lat,
            "longitude": lon
        }}

    return result




if __name__ == "__main__":
    # output : Store in a json file [x]
    output = datetime.today().strftime('%Y-%m-%d') + '.json'

    # Read JSON
    output_path = 'parsedjsontest/' + output

    if os.path.isfile(output_path):
        print('read existing file')
        existing_file = open(output_path, mode='r', encoding='utf-8')
        data = json.load(existing_file)
        existing_file.close()

    # get all the filename from a directory [x]
    FILEPATH = 'gdrivetest'
    dir_list = os.listdir(FILEPATH)
    data = []

    # parsing [x]
    for filename in dir_list:
        FULL_FILEPATH = f"{FILEPATH}/{filename}"
        exif = get_exif(FULL_FILEPATH)
        exif_json = json.loads(json.dumps(ast.literal_eval(exif)))
        parsed = get_parsed(filename, exif_json)
        print(parsed)
        data.append(parsed)
        print('=='*20)

    # Writing / Updating JSON file
    print('updating file')
    updating_file = open(output_path, mode='w+', encoding='utf-8')
    # data.append(parsed)
    updating_file.write(json.dumps(data))
    updating_file.close()
    print('DONE')
