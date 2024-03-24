import heapq

class Node:
    def __init__(self, x, y, g, h, parent=None):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.parent = parent

    def f(self):
        return self.g + self.h

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def astar(grid, start, goal):
    open_list = []
    closed_list = set()

    heapq.heappush(open_list, (start.f(), start))
    
    while open_list:
        _, current_node = heapq.heappop(open_list)
        
        if (current_node.x, current_node.y) == (goal.x, goal.y):
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]
        
        closed_list.add((current_node.x, current_node.y))
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = current_node.x + dx, current_node.y + dy
            if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == 0 and (next_x, next_y) not in closed_list:
                next_g = current_node.g + 1
                next_h = manhattan_distance(next_x, next_y, goal.x, goal.y)
                next_node = Node(next_x, next_y, next_g, next_h, current_node)
                heapq.heappush(open_list, (next_node.f(), next_node))
    
    return None

def read_input(file_name):
    with open(file_name, 'input.txt') as file:
        rows, cols = map(int, file.readline().split())
        grid = []
        for _ in range(rows):
            row = list(map(int, file.readline().split()))
            grid.append(row)
        start_x, start_y = map(int, file.readline().split())
        goal_x, goal_y = map(int, file.readline().split())
    return grid, Node(start_x, start_y, 0, 0), Node(goal_x, goal_y, 0, 0)

def write_output(path, file_name):
    with open(file_name, 'w') as file:
        if path:
            for x, y in path:
                file.write(f"{x} {y}\n")
            print("Kết quả đã được lưu vào", file_name)
        else:
            file.write("Không tìm thấy đường đi.")

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    grid, start, goal = read_input('input.txt')
    path = astar(grid, start, goal)
    write_output(path, output_file)

if __name__ == "__main__":
    main()