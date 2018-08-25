from django.test import TestCase

from .place import Place, Location


class Test(TestCase):
    def test_create_place_from_dict(self):
        data = {
            'location': {
                'lat': 10,
                'lng': 10,
            },
            'display_name': 'Dirty Bones',
            'display_address': 'Top Floor, Kingly Court',
        }
        expected = Place(
            location=Location(lat=10, lng=10),
            display_name='Dirty Bones',
            display_address='Top Floor, Kingly Court',
            description=None,
        )

        self.assertEqual(Place.from_dict(data), expected)

    def test_create_place_from_dict_throws_key_error(self):
        data = { 'display_name': 'foo' }
        with self.assertRaises(KeyError):
            _ = Place.from_dict(data)

    def test_create_place_safe_from_dict_returns_none(self):
        data = { 'display_name': 'foo' }
        self.assertEqual(Place.safe_from_dict(data), None)
