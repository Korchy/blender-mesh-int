# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

import bpy


class MeshIntPolygonRotate(bpy.types.Operator):
    bl_idname = 'mesh_int.polygonrotate'
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
            for polygon in bpy.context.active_object.data.polygons:
                if polygon.select:
                    if self.direction:
                        polygon.vertices = polygon.vertices[-1:] + polygon.vertices[:-1]
                    else:
                        polygon.vertices = polygon.vertices[1:] + polygon.vertices[:1]
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
            polygonactive = bpy.context.active_object.data.polygons.active
            # polygon direction - vector from polygon vertex 0 to polygon vertex 1
            polygonactivedirection = context.active_object.data.vertices[context.active_object.data.polygons[polygonactive].vertices[1]].co - context.active_object.data.vertices[context.active_object.data.polygons[polygonactive].vertices[0]].co
            polygonactivedirection.normalize()
            for polygon in bpy.context.active_object.data.polygons:
                if polygon.select and polygon.index != polygonactive:
                    edges = [(polygon.vertices[i:]+polygon.vertices[:i])[:-2] for i in range(polygon.loop_total)]
                    minangle = [0, 0]
                    for i, edge in enumerate(edges):
                        edgedirection = context.active_object.data.vertices[edge[1]].co - context.active_object.data.vertices[edge[0]].co
                        edgedirection.normalize()
                        angle = edgedirection.dot(polygonactivedirection) + 1   # cos()+1 - from 0 to 2
                        if minangle[1] < angle:
                            minangle = [i, angle]
                    polygon.vertices = polygon.vertices[minangle[0]:] + polygon.vertices[:minangle[0]]
            bpy.ops.object.mode_set(mode=activeobjectmode)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(MeshIntPolygonRotate)
    bpy.utils.register_class(MeshIntPolygonRotateFollowActive)


def unregister():
    bpy.utils.unregister_class(MeshIntPolygonRotateFollowActive)
    bpy.utils.unregister_class(MeshIntPolygonRotate)
