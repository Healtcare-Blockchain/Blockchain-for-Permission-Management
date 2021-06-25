import sys
import unittest
import logging

from web3 import Web3
from functions.blockchain import connection_setup

class BlockchainTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # Set up initial connection
        self.connection = connection_setup()
        print(self.connection.isConnected())

    def test_connection(self):
        # Check if the connection is working
        self.assertTrue(self.connection.isConnected(), msg="Not connected to chain")
        # self.assertEqual(type(self.connection), Web3, msg="Connection")

        



if __name__ == '__main__':
    unittest.main()