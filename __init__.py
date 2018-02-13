# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

bl_info = {
    'name': 'Mesh-Int',
    'category': 'Mesh',
    'author': 'Nikita Akimov',
    'version': (0, 0, 0),
    'blender': (2, 79, 0),
    'location': '3D_View window -> T-Panel > Mesh-Int',
    'wiki_url': '',
    'tracker_url': '',
    'description': 'Mesh-Int - some additional tools for working with meshes'
}

from . import mesh_int
from . import mesh_int_panel
from . import edges_int_panel
from . import edges_int_ops


def register():
    mesh_int.register()
    mesh_int_panel.register()
    edges_int_panel.register()
    edges_int_ops.register()


def unregister():
    mesh_int.unregister()
    mesh_int_panel.unregister()
    edges_int_panel.unregister()
    edges_int_ops.unregister()


if __name__ == '__main__':
    register()
