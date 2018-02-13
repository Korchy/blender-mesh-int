# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

import bpy


class MeshInt:
    pass


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

    axis = bpy.props.StringProperty(
        name='axis',
        default='XY'
    )

    def execute(self, context):
        if context.active_object:
            activeobjectmode = context.active_object.mode
            if activeobjectmode == 'EDIT':
                bpy.ops.object.mode_set(mode='OBJECT')
            polygonactive = bpy.context.active_object.data.polygons.active
            # self.followbynormaltransform(context, context.active_object.data.polygons[polygonactive], axis='XY')
            # self.followbynormaltransform(context, context.active_object.data.polygons[polygonactive], axis='X')
            self.followbynormaltransform(context, context.active_object.data.polygons[polygonactive], axis=self.axis)
            bpy.ops.object.mode_set(mode=activeobjectmode)
        return {'FINISHED'}

    def followbynormaltransform(self, context, polygonactive, axis='XY'):
        print(axis)
        # polygon direction - vector from polygon vertex 2 to polygon vertex 1 (red in normal transform orientation)
        polygonactivedirection = context.active_object.data.vertices[polygonactive.vertices[1]].co - context.active_object.data.vertices[polygonactive.vertices[2]].co
        polygonactivedirection.normalize()
        # polygon direction normal - vector from polygon vertex 0 to polygon vertex 1 (green in normal transform orientation)
        polygonactivedirectionnormal = context.active_object.data.vertices[polygonactive.vertices[1]].co - context.active_object.data.vertices[polygonactive.vertices[0]].co
        polygonactivedirectionnormal.normalize()
        for polygon in bpy.context.active_object.data.polygons:
            if polygon.select and polygon.index != polygonactive.index:
                edges = [(polygon.vertices[i:] + polygon.vertices[:i])[:-1] for i in range(polygon.loop_total)]
                minangle = [0, 0]
                # if angle between polygons normals > 90 - reverse edge normal direction
                # anglebetweenpolygonsnormals = polygonactive.normal.dot(polygon.normal)
                for i, edge in enumerate(edges):
                    edgedirection = context.active_object.data.vertices[edge[1]].co - context.active_object.data.vertices[edge[2]].co
                    edgedirection.normalize()
                    anglebetweenedges = edgedirection.dot(polygonactivedirection) + 1  # cos()+1 - from 0 to 2 (180 to 0)
                    edgedirectionnormal = context.active_object.data.vertices[edge[1]].co - context.active_object.data.vertices[edge[0]].co
                    # if anglebetweenpolygonsnormals < 0:
                    #     edgedirectionnormal = context.active_object.data.vertices[edge[2]].co - context.active_object.data.vertices[edge[1]].co
                    # else:
                    #     edgedirectionnormal = context.active_object.data.vertices[edge[1]].co - context.active_object.data.vertices[edge[2]].co
                    edgedirectionnormal.normalize()
                    # print(edgedirectionnormal)
                    anglebetweennormals = edgedirectionnormal.dot(polygonactivedirectionnormal) + 1
                    # print(anglebetweennormals)
                    if axis == 'XY':
                        angle = anglebetweenedges + anglebetweennormals
                    elif axis == 'X':
                        angle = anglebetweenedges
                    if minangle[1] < angle:
                        minangle = [i, angle]
                # print(minangle)
                polygon.vertices = polygon.vertices[minangle[0]:] + polygon.vertices[:minangle[0]]


def register():
    bpy.utils.register_class(MeshIntPolygonRotate)
    bpy.utils.register_class(MeshIntPolygonRotateFollowActive)


def unregister():
    bpy.utils.unregister_class(MeshIntPolygonRotateFollowActive)
    bpy.utils.unregister_class(MeshIntPolygonRotate)
