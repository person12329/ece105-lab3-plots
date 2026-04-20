"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.
from __future__ import annotations
import numpy as np


def generate_data(seed: int | None) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Generate synthetic timestamps and two sensor temperature arrays.

    The function uses a NumPy PCG-based RNG (default_rng) for reproducible
    results when a seed is provided.

    Parameters
    ----------
    seed : int or None
        Seed for np.random.default_rng. If None, a non-deterministic RNG is
        used.

    Returns
    -------
    t : numpy.ndarray, shape (n,)
        Sorted timestamps sampled uniformly from the interval [0, 10].
    sensor_a : numpy.ndarray, shape (n,)
        Simulated Sensor A temperature readings drawn from N(loc=25, scale=3).
    sensor_b : numpy.ndarray, shape (n,)
        Simulated Sensor B temperature readings drawn from N(loc=27, scale=4.5).

    Notes
    -----
    - n is fixed to 200 to match the lab notebook's intent.
    - The returned timestamps are sorted and the sensor arrays are permuted
      consistently so each reading corresponds to the same timestamp.
    """
    n = 200
    rng = np.random.default_rng(seed)

    # sample timestamps and sort so plots are chronological
    t = rng.uniform(0.0, 10.0, size=n)
    order = np.argsort(t)
    t = t[order]

    # independent Gaussian sensor noise around the specified means/stds
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n)[order]
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n)[order]

    return t, sensor_a, sensor_b


if __name__ == "__main__":
    # quick smoke test
    t, a, b = generate_data(7336)
    print(f"Generated arrays: t={t.shape}, sensor_a={a.shape}, sensor_b={b.shape}")

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(ax: plt.Axes, t: np.ndarray, sensor_a: np.ndarray, sensor_b: np.ndarray) -> None:
    """Plot sensor readings as a scatter plot on an existing Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes to draw on (modified in place).
    t : numpy.ndarray, shape (n,)
        Timestamps for readings.
    sensor_a : numpy.ndarray, shape (n,)
        Sensor A temperature readings.
    sensor_b : numpy.ndarray, shape (n,)
        Sensor B temperature readings.

    Returns
    -------
    None
    """
    t = np.asarray(t)
    sensor_a = np.asarray(sensor_a)
    sensor_b = np.asarray(sensor_b)

    if t.shape != sensor_a.shape or t.shape != sensor_b.shape:
        raise ValueError("t, sensor_a, and sensor_b must have the same shape")

    ax.scatter(t, sensor_a, label="Sensor A", color="C0", alpha=0.75,
               edgecolors="k", linewidths=0.4, s=36, zorder=3)
    ax.scatter(t, sensor_b, label="Sensor B", color="C1", alpha=0.75,
               edgecolors="k", linewidths=0.4, s=36, marker="s", zorder=3)

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Sensor temperature readings over time")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.4, zorder=0)

    ymin = float(min(sensor_a.min(), sensor_b.min()))
    ymax = float(max(sensor_a.max(), sensor_b.max()))
    padding = 0.05 * (ymax - ymin) if ymax > ymin else 1.0
    ax.set_ylim(ymin - padding, ymax + padding)