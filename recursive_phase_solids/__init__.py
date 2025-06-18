"""Utilities for recursive phase rotors and Platonic solids."""

from .recursive_phase import (
    generate_phase_rotor,
    stereographic_projection,
    generate_platonic_solid,
    verify_edge_lengths,
)
from .verify import (
    pairwise_distances,
    verify_edge_uniformity,
    verify_on_sphere,
    check_golden_ratios,
    full_verify,
)

__all__ = [
    "generate_phase_rotor",
    "stereographic_projection",
    "generate_platonic_solid",
    "verify_edge_lengths",
    "pairwise_distances",
    "verify_edge_uniformity",
    "verify_on_sphere",
    "check_golden_ratios",
    "full_verify",
]
