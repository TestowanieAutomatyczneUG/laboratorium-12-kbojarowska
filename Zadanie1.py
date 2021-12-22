import requests
import unittest


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


if __name__ == '__main__':
    unittest.main()