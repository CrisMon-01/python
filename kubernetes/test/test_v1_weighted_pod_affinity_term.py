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
from kubernetes.client.models.v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm


class TestV1WeightedPodAffinityTerm(unittest.TestCase):
    """ V1WeightedPodAffinityTerm unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1WeightedPodAffinityTerm(self):
        """
        Test V1WeightedPodAffinityTerm
        """
        model = kubernetes.client.models.v1_weighted_pod_affinity_term.V1WeightedPodAffinityTerm()


if __name__ == '__main__':
    unittest.main()
