import os
import subprocess
import pytest


class TestListContent():
    def setup_class(self):
        # Command to list available environments
        get_envs = 'env_scanner --list_envs'
        self.env_list = subprocess.run([get_envs])
        assert subprocess.CompletedProcess.returncode == 0
        self.output = subprocess.check_output(get_envs,
                                              stderr=subprocess.STDOUT,
                                              shell=True)
        assert len(self.output) > 0
        assert len(self.output) > 1


    def test_list_content_all_envs(self):
        command_list = ['env_scanner --list_content -env '
                        '{}'.format(env) for env in self.output]
        subprocess.run([command for command in command_list],
                       capture_output=True)
        print(command_list)
        assert subprocess.CompletedProcess.returncode == 0


if __name__ == '__main__':
    pytest.main()