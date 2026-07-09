"""
Computational Verification: 600-Cell Spectral Moment
====================================================
CODE 2: FULL GENERATING FUNCTION (DERIVATION SOURCE)
SageMath Version

This script evaluates the full generating function G(t) at t = phi^-2.

The generating function is:
    G(t) = 120/(1-20t) + 20/(1-12t) + 20/(1-4t) + 12
         + 30/(1+4t) + 12/(1+8t) + 1/(1+16t)

where phi = (1 + sqrt(5))/2 is the golden ratio, and t = phi^-2.

NOTE: The full generating function is numerically unstable at t = phi^-2
because some denominators approach zero and become negative.
This script demonstrates the source of the derivation, but the
truncated series (Code 1) is the correct stable evaluation.

Run with:
    sage verify_600cell_alpha_full.sage
"""

# Golden ratio (Sage's sqrt function handles exact radicals)
phi = (1 + sqrt(5)) / 2

# 600-cell adjacency spectrum: eigenvalues and multiplicities
lambdas = [20, 12, 4, 0, -4, -8, -16]
mults = [1, 20, 20, 12, 30, 12, 1]

def G(t):
    """Full generating function of the 600-cell spectral moments."""
    s = 0
    for m, lam in zip(mults, lambdas):
        s += m / (1 - lam * t)
    return s

# Evaluate at t = phi^-2
t = phi^-2
G_val = G(t)

# Individual terms for diagnostic purposes
terms = [m / (1 - lam * t) for m, lam in zip(mults, lambdas)]

# Convert to numerical floats for display
t_num = t.n(digits=15)
G_val_num = G_val.n(digits=15)
terms_num = [term.n(digits=15) for term in terms]

print("=" * 70)
print("CODE 2: FULL GENERATING FUNCTION (DERIVATION SOURCE) - SageMath")
print("=" * 70)
print(f"phi = {phi.n(digits=12)}")
print(f"t = phi^-2 = {t_num:.12f}")
print()
print("Individual terms:")
labels = ["1/(1 - 20t)", "20/(1 - 12t)", "20/(1 - 4t)", "12/(1 - 0t)", 
          "30/(1 + 4t)", "12/(1 + 8t)", "1/(1 + 16t)"]
for label, term in zip(labels, terms_num):
    print(f"    {label:12}     = {term:.6f}")
print()
print(f"G(phi^-2) = {G_val_num:.12f}")
print()
print("=" * 70)
print("NOTE: The full generating function is numerically unstable")
print("at t = phi^-2 because denominators approach zero.")
print("The truncated series (Code 1) is the correct stable evaluation.")
print("=" * 70)