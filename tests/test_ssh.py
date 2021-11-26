from helpers.ssh import SshHelper


def test_working_directory():
   ssh = SshHelper(ip_address='10.0.2.43', user='root', password='russia', ssh_port=22)
   answer = ssh.send_command_get_output('pwd')
   assert answer == '/root\n'
   ssh.disconnect()
