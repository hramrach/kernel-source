from obsapi import utils
import unittest

class MiscTests(unittest.TestCase):
    def test_config_sh(self):
        config = utils.read_config_sh('tests/config_sh')
        self.assertEqual(config['variant'], '')
        self.assertEqual(config['multibuild'], 'Yes')
        self.assertEqual(config.getboolean('multibuild'), True)
        self.assertEqual(config['bugzilla_product'], 'openSUSE Tumbleweed')
