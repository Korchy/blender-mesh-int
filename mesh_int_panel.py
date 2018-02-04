# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

import bpy


class MeshIntPanel(bpy.types.Panel):
    bl_idname = 'mesh_int.panel'
    bl_label = 'Mesh-Int'
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Mesh-Int"

    def draw(self, context):
        self.layout.label('Polygon')
        row = self.layout.row()
        row.operator("mesh_int.polygonrotate", text="Rotate:")
        row.prop(context.window_manager.mesh_int_vars, 'polygonrotatedirection', expand=True)
        row = self.layout.row()
        row.operator("mesh_int.polygonrotate_followactive", text="Follow Active")


def register():
    bpy.utils.register_class(MeshIntPanel)


def unregister():
    bpy.utils.unregister_class(MeshIntPanel)
