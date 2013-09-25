#!/usr/bin/python


class Repository(object):

    def __init__(self, name, serie, group, local_path, cloud_url=False):
        """
        Inicializate the repository object with the corresponding data
        @param name: name of the repository given for the user.
        @param serie: number of the project serie (the branch of the project
                      to push).
        @param group: launchpad group with permissions to push to the branch.
        @param local_path: the path of your local copy of the repository.
        @param cloud_url: the path of your local copy of the repository.
        """
        self.name = name
        self.serie = serie
        self.group = group
        self.local_path = local_path
        self.cloud_url = cloud_url


class Config(object):

    def __init__(self):
        """
        Create a config Object from openerp module. it set by default the
        repositories
        """
        self.repositories = {
            'addons-vauxoo': Repository(
                name='addons-vauxoo',
                serie='7.0',
                group='~vauxoo',
                local_path='~/bzr_projects/addons_vauxoo_branches/7.0-addons-vauxoo'),
            'vauxoo-private': Repository(
                name='vauxoo-private',
                serie=False,
                group='~vauxoo-private',
                local_path='~/bzr_projects/vauxoo-private'),
            'ovl70': Repository(
                name='openerp-venezuela-localization',
                serie='7.0',
                group='~vauxoo',
                local_path='~/bzr_projects/_VE/ovl_branches/ovl70'),
            'junk': Repository(
                name='~katherine-zaoral-7/+junk',
                serie=False,
                group='~katherine-zaoral-7',
                local_path='~/bzr_projects/+junk/katherine-zaoral-7'),
        }