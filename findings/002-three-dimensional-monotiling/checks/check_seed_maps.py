"""Exhaustive checks of selected fibres in a reduced shared-seed model.

Finding 002, Roger Malcolm III, 2026-10-08.
Research and implementation assistance: GPT-6 agents in one shared-model
investigation; this is not an independent proof certification.

This deliberately reduced model has S=(Z/5)^2, |S|=25, and the same
3/4/(D-7) seed-label decomposition, coprime CRT, and two seed maps
sharing one output rotation. It tests that local algebra, not the full Sudoku
compiler, its prime threshold, or any infinite tiling theorem. The seed
regions are abstract label spaces; this model does not test the Sudoku
seed congruences. Four target bases are tested for each of two seeds.

Requires Python 3.8+ and the standard library. Run without -O: assertions
check CRT residues, collisions, and full coverage. Successful execution
prints one JSON record: 2 seeds, 8 fibres, 614500 representations.
"""
import argparse
from collections import defaultdict
import json


def output_list(a, b):
    vals = []
    for x in range(a):
        for y in range(b):
            mult = 1 + ((x, y) in ((0, 0), (1, 1))) - ((x, y) in ((1, 0), (0, 1)))
            vals.extend([(x, y)] * mult)
    ra, rb = [0] * len(vals), [0] * len(vals)
    for y in range(b):
        group = [i for i, e in enumerate(vals) if e[1] == y]
        assert len(group) == a
        for v, i in enumerate(group):
            ra[i] = (v - vals[i][0]) % a
    for x in range(a):
        group = [i for i, e in enumerate(vals) if e[0] == x]
        assert len(group) == b
        for v, i in enumerate(group):
            rb[i] = (v - vals[i][1]) % b
    return vals, ra, rb


def block_data(a, b, r):
    choices = [(aa, bb) for aa in range(r // a + 1) for bb in range(r // b + 1) if aa * a + bb * b == r]
    assert choices
    aa, bb = choices[0]
    data, start = [], 0
    for dim in [a] * aa + [b] * bb:
        data.extend((start, dim, y) for y in range(dim))
        start += dim
    assert len(data) == r
    return data


regions = {}
for s in range(3):
    regions[s] = ('s1', 0, None, s)
for s in range(3, 7):
    copy, y1 = divmod(s - 3, 2)
    regions[s] = ('s2', copy, y1, None)
for s in range(7, 25):
    copy, rest = divmod(s - 7, 6)
    y1, y2 = divmod(rest, 3)
    regions[s] = ('s0', copy, y1, y2)
inverse_regions = {value: key for key, value in regions.items()}


def rotate(s, t):
    reg, copy, y1, y2 = regions[s]
    if y1 is not None:
        y1 = (y1 + t) % 2
    if y2 is not None:
        y2 = (y2 + t) % 3
    return inverse_regions[(reg, copy, y1, y2)]


def crt_coefficients(moduli):
    prod = 1
    for m in moduli:
        prod *= m
    return [prod // m * pow(prod // m, -1, m) for m in moduli], prod


parser = argparse.ArgumentParser(description=__doc__)
parser.parse_args()
if not __debug__:
    parser.error("assertions must be enabled; run Python without -O or -OO")

counts = defaultdict(int)
for seed, a, b, r, other_a in [(1, 2, 29, 37, 3), (2, 3, 31, 43, 2)]:
    shifts, ra, rb = output_list(a, b)
    blocks = block_data(a, b, r)
    coeff, modulus = crt_coefficients([r, a, b, 5, other_a])
    batches = []
    for low_shift in range(r):
        for delta, e in enumerate(shifts):
            for tau1 in range(5):
                residues = [low_shift, ra[delta], rb[delta], tau1, 0]
                h1 = sum(c * v for c, v in zip(coeff, residues)) % modulus
                assert all(h1 % m == v for m, v in zip([r, a, b, 5, other_a], residues))
                for tau2 in range(5):
                    batches.append((low_shift, e, tau1, tau2, h1))
    cardinality = r * a * b * 25
    assert len(batches) == cardinality
    for x1, x2, target_low in [(-7, 2, 0), (0, 0, 1), (6, -3, r - 1), (23, 19, 7)]:
        seen = bytearray(cardinality)
        for low_shift, e, tau1, tau2, h1 in batches:
            source_x1 = x1 - h1
            source_s = ((x1 - tau1) % 5) * 5 + (x2 - tau2) % 5
            source_low = (target_low - low_shift) % r
            reg, _, y1, y2 = regions[source_s]
            if reg == 's' + str(seed):
                start, dim, label = blocks[source_low]
                useful = (label, 0) if dim == a else (0, label)
                high = start + (label + source_x1) % dim
            else:
                useful = (y1 if seed == 1 else y2, 0)
                high = source_low
            out_a, out_b = (useful[0] + e[0]) % a, (useful[1] + e[1]) % b
            out_z = rotate(source_s, source_x1)
            index = (((out_a * b + out_b) * r + high) * 25) + out_z
            assert not seen[index], (seed, x1, x2, target_low, 'collision', index)
            seen[index] = 1
        assert all(seen), (seed, 'missing target')
        counts['fibers'] += 1
        counts['representations'] += cardinality
    counts['seeds'] += 1

print(json.dumps({'status': 'passed', **counts, 'scope': 'reduced finite shared-seed model only; not a proof of the theorem'}))
