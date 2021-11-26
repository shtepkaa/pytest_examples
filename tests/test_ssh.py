from helpers.ssh import SshHelper
import pytest


def test_working_directory():
   ssh = SshHelper(ip_address='10.0.2.43', user='root', password='russia', ssh_port=22)
   answer = ssh.send_command_get_output('pwd')
   assert answer == '/root\n'
   ssh.disconnect()


@pytest.mark.usefixtures('ssh_fixture1')
def test_working_directory_w_fixture1():
   pytest.disable_teardown = False
   answer = pytest.ssh.send_command_get_output('pwd')
   assert answer == '/root\n'


def test_working_directory_w_fixture2(ssh_fixture2):
   answer = ssh_fixture2.send_command_get_output('pwd')
   assert answer == '/root\n'