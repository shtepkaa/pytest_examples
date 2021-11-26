import pytest
from helpers.ssh import SshHelper
import configuration


@pytest.fixture
def ssh_fixture1():
   pytest.ssh = SshHelper(ip_address='10.0.2.43', user='root', password='russia', ssh_port=22)
   yield
   if pytest.disable_teardown is False:
       pass
   pytest.ssh.disconnect()


@pytest.fixture
def ssh_fixture2(request):
   pytest.ssh = SshHelper(
       ip_address=configuration.ip_address,
       user=configuration.user,
       password=configuration.password,
       ssh_port=configuration.ssh_port
   )
   def fin():
       pytest.ssh.disconnect()
   request.addfinalizer(fin)
   return pytest.ssh
