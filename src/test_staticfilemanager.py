import unittest
from staticfilemanager import *

class testBlockProcessor(unittest.TestCase):
    def test_replicate_dir(self):
        replicate_dir("./static/","./public/")


if __name__ == "__main__":
    unittest.main()