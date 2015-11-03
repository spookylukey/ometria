#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ometria
----------------------------------

Tests for `ometria` module.
"""

import unittest
import httpretty

from ometria import Client


class TestOmetriaV1(unittest.TestCase):

    def setUp(self):
        self.client = Client(key="ometria_api_key", secret="ometria_api_secret", version="1")

    @httpretty.activate
    def test_retrieving_products(self):
        httpretty.register_uri(httpretty.GET, self.client.base_url + "products",
                               body="{}")

        r = self.client.products.get()
        self.assertEqual(r.response.status_code, 200)
        self.assertIn('Auth-Signature', r.response.request.headers)
        self.assertIn('Auth-API-Key', r.response.request.headers)


class TestOmetriaV2(unittest.TestCase):

    def setUp(self):
        self.client = Client(key="ometria_api_key", version="2")

    @httpretty.activate
    def test_retrieving_products(self):
        httpretty.register_uri(httpretty.GET, self.client.base_url + "products",
                               body="{}")

        r = self.client.products.get()
        self.assertEqual(r.response.status_code, 200)
        self.assertIn('X-Ometria-Auth', r.response.request.headers)

if __name__ == '__main__':
    unittest.main()
