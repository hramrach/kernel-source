from obsapi import utils
import unittest

class MiscTests(unittest.TestCase):
    def test_config_sh(self):
        config = utils.read_config_sh('tests/config_sh')
        self.assertEqual(config['variant'], '')
        self.assertEqual(config['multibuild'], 'Yes')
        self.assertEqual(config.getboolean('multibuild'), True)
        self.assertEqual(config['bugzilla_product'], 'openSUSE Tumbleweed')

    def test_pkg_name(self):
        self.assertEqual(utils.get_kernel_project_package('tests/api/rpm/krn'), ('SUSE:SLE-15-SP7:Update', 'kernel-source'))
        self.assertEqual(utils.get_kernel_project_package('tests/api/rpm/krna'), ('SUSE:SLE-15-SP7:GA', 'kernel-source-azure'))
        self.assertEqual(utils.get_kernel_project_package('tests/api/rpm/krnf'), ('openSUSE:Factory', 'kernel-source'))
        self.assertEqual(utils.get_kernel_project_package('tests/api/rpm/kgr'),
                         ('SUSE:SLE-15-SP7:Update:Products:SLERT', 'kernel-livepatch-SLE15-SP7-RT_Update_0'))

    def test_list_files(self):
        result = [ f for f in sorted( '''
a directory/a file in a directory
a directory/another file in a directory
a directory/.a hidden file in a directory
another directory/a file in another directory
a file
another file
.a hidden file
'''.splitlines()) if len(f) > 0 ]
        self.assertEqual(utils.list_files('tests/api/dir'), result)
