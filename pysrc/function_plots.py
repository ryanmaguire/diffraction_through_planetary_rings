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
#       Helper function for plotting Fresnel integrals and Bessel functions.   #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       January 3, 2025.                                               #
################################################################################
"""

import matplotlib.pyplot as plt

def make_plots(first_func, second_func, first_label, second_label, file_name):
    """
        Function:
            make_plots
        Purpose:
            Plots two functions across the interval [-5, 5].
        Arguments:
            first_func (function):
                The first function being plotted (Fresnel cos, Bessel J0, etc.).
            second_func (function):
                Second function being plotted (Fresnel sin, Bessel J1, etc.).
            first_label (str):
                The label for the first function.
            second_label (str):
                The label for the second function.
    """

    # Parameters for the plot.
    start = -5.0
    end = +5.0
    number_of_samples = 200

    # Create an array of points evenly distributed along the interval.
    displacement = (end - start) / float(number_of_samples)
    x_vals = [start + k * displacement for k in range(number_of_samples)]

    # Evaluate the functions.
    f_of_x = first_func(x_vals)
    g_of_x = second_func(x_vals)

    # Plot the functions.
    plt.plot(x_vals, f_of_x, label = first_label)
    plt.plot(x_vals, g_of_x, label = second_label)
    plt.legend()
    plt.savefig(file_name.rsplit('.', 1)[0] + ".png")
