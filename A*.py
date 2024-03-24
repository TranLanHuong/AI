import heapq

# Định nghĩa lớp Node
class Node:
    def __init__(self, x, y, g, h, parent=None):
        self.x = x  # Tọa độ x
        self.y = y  # Tọa độ y
        self.g = g  # Chi phí thực hiện từ nút xuất phát đến nút hiện tại
        self.h = h  # Ước lượng chi phí từ nút hiện tại đến nút đích
        self.parent = parent  # Nút cha

    def f(self):
        return self.g + self.h

# Hàm tính khoảng cách Manhattan giữa hai điểm
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Hàm A*
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

# Lưới mẫu
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Điểm xuất phát và điểm đích
start = Node(0, 0, 0, 0)
goal = Node(4, 4, 0, 0)

# Tìm đường đi bằng thuật toán A*
path = astar(grid, start, goal)
print("Đường đi tìm được:", path)
