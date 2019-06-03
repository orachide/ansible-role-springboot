import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_is_started(host):
    ansible_vars = host.ansible.get_variables()
    if (ansible_vars['inventory_hostname'].startswith('sb_centos6')):
        f = host.file('/etc/init.d/simple-springboot-app')
        assert f.exists
        assert f.user == 'sbuser'
        assert f.group == 'sbgroup'
    else:
        service = host.service('simple-springboot-app')
        assert service.is_running
        assert service.is_enabled


def test_app_is_listening_on_http(host):
    cmd = host.run("curl -IL http://localhost:8080/actuator/health")
    assert cmd.rc == 0
    assert re.search(r'HTTP/1.1 200', cmd.stdout)


def test_app_is_listening_on_https(host):
    cmd = host.run("curl -IL -k https://localhost:8443/actuator/health")
    assert cmd.rc == 0
    assert re.search(r'HTTP/1.1 200', cmd.stdout)
