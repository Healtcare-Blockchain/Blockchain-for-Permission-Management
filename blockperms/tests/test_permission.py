import sys
import unittest
import logging

from web3 import Web3
from functions.blockchain import connection_setup

class BlockchainTest(unittest.TestCase):
    def setUpClass(self):
        # Set up initial connection
        self.connection = connection_setup()

    def test_connection(self):
        # Check if the connection is working
        self.assertIsInstance(self.connection, Web3)
        self.assertTrue(self.connection.isConnected())

if __name__ == '__main__':
    unittest.main()