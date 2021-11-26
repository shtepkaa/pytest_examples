import paramiko


class SshHelper:

    def __init__(self, ip_address, user, password, ssh_port):
        self.ssh = None
        self.connect(ip_address, user, password, ssh_port)

    def connect(self, ip_address, user, password, ssh_port):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=ip_address, username=user, password=password, port=ssh_port)

    def disconnect(self):
        self.ssh.close()

    def send_command_get_output(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        output = stdout.read()
        output = output.decode("utf8")
        return output