def blast_hole_dia(h, i):
    if i == 1:
        return h/40
    elif i == 2:
        return h/66

def burden(d, m):
    if m == 1:
        return 45*d
    elif m == 2:
        return 19.7 * d**0.79
    elif m == 3:
        return 30 * d

def spacing(b, m):
    if m == 1:
        return b
    elif m == 2:
        return 1.15*b
    elif m == 3:
        return 1.5*b
        
def stemming_length(b, d, m):
    if m == 1:
        return 1*b
    elif m ==2:
        return 20*d

def particle_size(d, m):
    if m == 1:
        return 0.05*d
        
    elif m == 2:
        return 0.15*d

H = int(input("Bench Height:"))

hard_or_soft = int(input("1:Hard rock 2:soft rock\n"))
D = blast_hole_dia(H, hard_or_soft)
method = int(input("Choose the method for burden \n 1: Hoek and bray 2:Atlas Copco 3:Dick et al\n"))
Burden = burden(D, method)
methodforspacing = int(input("Method for spacing\n 1.Square 2.Staggered 3.Commom\n"))
Spacing = spacing(Burden,methodforspacing)

methodforstem = int(input("Method for stemming\n 1.Atlas 2.Common\n"))
Stemming_length = stemming_length(Burden, D, methodforstem)

methodforps = int(input("Method for particle size\n 1.Kenya 2.Atlas\n"))
Particle_size = particle_size(D, methodforps)

print(f"Blast Hole Diameter:{D}")
print(f"Burden: {Burden}")
print(f"Spacing: {Spacing}")
print(f"Stemming Length:{Stemming_length}")
print(f"Particle Size:{Particle_size}")
