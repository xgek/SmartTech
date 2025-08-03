# test_smartnlp.py
"""
Tests for SmartNLP module.
"""

import unittest
from smartnlp import SmartNLP

class TestSmartNLP(unittest.TestCase):
    """Test cases for SmartNLP class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SmartNLP()
        self.assertIsInstance(instance, SmartNLP)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SmartNLP()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
