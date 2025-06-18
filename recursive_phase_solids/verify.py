import numpy as np
from itertools import combinations


def pairwise_distances(points):
    """Return all pairwise Euclidean distances for a set of points."""
    pts = np.asarray(points, dtype=float)
    return [np.linalg.norm(pts[i] - pts[j]) for i, j in combinations(range(len(pts)), 2)]


def verify_edge_uniformity(points, tolerance=1e-6):
    """Check that all edges have nearly equal length."""
    dists = pairwise_distances(points)
    if not dists:
        return True
    min_dist = min(dists)
    edge_diffs = [abs(d - min_dist) for d in dists]
    passed = all(diff < tolerance for diff in edge_diffs)
    if passed:
        print("✅ All edges are equal within tolerance.")
    else:
        print("❌ Edge lengths differ by more than tolerance.")
        print("  Max deviation:", max(edge_diffs))
    return passed


def verify_on_sphere(points, tolerance=1e-6):
    """Check that all points lie on a common sphere."""
    pts = np.asarray(points, dtype=float)
    norms = np.linalg.norm(pts, axis=1)
    radius = np.mean(norms)
    deviations = [abs(r - radius) for r in norms]
    passed = all(dev < tolerance for dev in deviations)
    if passed:
        print("✅ All vertices lie on a common sphere.")
    else:
        print("❌ Vertex distances from center vary beyond tolerance.")
        print("  Max deviation:", max(deviations))
    return passed


def check_golden_ratios(points, tolerance=1e-3):
    """Detect golden ratios in coordinate ratios of points."""
    phi = (1 + np.sqrt(5)) / 2
    for x, y, z in points:
        ratios = [abs(abs(x / y) - phi), abs(abs(y / z) - phi), abs(abs(x / z) - phi)]
        if any(r < tolerance for r in ratios):
            print("✅ Golden ratio detected in projected coordinate ratios.")
            return True
    print("⚠️ No golden ratio found within tolerance.")
    return False


def full_verify(points, tolerance=1e-6, check_phi=False):
    """Run multiple verification checks on a point set."""
    print("Verifying projected solid...")
    r1 = verify_edge_uniformity(points, tolerance)
    r2 = verify_on_sphere(points, tolerance)
    r3 = check_golden_ratios(points) if check_phi else True
    return r1 and r2 and r3


if __name__ == "__main__":
    from .recursive_phase import generate_platonic_solid

    solid = generate_platonic_solid("icosahedron")
    full_verify(solid, tolerance=1e-6, check_phi=True)
