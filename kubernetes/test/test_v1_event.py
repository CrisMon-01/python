# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_event import V1Event


class TestV1Event(unittest.TestCase):
    """ V1Event unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1Event(self):
        """
        Test V1Event
        """
        model = kubernetes.client.models.v1_event.V1Event()


if __name__ == '__main__':
    unittest.main()
