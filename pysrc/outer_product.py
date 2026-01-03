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
#       Provides a function for computing the outer product of two arrays.     #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       January 3, 2026.                                               #
################################################################################
"""

def outer_product(x_array, y_array):
    """
        Function:
            outer_product
        Purpose:
            Computes the outer product of two 1-dimensional arrays.
        Arguments:
            x_array (list, array):
                The first argument for the outer product.
            y_array (list, array):
                The second argument for the outer product.
        Output:
            product (list):
                The outer product of x_array and y_array.
        Method:
            The outer product is defined as the len(x_array)-by-len(y_array)
            matrix A where the (m, n) element is given by:

                A[m, n] = x_array[m] * y_array[n]

            We loop through the elements of x_array and y_array and compute
            these products, returning the matrix as a list of lists.
    """

    # Empty array for the outer product. We'll fill this as we go.
    product = []

    # Loop through the x-array first. This means A[x][y] represents
    # the (x, y) element, and not the (y, x) element.
    for x_val in x_array:

        # The output matrix is a list of lists. The current list is the
        # product x_val * y_array.
        array = []

        # Loop through the y-array and compute x_val * y_array.
        for y_val in y_array:

            # Add the product to our current array.
            array.append(x_val * y_val)

        # Add this list to the outer product.
        product.append(array)

    return product
