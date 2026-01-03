"""
################################################################################
#                                   LICENSE                                    #
################################################################################
#   This file is part of diffraction_through_planetary_rings.                  #
#                                                                              #
#   diffraction_through_planetary_rings is free software: you can redistribute #
#   it and/or modify it under the terms of the GNU General Public License as   #
#   published by the Free Software Foundation, either version 3 of the         #
#   License, or (at your option) any later version.                            #
#                                                                              #
#   diffraction_through_planetary_rings is distributed in the hope that it     #
#   will be useful, but WITHOUT ANY WARRANTY; without even the implied         #
#   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the  #
#   GNU General Public License for more details.                               #
#                                                                              #
#   You should have received a copy of the GNU General Public License          #
#   along with diffraction_through_planetary_rings.  If not, see               #
#   <https://www.gnu.org/licenses/>.                                           #
################################################################################
#   Purpose:                                                                   #
#       Provides common parameters for plots and functions.                    #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       December 21, 2025.                                             #
################################################################################
"""

# pylint wants all of the variables to be SCREAMING_CASE. Ignore this.
# pylint: disable = invalid-name

import numpy
import matplotlib.pyplot as plt

# Parameters for the monochromatic wave.
# Wavelength (lambda) is set to red, in the visible spectrum.
wavelength = 6.5E-07
initial_intensity = 1.0

# We'll clip the colors a bit so we can see the pattern more clearly.
low_clip = initial_intensity / 4.0
medium_clip = initial_intensity / 8.0
high_clip = initial_intensity / 16.0

# Parameters for the image.
x_size = 5.0E-03
y_size = 5.0E-03
x_pixels = 2048
y_pixels = 2048
plot_boundaries = [-x_size, x_size, -y_size, y_size]

# Step sizes used for sampling the x and y axes.
x_displacement = 2.0 * x_size / float(x_pixels)
y_displacement = 2.0 * y_size / float(y_pixels)

# Arrays for the two axes.
x_vals = numpy.arange(-x_size, x_size, x_displacement)
y_vals = numpy.arange(-y_size, y_size, y_displacement)

def make_plots(intensity, title, file_name, clip = medium_clip):
    """
        Function:
            make_plots
        Purpose:
            Makes 2D intensity plots for diffraction patterns on a screen.
        Arguments:
            intensity (list):
                A list of lists representing a grid of points in the plane.
                The values are for the intensity for the diffraction pattern.
            title (str):
                The title of the plot.
            file_name (str):
                The name of the file calling this function.
        Keywords:
            clip (float):
                Clipping parameter for the plot. Higher numbers make dark
                areas brighter. This should be less than initial_intensity.
        Output:
            None.
    """

    # Make the plots.
    figure, axes = plt.subplots()
    image = axes.imshow(
        intensity,
        extent = plot_boundaries,
        cmap = 'hot',
        vmin = 0.0,
        vmax = clip
    )

    # Add labels for the axes and the plot.
    axes.set_xlabel("x (meters)")
    axes.set_ylabel("y (meters)")
    axes.set_title(title)
    figure.colorbar(image, ax = axes)

    # Render the image.
    plt.savefig(file_name.rsplit('.', 1)[0] + ".png")
