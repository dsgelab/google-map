from gmap_retrieval import *
import pandas as pd

key = ''

data = pd.DataFrame([[1, '40.752937,-73.977240', 'NYC Grand Central Station'],
                     [2, '51.531090,-0.125752', 'London St Pancras Station'],
                     [3, '35.681463,139.767157', 'Tokyo Station'],
                     [4, '48.844544,2.374431', 'Paris-Gare-de-Lyon'],
                     [5, '60.171283,24.941472', 'Helsinki Central Station'],
                     [6, '42.3653,-71.1036', 'Cambridge Central Square Station'],
                     [7, '42.3361,-71.1075', "Boston Brigham And Women's Hospital"]],
                    columns=['id', 'loc', 'place'])

# get satellite images for locations in the 'data' variable
# this will store satellite images in the directory "satellite_images"
get_satellite_image(directory_name="satellite_images", API_key=key,
                    IDs=data['id'], latitude_longitude=data['loc'],
                    horizontal_coverage=2, horizontal_size=640, image_ratio=1,
                    image_scale=1, image_format="png", n_jobs=-1, verbose=True)

# get street view images from areas around the locations in the 'data' variable
# this will store street view images in the directory "street_views"
get_street_view_image(directory_name='street_view', API_key=key,
                      secret=None, IDs=data['id'], latitude_longitude=data['loc'],
                      n_images=10, rad=1, camera_direction=-1,
                      field_of_view=120, angle=0, search_radius=100,
                      outdoor=True, image_size="640x640",
                      limit=10, n_jobs=-1, verbose=True)

# get data of nearby restaurants on Google Maps
# around the locations in the 'data' variables
# this function saves json files containing data about nearby restaurants
# under the directory called 'nearby_places'
get_nearby_places(directory_name='nearby_places', API_key=key,
                  IDs=data['id'], latitude_longitude=data['loc'],
                  radius=1, place_types=['restaurant'],
                  verbose=True)

# create csv file called 'nearby_places.csv' from json files
# under the directory 'nearby_places'
nearby_places = create_csv_nearby_places(directory_name='nearby_places',
                                         place_types=['restaurant'], 
                                         file_name=None)

# get reviews for the restaurants around the locations in the 'data' variables
# saves json files containing review data under directory called 'reviews'
get_reviews(directory_name='reviews', API_key=key, place_id=place_id,
            verbose=True)

# create csv file called 'reviews.csv' from json files
# under the directory 'reviews'
_ = create_csv_reviews(directory_name='reviews', file_name=None)

# get the number of API calls made per location
get_n_api_calls(n_loc=len(data),
				satellite='satellite_images',
	            nearby_places='nearby_places',
	            street_view='street_view',
	            reviews='reviews',
	            place_types=['restaurant'])

# predict the cost for further data collection of 1000 locations
# nearby_search_per_entry and n_reviews_per_entry need to be estimated,
# but estimate based on only 5 examples as done above
# would not be reliable in practice
calculate_cost(n_loc=1000, price_table=None, # use default price table
               n_api_calls_per_loc=n_api_calls_per_loc,
               extra_expense=0)

