# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

import bpy
from mathutils import Vector

class MeshIntPolygonRotate(bpy.types.Operator):
    bl_idname = 'mesh_int.polygonrotate'
    bl_label = 'Mesh polygon rotation'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.active_object:
            activeobjectmode = context.active_object.mode
            if activeobjectmode == 'EDIT':
                bpy.ops.object.mode_set(mode='OBJECT')
            for polygon in bpy.context.active_object.data.polygons:
                if polygon.select:
                    if context.window_manager.mesh_int_vars.polygonrotatedirection == 'ccw':
                        polygon.vertices = polygon.vertices[1:] + polygon.vertices[:1]
                    else:
                        polygon.vertices = polygon.vertices[-1:] + polygon.vertices[:-1]
            bpy.ops.object.mode_set(mode=activeobjectmode)
        return {'FINISHED'}


class MeshIntPolygonRotateFollowActive(bpy.types.Operator):
    bl_idname = 'mesh_int.polygonrotate_followactive'
    bl_label = 'Mesh polygon rotation - follow active'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.active_object:
            activeobjectmode = context.active_object.mode
            if activeobjectmode == 'EDIT':
                bpy.ops.object.mode_set(mode='OBJECT')
            polygonactive = bpy.context.active_object.polygons.active
            # направление полигона (берем первый отрезок, точки 0 - 1)
            polygonactivedirection =  Vector(context.active_object.vertices[context.active_object.polygons[polygonactive].vertices[0]].co - context.active_object.vertices[context.active_object.polygons[polygonactive].vertices[1]].co)
            print(polygonactivedirection)

            # bpy.data.objects['Cube'].dupli_list_create(bpy.data.scenes[0])
            # [ob for ob in bpy.data.objects['Cube'].dupli_list]


            for polygon in bpy.context.active_object.data.polygons:
                if polygon.select:
                    if context.window_manager.mesh_int_vars.polygonrotatedirection == 'ccw':
                        polygon.vertices = polygon.vertices[1:] + polygon.vertices[:1]
                    else:
                        polygon.vertices = polygon.vertices[-1:] + polygon.vertices[:-1]
            bpy.ops.object.mode_set(mode=activeobjectmode)
        return {'FINISHED'}


class MeshIntVars(bpy.types.PropertyGroup):
    polygonrotatedirection = bpy.props.EnumProperty(
        items=[
            ('cw', '', 'CW', 'LOOP_FORWARDS', 0),
            ('ccw', '', 'CCW', 'LOOP_BACK', 1)
        ],
        default='cw'
    )

def register():
    bpy.utils.register_class(MeshIntPolygonRotate)
    bpy.utils.register_class(MeshIntVars)
    bpy.types.WindowManager.mesh_int_vars = bpy.props.PointerProperty(type=MeshIntVars)
    bpy.utils.register_class(MeshIntPolygonRotateFollowActive)


def unregister():
    bpy.utils.unregister_class(MeshIntPolygonRotateFollowActive)
    del bpy.types.WindowManager.mesh_int_vars
    bpy.utils.unregister_class(MeshIntVars)
    bpy.utils.unregister_class(MeshIntPolygonRotate)
