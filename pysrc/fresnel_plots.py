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
#       Helper function for plotting the Fresnel integrals.                    #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       January 3, 2025.                                               #
################################################################################
"""

import matplotlib.pyplot as plt

def make_plots(fcos, fsin, clabel, slabel, file_name):
    """
        Function:
            make_plots
        Purpose:
            Makes plots of the Fresnel sine and cosine functions.
        Arguments:
            fcos (function):
                The Fresnel cosine function (normalized or unnormalized).
            fsin (function):
                The Fresnel sine function (normalized or unnormalized).
            clabel (str):
                The label for the Fresnel cosine function.
            slabel (str):
                The label for the Fresnel sine function.
    """

    # Parameters for the plot.
    start = -5.0
    end = +5.0
    number_of_samples = 200

    # Create an array of points evenly distributed along the interval.
    displacement = (end - start) / float(number_of_samples)
    x_vals = [start + k * displacement for k in range(number_of_samples)]

    # Compute the Fresnel functions.
    fresnel_cos_x = fcos(x_vals)
    fresnel_sin_x = fsin(x_vals)

    # Plot the functions.
    plt.plot(x_vals, fresnel_cos_x, label = clabel)
    plt.plot(x_vals, fresnel_sin_x, label = slabel)
    plt.legend()
    plt.savefig(file_name.rsplit('.', 1)[0] + ".png")
