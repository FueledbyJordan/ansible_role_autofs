def test_autofs_package_present(host):
    autofs = host.package("autofs")
    assert autofs.is_installed


def test_autofs_service(host):
    autofs = host.service("autofs")
    assert autofs.is_running
    assert autofs.is_enabled


def test_etc_auto_master_d_somename(host):
    file = host.file('/etc/auto.master.d/somename.autofs')
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o600
    assert file.content == b'#\n# Ansible managed\n#\n/- /etc/somename --timeout 60\n'  # noqa E501


def test_etc_auto_master_d_someothername(host):
    file = host.file('/etc/auto.master.d/someothername.autofs')
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o600
    assert file.content == b'#\n# Ansible managed\n#\n/- /etc/someothername --timeout 60\n'  # noqa E501


def test_etc_auto_somename(host):
    file = host.file('/etc/auto.somename')
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o600
    assert file.content == b'#\n# Ansible managed\n#\n/TESTING test_host:/opt/test_path\n'  # noqa E501


def test_etc_auto_someothername(host):
    file = host.file('/etc/auto.someothername')
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o600
    assert file.content == b'#\n# Ansible managed\n#\n/TESTING2 test_host2:/opt/test_path2\n'  # noqa E501
