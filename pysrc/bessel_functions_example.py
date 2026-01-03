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
#       Use tmpyl to plot the Bessel functions.                                #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       December 21, 2025.                                             #
################################################################################
"""

# pylint has difficulty determining what's inside a C module. Ignore.
# pylint: disable = c-extension-no-member

import tmpyl
from function_plots import make_plots

# Labels for the two functions.
J0_LABEL = "$J_{0}(x)$"
J1_LABEL = "$J_{1}(x)$"

# Plot the functions and save them to a PNG.
make_plots(tmpyl.bessel_j0, tmpyl.bessel_j1, J0_LABEL, J1_LABEL, __file__)
