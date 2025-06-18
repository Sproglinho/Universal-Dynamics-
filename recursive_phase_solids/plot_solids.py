"""3D plotting utilities for Platonic solids."""

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 for 3D projections
import matplotlib.pyplot as plt

from .recursive_phase import generate_platonic_solid


def _set_axes_equal(ax):
    """Set 3D plot axes to equal scale."""
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = sum(x_limits) / 2
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = sum(y_limits) / 2
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = sum(z_limits) / 2

    plot_radius = 0.5 * max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


def plot_solid(name: str, ax=None):
    """Plot the vertices of a Platonic solid in 3D.

    Parameters
    ----------
    name : str
        Name of the Platonic solid to plot.
    ax : matplotlib.axes._subplots.Axes3DSubplot, optional
        Existing axes to draw on. If ``None``, a new figure and axes are created.
    """
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
    vertices = generate_platonic_solid(name)
    xs, ys, zs = zip(*vertices)
    ax.scatter(xs, ys, zs, color="C0")
    for idx, (x, y, z) in enumerate(vertices):
        ax.text(x, y, z, str(idx))

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(name.capitalize())
    _set_axes_equal(ax)
    return ax


__all__ = ["plot_solid"]


if __name__ == "__main__":
    plot_solid("tetrahedron")
    plt.show()
