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
from kubernetes.client.models.v1_node_selector_requirement import V1NodeSelectorRequirement


class TestV1NodeSelectorRequirement(unittest.TestCase):
    """ V1NodeSelectorRequirement unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1NodeSelectorRequirement(self):
        """
        Test V1NodeSelectorRequirement
        """
        model = kubernetes.client.models.v1_node_selector_requirement.V1NodeSelectorRequirement()


if __name__ == '__main__':
    unittest.main()
