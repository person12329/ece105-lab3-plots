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

    import numpy as np
import matplotlib.pyplot as plt

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


def plot_histogram(ax: plt.Axes, sensor_a: np.ndarray, sensor_b: np.ndarray, bins: int = 30) -> None:
    """Draw an overlaid histogram of Sensor A and Sensor B temperature distributions.

    Modifies `ax` in place and returns None.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes to draw on (modified in place).
    sensor_a : numpy.ndarray, shape (n,)
        Sensor A temperature readings.
    sensor_b : numpy.ndarray, shape (n,)
        Sensor B temperature readings.
    bins : int, optional
        Number of histogram bins (default is 30).

    Returns
    -------
    None
    """
    sensor_a = np.asarray(sensor_a)
    sensor_b = np.asarray(sensor_b)

    ax.hist(sensor_a, bins=bins, alpha=0.5, label="Sensor A", color="C0", edgecolor="k")
    ax.hist(sensor_b, bins=bins, alpha=0.5, label="Sensor B", color="C1", edgecolor="k")

    mean_a = float(np.mean(sensor_a))
    mean_b = float(np.mean(sensor_b))
    ax.axvline(mean_a, color="C0", linestyle="--", linewidth=1.5, label="Mean A")
    ax.axvline(mean_b, color="C1", linestyle="--", linewidth=1.5, label="Mean B")

    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Count")
    ax.set_title("Overlaid histogram of Sensor A and Sensor B")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.3)


def plot_boxplot(ax: plt.Axes, sensor_a: np.ndarray, sensor_b: np.ndarray) -> None:
    """Draw side-by-side box plots comparing Sensor A and Sensor B.

    Modifies `ax` in place and returns None.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes to draw on (modified in place).
    sensor_a : numpy.ndarray, shape (n,)
        Sensor A temperature readings.
    sensor_b : numpy.ndarray, shape (n,)
        Sensor B temperature readings.

    Returns
    -------
    None
    """
    sensor_a = np.asarray(sensor_a)
    sensor_b = np.asarray(sensor_b)

    data = [sensor_a, sensor_b]
    labels = ["Sensor A", "Sensor B"]

    bp = ax.boxplot(data, labels=labels, notch=True, patch_artist=True,
                    showmeans=True, widths=0.6)

    colors = ["C0", "C1"]
    for box, color in zip(bp["boxes"], colors):
        box.set(facecolor=color, alpha=0.5, edgecolor="k")

    for median in bp.get("medians", []):
        median.set(color="black", linewidth=1.5)
    for mean_marker in bp.get("means", []):
        mean_marker.set(marker="D", markeredgecolor="black", markerfacecolor="white", markersize=6)

    overall_mean = float(np.mean(np.concatenate(data)))
    ax.axhline(overall_mean, linestyle="--", color="grey", linewidth=1.2, label="Overall mean")

    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Side-by-side box plot: Sensor A vs Sensor B")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.3)
# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.

def main(seed: int | None = 7336, outdir: str | os.PathLike = '.', show: bool = False) -> None:
    """Generate data and produce plots.

    Parameters
    ----------
    seed : int or None, optional
        RNG seed passed to ``generate_data``. Default is 7336.
    outdir : str or os.PathLike, optional
        Directory where generated PNG files will be written. Defaults to current directory.
    show : bool, optional
        If True, display the figures interactively using ``plt.show()``.

    Returns
    -------
    None
    """
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    t, sensor_a, sensor_b = generate_data(seed)

    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    plot_scatter(axs[0], t, sensor_a, sensor_b)
    plot_histogram(axs[1], sensor_a, sensor_b)
    plot_boxplot(axs[2], sensor_a, sensor_b)
    fig.tight_layout()
    fig.savefig(outdir / "sensor_plots_combined.png", dpi=150)

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    plot_scatter(ax2, t, sensor_a, sensor_b)
    fig2.tight_layout(); fig2.savefig(outdir / "sensor_scatter.png", dpi=150)

    fig3, ax3 = plt.subplots(figsize=(6, 4))
    plot_histogram(ax3, sensor_a, sensor_b)
    fig3.tight_layout(); fig3.savefig(outdir / "sensor_histogram.png", dpi=150)

    fig4, ax4 = plt.subplots(figsize=(6, 4))
    plot_boxplot(ax4, sensor_a, sensor_b)
    fig4.tight_layout(); fig4.savefig(outdir / "sensor_boxplot.png", dpi=150)

    print(f"Wrote plots to: {outdir}")

    if show:
        plt.show()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Generate sensor plots.")
    parser.add_argument('--seed', type=int, default=7336, help='RNG seed (default: 7336)')
    parser.add_argument('--outdir', type=str, default='.', help='Output directory for PNG files')
    parser.add_argument('--show', action='store_true', help='Display plots interactively')
    args = parser.parse_args()

    main(seed=args.seed, outdir=args.outdir, show=args.show)

