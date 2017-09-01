#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage OpenVZ containers
#
# Licensed under GPL version 3 or later
# (c) 2015 YAEGASHI Takeshi <yaegashi@debian.org>

DOCUMENTATION = """
---
module: openvz
author: YAEGASHI Takeshi
short_description: Manage OpenVZ Containers
version_added: 0.0
description:
  - 'Manage OpenVZ containers using vzctl/vzlist command line tools'
requirements:
  - 'vzctl >= 4.0'
notes:
  - vzctl/vzlist command line tools in the system must be new enough
    to support JSON outputs (C(vzlist --json)).
# OPTION DOC BEGIN
options:
    applyconfig:
        description:
        - Parameter passed to C(vzctl set --applyconfig).
    avnumproc:
        description:
        - UBC parameter passed to C(vzctl set --avnumproc).
    capability:
        description:
        - Parameter passed to C(vzctl set --capability).
    config:
        description:
        - Parameter passed to C(vzctl create --config).
    cpulimit:
        description:
        - Parameter passed to C(vzctl set --cpulimit).
    cpumask:
        description:
        - Parameter passed to C(vzctl set --cpumask).
    cpus:
        description:
        - Parameter passed to C(vzctl set --cpus).
    cpuunits:
        description:
        - Parameter passed to C(vzctl set --cpuunits).
    ctid:
        description:
        - Container ID or name to manage.
        required: true
    dcachesize:
        description:
        - UBC parameter passed to C(vzctl set --dcachesize).
    description:
        description:
        - Parameter passed to C(vzctl set --description).
    dgramrcvbuf:
        description:
        - UBC parameter passed to C(vzctl set --dgramrcvbuf).
    disabled:
        choices:
        - 'yes'
        - 'no'
        description:
        - Parameter passed to C(vzctl set --disabled).
    diskinodes:
        description:
        - Parameter passed to C(vzctl set --diskinodes).
    diskspace:
        description:
        - Parameter passed to C(vzctl set --diskspace).
    features:
        description:
        - Parameter passed to C(vzctl set --features).
    hostname:
        description:
        - Parameter passed to C(vzctl set --hostname).
    iolimit:
        description:
        - Parameter passed to C(vzctl set --iolimit).
    ioprio:
        description:
        - Parameter passed to C(vzctl set --ioprio).
    iopslimit:
        description:
        - Parameter passed to C(vzctl set --iopslimit).
    ipadd:
        description:
        - Parameter passed to C(vzctl set --ipadd).
    ipaddr:
        description:
        - IP address settings in the idempotent way.  Specify addresses in an array
            or a space delimited string.
    ipdel:
        description:
        - Parameter passed to C(vzctl set --ipdel).
    netfilter:
        description:
        - Parameter passed to C(vzctl set --netfilter).
    kmemsize:
        description:
        - UBC parameter passed to C(vzctl set --kmemsize).
    layout:
        description:
        - Parameter passed to C(vzctl create --layout).
    lockedpages:
        description:
        - UBC parameter passed to C(vzctl set --lockedpages).
    mount_opts:
        description:
        - Parameter passed to C(vzctl set --mount_opts).
    name:
        description:
        - Parameter passed to C(vzctl set --name).
    nameserver:
        description:
        - Parameter passed to C(vzctl set --nameserver).
    netif:
        description:
        - Network interface settings in the idempotent way.  Specify interfaces in
            an array or a space delimited string.
    netif_add:
        description:
        - Parameter passed to C(vzctl set --netif_add).
    netif_del:
        description:
        - Parameter passed to C(vzctl set --netif_del).
    nodemask:
        description:
        - Parameter passed to C(vzctl set --nodemask).
    numfile:
        description:
        - UBC parameter passed to C(vzctl set --numfile).
    numflock:
        description:
        - UBC parameter passed to C(vzctl set --numflock).
    numiptent:
        description:
        - UBC parameter passed to C(vzctl set --numiptent).
    numothersock:
        description:
        - UBC parameter passed to C(vzctl set --numothersock).
    numproc:
        description:
        - UBC parameter passed to C(vzctl set --numproc).
    numpty:
        description:
        - UBC parameter passed to C(vzctl set --numpty).
    numsiginfo:
        description:
        - UBC parameter passed to C(vzctl set --numsiginfo).
    numtcpsock:
        description:
        - UBC parameter passed to C(vzctl set --numtcpsock).
    onboot:
        choices:
        - 'yes'
        - 'no'
        description:
        - Parameter passed to C(vzctl set --onboot).
    oomguarpages:
        description:
        - UBC parameter passed to C(vzctl set --oomguarpages).
    ostemplate:
        description:
        - Parameter passed to C(vzctl create --ostemplate).
    othersockbuf:
        description:
        - UBC parameter passed to C(vzctl set --othersockbuf).
    physpages:
        description:
        - UBC parameter passed to C(vzctl set --physpages).
    private:
        description:
        - Parameter passed to C(vzctl create --private).
    privvmpages:
        description:
        - UBC parameter passed to C(vzctl set --privvmpages).
    quotatime:
        description:
        - Parameter passed to C(vzctl set --quotatime).
    quotaugidlimit:
        description:
        - Parameter passed to C(vzctl set --quotaugidlimit).
    ram:
        description:
        - Parameter passed to C(vzctl set --ram).
    root:
        description:
        - Parameter passed to C(vzctl create --root).
    searchdomain:
        description:
        - Parameter passed to C(vzctl set --searchdomain).
    shmpages:
        description:
        - UBC parameter passed to C(vzctl set --shmpages).
    state:
        choices:
        - started
        - stopped
        - present
        - absent
        description:
        - Container target state.
    swap:
        description:
        - Parameter passed to C(vzctl set --swap).
    swappages:
        description:
        - UBC parameter passed to C(vzctl set --swappages).
    tcprcvbuf:
        description:
        - UBC parameter passed to C(vzctl set --tcprcvbuf).
    tcpsndbuf:
        description:
        - UBC parameter passed to C(vzctl set --tcpsndbuf).
    userpasswd:
        description:
        - Parameter passed to C(vzctl set --userpasswd).
    vmguarpages:
        description:
        - UBC parameter passed to C(vzctl set --vmguarpages).
# OPTION DOC END
"""

EXAMPLES = """
- openvz:
    ctid: 1000
    state: started
    ostemplate: ubuntu-14.04-x86_64-minimal
    ram: 1G
    swap: 512M
    diskspace: 2G
    hostname: foobar
    name: foobar
    ipaddr:
    - 192.168.0.100
    - 192.168.0.101
    nameserver: 192.168.0.1
    userpasswd: ansible:secret
    description: Ubuntu trusty amd64 container
"""

CREATE_PARAMS = set((
    'ostemplate', 'config', 'root', 'private', 'layout', 'diskspace',
    'diskinodes'
))

SET_PARAMS = set((
    'ram', 'swap', 'ipaddr', 'ipadd', 'ipdel', 'hostname', 'nameserver',
    'searchdomain', 'onboot', 'userpasswd', 'cpuunits', 'cpulimit', 'cpus',
    'cpumask', 'nodemask', 'diskspace', 'diskinodes', 'quotatime',
    'quotaugidlimit', 'mount_opts', 'capability', 'netif', 'netif_add',
    'netif_del', 'applyconfig', 'features', 'name', 'description', 'ioprio',
    'iolimit', 'iopslimit', 'netfilter', 'disabled'
))

UBC_PARAMS = set((
    'kmemsize', 'lockedpages', 'privvmpages', 'shmpages', 'numproc',
    'physpages', 'vmguarpages', 'oomguarpages', 'numtcpsock', 'numflock',
    'numpty', 'numsiginfo', 'tcpsndbuf', 'tcprcvbuf', 'othersockbuf',
    'dgramrcvbuf', 'numothersock', 'dcachesize', 'numfile', 'numiptent',
    'swappages', 'avnumproc'
))

DIFF_PARAMS = set((
    'private', 'root', 'mount_opts', 'hostname', 'name', 'description', 'ip',
    'nameserver', 'searchdomain', 'status', 'cpulimit', 'cpuunits', 'cpus',
    'ioprio', 'iolimit', 'iopslimit', 'onboot', 'bootorder', 'layout',
    'features', 'disabled'
))

def docupdate():
    options = {}
    options.update(dict([
        (i, {'description': ['Parameter passed to C(vzctl create --%s).' % i]})
        for i in CREATE_PARAMS]))
    options.update(dict([
        (i, {'description': ['Parameter passed to C(vzctl set --%s).' % i]})
        for i in SET_PARAMS]))
    options.update(dict([
        (i, {'description': ['UBC parameter passed to C(vzctl set --%s).' % i]})
        for i in UBC_PARAMS]))
    options.update({
        'ctid': {
            'description': ['Container ID or name to manage.'],
            'required': True
        },
        'state': {
            'description': ['Container target state.'],
            'choices': ['started', 'stopped', 'present', 'absent'],
        },
        'onboot': {
            'description': ['Parameter passed to C(vzctl set --onboot).'],
            'choices': ['yes', 'no']
        },
        'disabled': {
            'description': ['Parameter passed to C(vzctl set --disabled).'],
            'choices': ['yes', 'no']
        },
        'ipaddr' : {
            'description': [
                'IP address settings in the idempotent way.  '
                'Specify addresses in an array or a space delimited string.'
            ],
        },
        'netif' : {
            'description': [
                'Network interface settings in the idempotent way.  '
                'Specify interfaces in an array or a space delimited string.'
            ],
        },
    })

    with open(__file__) as f:
        lines = f.readlines()
    n0 = n1 = -1

    for i, line in enumerate(lines):
        if line.startswith('# OPTION DOC BEGIN'): n0 = i
        if line.startswith('# OPTION DOC END'): n1 = i

    if n0 >= 0 and n1 >= 0 and n1 > n0:
        import yaml
        lines[n0+1:n1] = yaml.dump({'options': options},
                                   indent=4, default_flow_style=False)
        with open(__file__, 'w') as f:
            f.writelines(lines)
        print 'Updated documentation in %s' % __file__

def maint():
    if len(sys.argv) > 1 and sys.argv[1] == 'docupdate':
        docupdate()

def main():

    def get_vzjson():
        (rc, out, err) = m.run_command([vzlist_path, '-j', ctid])
        if not rc:
            return json.loads(out)[0]
        elif out == '[]\n' or 'Container(s) not found' in err:
            return {}
        m.fail_json(msg='No JSON support, vzlist is too old?', err=err)

    def diff_vzjson(a, b):
        if not a and not b:
            return False
        if (a and not b) or (not a and b):
            return True
        for i in UBC_PARAMS:
            if (i in a and i not in b) or (i not in a and i in b):
                return True
            if i in a:
                if a[i]['barrier'] != b[i]['barrier'] or \
                   a[i]['limit'] != b[i]['limit']:
                    return True
        for i in ('diskspace', 'diskinodes'):
            if (i in a and i not in b) or (i not in a and i in b):
                return True
            if i in a:
                if a[i]['softlimit'] != b[i]['softlimit'] or \
                   a[i]['hardlimit'] != b[i]['hardlimit']:
                    return True
        for i in DIFF_PARAMS:
            if (i in a and i not in b) or (i not in a and i in b):
                return True
            if i in a:
                if type(a[i]) is list:
                    if sorted(a[i]) != sorted(b[i]):
                        return True
                elif a[i] != b[i]:
                    return True
        return False

    def get_vzargs(params):
        args = []
        for i in params:
            p = m.params[i]
            if not p: continue
            if i == 'ipaddr':
                args += ['--ipdel', 'all', '--ipadd']
                args.append(' '.join(p) if type(p) is list else str(p))
            elif i == 'netif':
                args += ['--netif_del', 'all', '--netif_add']
                args.append(' '.join(p) if type(p) is list else str(p))
            else:
                args.append('--%s' % i)
                if type(p) is bool:
                    args.append('yes' if p else 'no')
                else:
                    args.append(str(p))
        return args

    spec = dict([(i, dict()) for i in CREATE_PARAMS | SET_PARAMS | UBC_PARAMS])
    spec.update(
        ctid=dict(required=True),
        state=dict(choices=['started', 'stopped', 'present', 'absent']),
        onboot=dict(choices=BOOLEANS, type='bool'),
        disabled=dict(choices=BOOLEANS, type='bool'),
    )
    m = AnsibleModule(argument_spec=spec)

    vzctl_path = m.get_bin_path('vzctl', required=True)
    vzlist_path = m.get_bin_path('vzlist', required=True)

    ctid = str(m.params['ctid'])
    state = str(m.params['state'])
    vzjson = vzjson_original = get_vzjson()
    done = []

    if state in ('started', 'stopped', 'present'):
        if not vzjson:
            args = [vzctl_path, 'create', ctid]
            args += get_vzargs(CREATE_PARAMS)
            (rc, out, err) = m.run_command(args, check_rc=True)
            done.append('created')
            vzjson = get_vzjson()

    if vzjson:
        args = get_vzargs(SET_PARAMS | UBC_PARAMS)
        if args:
            args = [vzctl_path, 'set', ctid, '--save'] + args
            (rc, out, err) = m.run_command(args, check_rc=True)
            done.append('configured')

    if state == 'started':
        if vzjson and vzjson['status'] != 'running':
            args = [vzctl_path, 'start', ctid]
            (rc, out, err) = m.run_command(args, check_rc=True)
            done.append('started')

    if state in ('stopped', 'absent'):
        if vzjson and vzjson['status'] != 'stopped':
            args = [vzctl_path, 'stop', ctid]
            (rc, out, err) = m.run_command(args, check_rc=True)
            done.append('stopped')

    if state == 'absent':
        if vzjson:
            args = [vzctl_path, 'destroy', ctid]
            (rc, out, err) = m.run_command(args, check_rc=True)
            done.append('destroyed')

    vzjson = get_vzjson()
    if state == 'present' and not vzjson:
        m.fail_json(msg='Failed to make the container present')
    elif state == 'started' and vzjson and vzjson['status'] != 'running':
        m.fail_json(msg='Failed to make the container started')
    elif state == 'stopped' and vzjson and vzjson['status'] != 'stopped':
        m.fail_json(msg='Failed to make the container stopped')
    elif state == 'absent' and vzjson:
        m.fail_json(msg='Failed to make the container absent')

    changed = diff_vzjson(vzjson, vzjson_original)
    msg = ', '.join(done) if changed else 'nothing done'
    m.exit_json(changed=changed, msg=msg.capitalize())

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()  # Run as a module
