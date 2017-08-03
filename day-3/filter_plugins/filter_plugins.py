from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible import errors


def get_mongo_src(arg, os_family, os_release, mongodb_version):
      for lin in arg:
            if  os_family in lin:
                ver_index = lin.index(os_family) + len(os_family)
                ver_slice = lin[ver_index:]
                if ver_slice.startswith(os_release):
                    ver_mongo_slice = lin[ver_index + len(os_release):]
                    if mongodb_version in ver_mongo_slice:
                            return lin


class FilterModule(object):
    def filters(self):
        return {
            'get_mongo_src': get_mongo_src
        }

