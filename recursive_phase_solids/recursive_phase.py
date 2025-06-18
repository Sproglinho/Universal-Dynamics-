import math
from typing import List, Tuple


PHI = (1 + math.sqrt(5)) / 2


def generate_phase_rotor(n: int) -> Tuple[float, float, float, float]:
    """Generate a normalized 4D phase rotor on the 3-sphere.

    Parameters
    ----------
    n : int
        The power of two exponent used inside the complex exponential.

    Returns
    -------
    Tuple[float, float, float, float]
        The normalized 4D vector ``(Re(e^{iπ·2ⁿ}), Im(e^{iπ·2ⁿ}),
        Re(e^{-iπ·2ⁿ}), Im(e^{-iπ·2ⁿ}))``.
    """
    theta = math.pi * (2 ** n)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    q = (cos_theta, sin_theta, cos_theta, -sin_theta)
    norm = math.sqrt(sum(component ** 2 for component in q))
    return tuple(component / norm for component in q)


def stereographic_projection(q: Tuple[float, float, float, float]) -> Tuple[float, float, float]:
    """Project a point on the 3-sphere to 3D using stereographic projection.

    Parameters
    ----------
    q : Tuple[float, float, float, float]
        The 4D vector ``(x, y, z, w)`` on ``S^3``.

    Returns
    -------
    Tuple[float, float, float]
        The projected 3D vector ``(x/(1-w), y/(1-w), z/(1-w))``.
    """
    x, y, z, w = q
    denom = 1 - w
    if denom == 0:
        raise ValueError("Stereographic projection undefined for w = 1")
    return (x / denom, y / denom, z / denom)


PLATONIC_SOLIDS = {
    "tetrahedron": [
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, -1),
        (1, -1, -1),
    ],
    "cube": [
        (1, 1, 1),
        (1, 1, -1),
        (1, -1, 1),
        (1, -1, -1),
        (-1, 1, 1),
        (-1, 1, -1),
        (-1, -1, 1),
        (-1, -1, -1),
    ],
    "octahedron": [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ],
    "icosahedron": [
        (0, 1, PHI),
        (0, -1, PHI),
        (0, 1, -PHI),
        (0, -1, -PHI),
        (1, PHI, 0),
        (-1, PHI, 0),
        (1, -PHI, 0),
        (-1, -PHI, 0),
        (PHI, 0, 1),
        (-PHI, 0, 1),
        (PHI, 0, -1),
        (-PHI, 0, -1),
    ],
    "dodecahedron": [
        (1, 1, 1),
        (1, 1, -1),
        (1, -1, 1),
        (1, -1, -1),
        (-1, 1, 1),
        (-1, 1, -1),
        (-1, -1, 1),
        (-1, -1, -1),
        (0, 1 / PHI, PHI),
        (0, -1 / PHI, PHI),
        (0, 1 / PHI, -PHI),
        (0, -1 / PHI, -PHI),
        (PHI, 0, 1 / PHI),
        (-PHI, 0, 1 / PHI),
        (PHI, 0, -1 / PHI),
        (-PHI, 0, -1 / PHI),
        (1 / PHI, PHI, 0),
        (-1 / PHI, PHI, 0),
        (1 / PHI, -PHI, 0),
        (-1 / PHI, -PHI, 0),
    ],
}


def generate_platonic_solid(name: str) -> List[Tuple[float, float, float]]:
    """Return the canonical vertex coordinates of a Platonic solid.

    Parameters
    ----------
    name : str
        One of ``['tetrahedron', 'cube', 'octahedron', 'icosahedron', 'dodecahedron']``.

    Returns
    -------
    List[Tuple[float, float, float]]
        The list of vertex coordinates for the requested solid.
    """
    name = name.lower()
    if name not in PLATONIC_SOLIDS:
        raise ValueError(f"Unknown solid '{name}'")
    return PLATONIC_SOLIDS[name]


def verify_edge_lengths(points: List[Tuple[float, float, float]], tolerance: float = 1e-5) -> bool:
    """Verify that the shortest edges of a polyhedron are equal in length.

    Parameters
    ----------
    points : List[Tuple[float, float, float]]
        The list of 3D vertices ``(x, y, z)``.
    tolerance : float, optional
        Absolute tolerance used when comparing edge lengths.

    Returns
    -------
    bool
        ``True`` if all shortest edges match within ``tolerance``. ``False``
        otherwise. In the failing case the mismatched edge lengths are printed.
    """

    if len(points) < 2:
        return True

    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = math.dist(points[i], points[j])
            distances.append(d)

    min_dist = min(distances)
    # Consider all edges whose length is close to the minimum distance
    candidate_edges = [d for d in distances if d <= min_dist + 10 * tolerance]

    if not candidate_edges:
        return True

    expected = min(candidate_edges)
    max_dev = max(abs(d - expected) for d in candidate_edges)
    if max_dev <= tolerance:
        return True

    mismatched = [d for d in candidate_edges if abs(d - expected) > tolerance]
    print("Mismatched edge lengths:", mismatched)
    return False


__all__ = [
    "generate_phase_rotor",
    "stereographic_projection",
    "generate_platonic_solid",
    "verify_edge_lengths",
]
