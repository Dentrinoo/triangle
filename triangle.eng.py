from math import sqrt
from dataclasses import dataclass


@dataclass
class Point:
    """Represents a point in 2D space."""
    x: int
    y: int


class Triangle:
    """Represents a triangle defined by three vertices."""

    def __init__(self, vertex_a: Point, vertex_b: Point, vertex_c: Point):
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b
        self.vertex_c = vertex_c
        self.side_ab = self.calculate_distance(self.vertex_a, self.vertex_b)
        self.side_ac = self.calculate_distance(self.vertex_a, self.vertex_c)
        self.side_bc = self.calculate_distance(self.vertex_b, self.vertex_c)
        self.semi_perimeter = (self.side_ab + self.side_ac + self.side_bc) / 2
        self.area = self.calculate_area()
        self.shortest_side = self.find_shortest_side()
        self.height = self.calculate_height()

    @staticmethod
    def calculate_distance(p1: Point, p2: Point) -> float:
        """Calculates the Euclidean distance between two points."""
        return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def calculate_area(self) -> float:
        """Calculates the area of the triangle using Heron's formula."""
        p = self.semi_perimeter
        return sqrt(p * (p - self.side_ab) * (p - self.side_ac) * (p - self.side_bc))

    def find_shortest_side(self) -> float:
        """Finds the shortest side of the triangle."""
        return min(self.side_ab, self.side_ac, self.side_bc)

    def calculate_height(self) -> float:
        """Calculates the height from the smallest angle."""
        return (2 * self.area) / self.shortest_side

    def are_collinear(self) -> bool:
        """Checks if the three vertices are collinear."""
        # Using the area formula to check collinearity
        return self.area == 0

    def are_vertices_coincident(self) -> bool:
        """Checks if all three vertices coincide."""
        return (self.vertex_a.x == self.vertex_b.x == self.vertex_c.x and
                self.vertex_a.y == self.vertex_b.y == self.vertex_c.y)

    def position_of_point(self, point_o: Point) -> str:
        """
        Determines the position of point O relative to the triangle:
        - On a vertex
        - On a side
        - Inside the triangle
        - Outside the triangle
        """
        # Calculate determinants
        det_ab = (self.vertex_a.x - point_o.x) * (self.vertex_b.y - self.vertex_a.y) - \
                 (self.vertex_b.x - self.vertex_a.x) * (self.vertex_a.y - point_o.y)
        det_bc = (self.vertex_b.x - point_o.x) * (self.vertex_c.y - self.vertex_b.y) - \
                 (self.vertex_c.x - self.vertex_b.x) * (self.vertex_b.y - point_o.y)
        det_ac = (self.vertex_c.x - point_o.x) * (self.vertex_a.y - self.vertex_c.y) - \
                 (self.vertex_a.x - self.vertex_c.x) * (self.vertex_c.y - point_o.y)

        # Check if point O coincides with any vertex
        if (point_o.x == self.vertex_a.x and point_o.y == self.vertex_a.y) or \
           (point_o.x == self.vertex_b.x and point_o.y == self.vertex_b.y) or \
           (point_o.x == self.vertex_c.x and point_o.y == self.vertex_c.y):
            return "Point O coincides with one of the vertices of triangle ABC."

        # Check if point O lies on any side of the triangle
        if det_ab == 0 or det_bc == 0 or det_ac == 0:
            return "Point O lies on one of the sides of triangle ABC."

        # Check if point O is inside the triangle
        if (det_ab < 0 and det_bc < 0 and det_ac < 0) or (det_ab > 0 and det_bc > 0 and det_ac > 0):
            return "Point O lies inside triangle ABC."

        # Otherwise, point O is outside the triangle
        return "Point O lies outside triangle ABC."


def get_point_input(label: str) -> Point:
    """Prompts the user to input the coordinates of a point."""
    x = int(input(f'Enter the X-coordinate of point {label}: '))
    y = int(input(f'Enter the Y-coordinate of point {label}: '))
    return Point(x, y)


def main() -> None:
    """Main function to execute the triangle analysis."""
    print("Input the coordinates of the vertices of triangle ABC.")
    vertex_a = get_point_input('A')
    vertex_b = get_point_input('B')
    vertex_c = get_point_input('C')

    print("\nInput the coordinates of point O.")
    point_o = get_point_input('O')

    triangle = Triangle(vertex_a, vertex_b, vertex_c)

    # Handle special cases
    if triangle.are_collinear():
        print('\nInvalid input: All points lie on a single line.')
    elif triangle.are_vertices_coincident():
        print('\nInvalid input: All three vertices coincide.')
    else:
        # Determine the position of point O relative to the triangle
        position = triangle.position_of_point(point_o)
        print(f'\n{position}')

        # Output the height and side lengths of the triangle
        print(f'\nHeight from the smallest angle of triangle ABC: {triangle.height:.3f}')
        print(f'Length of side AB: {triangle.side_ab:.3f}')
        print(f'Length of side BC: {triangle.side_bc:.3f}')
        print(f'Length of side AC: {triangle.side_ac:.3f}')

    input('\nPress Enter to exit...')


if __name__ == "__main__":
    main()
