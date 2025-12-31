/******************************************************************************
 *                                  LICENSE                                   *
 ******************************************************************************
 *  This file is part of diffraction_through_planetary_rings.                 *
 *                                                                            *
 *  diffraction_through_planetary_rings is free software: you can             *
 *  redistribute it and/or modify it under the terms of the GNU General       *
 *  Public License as published by the Free Software Foundation, either       *
 *  version 3 of the License, or (at your option) any later version.          *
 *                                                                            *
 *  diffraction_through_planetary_rings is distributed in the hope that it    *
 *  will be useful, but WITHOUT ANY WARRANTY; without even the implied        *
 *  warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  *
 *  GNU General Public License for more details.                              *
 *                                                                            *
 *  You should have received a copy of the GNU General Public License         *
 *  along with diffraction_through_planetary_rings.                           *
 *  If not, see <https://www.gnu.org/licenses/>.                              *
 ******************************************************************************
 *                              tmpl_abs_double                               *
 ******************************************************************************
 *  Purpose:                                                                  *
 *      Computes |x|. Source: libtmpl/include/inline/math/tmpl_abs_double.h.  *
 ******************************************************************************
 *  Author:     Ryan Maguire                                                  *
 *  Date:       February 16, 2021                                             *
 ******************************************************************************/

/*  2D vector types found here. We will simplify things by assuming that      *
 *  Earth and Jupiter lie in the exact same orbital plane.                    */
#include <libtmpl/include/tmpl_vec2.h>

/*  Note: all lengths are in meters, all times are in second, all angles are  *
 *  in radians, and angular velocities are radians per second.                */
#define SPEED_OF_LIGHT (+2.99792E+08)

#define EARTH_DISTANCE_TO_SUN (1.471E+11)

#define EARTH_ANGULAR_VELOCITY (+1.9909866E-07)

/*  Jupiter is 11 times further from the Sun than Earth is.                   */
#define JUPITER_DISTANCE_TO_SUN (+7.795E+09)

/*  One Jupiter year is 3.744 x 10^8 seconds, the angular velocity is 2 pi    *
 *  divided by the orbital period, which gives us the following.              */
#define JUPITER_ANGULAR_VELOCITY (+1.6784E-08)

static tmpl_TwoVectorDouble jupiter_position(const double time)
{
    const double angle = JUPITER_ANGULAR_VELOCITY * time;

    return tmpl_2DDouble_Polar(JUPITER_DISTANCE_TO_SUN, angle);
}

static tmpl_TwoVectorDouble earth_position(const double time)
{
    const double angle = EARTH_ANGULAR_VELOCITY * time;

    return tmpl_2DDouble_Polar(EARTH_DISTANCE_TO_SUN, angle);
}
