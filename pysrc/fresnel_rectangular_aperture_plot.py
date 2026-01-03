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
#       Makes a visual for Fresnel diffraction with a rectangular aperture.    #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       December 21, 2025.                                             #
################################################################################
"""

# pylint has difficulty determining what is inside a C module. Ignore.
# pylint: disable = c-extension-no-member

# Note: ALL UNITS ARE IN METERS.
import tmpyl
import common
from fresnel_integral import fresnel_integral
from outer_product import outer_product

# Produce of the wavelength and the distance, which appears in the formula.
def fresnel_rectangular_aperture_plot(width, height, distance, file_name):
    """
        Function:
            fresnel_rectangular_aperture_plot
        Purpose:
            Makes plots using the Fresnel approximation
            with a rectangular aperture.
        Argument:
            width (float):
                The width, in meters, of the aperture.
            height (float):
                The height, in meters, of the aperture.
            distance (float):
                The distance, in meters, from the observer to the aperture.
            file_name (str):
                The name of the file that is calling this function.
        Output:
            None.
    """

    # The product of the wavelength and the distance to the observer occurs
    # frequently enough to pre-compute. In particular, the scale factor for
    # the Fresnel integrals is sqrt(2 / lambda z). Compute these values.
    lambda_z = common.wavelength * distance
    factor = tmpyl.sqrt(2.0 / lambda_z)

    # Compute the x and y integrals using the Fresnel integral.
    x_term = fresnel_integral(common.x_vals, width, factor)
    y_term = fresnel_integral(common.y_vals, height, factor)

    # The intensity map is computed from the outer product of the
    # x and y integrals. This is because these respective integrals
    # are independent of each other, similar to what we saw in the
    # Fraunhofer limit.
    intensity = outer_product(y_term, x_term)

    # Scale by the initial intensity, which is the intensity at the origin.
    intensity = [common.initial_intensity * value for value in intensity]

    # A label for the plot.
    title = "Fresnel Diffraction: Rectangular Aperture"

    # Make the plot and save it to a PNG file.
    common.make_plots(intensity, title, file_name, clip = common.low_clip)
