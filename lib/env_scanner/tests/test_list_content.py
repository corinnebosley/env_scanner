import os
import subprocess
import pytest


HERE = os.path.abspath(os.path.dirname(__file__))
ENV_SC = os.path.abspath(os.path.dirname(os.path.join(HERE, '../..')))

class TestListContent():
    def setup_class(self):
        # Command to list available environments
        get_envs = 'python {}/env_scanner.py --list_envs'.format(ENV_SC)
        self.env_list = subprocess.run([get_envs])
        assert subprocess.CompletedProcess.returncode == 0

        self.output = subprocess.check_output(get_envs,
                                              stderr=subprocess.STDOUT,
                                              shell=True)
        assert len(self.output) > 0
        assert len(self.output) > 1


    def test_list_content_all_envs(self):
        command_list = ['python {}env_scanner.py --list_content -env '
                        '{}'.format(env) for env in self.output]
        subprocess.run([command for command in command_list],
                       capture_output=True)
        print(command_list)
        assert subprocess.CompletedProcess.returncode == 0


if __name__ == '__main__':
    pytest.main()
