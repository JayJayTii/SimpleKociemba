# Simple Kociemba's Algorithm Implementation
import time

#================== CUBE ===================
#Edge order: UR,   UF,   UL,   UB,   DR ,  DF,   DL,   DB,   FR,   FL,   BL,   BR
#Corner order: URF,  UFL,  ULB,  UBR,  DFR,  DLF,  DBL,  DRB
turns = [
	#Edge permutation                         Edge Orientation                       Corner Permutation         Corner Orientation
	[3, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    3, 0, 1, 2, 4, 5, 6, 7,    0, 0, 0, 0, 0, 0, 0, 0],   #U	0
	[2, 3, 0, 1, 4, 5, 6, 7, 8, 9, 10, 11,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    2, 3, 0, 1, 4, 5, 6, 7,    0, 0, 0, 0, 0, 0, 0, 0],   #U2	1
	[1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    1, 2, 3, 0, 4, 5, 6, 7,    0, 0, 0, 0, 0, 0, 0, 0],   #U'	2
	[8, 1, 2, 3, 11, 5, 6, 7, 4, 9, 10, 0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    4, 1, 2, 0, 7, 5, 6, 3,    2, 0, 0, 1, 1, 0, 0, 2],   #R 	3
	[4, 1, 2, 3, 0, 5, 6, 7, 11, 9, 10, 8,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    7, 1, 2, 4, 3, 5, 6, 0,    0, 0, 0, 0, 0, 0, 0, 0],   #R2	4
	[11, 1, 2, 3, 8, 5, 6, 7, 0, 9, 10, 4,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    3, 1, 2, 7, 0, 5, 6, 4,    2, 0, 0, 1, 1, 0, 0, 2],   #R'	5
	[0, 9, 2, 3, 4, 8, 6, 7, 1, 5, 10, 11,    0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0,    1, 5, 2, 3, 0, 4, 6, 7,    1, 2, 0, 0, 2, 1, 0, 0],   #F 	6
	[0, 5, 2, 3, 4, 1, 6, 7, 9, 8, 10, 11,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    5, 4, 2, 3, 1, 0, 6, 7,    0, 0, 0, 0, 0, 0, 0, 0],   #F2	7
	[0, 8, 2, 3, 4, 9, 6, 7, 5, 1, 10, 11,    0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0,    4, 0, 2, 3, 5, 1, 6, 7,    1, 2, 0, 0, 2, 1, 0, 0],   #F'	8
	[0, 1, 2, 3, 5, 6, 7, 4, 8, 9, 10, 11,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0, 1, 2, 3, 5, 6, 7, 4,    0, 0, 0, 0, 0, 0, 0, 0],   #D	9
	[0, 1, 2, 3, 6, 7, 4, 5, 8, 9, 10, 11,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0, 1, 2, 3, 6, 7, 4, 5,    0, 0, 0, 0, 0, 0, 0, 0],   #D2	10
	[0, 1, 2, 3, 7, 4, 5, 6, 8, 9, 10, 11,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0, 1, 2, 3, 7, 4, 5, 6,    0, 0, 0, 0, 0, 0, 0, 0],   #D'	11
	[0, 1, 10, 3, 4, 5, 9, 7, 8, 2, 6, 11,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0, 2, 6, 3, 4, 1, 5, 7,    0, 1, 2, 0, 0, 2, 1, 0],   #L	12
	[0, 1, 6, 3, 4, 5, 2, 7, 8, 10, 9, 11,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0, 6, 5, 3, 4, 2, 1, 7,    0, 0, 0, 0, 0, 0, 0, 0],   #L2	13
	[0, 1, 9, 3, 4, 5, 10, 7, 8, 6, 2, 11,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0, 5, 1, 3, 4, 6, 2, 7,    0, 1, 2, 0, 0, 2, 1, 0],   #L'	14
	[0, 1, 2, 11, 4, 5, 6, 10, 8, 9, 3, 7,    0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1,    0, 1, 3, 7, 4, 5, 2, 6,    0, 0, 1, 2, 0, 0, 2, 1],   #B	15
	[0, 1, 2, 7, 4, 5, 6, 3, 8, 9, 11, 10,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0, 1, 7, 6, 4, 5, 3, 2,    0, 0, 0, 0, 0, 0, 0, 0],   #B2	16
	[0, 1, 2, 10, 4, 5, 6, 11, 8, 9, 7, 3,    0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1,    0, 1, 6, 2, 4, 5, 7, 3,    0, 0, 1, 2, 0, 0, 2, 1],   #B'	17
]

solved_cube = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0, 1, 2, 3, 4, 5, 6, 7,    0, 0, 0, 0, 0, 0, 0, 0]

def cube_mult(a, b):
	result = [0 for i in range(40)]
	for i in range(12):
		result[i] = a[b[i]]
		result[12 + i] = (b[12 + i] + a[12 + b[i]]) % 2
		
	for i in range(8):
		result[24 + i] = a[24 + b[24 + i]]
		result[32 + i] = (a[32 + b[24 + i]] + b[32 + i]) % 3

	return result

def cube_mult_edges(a, b):
	result = [0 for i in range(40)]
	for i in range(12):
		result[i] = a[b[i]]
		result[12 + i] = (b[12 + i] + a[12 + b[i]]) % 2

	return result

def cube_mult_corns(a, b):
	result = [0 for i in range(40)]
	for i in range(8):
		result[24 + i] = a[24 + b[24 + i]]
		result[32 + i] = (a[32 + b[24 + i]] + b[32 + i]) % 3

	return result

def cube_print(cube):
	out = "----\n"

	for i in range(40):
		out += str(cube[i]).zfill(2) + " "

		if (i == 11 or i == 31): out += "    "
		elif i == 23: out += "\n"

	out += "\n----"
	print(out)

def cube_equals(a, b):
	for i in range(40):
		if a[i] != b[i]: return False

	return True


#================== NOTATION ===================
def scramble_to_cube(scramble_str):
	cube = solved_cube.copy()
	index = 0

	while index < len(scramble_str):
		turn = -1

		match scramble_str[index]:
			case 'U': turn = 0
			case 'R': turn = 3
			case 'F': turn = 6
			case 'D': turn = 9
			case 'L': turn = 12
			case 'B': turn = 15
			case _:
				index += 1
				continue
			
		if index + 1 != len(scramble_str):
			if scramble_str[index + 1] == '\'':
				turn += 2
				index += 1
			elif scramble_str[index +  1] == '2':
				turn += 1
				index += 1

		cube = cube_mult(cube, turns[turn])
		index += 1
	return cube

def turns_to_string(sequence):
	result = ""

	for i in range(len(sequence)):
		match sequence[i] // 3:
			case 0: result += "U"
			case 1: result += "R"
			case 2: result += "F"
			case 3: result += "D"
			case 4: result += "L"
			case 5: result += "B"
		match sequence[i] % 3:
			case 1: result += "2"
			case 2: result += "\'"

		result += " "

	return result

def cancel_turns(sequence):
	result = sequence.copy()
	collapsed = True
	while collapsed:
		collapsed = False
		i = -1
		while i < len(result) - 2:
			i += 1
			# Put parallel sides in ascending order of face index, so that U D U -> U U D -> handled later
			if result[i]//3 + 3 == result[i + 1]//3: 
				result[i], result[i+1] = result[i+1], result[i]
				collapsed = True
				continue

			# Combine consecutive turns on the same face
			if result[i]//3 == result[i + 1]//3:
				face = result[i]//3
				new_turn_size = ((result[i] % 3) + (result[i + 1] % 3) + 1) % 4
				del result[i]
				if new_turn_size == 3: del result[i] # If the 2 turns cancelled out, delete both turns
				else: result[i] = face * 3 + new_turn_size # Replace the 2 turns with one turn

				collapsed = True
				continue
	return result
	

#================== COORDINATES ===================

#=== Phase One Coordinates ===
#EO is edge orientation: 0 -> 2047 (2^11 - 1)
def get_eo(cube):
	eo = 0
	for i in range(11):
		eo = 2 * eo + cube[12 + i]
	return eo

def set_eo(cube, eo):
	total = 0
	for i in range(11):
		cube[22 - i] = eo % 2
		total += eo % 2
		eo = eo // 2
	cube[23] = total % 2

#CO is corner orientation: 0 -> 2186 (3^7 - 1)
def get_co(cube):
	co = 0
	for i in range(7):
		co = 3 * co + cube[32 + i]
	return co

def set_co(cube, co):
	total = 0
	for i in range(7):
		cube[38 - i] = co % 3
		total += co % 3
		co = co // 3
	cube[39] = (-total) % 3
	
# Choose function look-up table up to n = 12
nCk = [1,0,0,0,0,0,0,0,0,0,0,0, 1,1,0,0,0,0,0,0,0,0,0,0, 1,2,1,0,0,0,0,0,0,0,0,0, 1,3,3,1,0,0,0,0,0,0,0,0, 1,4,6,4,1,0,0,0,0,0,0,0, 1,5,10,10,5,1,0,0,0,0,0,0, 1,6,15,20,15,6,1,0,0,0,0,0, 1,7,21,35,35,21,7,1,0,0,0,0, 1,8,28,56,70,56,28,8,1,0,0,0, 1,9,36,84,126,126,84,36,9,1,0,0, 1,10,45,120,210,252,210,120,45,10,1,0, 1,11,55,165,330,462,462,330,165,55,11,1]

#UDS is position of UD-Slice Edges: 0 -> 494 (12 choose 4 - 1)
#Only ensures UD-Slice Edges get into the UD-Slice, not necessarily permuted
#https://github.com/hkociemba/CubeExplorer/blob/5cfee2297736ab56e8c615d4061cd433a56746d0/CubiCube.pas#L486
def get_uds(cube):
	uds = 0
	k = 3
	n = 11
	while k >= 0:
		if cube[n] >= 8: k -= 1 #UD-Slice edge
		else: uds += nCk[n * 12 + k]
		n -= 1
	return uds

#https://github.com/hkociemba/CubeExplorer/blob/5cfee2297736ab56e8c615d4061cd433a56746d0/CubiCube.pas#L504
def set_uds(cube, uds):
	occupied = [False for i in range(12)]
	n = 11
	k = 3
	while k >= 0:
		v = nCk[n * 12 + k]
		if uds < v:
			k -= 1
			occupied[n] = True
		else: 
			uds -= v

		n -= 1
	UDSliceEdge = 8
	for edge in range(12):
		if occupied[edge]:
			#Swap the current UDSliceEdge with this slot where there should be one
			for i in range(12):
				if cube[i] == UDSliceEdge:
					cube[i] = cube[edge]
					break
			cube[edge] = UDSliceEdge
			UDSliceEdge += 1
			
#=== Phase Two Coordinates ===
#EP8 is the permutation of the 8 white/yellow edges (UR, UF, UL, UB, DR, DF, DL, DB): 0 -> 40319 (8! - 1)
# https://github.com/hkociemba/CubeExplorer/blob/5cfee2297736ab56e8c615d4061cd433a56746d0/CubiCube.pas#L743
def get_ep8(cube):
	ep8 = 0
	for i in reversed(range(1,8)):
		s = 0
		for j in reversed(range(0, i)):
			if (cube[j] > cube[i]): s += 1
		ep8 = (ep8 + s) * i
	return ep8

def set_ep8(cube, ep8):
	used = [False for i in range(8)]
	order = [-1 for i in range(8)]
	for i in range(8):
		used[i] = False
		order[i] = ep8 % (i + 1)
		ep8 = ep8 // (i + 1)

	for i in reversed(range(8)):
		k = 7
		while used[k]: k -= 1
		while order[i] > 0:
			order[i] -= 1
			k -= 1
			while used[k]: k -= 1
		cube[i] = k
		used[k] = True

#CP is corner permutation: 0 -> 40319 (8! - 1)
def get_cp(cube):
	cp = 0
	for i in reversed(range(1,8)):
		s = 0
		for j in reversed(range(0, i)):
			if (cube[24 + j] > cube[24 + i]): s += 1

		cp = (cp + s) * i
	return cp

def set_cp(cube, cp):
	used = [False for i in range(8)]
	order = [-1 for i in range(8)]
	for i in range(8):
		used[i] = False
		order[i] = cp % (i + 1)
		cp = cp // (i + 1)
		
	for i in reversed(range(8)):
		k = 7
		while used[k]:
			k -= 1

		while order[i] > 0:
			order[i] -= 1
			k -= 1
			while used[k]:
				k -= 1
		cube[24 + i] = k
		used[k] = True

#EP4 is the permutation of the 4 UD-Slice Edges (FR, FL, BL, BR): 0 -> 23 (4! - 1)
def get_ep4(cube):
	ep4 = 0
	for i in reversed(range(1,4)):
		s = 0
		for j in reversed(range(0, i)):
			if (cube[8 + j] > cube[8 + i]): s += 1

		ep4 = (ep4 + s) * i
	return ep4

def set_ep4(cube, ep4):
	used = [False for i in range(4)]
	order = [-1 for i in range(4)]
	for i in range(4):
		used[i] = False
		order[i] = ep4 % (i + 1)
		ep4 = ep4 // (i + 1)

	for i in reversed(range(4)):
		k = 3
		while used[k]: k -= 1

		while order[i] > 0:
			order[i] -= 1
			k -= 1
			while used[k]: k -= 1

		cube[8 + i] = 8 + k
		used[k] = True

		
#================== TABLES ===================
def generate_move_table(coord_count, get_coord, set_coord, allowed_moves, inverted_moves, is_corners):
	#2D array that takes a coordinate and a turn, and says which new coordinate it goes to
	table = [[99999999 for i in range(len(allowed_moves))] for j in range(coord_count)]
	cube = solved_cube.copy()
	cube_copy = solved_cube.copy()
	
	# For every coordinate, do every move and record which coordinate each one went to
	for coord in range(coord_count):
		set_coord(cube, coord)
		cube_copy = cube.copy()
		for turn_index in range(len(allowed_moves)):
			if table[coord][turn_index] != 99999999: continue

			if is_corners:
				cube = cube_mult_corns(cube, turns[allowed_moves[turn_index]])
			else:
				cube = cube_mult_edges(cube, turns[allowed_moves[turn_index]])

			new_coord = get_coord(cube)
			table[coord][turn_index] = new_coord
			# Doing the opposite move to the new coord will lead back to the original coord
			table[new_coord][inverted_moves[turn_index]] = coord

			if turn_index < len(allowed_moves) - 1:
				cube = cube_copy.copy()
				
	return table

def generate_prune_table(coord1_move_table, coord1_count, coord2_move_table, coord2_count, allowed_moves_count):
	#A table which takes 2 coordinates and says the minimum number of turns it will take to get them both solved
	table = [[255 for i in range(coord2_count)] for j in range(coord1_count)]
	table[0][0] = 0
	filled = 1
	
	depth = 0
	filled_per_iteration = 0

	while filled < coord1_count * coord2_count:
		filled_per_iteration = 0

		# Breadth first search ensures optimal turn count
		for c1 in range(coord1_count):
			for c2 in range(coord2_count):
				if(table[c1][c2] != depth):
					continue

				# Do every turn on every pair of coordinates at the current depth
				# If a new pair is not yet filled, then it must be one turn deeper
				for turn_index in range(allowed_moves_count):
					new_c1 = coord1_move_table[c1][turn_index]
					new_c2 = coord2_move_table[c2][turn_index]

					if table[new_c1][new_c2] == 255:
						table[new_c1][new_c2] = depth + 1
						filled_per_iteration += 1

		filled += filled_per_iteration
		if filled_per_iteration == 0:
			break
		
		depth += 1
		
	return table


# Generate look-up tables
p1_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
p1_moves_inverted = [2, 1, 0, 5, 4, 3, 8, 7, 6, 11, 10, 9, 14, 13, 12, 17, 16, 15]
p2_moves = [0, 1, 2, 4, 7, 9, 10, 11, 13, 16]
p2_moves_inverted = [2, 1, 0, 3, 4, 7, 6, 5, 8, 9]

print("Generating tables...")
start = time.time()
eo_move_table = generate_move_table(2048, get_eo, set_eo, p1_moves, p1_moves_inverted, False)
co_move_table = generate_move_table(2187, get_co, set_co, p1_moves, p1_moves_inverted, True)
uds_move_table = generate_move_table(495, get_uds, set_uds, p1_moves, p1_moves_inverted, False)
eo_uds_prune_table = generate_prune_table(eo_move_table, 2048, uds_move_table, 495, len(p1_moves))
co_uds_prune_table = generate_prune_table(co_move_table, 2187, uds_move_table, 495, len(p1_moves))

ep8_move_table = generate_move_table(40320, get_ep8, set_ep8, p2_moves, p2_moves_inverted, False)
cp_move_table = generate_move_table(40320, get_cp, set_cp, p2_moves, p2_moves_inverted, True)
ep4_move_table = generate_move_table(24, get_ep4, set_ep4, p2_moves, p2_moves_inverted, False)
ep8_ep4_prune_table = generate_prune_table(ep8_move_table, 40320, ep4_move_table, 24, len(p2_moves))
cp_ep4_prune_table = generate_prune_table(cp_move_table, 40320, ep4_move_table, 24, len(p2_moves))
end = time.time()
print("Took " + str(round(end-start, 1)) + " seconds")


#================== SOLVER ===================
lowest_pruned = 99999999
threshold = 0
result = [0 for i in range(20)]

# Depth first search of Phase 1 with a threshold
def phase1_dfs(depth, eo, co, uds, last_turn, last_turn_2):
	global lowest_pruned, threshold, result
	
	# Cost of current node
	cost = depth + max(eo_uds_prune_table[eo][uds], co_uds_prune_table[co][uds])
	if cost > threshold:
		lowest_pruned = min(cost, lowest_pruned)
		return -1

	# Do every turn to this node
	for turn_index in range(len(p1_moves)):
		if (last_turn != -1 and ((turn_index//3 == last_turn//3) or (last_turn_2 != -1 and (last_turn//3 + 3 == last_turn_2//3 or last_turn//3 == last_turn_2//3 + 3) and (turn_index//3 == last_turn_2//3)))):
			continue # Avoid turns which cancel out (e.g. U U2 or F' B F2)

		result[depth] = p1_moves[turn_index]
		
		new_eo = eo_move_table[eo][turn_index]
		new_co = co_move_table[co][turn_index]
		new_uds = uds_move_table[uds][turn_index]
		if new_eo == 0 and new_co == 0 and new_uds == 0:
			return 0 # Phase 1 solution found
 
		dfs_result = phase1_dfs(depth+1, new_eo, new_co, new_uds, p1_moves[turn_index], last_turn)
		if dfs_result > -1:
			return dfs_result + 1
		
	# Made it through all child nodes without finding the goal
	return -1

# Depth first search of Phase 2 with a threshold
def phase2_dfs(depth, ep8, cp, ep4, last_turn, last_turn_2):
	global lowest_pruned, threshold, result
	
	# Cost of current node
	cost = depth + max(ep8_ep4_prune_table[ep8][ep4], cp_ep4_prune_table[cp][ep4])
	if cost > threshold:
		lowest_pruned = min(cost, lowest_pruned)
		return -1
	
	for turn_index in range(10):
		if (last_turn != -1 and ((p2_moves[turn_index]//3 == last_turn//3) or (last_turn_2 != -1 and (last_turn//3 + 3 == last_turn_2//3 or last_turn//3 == last_turn_2//3 + 3) and (p2_moves[turn_index]//3 == last_turn_2//3)))):
			continue # Avoid turns which cancel out (e.g. U U2 or F' B F2)

		new_ep8 = ep8_move_table[ep8][turn_index]
		new_cp = cp_move_table[cp][turn_index]
		new_ep4 = ep4_move_table[ep4][turn_index]

		result[depth] = p2_moves[turn_index]
		if new_ep8 == 0 and new_cp == 0 and new_ep4 == 0:
			return 0 # Phase 2 solution found
 
		dfs_result = phase2_dfs(depth+1, new_ep8, new_cp, new_ep4, p2_moves[turn_index], last_turn)
		if dfs_result > -1:
			return dfs_result + 1
	
	return -1 # Made it through all child nodes without finding the goal

# https://www.redblobgames.com/pathfinding/a-star/introduction.html
# https://www.geeksforgeeks.org/artificial-intelligence/iterative-deepening-a-algorithm-ida-artificial-intelligence
def solve(cube):
	global threshold, lowest_pruned
	solution = []
	
	# If Phase 1 is not already solved, run Phase 1 solver
	if get_eo(cube) != 0 or get_co(cube) != 0 or get_uds(cube) != 0:
		dfs_result = -1
		threshold = 0
		while dfs_result == -1:
			lowest_pruned = 99999999
			dfs_result = phase1_dfs(0, get_eo(cube), get_co(cube), get_uds(cube), -1, -1)
			threshold = lowest_pruned

		# Apply Phase 1 solution to cube
		solution = result[:dfs_result+1]
		for i in range(dfs_result + 1):
			cube = cube_mult(cube, turns[solution[i]])

	# If Phase 2 is not already solved, run Phase 2 solver
	if get_ep8(cube) != 0 or get_cp(cube) != 0 or get_ep4(cube) != 0:
		dfs_result = -1
		threshold = 0
		while dfs_result == -1:
			lowest_pruned = 99999999
			dfs_result = phase2_dfs(0, get_ep8(cube), get_cp(cube), get_ep4(cube), -1, -1)
			threshold = lowest_pruned
			
		solution = solution + result[:dfs_result+1]

	return cancel_turns(solution)

# Solve scrambles forever
while True:
	cube = solved_cube.copy()
	print("Enter a scramble: ", end='')
	scramble = input()
	cube = scramble_to_cube(scramble)
	print(turns_to_string(solve(cube)))


