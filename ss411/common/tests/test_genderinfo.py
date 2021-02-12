#test_genderinfo.py

from unittest import TestCase
from core.models.genderinfo import gender_list
from string import ascii_lowercase
#
# class Test_get_gender_strings_function(TestCase):
#     for l in ascii_lowercase:
#         if l in gender_list:
#             self.assertEqual(l in gender_list, True)
#         else self.assertEqual(l in gender_list, False)
#
#         self.assertEqual(gi.pronoun_char, "m")
#         self.assertEqual(gi.possessive_string, "his")
#         self.assertEqual(gi.gender_string, "Male")
#         self.assertEqual(gi.pronoun_string, "he")
#
#         #test for outputs where g_char = "m" and there is no pronoun_char passed
#         gi = GenderInfo(g_char="f")
#         self.assertEqual(gi.pronoun_char, "f")
#         self.assertEqual(gi.possessive_string, "her")
#         self.assertEqual(gi.gender_string, "Female")
#         self.assertEqual(gi.pronoun_string, "she")
#
#         # test for outputs where g_char = "n" and there is no pronoun_char passed
#         gi = GenderInfo(g_char="n")
#         self.assertEqual(gi.pronoun_char, "n")
#         self.assertEqual(gi.possessive_string, "their")
#         self.assertEqual(gi.gender_string, "Non-Binary")
#         self.assertEqual(gi.pronoun_string, "they")
#
#         # test for outputs where g_char = "u" and there is no pronoun_char passed
#         gi = GenderInfo(g_char="u")
#         self.assertEqual(gi.pronoun_char, "u")
#         self.assertEqual(gi.possessive_string, "their")
#         self.assertEqual(gi.gender_string, "Unknown")
#         self.assertEqual(gi.pronoun_string, "they")
#
#         # test for outputs where g_char = "f" and pronoun is "p"
#         gi = GenderInfo(g_char="f", pronoun_char="p")
#         self.assertEqual(gi.gender_char, "f")
#         self.assertEqual(gi.pronoun_char, "p")
#         self.assertEqual(gi.possessive_string, "their")
#         self.assertEqual(gi.gender_string, "Female")
#         self.assertEqual(gi.pronoun_string, "they")
#


