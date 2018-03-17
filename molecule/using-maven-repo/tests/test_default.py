import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_is_started(host):
    ansible_vars = host.ansible.get_variables()
    if (ansible_vars['inventory_hostname'] == 'sb_centos6_maven_repo'):
        f = host.file('/etc/init.d/dummy-boot-app')
        assert f.exists
        assert f.user == 'sbuser'
        assert f.group == 'sbgroup'
    else:
        service = host.service('dummy-boot-app')
        assert service.is_running
        assert service.is_enabled


def test_app_is_listening(host):
    cmd = host.run("curl -IL localhost:8082/actuator/health")
    assert cmd.rc == 0
    assert re.search(r'HTTP/1.1 200', cmd.stdout)
