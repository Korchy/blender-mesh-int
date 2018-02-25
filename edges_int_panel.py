# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

import bpy
from .edges_int_ops import EdgesIntVars

class EdgesIntPanel(bpy.types.Panel):
    bl_idname = 'edges_int.edges_panel'
    bl_label = 'Edges'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Mesh-Int'

    def draw(self, context):
        self.layout.label(text='Get angle between 2 edges:')
        row = self.layout.row()
        row.operator('edges_int.anglebetweenedges', text='Get Angle')
        row.label(str(EdgesIntVars.anglebetweenedges) if EdgesIntVars.anglebetweenedges is not None else '')


def register():
    bpy.utils.register_class(EdgesIntPanel)


def unregister():
    bpy.utils.unregister_class(EdgesIntPanel)
