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
#       Plots the unnormalized Fresnel functions.                              #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       December 21, 2025.                                             #
################################################################################
"""

# pylint has difficulty determining what is inside a C module. Ignore.
# pylint: disable = c-extension-no-member

import tmpyl
import fresnel_plots

# This program plots the unnormalized Fresnel functions, provided by tmpyl.
fcos = tmpyl.fresnel_cos
fsin = tmpyl.fresnel_sin

# The unnormalized Fresnel functions have the "hats" on them.
C_LABEL = "$\\hat{C}(x)$"
S_LABEL = "$\\hat{S}(x)$"

# Make the plots.
fresnel_plots.make_plots(fcos, fsin, C_LABEL, S_LABEL, __file__)
