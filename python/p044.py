from tqdm import tqdm

def pentagonal(n):
	# Pn = n(3n-1)/2
	return int(((n * 3 * n) - n) * 0.5)

def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)

mx = 2500
pnums = []
for i in range(1, mx+1):
	pnums.append(pentagonal(i))

result = 0
for i, j in enumerate(tqdm(pnums)):
	for k in pnums[i:]:
		s = j + k
		d = abs(k - j)
		if s in pnums and d in pnums:
			print("\n")
			print(f"P{get_sub('j')}: {j}")
			print(f"P{get_sub('k')}: {k}")
			print(f"S = {j} + {k} = {s} ... OK")
			print(f"D = |{k} - {j}| = {d} ... OK")
			print("\n")
			break			
	else:
		continue
	break