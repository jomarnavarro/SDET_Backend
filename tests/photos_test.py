import requests
from assertpy.assertpy import assert_that
from clients.photos.photos_client import PhotosClient

photos_client = PhotosClient()

def test_fetch_ten_photos_sol_1000():
    photo_list = photos_client.get_mars_photos(num_photos=10, date_type='sol', date_value=1000)
    for photo in photo_list:
        assert_that(photo).contains('id')
        assert_that(photo).contains('sol')
        assert_that(photo).contains('camera')
        assert_that(photo).contains('img_src')
        assert_that(photo).contains('earth_date')
        assert_that(photo).contains('rover')
        assert_that(photo['earth_date']).is_equal_to('2015-05-30')


def test_fetch_ten_photos_earth_date_sol_1000():
    photo_list = photos_client.get_mars_photos(num_photos=10, date_type='earth_date', date_value='2015-05-30')
    for photo in photo_list:
        assert_that(photo).contains('id')
        assert_that(photo).contains('sol')
        assert_that(photo).contains('camera')
        assert_that(photo).contains('img_src')
        assert_that(photo).contains('earth_date')
        assert_that(photo).contains('rover')
        assert_that(photo['sol']).is_equal_to(1000)


def test_first_ten_photos_sol_equal_first_ten_photos_earth_date_sol_1000():
    photo_list_sol = photos_client.get_mars_photos(num_photos=10, date_type='sol', date_value=1000)
    photo_list_earth_date = photos_client.get_mars_photos(num_photos=10, date_type='earth_date', date_value='2015-05-30')
    ids_sol = [x['id'] for x in photo_list_sol]
    ids_earth_date = [x['id'] for x in photo_list_earth_date]
    diff_list = [x for x in ids_sol if x not in ids_earth_date]
    assert_that(diff_list).is_empty()


def test_picture_amounts_by_camera_not_greater_than_ten():
    photo_list = photos_client.get_mars_photos(date_type='sol', date_value=1000)
    print(len(photo_list))
    
    freqs = {}
    for camera_name in [photo['camera']['name'] for photo in photo_list ]:
        if camera_name in freqs:
            freqs[camera_name] += 1
        else:
            freqs[camera_name] = 1
    
    l = list(freqs.values())
    l.sort()
    
    times = l[-1] / l[0]
    assert_that(times).is_less_than_or_equal_to(10)


