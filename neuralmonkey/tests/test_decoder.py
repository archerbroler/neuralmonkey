#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# tests: mypy, lint

import unittest

from neuralmonkey.decoders.decoder import Decoder
from neuralmonkey.vocabulary import Vocabulary

class TestDecoder(unittest.TestCase):

    def test_init(self):
        decoder = Decoder([], Vocabulary(), "foo")
        self.assertIsNotNone(decoder)

if __name__ == "__main__":
    unittest.main()
