"""
Python Data Structures - A Game-Based Approach
DFS maze solver.
Robin Andrews - https://compucademy.net/
The stack contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
"""

from helpers import get_path, offsets, is_legal_pos, read_maze
from stack import Stack

# depth first search algorithm based on the stack data structure

def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    predecessors = {start: None}
    while not stack.is_empty():
        current = stack.pop()
        if current == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            [row_offset, col_offset] = offsets[direction]
            next = (current[0] + row_offset, current[1] + col_offset)
            if is_legal_pos(maze, next) and next not in predecessors:
                stack.push(next)
                predecessors[next] = current
    return None


if __name__ == "__main__":
    #Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)

    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    print("Test 1 passed!")

    #Test 2
    maze = read_maze("mazes/mini_maze_dfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
    print("Test 2 passed!")

    # Test 3
    maze = read_maze("mazes/mini_maze_dfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = dfs(maze, start_pos, goal_pos)
    print(result)
    assert result is None
    print("Test 3 passed!")
