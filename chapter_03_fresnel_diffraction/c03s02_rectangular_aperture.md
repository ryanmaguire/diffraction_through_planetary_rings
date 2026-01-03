# Rectangular Aperture
```{include} c03s02_rectangular_aperture.tex
```

Both the normalized and unnormalized Fresnel integrals
are provided by `tmpyl`. We can make plots using
[`function_plots.py`](#function_plots.py).

```{literalinclude}  ../pysrc/fresnel_sine_and_cosine.py
:lang: python
:caption: Fresnel Sine and Cosine
:start-line:31
```

:::{figure} ../images/fresnel_sine_and_cosine.png
Fresnel Sine and Cosine
:::

We can do a similar thing for the normalized Fresnel functions.

```{literalinclude}  ../pysrc/normalized_fresnel_sine_and_cosine.py
:lang: python
:caption: Normalized Fresnel Sine and Cosine
:start-line:31
```

:::{figure} ../images/normalized_fresnel_sine_and_cosine.png
Normalized Fresnel Sine and Cosine
:::

Let's use these to craft a solution. First we need to create another helper
function to make plots using the Fresnel integrals. These types of plots can
be created using the *outer product*. Let's make a function to compute this,
putting it in `outer_product.py`.

```{literalinclude}  ../pysrc/outer_product.py
:label: outer_product.py
:lang: python
:caption: Outer Product Function
:start-line:28
```

Using [outer_product.py](#outer_product.py) we can make a plotting function.
The following goes in
`fresnel_rectangular_aperture_plot.py`.

```{literalinclude}  ../pysrc/fresnel_rectangular_aperture_plot.py
:label: fresnel_rectangular_aperture_plot.py
:lang: python
:caption: Fresnel Diffraction Helper Function
:start-line:31
```

With
[`fresnel_rectangular_aperture_plot.py`](#fresnel_rectangular_aperture_plot.py)
it becomes very straight-forward to make the plots.

```{literalinclude}  ../pysrc/fresnel_diffraction_rectangular_aperture.py
:lang: python
:caption: Fresnel Diffraction - Rectangular Aperture
:start-line:28
```

:::{figure} ../images/fresnel_diffraction_rectangular_aperture.png
Fresnel Diffraction - Rectangular Aperture
:::

If we decrease the aperture size we return to the Fraunhofer limit.
The product of the $\textrm{sinc}$ functions start to approximate
the Fresnel functions, as shown below.

```{literalinclude}  ../pysrc/fresnel_diffraction_rectangular_fraunhofer_limit.py
:lang: python
:caption: Fresnel Diffraction - Rectangular Aperture
:start-line:28
```

:::{figure} ../images/fresnel_diffraction_rectangular_fraunhofer_limit.png
Fresnel Diffraction - Rectangular Aperture
:::
