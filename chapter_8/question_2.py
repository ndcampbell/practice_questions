# Robot in a girid, RxC. Can only move down and right but some cells are off limits. Find path for robot from top left to bottom right

def robot_grid(grid, cur, offlimits):
    print(cur)
    if grid == cur:
        return cur
    if cur in offlimits:
        return cu
    if cur[0] == grid[0]:
        return cur
    elif cur[1] == grid[1]:
        return cur
    #goright:
    cur = robot_grid(grid, (cur[0]+1, cur[1]), offlimits)
    cur = robot_grid(grid, (cur[0], cur[1]+1), offlimits)
    return cur


if __name__ == "__main__":
    grid = (3, 3)
    cur = (0, 0)
    offlimits = [(3,0)]
    robot_grid(grid, cur, offlimits)

