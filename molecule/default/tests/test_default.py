import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nsd_server_is_installed(host):
    nsd = host.package('nsd')

    assert nsd.is_installed


def test_nsd_is_running(host):
    nsd = host.service('nsd')

    assert nsd.is_running
    assert nsd.is_enabled


def test_nsd_is_listening(host):
    assert host.socket("udp://0.0.0.0:5353").is_listening
