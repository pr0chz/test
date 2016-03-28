import sys,operator

norm = [(0, 1), (1, 0), (0, -1), (-1, 0)]
xnorm = [(0, n[0], n[1]) for n in norm]
ynorm = [(n[0], 0, n[1]) for n in norm]
znorm = [(n[0], n[1], 0) for n in norm]

def normals(vector):
	if vector[0] != 0:
		return xnorm
	elif vector[1] != 0:
		return ynorm
	elif vector[2] != 0:
		return znorm
	else:
		raise Error("Cannot compute on zero vector")
	
def add_vect(p1, p2):
	return tuple(map(sum, zip(p1, p2)))

def dist(d):
	return abs(d[0] - d[1])

def max_dist(p1, p2):
	return max(map(dist, zip(p1, p2)))

def print_output(pset, minpos, maxpos):
	print('Found solution:')
	for z in reversed(range(minpos[2], maxpos[2]+1)):
		for y in range(minpos[1], maxpos[1] + 1):
			for x in range(minpos[0], maxpos[0] + 1):
				sys.stdout.write(str(pset[(x, y, z)]).ljust(3))
			print('')
		print('')

def traverse(index, maxdim, chain, state):
	pos, rdir, ddir, pset, minpos, maxpos = state
	if pos in pset: return

	minpos = tuple(map(min,zip(pos, minpos)))
	maxpos = tuple(map(max,zip(pos, maxpos)))
	if max_dist(minpos, maxpos) > maxdim: return

	pset[pos] = index
	if not chain:
		print_output(pset, minpos, maxpos)
		return #sys.exit(0)

	head, tail = chain[0], chain[1:]
	if head == 'R':
		for n in normals(rdir):
			traverse(index + 1, maxdim, tail, (add_vect(pos, rdir), rdir, n, pset, minpos, maxpos))
	elif head == 'D':
		for n in normals(ddir):
			traverse(index + 1, maxdim, tail, (add_vect(pos, ddir), n, ddir, pset, minpos, maxpos))
	del pset[pos]
	return


chain = sys.stdin.readline().strip()
traverse(0, 2, chain, ((0, 0, 0), (1, 0, 0), (0, 1, 0), {}, (0, 0, 0), (0, 0, 0) ))

