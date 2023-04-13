import unittest
from helpers import snake_case


class TestSnakeCase(unittest.TestCase):
    def test_snake_case(self):
        self.assertEqual(snake_case("HelloWorld"), "hello_world")
        self.assertEqual(snake_case("Hello-World"), "hello_world")
        self.assertEqual(snake_case("helloWorld"), "hello_world")
        self.assertEqual(snake_case("hello_world"), "hello_world")
        self.assertEqual(snake_case("HELLO_WORLD"), "hello_world")
        self.assertEqual(snake_case("Hello_World_Test"), "hello_world_test")
        self.assertEqual(snake_case("snake_case"), "snake_case")
