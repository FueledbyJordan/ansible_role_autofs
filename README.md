ansible_role_autofs
=========

Installs and configures autofs for nfs mounts.

Requirements
------------

None.

Role Variables
--------------

autofs_mounts:
  - { name: 'the name of the mount', local_path: 'path to point on local system', remote_host: 'the name or ip address of the host with the nfs mount', remote_path: 'the path on the remote host' }

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: fueledbyjordan.ansible_role_autofs }

License
-------

MIT

Author Information
------------------

I can be reached at [djm@murrayfoundry.com](mailto:djm@murrayfoundry.com).
