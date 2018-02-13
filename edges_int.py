# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-mesh-int

from mathutils import Vector


class Edge:

    def __init__(self, point0, point1):
        self.__point0 = Vector((0,0,0))
        if isinstance(point0, Vector):
            self.__point0 = point0
        self.__point1 = Vector((0,0,0))
        if isinstance(point1, Vector):
            self.__point1 = point1

    def __repr__(self):
        return "Edge({}, {})".format(self.__point0, self.__point1)

    @property
    def vertices(self):
        return [self.__point0, self.__point1]


class EdgesInt:

    @staticmethod
    def anglebetweenedges(edge0, edge1):
        # return cos() of the angle between two edges (from -1 (180) to 1 (0))
        vector0 = edge0.vertices[1] - edge0.vertices[0]
        vector0.normalize()
        vector1 = edge1.vertices[1] - edge1.vertices[0]
        vector1.normalize()
        return vector0.dot(vector1)
