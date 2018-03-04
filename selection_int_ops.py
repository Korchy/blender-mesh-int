# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

import bpy
from .selection_int import SelectionInt


class SelectionIntSelectParents(bpy.types.Operator):
    bl_idname = 'selection_int.select_parents'
    bl_label = 'Parents chain'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        SelectionInt.selectparentsbychildred(context.active_object)
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return context.active_object.mode == 'OBJECT'


class SelectionIntSelectChildrens(bpy.types.Operator):
    bl_idname = 'selection_int.select_childrens'
    bl_label = 'Children chain'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        SelectionInt.selectchildrensbyparent(context.active_object)
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return context.active_object.mode == 'OBJECT'


def toselectionmenu(self, context):
    self.layout.separator()
    self.layout.operator('selection_int.select_parents')
    self.layout.operator('selection_int.select_childrens')


selection_int_keymaps = []


def register():
    bpy.utils.register_class(SelectionIntSelectParents)
    bpy.utils.register_class(SelectionIntSelectChildrens)
    bpy.types.VIEW3D_MT_select_object_more_less.append(toselectionmenu)

    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new(SelectionIntSelectParents.bl_idname, 'LEFT_BRACKET', 'PRESS', ctrl=True)
        selection_int_keymaps.append((km, kmi))
        kmi = km.keymap_items.new(SelectionIntSelectChildrens.bl_idname, 'RIGHT_BRACKET', 'PRESS', ctrl=True)
        selection_int_keymaps.append((km, kmi))


def unregister():
    for km, kmi in selection_int_keymaps:
        km.keymap_items.remove(kmi)
    selection_int_keymaps.clear()
    bpy.types.VIEW3D_MT_select_object_more_less.remove(toselectionmenu)
    bpy.utils.unregister_class(SelectionIntSelectChildrens)
    bpy.utils.unregister_class(SelectionIntSelectParents)
