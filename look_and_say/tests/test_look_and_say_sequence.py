import unittest
from look_and_say.look_and_say_sequence import LookAndSaySequence


class TestLookAndSaySequence(unittest.TestCase  ):

    def test_get_sequence_returns_look_and_say_sequence_of_a_number(self):
        look_and_say_sequence = LookAndSaySequence()
        result = look_and_say_sequence.get_sequence("1")

        self.assertEqual(result, "11")
