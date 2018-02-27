# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

import bpy
from .polygon_int import PolygonInt


class PolygonIntPolygonRotate(bpy.types.Operator):
    bl_idname = 'polygon_int.polygonrotate'
    bl_label = 'Mesh polygon rotation'
    bl_options = {'REGISTER', 'UNDO'}

    direction = bpy.props.BoolProperty(
        name='direction',
        default=True  # True = CW, False = CCW
    )

    def execute(self, context):
        if context.active_object:
            activeobjectmode = context.active_object.mode
            if activeobjectmode == 'EDIT':
                bpy.ops.object.mode_set(mode='OBJECT')
            for polygon in context.active_object.data.polygons:
                if polygon.select:
                    PolygonInt.rotatepolygon(context, polygon, self.direction, 1)
            bpy.ops.object.mode_set(mode=activeobjectmode)
        return {'FINISHED'}


class PolygonIntPolygonRotateFollowActive(bpy.types.Operator):
    bl_idname = 'polygon_int.polygonrotate_followactive'
    bl_label = 'Mesh polygon rotation - follow active'
    bl_options = {'REGISTER', 'UNDO'}

    mode = bpy.props.EnumProperty(
        items=[
            ('Direction', 'Direction', '', '', 0),
            ('Projection', 'Projection', '', '', 1)
        ],
        default='Direction'
    )

    def execute(self, context):
        if context.active_object:
            activeobjectmode = context.active_object.mode
            if activeobjectmode == 'EDIT':
                bpy.ops.object.mode_set(mode='OBJECT')
            polygonactiveindex = context.active_object.data.polygons.active
            if self.mode == 'Direction':
                PolygonInt.followpolygondirectionbyactive(context, context.active_object.data.polygons[polygonactiveindex])
            elif self.mode == 'Projection':
                PolygonInt.followpolygondirectionbyactiveproj(context, context.active_object.data.polygons[polygonactiveindex])
            bpy.ops.object.mode_set(mode=activeobjectmode)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(PolygonIntPolygonRotate)
    bpy.utils.register_class(PolygonIntPolygonRotateFollowActive)


def unregister():
    bpy.utils.unregister_class(PolygonIntPolygonRotateFollowActive)
    bpy.utils.unregister_class(PolygonIntPolygonRotate)
