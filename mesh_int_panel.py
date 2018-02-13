# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

import bpy


class MeshIntPanel(bpy.types.Panel):
    bl_idname = 'mesh_int.polygon_panel'
    bl_label = 'Polygon'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Mesh-Int'

    def draw(self, context):
        self.layout.label('Rotate:')
        col = self.layout.column(align=True)
        row = col.row(align=True)
        row.operator('mesh_int.polygonrotate', text='CW', icon='LOOP_FORWARDS').direction = True
        row.operator('mesh_int.polygonrotate', text='CCW', icon='LOOP_BACK').direction = False
        col.operator('mesh_int.polygonrotate_followactive', text='Follow Active')

        self.layout.operator('mesh_int.polygonrotate_followactive', text='Follow Active XY').axis = 'XY'
        self.layout.operator('mesh_int.polygonrotate_followactive', text='Follow Active X').axis = 'X'

def register():
    bpy.utils.register_class(MeshIntPanel)


def unregister():
    bpy.utils.unregister_class(MeshIntPanel)
