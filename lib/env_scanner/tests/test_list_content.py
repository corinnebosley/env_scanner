import subprocess
import pytest


class TestListContent():
    def setup_class(self):
        # List available environments to test functionality with
        get_envs = 'python env_scanner.py --list_envs'
        self.env_list = subprocess.run([get_envs])
        assert subprocess.CompletedProcess.returncode == 0

        self.output = subprocess.check_output(get_envs,
                                              stderr=subprocess.STDOUT,
                                              shell=True)
        assert len(self.output) > 0
        assert len(self.output) > 1


    def test_list_content_all_envs(self):
        command_list = ['python env_scanner.py --list_content -env '
                        '{}'.format(env) for env in self.output]
        subprocess.run([command for command in command_list],
                       capture_output=True)
        print(command_list)
        assert subprocess.CompletedProcess.returncode == 0


if __name__ == '__main__':
    pytest.main()
