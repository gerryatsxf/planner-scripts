import unittest
from app.hello_world.script.hello_world import main as hello_world_script

class HelloWorldScripTest(unittest.TestCase):
    
    def setUp(self):
        self.hello_world_script = hello_world_script

    def test_hello_world_script_returns_uppercase_string(self):
        input = {'message':'Hey there!'}
        expected_output = 'HEY THERE!'
        result = self.hello_world_script(input)
        self.assertTrue(result['message'] == expected_output)
