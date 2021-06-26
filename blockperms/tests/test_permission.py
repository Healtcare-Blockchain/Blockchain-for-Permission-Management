import sys
import unittest
import logging
from web3 import Web3
from functions.blockchain import connection_setup
from functions.account import unlock_account, list_accounts
from functions.permission import set_permission, check_permission

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

    def test_unlock_account(self):
        # Check if unlocking accounts works
        self.assertEqual(unlock_account("0x490CD3cAbED9f706055e617Ed09F96a905E0BD31", "root"), 'Account unlocked')

    def test_list_accounts(self):
        # Check if accounts are detected on the chain
        self.assertIsInstance(list_accounts(), list)

    def test_set_permission(self):
        self.assertTrue(check_permission("0x50b72d23E5F3c1E0002E2E4C44C2f01ddd605b6F", "0x490CD3cAbED9f706055e617Ed09F96a905E0BD31"))


if __name__ == '__main__':
    unittest.main()