from django.test import TestCase

from ..models.place import Place as DBPlace
from .place import Place, Location


class PlaceTest(TestCase):
    def setUp(self):
        self.data = {
            'lat': 10,
            'lng': 10,
            'display_name': 'Dirty Bones',
            'display_address': 'Top Floor, Kingly Court',
        }

    def test_create_place_from_dict(self):
        expected = Place(
            location=Location(lat=self.data['lat'], lng=self.data['lng']),
            display_name=self.data['display_name'],
            display_address=self.data['display_address'],
            description=None,
        )

        self.assertEqual(Place.from_dict(self.data), expected)

    def test_create_from_args_raises_unless_all_given(self):
        with self.assertRaises(TypeError):
            _ = Place(
                location=Location(lat=0, lng=0),
                display_name='foo',
                display_address='foo',
            )

    def test_create_place_from_dict_raises_key_error(self):
        data = { 'display_name': 'foo' }
        with self.assertRaises(KeyError):
            _ = Place.from_dict(data)

    def test_create_place_safe_from_dict_returns_none(self):
        data = { 'display_name': 'foo' }
        self.assertEqual(Place.safe_from_dict(data), None)

    def test_from_db_model(self):
        db_model = DBPlace(
            lat=self.data['lat'],
            lng=self.data['lng'],
            display_name=self.data['display_name'],
            display_address=self.data['display_address'],
            description=None,
        )
        place = Place.from_db_model(db_model)
        expected = Place.from_dict(self.data)

        self.assertIsInstance(place, Place)
        self.assertEqual(place, expected)

    def test_to_db_model(self):
        expected = DBPlace(
            lat=self.data['lat'],
            lng=self.data['lng'],
            display_name=self.data['display_name'],
            display_address=self.data['display_address'],
            description=None,
        )

        place = Place.from_dict(self.data)
        db_place = place.to_db_model()

        self.assertIsInstance(db_place, DBPlace)
        self.assertEqual(expected.lat, db_place.lat)
        self.assertEqual(expected.lng, db_place.lng)
        self.assertEqual(expected.display_name, db_place.display_name)
        self.assertEqual(expected.display_address, db_place.display_address)
        self.assertEqual(expected.description, db_place.description)
