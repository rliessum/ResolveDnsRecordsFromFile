from __future__ import unicode_literals
from distutils import dir_util
from pytest import fixture
import os
import resolveDnsRecordsFromFile

@fixture
def datadir(tmpdir, request):
    '''
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.
    '''
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, bytes(tmpdir))

    return tmpdir


FILENAME = 'dnsInput.csvvv'
REQUIREMENTS = 'dev-requirements.txt'


def test_files(datadir):
    expected_config_1 = datadir.join(FILENAME)
    expected_config_2 = datadir.join(REQUIREMENTS)
    

def test_starting_out():
        assert 1 == 1


# def test_read_and_resolve_from_file():
#         assert read_and_resolve_from_file() == 1
