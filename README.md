<!-- Create a README.md with these sections:
     1. Project title and one-sentence description
     2. Installation (activate ece105 conda env, pip install numpy matplotlib)
     3. Usage (python generate_plots.py)
     4. Example output (describe the three plots briefly)
     5. AI tools used and disclosure -->

# Sensor Plotting (ECE105 Lab 3)

A small utility to generate synthetic temperature readings for two sensors and produce publication-quality plots (scatter, histogram, and box plot).

## Installation

1. Activate course environment (recommended):

   conda activate ece105

2. Install dependencies (using conda/mamba):

   conda install -c conda-forge numpy matplotlib

   Or with mamba:

   mamba install -c conda-forge numpy matplotlib

   Alternatively, using pip with the same Python interpreter:

   python -m pip install --upgrade pip
   python -m pip install numpy matplotlib

## Usage

Run the script from the repository root:

   python generate_plots.py [--seed SEED] [--outdir DIR] [--show]

Options:
- --seed: RNG seed (default 7336)
- --outdir: output directory for PNG files (default: current directory)
- --show: display plots interactively after generation

## Example output

The script writes the following PNG files to the output directory:

- sensor_plots_combined.png — a 1×3 figure containing the scatter, histogram, and box plot.
- sensor_scatter.png — scatter plot of both sensors over time.
- sensor_histogram.png — overlaid histogram of the two sensors with mean lines.
- sensor_boxplot.png — side-by-side box plots with the overall mean annotated.

## AI tools used and disclosure

- Copilot CLI/Copilot Chat