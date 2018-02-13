# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

import bpy
from .edges_int import EdgesInt
from .edges_int import Edge
import math

class EdgesIntAngleBetweenEdges(bpy.types.Operator):
    bl_idname = 'edges_int.anglebetweenedges'
    bl_label = 'Angle Between Edges'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.active_object:
            activeobjectmode = context.active_object.mode
            if activeobjectmode == 'EDIT':
                bpy.ops.object.mode_set(mode='OBJECT')
            selectededges = [edge for edge in context.active_object.data.edges if edge.select]
            if len(selectededges) == 2:
                edge0 = Edge(context.active_object.data.vertices[selectededges[0].vertices[0]].co, context.active_object.data.vertices[selectededges[0].vertices[1]].co)
                edge1 = Edge(context.active_object.data.vertices[selectededges[1].vertices[0]].co, context.active_object.data.vertices[selectededges[1].vertices[1]].co)
                context.window_manager.edgesintvars.anglebetweenedges = math.acos(EdgesInt.anglebetweenedges(edge0, edge1))*180/math.pi
            bpy.ops.object.mode_set(mode=activeobjectmode)
        return {'FINISHED'}


class EdgesIntVars(bpy.types.PropertyGroup):
    anglebetweenedges = bpy.props.FloatProperty(
        name='anglebetweenedges',
        default=0.0
    )


def register():
    bpy.utils.register_class(EdgesIntAngleBetweenEdges)
    bpy.utils.register_class(EdgesIntVars)
    bpy.types.WindowManager.edgesintvars = bpy.props.PointerProperty(type=EdgesIntVars)


def unregister():
    del bpy.types.WindowManager.edgesintvars
    bpy.utils.unregister_class(EdgesIntVars)
    bpy.utils.unregister_class(EdgesIntAngleBetweenEdges)
