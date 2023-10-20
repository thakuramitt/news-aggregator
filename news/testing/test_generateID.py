from news.uuids import generateID
from django.test import TestCase
from news.uuids.generateID import generateUUIDfromString

import pytest
import logging
logger = logging.getLogger(__name__)
class test_uuid(TestCase):
    def test_generateUUIDfromString_length(self):
        logger.info("test_generateUUIDfromString_length test case run") 
        result = generateID.generateUUIDfromString("This is testing title")
        self.assertTrue(len(result)==10)

    def test_generateUUIDfromString_empty(self):
        temp = ""
        data = generateUUIDfromString(temp)
        self.assertEqual(data,"empty_title")
        logger.info("test_generateUUIDfromString_empty test case run")

    