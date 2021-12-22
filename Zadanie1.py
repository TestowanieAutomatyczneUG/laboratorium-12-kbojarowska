import requests
import unittest
from unittest.mock import *


class RandomUser:
    def __init__(self):
        self.url = "https://randomuser.me/api"

    def getRandomUser(self):
        r = requests.get(self.url)
        return r.json()['results'][0]

    def getRandomFrenchUser(self):
        r = requests.get(f'{self.url}?nat=fr')
        return r.json()['results'][0]

    def getRandomUserWithGender(self, gender):
        if type(gender) is str and gender in ["female", "male"]:
            r = requests.get(f'{self.url}?gender={gender}')
            return r.json()['results'][0]
        raise Exception("Bad gender")

    


class TestRandomUser(unittest.TestCase):
    def setUp(self):
        self.temp = RandomUser()

    def test_random_user_get_random_user_returns_dict(self):
        user = self.temp.getRandomUser()
        self.assertIsInstance(user, dict)

    def test_random_user_get_random_french_user_returns_dict(self):
        user = self.temp.getRandomFrenchUser()
        self.assertIsInstance(user, dict)

    def test_random_user_get_random_french_user_returns_french_user(self):
        user = self.temp.getRandomFrenchUser()
        self.assertEqual(user["location"]["country"], "France")

    def test_random_user_get_user_with_gender_male_returns_dict(self):
        user = self.temp.getRandomUserWithGender("male")
        self.assertIsInstance(user, dict)

    def test_random_user_get_user_with_gender_male_returns_male_user(self):
        user = self.temp.getRandomUserWithGender("male")
        self.assertEqual(user["gender"], "male")

    def test_random_user_get_user_with_gender_female_returns_dict(self):
        user = self.temp.getRandomUserWithGender("female")
        self.assertIsInstance(user, dict)

    def test_random_user_get_user_with_gender_male_returns_male_user(self):
        user = self.temp.getRandomUserWithGender("female")
        self.assertEqual(user["gender"], "female")

    def test_random_user_get_user_with_gender_bad_gender_int(self):
        self.assertRaises(Exception, self.temp.getRandomUserWithGender, 123)

    def test_random_user_get_user_with_gender_bad_gender_str(self):
        self.assertRaises(Exception, self.temp.getRandomUserWithGender, "gender")

    def test_random_user_get_user_with_gender_bad_gender_list(self):
        self.assertRaises(Exception, self.temp.getRandomUserWithGender, [])

    def test_random_user_get_user_with_gender_bad_gender_tuple(self):
        self.assertRaises(Exception, self.temp.getRandomUserWithGender, ())

    def test_random_user_get_user_with_gender_bad_gender_dict(self):
        self.assertRaises(Exception, self.temp.getRandomUserWithGender, {})

    def tearDown(self):
        self.temp = None


class TestRandomUserMock(unittest.TestCase):
    def setUp(self):
        self.temp = RandomUser()

    def test_random_user_get_user_mock(self):
        random_user_result = {"gender":"male","name":{"title":"Mr","first":"Arnout","last":"Luyten"},"location":{"street":{"number":5117,"name":"Blekershof"},"city":"Glanerbrug","state":"Utrecht","country":"Netherlands","postcode":10964,"coordinates":{"latitude":"40.4648","longitude":"-125.7953"},"timezone":{"offset":"-9:00","description":"Alaska"}},"email":"arnout.luyten@example.com","login":{"uuid":"171824d0-ef7d-4932-afe5-2b9ede508998","username":"tinyfrog230","password":"woofwoof","salt":"30C2Lolj","md5":"5b2d94507e292f5dce20e9a66d03ceb0","sha1":"f4122bd45270102379fd027cc47e7f1d639496de","sha256":"be39cbed579e6e2771dab7009c8b3f99bd3e67b584826b7f1f424187089bedd5"},"dob":{"date":"1981-11-23T11:40:04.918Z","age":40},"registered":{"date":"2012-12-01T00:58:29.037Z","age":9},"phone":"(893)-056-6500","cell":"(109)-031-8577","id":{"name":"BSN","value":"23021839"},"picture":{"large":"https://randomuser.me/api/portraits/men/90.jpg","medium":"https://randomuser.me/api/portraits/med/men/90.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/90.jpg"},"nat":"NL"}
        self.temp.getRandomUser = MagicMock(return_value=random_user_result)
        self.assertEqual(self.temp.getRandomUser(), random_user_result)

    def test_random_french_user_mock(self):
        random_french_user_result = {"gender":"female","name":{"title":"Ms","first":"Héloïse","last":"Charles"},"location":{"street":{"number":5029,"name":"Rue de la Mairie"},"city":"Perpignan","state":"Paris","country":"France","postcode":11977,"coordinates":{"latitude":"20.2270","longitude":"143.7339"},"timezone":{"offset":"-11:00","description":"Midway Island, Samoa"}},"email":"heloise.charles@example.com","login":{"uuid":"62d08abc-0c1d-47a8-9e05-6cdce14e3ceb","username":"goldenkoala786","password":"*****","salt":"WeYDOF15","md5":"c481603f25a003270915f27c8db85061","sha1":"591f5e3feb8de959b84656d0be44bc2ce396f263","sha256":"6b34b39186b1f7e44d36a6b750bf2860c0b702a0a3b0889cecce7a5ceb8747d3"},"dob":{"date":"1989-06-05T07:27:46.468Z","age":32},"registered":{"date":"2015-08-05T20:06:44.843Z","age":6},"phone":"01-29-28-86-94","cell":"06-03-69-16-57","id":{"name":"INSEE","value":"2NNaN90401154 02"},"picture":{"large":"https://randomuser.me/api/portraits/women/85.jpg","medium":"https://randomuser.me/api/portraits/med/women/85.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/85.jpg"},"nat":"FR"}
        self.temp.getRandomFrenchUser = MagicMock(return_value=random_french_user_result)
        self.assertEqual(self.temp.getRandomFrenchUser(), random_french_user_result)

    def test_random_user_get_user_with_gender(self):
        random_user_with_gender_result = {"gender":"female","name":{"title":"Ms","first":"Héloïse","last":"Charles"},"location":{"street":{"number":5029,"name":"Rue de la Mairie"},"city":"Perpignan","state":"Paris","country":"France","postcode":11977,"coordinates":{"latitude":"20.2270","longitude":"143.7339"},"timezone":{"offset":"-11:00","description":"Midway Island, Samoa"}},"email":"heloise.charles@example.com","login":{"uuid":"62d08abc-0c1d-47a8-9e05-6cdce14e3ceb","username":"goldenkoala786","password":"*****","salt":"WeYDOF15","md5":"c481603f25a003270915f27c8db85061","sha1":"591f5e3feb8de959b84656d0be44bc2ce396f263","sha256":"6b34b39186b1f7e44d36a6b750bf2860c0b702a0a3b0889cecce7a5ceb8747d3"},"dob":{"date":"1989-06-05T07:27:46.468Z","age":32},"registered":{"date":"2015-08-05T20:06:44.843Z","age":6},"phone":"01-29-28-86-94","cell":"06-03-69-16-57","id":{"name":"INSEE","value":"2NNaN90401154 02"},"picture":{"large":"https://randomuser.me/api/portraits/women/85.jpg","medium":"https://randomuser.me/api/portraits/med/women/85.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/85.jpg"},"nat":"FR"}
        self.temp.getRandomUserWithGender = MagicMock(return_value=random_user_with_gender_result)
        self.assertEqual(self.temp.getRandomUserWithGender(), random_user_with_gender_result)

    def tearDown(self):
        self.temp = None

