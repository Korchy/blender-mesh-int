# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

from . import polygon_int_ops
from . import polygon_int_panel
from . import edges_int_ops
from . import edges_int_panel
from . import selection_int_ops

bl_info = {
    'name': 'Mesh-Int',
    'category': 'Mesh',
    'author': 'Nikita Akimov',
    'version': (1, 1, 4),
    'blender': (2, 79, 0),
    'location': '3D_View window -> T-Panel > Mesh-Int',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-mesh-int/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-mesh-int/',
    'description': 'Mesh-Int - some additional tools for working with meshes'
}


def register():
    if not Addon.dev_mode():
        selection_int_ops.register()
        polygon_int_ops.register()
        polygon_int_panel.register()
        edges_int_ops.register()
        edges_int_panel.register()
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] + ' add-on. It may work not properly. Please download and use the release version!')


def unregister():
    if not Addon.dev_mode():
        polygon_int_ops.unregister()
        polygon_int_panel.unregister()
        edges_int_ops.unregister()
        edges_int_panel.unregister()
        selection_int_ops.unregister()


if __name__ == '__main__':
    register()
