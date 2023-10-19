from news.uuids import generateID
from django.test import TestCase
from news.uuids.generateID import generateUUIDfromString

import pytest
import logging

logging.basicConfig(filename='logs/newsapplogs.log',
                    level=10,
                    format="{asctime}:{levelname}:{filename}:{process}:{message}",
                    style='{'
                    )
class test_uuid(TestCase):
    def test_generateUUIDfromString_length(self):
        logging.info("test_generateUUIDfromString_length test case run") 
        result = generateID.generateUUIDfromString("This is testing title")
        self.assertTrue(len(result)==10)

    def test_generateUUIDfromString_empty(self):
        temp = ""
        data = generateUUIDfromString(temp)
        self.assertEqual(data,"empty_title")

    