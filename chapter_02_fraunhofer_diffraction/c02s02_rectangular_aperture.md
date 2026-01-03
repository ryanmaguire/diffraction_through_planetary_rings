# Rectangular Aperture
```{include} c02s02_rectangular_aperture.tex
```

```{literalinclude} ../pysrc/common.py
:label: common.py
:lang: python
:caption: Common Parameters for Plots
:start-line:31
```

We may use [`common.py`](#common.py) to create a Fraunhofer diffraction pattern.

```{literalinclude} ../pysrc/fraunhofer_diffraction_rectangular_aperture.py
:label: fraunhofer_diffraction_rectangular_aperture.py
:lang: python
:caption: Fraunhofer Diffraction in Python
:start-line:33
```

If we save this to `fraunhofer_diffraction_rectangular_aperture.py` and then
run:

```bash
python3 fraunhofer_diffraction_rectangular_aperture.py
```

we'll obtain the image below.

:::{figure} ../images/fraunhofer_diffraction_rectangular_aperture.png
Fraunhofer Diffraction - Rectangular Aperture
:::
