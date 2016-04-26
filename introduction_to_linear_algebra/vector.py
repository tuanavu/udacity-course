from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the vector zero'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        """ Adding vector
        """
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        """ Minus vector
        """
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        """ Scalar multiplication
        """
        new_coordinates = [Decimal(c) * x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        """ Magnitude of the vector
        """
        coordinates_squared = [x**2 for x in self.coordinates]
        return Decimal(sqrt(sum(coordinates_squared)))

    def normalized(self):
        """ Normalize a vector
        """
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0')/magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, v):
        """ Dot product between 2 vectors
        """
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        """ Compute angle between 2 vectors
        """
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(u1.dot(u2))

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot copute an angle with the zero vector')
            else:
                raise e

    def is_orthogonal_to(self, v, tolerance=1e-10):
        """ Check if one vector is orthogonal with another vector
        """
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v, tolerance=1e-10):
        """ Check if one vector is parallel to another vector
        """
        return ( self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == pi )

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance




my_vector = Vector([1,2,3])
print my_vector

my_vector2 = Vector([1,2,3])
my_vector3 = Vector([-1,2,3])

print my_vector == my_vector2
print my_vector == my_vector3

print "\n### quiz 1: plus, minus, scalar multiply ###\n"
v = Vector([8.218,-9.341])
w = Vector([-1.129,2.111])
print v.plus(w)

v = Vector([7.119,8.215])
w = Vector([-8.223,0.878])
print v.minus(w)

v = Vector([1.671,-1.012,-0.318])
c = 7.41
print v.times_scalar(c)

print "\n### quiz 2: magnitude, direction ###\n"
v = Vector([-0.221,7.437])
print v.magnitude()

v = Vector([8.813,-1.331,-6.247])
print v.magnitude()

v = Vector([5.581,-2.136])
print v.normalized()

v = Vector([1.996,3.108,-4.554])
print v.normalized()

print "\n### quiz 3: Dot product and Angle ###\n"
v = Vector([7.887,4.138])
w = Vector([-8.802,6.776])
print v.dot(w)

v = Vector([-5.955,-4.904,-1.874])
w = Vector([-4.496,-8.755,7.103])
print v.dot(w)


v = Vector([3.183,-7.627])
w = Vector([-2.668,5.319])
print v.angle_with(w)

v = Vector(['7.35','0.221','5.188'])
w = Vector(['2.751','8.259','3.985'])
print v.angle_with(w, in_degrees=True)

# print "\n### quiz 4: Parallel or Orthogonal ###\n"
# print "first pair..."
# v = Vector([-7.579, -7.88])
# w = Vector([22.737, 23.64])
# print 'is parallel:', v.is_parallel_to(w)
# print 'is orthogonal', v.is_orthogonal_to(w)

# print "sec?al', v.is_orthogonal_to(w)??

# print "second pair..."
# v = Vector(['-2.029', '9.97', '4.172'])
# w = Vector(['-9.231', '-6.639', '-7.245'])
# print 'is parallel:', v.is_parallel_to(w)
# print 'is orthogonal', v.is_orthogonal_to(w)
