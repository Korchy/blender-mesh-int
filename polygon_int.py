# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

import bpy
from bpy_extras.view3d_utils import location_3d_to_region_2d
import math

class PolygonInt:

    @staticmethod
    def rotatepolygon(context, polygon, direction=True, rounds=0):
        # rotates polygon
        # direction = True -> CW, False -> CCW
        if polygon and rounds > 0:
            if direction:
                rounds = -rounds
            activeobjectmode = context.active_object.mode
            if activeobjectmode == 'EDIT':
                bpy.ops.object.mode_set(mode='OBJECT')
            polygon.vertices = polygon.vertices[rounds:] + polygon.vertices[:rounds]
            bpy.ops.object.mode_set(mode=activeobjectmode)

    @staticmethod
    def followpolygondirectionbyactive(context, activepolygon):
        # rotate selected polygons to follow the direction (normal X-axis) of the active polygon
        # Rotate to achieve min angle between X-axis of the selected and active polygon
        if context and activepolygon:
            activepolygon_x_axis = context.active_object.data.vertices[activepolygon.vertices[1]].co - context.active_object.data.vertices[activepolygon.vertices[2]].co
            activepolygon_x_axis.normalize()
            activeobjectmode = context.active_object.mode
            if activeobjectmode == 'EDIT':
                bpy.ops.object.mode_set(mode='OBJECT')
            for polygon in context.active_object.data.polygons:
                if polygon.select and polygon.index != activepolygon.index:
                    variants = [(polygon.vertices[i:] + polygon.vertices[:i]) for i in range(polygon.loop_total)]
                    minangle = [0, 0]
                    anglebetweennormals = activepolygon.normal.dot(polygon.normal)
                    for i, variant in enumerate(variants):
                        polygon_x_axis = context.active_object.data.vertices[variant[1]].co - context.active_object.data.vertices[variant[2]].co
                        polygon_x_axis.normalize()
                        anglebetween_x_axis = polygon_x_axis.dot(activepolygon_x_axis)  # cos() - from -1 to 1 (180 to 0)
                        if minangle[1] < anglebetween_x_axis:
                            minangle = [i, anglebetween_x_axis]
                    # if angle between polygons normals > 90 - reverse rotation direction
                    direction = True if anglebetweennormals < 0 else False
                    __class__.rotatepolygon(context, polygon, direction=direction, rounds=minangle[0])
            bpy.ops.object.mode_set(mode=activeobjectmode)

    @staticmethod
    def followpolygondirectionbyactiveproj(context, activepolygon):
        # rotate selected polygons to follow the direction (normal X-axis) of the active polygon
        # Rotate to achieve min angle between projectons of the X-axis of the selected and active polygon to viewport
        if context and activepolygon:
            activepolygon_x_axis_p2 = context.active_object.data.vertices[activepolygon.vertices[2]].co
            activepolygon_x_axis_p1 = context.active_object.data.vertices[activepolygon.vertices[1]].co
            activepolygon_x_axis_p2_proj = location_3d_to_region_2d(context.area.regions[0], context.area.spaces.active.region_3d, activepolygon_x_axis_p2)
            activepolygon_x_axis_p1_proj = location_3d_to_region_2d(context.area.regions[0], context.area.spaces.active.region_3d, activepolygon_x_axis_p1)
            activepolygon_x_axis_proj = activepolygon_x_axis_p1_proj - activepolygon_x_axis_p2_proj
            activepolygon_x_axis_proj.normalize()
            activeobjectmode = context.active_object.mode
            if activeobjectmode == 'EDIT':
                bpy.ops.object.mode_set(mode='OBJECT')
            for polygon in context.active_object.data.polygons:
                if polygon.select and polygon.index != activepolygon.index:
                    variants = [(polygon.vertices[i:] + polygon.vertices[:i]) for i in range(polygon.loop_total)]
                    minangle = [0, 0]
                    anglebetweennormals = activepolygon.normal.dot(polygon.normal)
                    for i, variant in enumerate(variants):
                        polygon_x_axis_p2 = context.active_object.data.vertices[variant[2]].co
                        polygon_x_axis_p1 = context.active_object.data.vertices[variant[1]].co
                        polygon_x_axis_p2_proj = location_3d_to_region_2d(context.area.regions[0], context.area.spaces.active.region_3d, polygon_x_axis_p2)
                        polygon_x_axis_p1_proj = location_3d_to_region_2d(context.area.regions[0], context.area.spaces.active.region_3d, polygon_x_axis_p1)
                        polygon_x_axis_proj = polygon_x_axis_p1_proj - polygon_x_axis_p2_proj
                        polygon_x_axis_proj.normalize()
                        anglebetween_x_axis = polygon_x_axis_proj.dot(activepolygon_x_axis_proj)  # cos() - from -1 to 1 (180 to 0)
                        if minangle[1] < anglebetween_x_axis:
                            minangle = [i, anglebetween_x_axis]
                    # if angle between polygons normals > 90 - reverse rotation direction
                    direction = True if anglebetweennormals < 0 else False
                    __class__.rotatepolygon(context, polygon, direction=direction, rounds=minangle[0])
            bpy.ops.object.mode_set(mode=activeobjectmode)
