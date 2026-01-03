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
#       Creates a visual for Fraunhofer diffraction with a circular aperture.  #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       December 21, 2025.                                             #
################################################################################
"""
# pylint wants all of the variables to be SCREAMING_CASE. Ignore this.
# pylint: disable = invalid-name

# pylint also has difficulty determining what's inside a C module. Ignore.
# pylint: disable = c-extension-no-member

# Note: ALL UNITS ARE IN METERS.
import math
import tmpyl
import common

# Parameters for the aperture. It is circular, we only need the radius.
radius = 5.0E-04

# Distance between the aperture and the screen.
# This must be much larger than the radius.
distance = 5.0E-01

# Scale factor for the independent variable.
factor = 2.0 * math.pi * radius / (distance * common.wavelength)

# The title for the plot.
title = "Fraunhofer Diffraction: Airy Disks"

# Empty list for the intensity. We'll fill this as we go.
intensity = []

# Loop through the points in the grid and compute the diffraction pattern.
for x_val in common.x_vals:

    # The output is a grid, which is represented by a list of lists. Create an
    # empty list, we'll fill it with the current column in the next for-loop.
    array = []

    # Loop through the elements of the current column.
    for y_val in common.y_vals:

        # The argument is given by the distance from the point to the origin,
        # times the scale factor. Use Pythagoras to compute this.
        argument = factor * tmpyl.sqrt(x_val ** 2 + y_val ** 2)

        # We may use the Airy J1 function to compute the diffraction value.
        diffraction_value = tmpyl.airy_j1(argument) ** 2

        # Add the intensity to our array for the column.
        array.append(common.initial_intensity * diffraction_value)

    # Add the entire column to the intensity array.
    intensity.append(array)

# Create the plot.
common.make_plots(intensity, title, __file__, clip = common.high_clip)
