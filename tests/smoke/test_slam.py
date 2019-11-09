from misty_client.navigation.slam import SLAM

import json
import time

nav = SLAM("10.10.0.7")
nav.start_mapping()

time.sleep(5)

nav.stop_mapping()
x = nav.get_map()
z = json.loads(x.content)["result"]

grid = z["grid"]


def get_coord(grid):
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            print("LOOKING AT GRID: {}, {}".format(x, y))
            if grid[x][y] == 2:
                print("COORDINATES ARE: {}, {}".format(x,y))
                return x,y

a,b = get_coord(grid)

path = nav.get_slampath(a,b)
import pdb; pdb.set_trace()
z = json.loads(path.content)["result"]

#nav.follow_path(path)
