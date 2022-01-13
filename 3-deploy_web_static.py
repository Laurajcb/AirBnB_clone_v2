#!/usr/bin/python3
""" Function that do a full deployment of static content into servers
"""

from fabric.api import run, put, env
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['34.75.150.142', '54.205.3.49']


def deploy():
    """Function that do a full deployment"""
    web_static_pack = do_pack()

    if web_static_pack is None:
        return False
    return do_deploy(web_static_pack)


def do_pack():
    """ Function to generate a tgz from web_static"""
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        tgz_file = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static".format(tgz_file))
        return tgz_file
    except:
        return None


def do_deploy(archive_path):
    """Deploy the boxing package tgz file
    """
    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + archive.strip('.tgz')
        current = '/data/web_static/current'
        put(archive_path, '/tmp/')

        run('mkdir -p {}/'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(path, current))
        print('New version deployed!')
        return True
    except Exception as e:
        print(e)
        return False
