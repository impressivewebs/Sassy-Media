#!/usr/bin/python

import sys
import unittest

sys.path.append("lib")
import sassymedia


class TestSassyMedia(unittest.TestCase):

    def setUp(self):
        self.SM = sassymedia.SassyMedia()

    def tearDown(self):
        self.SM = None

    def _run_match_test(self, test_folder, message=None):
        # Get CSS input
        fh = open("tests/%s/input.css" % test_folder, "r")
        input_ = fh.read()
        fh.close()
        # Get expected output
        fh = open("tests/%s/expected.css" % test_folder, "r")
        expected = fh.read()
        fh.close()
        # Run input through Sassy Media
        self.SM.contents = input_
        self.SM.run()
        # Test against expected output
        try:
            self.assertEqual(self.SM.contents, expected, message)
        except AssertionError, e:
            print self.SM.contents
            raise e

#-------------------------------------------------------------------------------

    def test_is_class(self):
        self.assertIsInstance(self.SM, sassymedia.SassyMedia,
            "Instance does not match class.")

#-------------------------------------------------------------------------------

    def test_no_media_query(self):
        self._run_match_test("no_media_query",
            "Input with no media query did not produce the expected output")

#-------------------------------------------------------------------------------

    def test_single_query_at_end(self):
        self._run_match_test("single_query_at_end",
            "Input with a single media query at the end did not produce the expected output")

    def test_single_query_at_beginning(self):
        self._run_match_test("single_query_at_beginning",
            "Input with a single media query at the beginning did not produce the expected output")

#-------------------------------------------------------------------------------

    def test_two_different_queries_at_end(self):
        self._run_match_test("two_different_queries_at_end",
            "Input with two different media queries at the end did not produce the expected output")

    def test_two_different_queries_at_beginning(self):
        self._run_match_test("two_different_queries_at_beginning",
            "Input with two different media queries at the beginning did not produce the expected output")

    def test_two_different_queries_at_beginning_and_end(self):
        self._run_match_test("two_different_queries_at_beginning_and_end",
            "Input with two different media queries at the beginning and end did not produce the expected output")

#-------------------------------------------------------------------------------

    def test_two_similar_queries_at_end(self):
        self._run_match_test("two_similar_queries_at_end",
            "Input with two similar media queries at the end did not produce the expected output")

    def test_two_similar_queries_at_beginning(self):
        self._run_match_test("two_similar_queries_at_beginning",
            "Input with two similar media queries at the beginning did not produce the expected output")

    def test_two_similar_queries_at_beginning_and_end(self):
        self._run_match_test("two_similar_queries_at_beginning_and_end",
            "Input with two similar media queries at the beginning and end did not produce the expected output")

#-------------------------------------------------------------------------------

    def test_two_selectors_with_multiple_queries(self):
        # The output is correct by the algorithm, though not necessarily the output desired by the user
        self._run_match_test("two_selectors_with_multiple_queries",
            "Input with two selectors and multiple media queries did not produce the expected output")

#-------------------------------------------------------------------------------


if __name__ == "__main__":
    unittest.main()
