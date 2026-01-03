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
#       Simple example of using the Fourier expansion for a smooth function.   #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       December 19, 2025.                                             #
################################################################################
"""
# pylint wants all of the variables to be SCREAMING_CASE. Ignore this.
# pylint: disable = invalid-name

# pylint also has difficulty determining what's inside a C module. Ignore.
# pylint: disable = c-extension-no-member

import math
import matplotlib.pyplot as plt
import tmpyl

def parabola(input_array):
    """
        Computes the function y(x) = x * (1 - x).
        This is the function we are plotting and the function
        we are approximating using a Fourier series.
    """
    return [input_val * (1.0 - input_val) for input_val in input_array]

def error(test_array, exact_array):
    """
        Computes the error between two arrays.
        This is simply the difference. Neither the absolute
        error nor the relative errors are plotted below.
    """
    length = len(exact_array)
    return [exact_array[ind] - test_array[ind] for ind in range(length)]

def fourier_coeff(index):
    """
        Computes the nth coefficient for the Fourier expansion
        of x * (1 - x) on the interval [0, 1].
    """

    # The constant factor we found in our computation.
    fourier_factor = 4.0 / math.pi ** 3

    # The numerator and denominator of the expression.
    numer = 1.0 - (-1.0)**index
    denom = index ** 3

    # The output is the Fourier coefficient for the given index.
    return fourier_factor * numer / denom

def fourier_expansion(input_array, degree):
    """
        Computes the Fourier expansion for x * (1 - x)
        up to a user-provided degree.

        Note:
            The even degree contributions are all zero.
            That is, degree = 2n and degree = 2n - 1
            will produce the same approximation.
    """

    # The input is an array (points along the x-axis), and so is the output.
    ouput_array = []

    # Loop through the elements of the input array and compute the Fourier sum.
    for x_val in input_array:

        # Initialize the sum to zero so that we may iteratively update
        # it in the for-loop below.
        out = 0

        # Perform the sum. We may skip index = 0 since this corresponds to zero.
        for index in range(1, degree + 1):

            # The wavelength of the current wave is given by the
            # index and the length of the interval. Since we are
            # working on the unit interval [0, 1], the scale
            # factor is n * pi. That is, the current wave is
            # described by sin(n * pi * x).
            wave = tmpyl.sin(index * math.pi * x_val)

            # The amplitudes of the waves must decay for the
            # Fourier series to be valid (this is the Riemann-Lebesgue theorem).
            coeff = fourier_coeff(index)

            # Update our approximation with the damped wave.
            out += coeff * wave

        # Append this Fourier approximation to our array.
        ouput_array.append(out)

    return ouput_array

# The number of samples used for the unit interval.
number_of_samples = 1000

# The maximum number of Fourier approximations we'll plot.
max_index = 3

# Create an array of points evenly spaced on the unit interval [0, 1].
x_array = [k / (number_of_samples - 1) for k in range(number_of_samples)]

# The function we are approximating is y(x) = x * (1 - x). Compute this.
y_array = parabola(x_array)

# Create a plot of the actual function.
plt.subplot(2, 1, 1)
plt.plot(x_array, y_array, label = "Initial Condition")
plt.xlabel("Horizontal Coordinate (Meters)")
plt.ylabel("Temperature (Celcius)")
plt.title("Fourier Expansion")

# Add the Fourier approximation to the plot.
f_array = fourier_expansion(x_array, 2 * max_index - 1)
plt.plot(x_array, f_array, label = f"Degree {2*max_index - 1} Approximation")

# Provide a legend for the first plot.
plt.legend()

# Create a plot for the error in the Fourier approximations.
plt.subplot(2, 1, 2)
plt.xlabel("Horizontal Coordinate (Meters)")
plt.ylabel("Temperature (Celcius)")
plt.title("Fourier Approximation Errors")

# Loop through and plot the errors for each approximation.
for ind in range(1, max_index + 1):
    f_array = fourier_expansion(x_array, 2 * ind - 1)
    error_array = error(y_array, f_array)
    plt.plot(x_array, error_array, label = f"Degree {2*ind - 1} Error")

# Provide a legend for this plot as well.
plt.legend()

# The plots and the titles may overlap. Avoid this by making it a tight layout.
plt.tight_layout()

# Render the image and save it to a PNG file. The output PNG file will have the
# same file name as this file, but with the ".png" extension instead of ".py".
plt.savefig(__file__.rsplit('.', 1)[0] + ".png")
