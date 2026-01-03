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
#       Makes a visual for Fraunhofer diffraction with a rectangular aperture. #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       March 20, 2025.                                                #
################################################################################
"""
# pylint wants all of the variables to be SCREAMING_CASE. Ignore this.
# pylint: disable = invalid-name

# pylint also has difficulty determining what's inside a C module. Ignore.
# pylint: disable = c-extension-no-member

# Note: ALL UNITS ARE IN METERS.
import numpy
import tmpyl
import common

# Parameters for the aperture. It is rectangular and
# centered about the origin. We only need a width and height.
# Visible light (which is what we are working with)
# diffracts through millimeter apertures (try this out yourself!),
# so if we set W and H to 10^-3 we should expect a nice pattern.
width = 1.0E-03
height = 1.0E-03

# Distance between the aperture and the screen.
# This is the "z" factor in the Fraunhofer equation.
# For Fraunhofer to hold, this should be much larger than
# width and height.
distance = 5.0E-01

# The title for the plot.
title = "Fraunhofer Diffraction: Rectangular Aperture"

# Multiplication is faster than division.
# Compute 1 / (lambda z) and store it as a new variable.
lambda_z = common.wavelength * distance
rcpr_lambda_z = 1.0 / lambda_z

# The Fraunhofer integral splits into two parts, x and y, and can
# be handled individually. The output for a rectangular aperture is the
# square of the normalized sinc function, given by sin(pi x) / (pi x)
# for non-zero x, and 1 at the origin.
x_term = numpy.square(tmpyl.sincpi(width * common.x_vals * rcpr_lambda_z))
y_term = numpy.square(tmpyl.sincpi(height * common.y_vals * rcpr_lambda_z))

# The intensity map for the (x, y) pixel is the product of sinc^2 for the
# x component and sinc^2 for the y component. All together, this is the
# "outer product" of the x and y arrays. Inner products take in two vectors
# and return a number, whereas outer products take in two vectors and
# return a matrix.
intensity = common.initial_intensity * numpy.outer(x_term, y_term)

# Make the plots.
common.make_plots(intensity, title, __file__, clip = common.high_clip)
