# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

import bpy


class SelectionInt:

    @staticmethod
    def selectchildrensbyparent(mesh):
        # selects all childrens of the mesh object
        childrens = list(mesh.children)
        for child in childrens:
            child.select = True
            if child.children:
                for nextchild in child.children:
                    if nextchild not in childrens:
                        childrens.append(nextchild)

    @staticmethod
    def selectparentsbychildred(mesh):
        # selects all parents of the mesh object
        while mesh.parent:
            mesh = mesh.parent
            mesh.select = True
