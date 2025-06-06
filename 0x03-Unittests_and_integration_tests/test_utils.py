#!/usr/bin/env python3

import unittest
import utils
from parameterized import parameterized
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a","b"), 2),

    ])
    def test_access_nested_map(self, map, path, expected):
        self.assertEqual(utils.access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a","b")),

    ])
    def test_access_nested_map_exception(self, map, path):
        with self.assertRaises(KeyError):
            utils.access_nested_map(map, path)

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_request):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_request.return_value = mock_response

        result = utils.get_json(test_url)
        mock_request.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        test_class_ins = TestClass()
        with patch.object(test_class_ins, 'a_method') as mock_method:
            mock_method.return_value = 42
            result1 = test_class_ins.a_property
            self.assertEqual(result1, 42)
            result2 = test_class_ins.a_property
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
