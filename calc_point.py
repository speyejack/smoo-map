import numpy as np

pix_adjust_off = np.array([2048, 0])
pix_adjust_mult = np.array([-1, 1])

game_pts = np.array() # Array of x/y points from measured in game
map_pts = np.array() # Array of x/y points using pixels of the map (origin = top left)

def get_a_matrix(pts):
    out = np.array([], dtype=pts.dtype)
    for i in range(pts.shape[0]):
        out = np.append(out,pts[i,:])
        out = np.append(out,[1,0,0,0,0,0,0])
        out = np.append(out,pts[i,:])
        out = np.append(out,[1])

    return out.reshape((-1, 6))

def calc_transform(game_pts, map_pts, ):
    a = get_a_matrix(game_pts)
    b = map_pts.reshape((-1,1))
    lst_sq = np.linalg.lstsq(a,b, rcond=None)
    x = np.append(lst_sq[0], [0,0,1]).reshape((3,3))
    return x

def run_numbers(in_pts, trans_matrix):
    in_pts = np.concatenate([in_pts,np.ones(in_pts.shape[0],dtype=in_pts.dtype).reshape((-1,1))],axis=-1)
    out_pts = x.dot(in_pts.T).astype(np.int32).T
    out_pts = out_pts[:,0:2]
    return out_pts

def fix_pix_points(map_pts):
    return map_pts * pix_adjust_mult + pix_adjust_off


map_pts = fix_pix_points(map_pts)
x = calc_transform(game_pts,map_pts)
outs = run_numbers(game_pts,x)
breakpoint()

print("Matrix")
print(x)
print("Test points")
print(game_pts)
print("=>")
print(outs)
print("==")
print(map_pts)
# y = mx + b

# X POINTS
# -33419 -> (2048-1518 ) -> 530: oasis
# 13238 -> (2048-416 ) -> 1632: maze
# 8697  -> (2048-530 ) -> 1508: pillar

# Y POINTS
# 36098 -> 1840 : oasis
# -35274 -> 196 : maze
# -4417-> 952 : pillar
