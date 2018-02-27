# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

bl_info = {
    'name': 'Mesh-Int',
    'category': 'Mesh',
    'author': 'Nikita Akimov',
    'version': (1, 0, 2),
    'blender': (2, 79, 0),
    'location': '3D_View window -> T-Panel > Mesh-Int',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-mesh-int/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-mesh-int/',
    'description': 'Mesh-Int - some additional tools for working with meshes'
}

from . import polygon_int_ops
from . import polygon_int_panel
from . import edges_int_ops
from . import edges_int_panel


def register():
    polygon_int_ops.register()
    polygon_int_panel.register()
    edges_int_ops.register()
    edges_int_panel.register()


def unregister():
    polygon_int_ops.unregister()
    polygon_int_panel.unregister()
    edges_int_ops.unregister()
    edges_int_panel.unregister()


if __name__ == '__main__':
    register()
