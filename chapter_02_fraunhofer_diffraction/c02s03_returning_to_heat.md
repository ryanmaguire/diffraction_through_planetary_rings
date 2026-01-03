# Returning to Heat
```{include} c02s03a_returning_to_heat.tex
```

We can implement this in a short Python script.

```{literalinclude}  ../pysrc/fourier_series_example.py
:lang: python
:caption: Fourier Series in Python
:start-line:33
```

This produces the image below.

:::{figure} ../images/fourier_series_example.png
Fourier Series Example
:::

## Numerical PDEs
```{include} c02s03b_numerical_pdes.tex
```

This method is very concrete and can be implemented in just
a handful of lines.

```{literalinclude}  ../pysrc/numerical_solution_to_the_heat_equation.py
:lang: python
:caption: Numerical Solution to the Heat Equation
:start-line:30
```

:::{figure} ../images/numerical_solution_to_the_heat_equation.png
Numerical Solution to the Heat Equation
:::

## Validity of the Heat Equation
```{include} c02s03c_validity_of_the_heat_equation.tex
```

## Sturm-Liouville Theory
```{include} c02s03d_sturm_liouville_theory.tex
```

`tmpyl` provides $J_{0}$ and $J_{1}$.

```{literalinclude}  ../pysrc/bessel_functions_example.py
:lang: python
:caption: Bessel Functions Example
:start-line:33
```

:::{figure} ../images/bessel_functions_example.png
Plotting the Bessel Functions
:::
