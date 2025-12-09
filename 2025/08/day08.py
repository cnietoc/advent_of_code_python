import os

from dotenv import load_dotenv

from utils.aoc_utils import AOCDay, Input


class Day08(AOCDay):
    expected_example_part1_result = 40
    expected_example_part2_result = 25272

    def part1(self, data: Input) -> int:
        points: list[Point3D] = [Point3D(*map(int, line.split(","))) for line in data.lines]
        distance_map = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):  # Solo j > i
                distance = points[i].distance_to(points[j])
                if distance not in distance_map:
                    distance_map[distance] = []
                distance_map[distance].append((i, j))

        distances_sorted = sorted(distance_map.keys())

        connections_made = Connections(1000 if len(points) != 20 else 10, points)

        for distance in distances_sorted:
            for point_pair in distance_map[distance]:
                if not connections_made.has_more_connections():
                    break
                point1_index, point2_index = point_pair
                point1 = points[point1_index]
                point2 = points[point2_index]
                connections_made.connect(point1, point2)

        sorted_by_size_sets = sorted(connections_made.circuits, key=lambda s: len(s), reverse=True)
        multiplication_of_top3 = 1
        for s in sorted_by_size_sets[:3]:
            multiplication_of_top3 *= len(s)

        return multiplication_of_top3

    def part2(self, data: Input) -> int:
        points: list[Point3D] = [Point3D(*map(int, line.split(","))) for line in data.lines]
        distance_map = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):  # Solo j > i
                distance = points[i].distance_to(points[j])
                if distance not in distance_map:
                    distance_map[distance] = []
                distance_map[distance].append((i, j))

        distances_sorted = sorted(distance_map.keys())

        connections_made = AllConnections(points)

        for distance in distances_sorted:
            for point_pair in distance_map[distance]:
                if len(connections_made.circuits) == 1:
                    break
                point1_index, point2_index = point_pair
                point1 = points[point1_index]
                point2 = points[point2_index]
                connections_made.connect(point1, point2)

        point1, point2 = connections_made.last_connection

        return point1.x * point2.x


class Point3D:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other: 'Point3D') -> float:
        return float(((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5)

    def __repr__(self) -> str:
        return f"[{self.x}, {self.y}, {self.z}]"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point3D):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))


class Circuit:
    def __init__(self, points: set[Point3D]):
        self.points = points

    def size(self) -> int:
        return len(self.points)

    def distance_to(self, other: 'Circuit') -> float:
        min_distance = float('inf')
        for point1 in self.points:
            for point2 in other.points:
                distance = point1.distance_to(point2)
                if distance < min_distance:
                    min_distance = distance
        return min_distance


class Connections:
    def __init__(self, max_connections: int, points: list[Point3D]):
        self.circuits: list[set[Point3D]] = []
        for point in points:
            self.circuits.append({point})
        self.connections = 0
        self.max_connections = max_connections

    def has_more_connections(self) -> bool:
        return self.connections < self.max_connections

    def connect(self, point1: Point3D, point2: Point3D):
        for connected_set in self.circuits:
            if point1 in connected_set:
                if point2 in connected_set:
                    self.connections += 1
                    return
                for other_set_index, other_set in enumerate(self.circuits):
                    if point2 in other_set:
                        connected_set.update(other_set)
                        del self.circuits[other_set_index]
                        self.connections += 1
                        return


class AllConnections:
    def __init__(self, points: list[Point3D]):
        self.circuits: list[set[Point3D]] = []
        for point in points:
            self.circuits.append({point})
        self.connections = 0
        self.last_connection = []

    def connect(self, point1: Point3D, point2: Point3D):
        for connected_set in self.circuits:
            if point1 in connected_set:
                if point2 in connected_set:
                    self.connections += 1
                    return
                for other_set_index, other_set in enumerate(self.circuits):
                    if point2 in other_set:
                        connected_set.update(other_set)
                        self.last_connection = [point1, point2]
                        del self.circuits[other_set_index]
                        self.connections += 1
                        return


if __name__ == "__main__":
    load_dotenv()
    year = os.getenv('AOC_YEAR')
    session_token = os.getenv('AOC_SESSION_COOKIE')
    day_number = "08"
    day = Day08(year, day_number, session_token)
    day.run()
