
import numpy as np
import matplotlib.pyplot as plt
import random

def load_maze(path='maze.png'):
    img = plt.imread(path)
    gray = img.mean(axis=2)
    return (gray > 0.5).astype(int)  # 1 => path, 0 => wall

def solve_backtracking(maze):
    rows, cols = maze.shape
    start = (0, np.where(maze[0] == 1)[0][0])
    end = (rows - 1, np.where(maze[-1] == 1)[0][0])
    visited = set()
    stack = [(start, [start])]  # (current_position, path_so_far)

    while stack:
        (r, c), path = stack.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))

        if (r, c) == end:
            return visited, path

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr, nc] == 1:
                stack.append(((nr, nc), path + [(nr, nc)]))

    return visited, []  

def solve_las_vegas(maze, max_steps=1000000):
    rows, cols = maze.shape
    start = (0, np.where(maze[0] == 1)[0][0])
    end = (rows - 1, np.where(maze[-1] == 1)[0][0])
    pos = start
    visited = {pos}
    path = [pos]

    for step in range(max_steps):
        r, c = pos
        moves = [(r + dr, c + dc) for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]
                 if 0 <= r + dr < rows and 0 <= c + dc < cols and maze[r + dr, c + dc] == 1 and (r + dr, c + dc) not in visited]
        if not moves:
            break
        pos = random.choice(moves)
        visited.add(pos)
        path.append(pos)
        if pos == end:
            return True, visited, path

    return False, visited, path

if __name__=='__main__':
    maze=load_maze('maze.png')
    choice=input('Choose approach (B for Backtracking, L for LasVegas): ').strip().upper()
    if choice=='B':
        visited,path=solve_backtracking(maze)
        print(f'Backtracking visited {len(visited)} squares. Path length={len(path)}')
    else:
        success,visited,path=solve_las_vegas(maze)
        print(f'Las Vegas success={success}. Visited {len(visited)} squares.')
    
    plt.figure(figsize=(10, 10))
    plt.imshow(maze, cmap='gray')

    # Plot visited 
    ys, xs = zip(*visited)
    plt.scatter(xs, ys, s=5, color='deepskyblue', label='Visited')

    # Plot path (even though partial)
    if path:
        ys2, xs2 = zip(*path)
        plt.plot(xs2, ys2, 'r-', linewidth=2, label='Path (even if failed)')

    if choice == 'L':
        if success:
            plt.title("Las Vegas Maze Success")
        else:
            plt.title("Las Vegas Maze Failed")
    elif choice == 'B':
        plt.title("Backtrack")
    plt.legend()
    plt.axis('off')
    plt.tight_layout()
    plt.show()