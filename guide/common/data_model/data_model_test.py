import attr
from django.test import TestCase

from .data_model import data_model


class DataModelTest(TestCase):
    def setUp(self):
        @data_model
        class Foo:
            __slots__ = (
                'a',
                'b',
            )

        self.model = Foo

    def test_has_expected_attributes(self):
        self.assertTrue(hasattr(self.model, 'to_dict'))
        self.assertTrue(hasattr(self.model, 'from_dict'))
        self.assertTrue(hasattr(self.model, 'safe_from_dict'))

    def test_missing_attributes_are_none(self):
        model = self.model()
        self.assertIsNone(model.a, model.b)

    def test_to_dict(self):
        data = self.model(1, 2).to_dict()
        self.assertEqual(data, dict(a=1, b=2))

    def test_create_from_dict(self):
        data = dict(a=1, b=2)
        model = self.model.from_dict(data)
        self.assertEqual(model, self.model(a=1, b=2))

    def test_safe_from_dict(self):
        data = self.model.safe_from_dict(dict(a=1, b=2))
        self.assertEqual(data, self.model(1, 2))

    def test_safe_from_dict_returns_none_if_from_dict_raises(self):
        @data_model
        class Bar:
            __slots__ = 'a',

            @classmethod
            def from_dict(cls, data):
                return cls(data['a'])

        self.assertIsNone(Bar.safe_from_dict(dict))
        self.assertIsNone(Bar.safe_from_dict('random'))

    def test_custom_from_dict(self):
        @data_model
        class Bar:
            __slots__ = 'a',

            @classmethod
            def from_dict(cls, data):
                return cls(a=data['a'] + 1)

        model = Bar.from_dict(dict(a=1))
        self.assertEqual(model.a, 2)

    def test_to_dict_only_returns_fields_with_values(self):
        model = self.model(a=1)
        self.assertEqual(model.to_dict(), dict(a=1))
