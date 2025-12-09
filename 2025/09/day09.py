import os
from functools import lru_cache

import matplotlib.pyplot as plt
from dotenv import load_dotenv

from utils.aoc_utils import AOCDay, Input


def print_tiles(tiles, first_tile, second_tile):
    max_x = max(tile[0] for tile in tiles)
    max_y = max(tile[1] for tile in tiles)

    grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for i in range(min(first_tile[0], second_tile[0]), max(first_tile[0], second_tile[0]) + 1):
        for j in range(min(first_tile[1], second_tile[1]), max(first_tile[1], second_tile[1]) + 1):
            grid[j][i] = 'O'

    for tile in tiles:
        grid[tile[1]][tile[0]] = '#'

    grid[first_tile[1]][first_tile[0]] = 'A'
    grid[second_tile[1]][second_tile[0]] = 'B'

    for row in grid:
        print(''.join(row))
    print()


def print_visualization(tiles, first_tile, second_tile):
    x_coords, y_coords = zip(*tiles)

    # Cerrar el polígono
    x_coords += (x_coords[0],)
    y_coords += (y_coords[0],)

    plt.figure(figsize=(10, 10))
    plt.plot(x_coords, y_coords, marker='o')
    plt.title('Polígono')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    plt.plot([first_tile[0], second_tile[0], second_tile[0], first_tile[0], first_tile[0]],
             [first_tile[1], first_tile[1], second_tile[1], second_tile[1], first_tile[1]],
             'r--', label='Área candidata')

    plt.show()


def point_on_segment(px, py, x1, y1, x2, y2):
    cross = (px - x1) * (y2 - y1) - (py - y1) * (x2 - x1)
    if abs(cross) > 1e-9:
        return False

    dot = (px - x1) * (px - x2) + (py - y1) * (py - y2)
    return dot <= 0


def segments_intersect_orthogonal(line1: tuple[tuple[int, int], tuple[int, int]],
                                  line2: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    l1a, l1b = line1
    l2a, l2b = line2
    seg1_horizontal = l1a[1] == l1b[1]
    seg2_horizontal = l2a[1] == l2b[1]

    if seg1_horizontal == seg2_horizontal:
        return False

    if seg1_horizontal:
        x_min1, x_max1 = min(l1a[0], l1b[0]), max(l1a[0], l1b[0])
        y_min2, y_max2 = min(l2a[1], l2b[1]), max(l2a[1], l2b[1])
        return x_min1 < l2a[0] < x_max1 and y_min2 < l1a[1] < y_max2
    else:
        y_min1, y_max1 = min(l1a[1], l1b[1]), max(l1a[1], l1b[1])
        x_min2, x_max2 = min(l2a[0], l2b[0]), max(l2a[0], l2b[0])
        return x_min2 < l1a[0] < x_max2 and y_min1 < l2a[1] < y_max1


class Day09(AOCDay):
    expected_example_part1_result = 50
    expected_example_part2_result = 24

    def part1(self, data: Input) -> int:
        tiles: list[tuple[int, int]] = [tuple(map(int, line.split(","))) for line in data.lines]
        max_area = 0
        for first_tile_index, first_tile in enumerate(tiles):
            for second_tile_index in range(first_tile_index + 1, len(tiles)):
                second_tile = tiles[second_tile_index]
                if first_tile == second_tile:
                    continue
                area_size = (max(first_tile[0], second_tile[0]) - min(first_tile[0], second_tile[0]) + 1) * \
                            (max(first_tile[1], second_tile[1]) - min(first_tile[1], second_tile[1]) + 1)
                if area_size > max_area:
                    max_area = area_size
        return max_area

    def part2(self, data: Input) -> int:
        tiles: list[tuple[int, int]] = [tuple(map(int, line.split(","))) for line in data.lines]

        @lru_cache(maxsize=None)
        def point_in_figure(point: tuple[int, int]):
            x, y = point
            inside = False
            n = len(tiles)

            for tile_index in range(n):
                x1, y1 = tiles[tile_index]
                x2, y2 = tiles[(tile_index + 1) % n]

                if point_on_segment(x, y, x1, y1, x2, y2):
                    return True

                intersects = ((y1 > y) != (y2 > y)) and \
                             (x < (x2 - x1) * (y - y1) / (y2 - y1 + 1e-12) + x1)

                if intersects:
                    inside = not inside

            return inside

        segments: list[tuple[tuple[int, int], tuple[int, int]]] = []
        for i in range(0, len(tiles)):
            if i > 0:
                first_point = tiles[i - 1]
            else:
                first_point = tiles[-1]
            second_point = tiles[i]
            segments.append((first_point, second_point))

        max_area = 0
        for first_tile_index, first_tile in enumerate(tiles):
            for second_tile_index in range(first_tile_index + 1, len(tiles)):
                second_tile = tiles[second_tile_index]
                if first_tile == second_tile:
                    continue
                intersect = False
                min_x = min(first_tile[0], second_tile[0])
                max_x = max(first_tile[0], second_tile[0])
                min_y = min(first_tile[1], second_tile[1])
                max_y = max(first_tile[1], second_tile[1])
                first_line = ((min_x, min_y), (max_x, min_y))
                second_line = ((max_x, min_y), (max_x, max_y))
                third_line = ((max_x, max_y), (min_x, max_y))
                fourth_line = ((min_x, max_y), (min_x, min_y))
                if point_in_figure((min_x, min_y)) and \
                        point_in_figure((max_x, min_y)) and \
                        point_in_figure((max_x, max_y)) and \
                        point_in_figure((min_x, max_y)):

                    for segment in segments:
                        if segments_intersect_orthogonal(first_line, segment) or \
                                segments_intersect_orthogonal(second_line, segment) or \
                                segments_intersect_orthogonal(third_line, segment) or \
                                segments_intersect_orthogonal(fourth_line, segment):
                            # print(f"Segments intersect between tiles {first_tile} and {second_tile} with segment {segment}")
                            intersect = True
                            break

                    if not intersect:
                        area_size = (max(first_tile[0], second_tile[0]) - min(first_tile[0], second_tile[0]) + 1) * \
                                    (max(first_tile[1], second_tile[1]) - min(first_tile[1], second_tile[1]) + 1)
                        if area_size > max_area:
                            # print_visualization(tiles, first_tile, second_tile)
                            max_area = area_size
                            break
        return max_area


if __name__ == "__main__":
    load_dotenv()
    year = os.getenv('AOC_YEAR')
    session_token = os.getenv('AOC_SESSION_COOKIE')
    day_number = "09"
    day = Day09(year, day_number, session_token)
    day.run()
