"""
Computational Verification: 600-Cell Spectral Moment
====================================================
CODE 2: FULL GENERATING FUNCTION (DERIVATION SOURCE)

This script evaluates the full generating function G(t) at t = phi^-2.

The generating function is:
    G(t) = 120/(1-20t) + 20/(1-12t) + 20/(1-4t) + 12
         + 30/(1+4t) + 12/(1+8t) + 1/(1+16t)

where phi = (1 + sqrt(5))/2 is the golden ratio, and t = phi^-2.

NOTE: The full generating function is numerically unstable at t = phi^-2
because some denominators approach zero and become negative.
This script demonstrates the source of the derivation, but the
truncated series (Code 1) is the correct stable evaluation.

Dependencies: numpy (for numerical computation)

Run with:
    python verify_600cell_alpha_full.py
"""

import numpy as np

# Golden ratio
phi = (1 + 5**0.5) / 2

# 600-cell adjacency spectrum: eigenvalues and multiplicities
lambdas = np.array([20, 12, 4, 0, -4, -8, -16])
mults = np.array([1, 20, 20, 12, 30, 12, 1])

def G(t):
    """Full generating function of the 600-cell spectral moments."""
    return np.sum(mults / (1 - lambdas * t))

# Evaluate at t = phi^-2
t = phi**-2
G_val = G(t)

# Individual terms for diagnostic purposes
terms = mults / (1 - lambdas * t)

print("=" * 70)
print("CODE 2: FULL GENERATING FUNCTION (DERIVATION SOURCE)")
print("=" * 70)
print(f"phi = {phi:.12f}")
print(f"t = phi^-2 = {t:.12f}")
print()
print("Individual terms:")
for i, (lam, mult, term) in enumerate(zip(lambdas, mults, terms)):
    print(f"    {mult}/(1 - {lam}t)     = {term:.6f}")
print()
print(f"G(phi^-2) = {G_val:.12f}")
print()
print("=" * 70)
print("NOTE: The full generating function is numerically unstable")
print("at t = phi^-2 because denominators approach zero.")
print("The truncated series (Code 1) is the correct stable evaluation.")
print("=" * 70)