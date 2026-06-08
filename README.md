# Neutron Star Structure - TOV Equations

This project numerically solves the Tolman–Oppenheimer–Volkoff (TOV) equations for neutron star structure using multiple equations of state (EOS). The goal is to compute mass–radius relations for compact stars under general relativistic hydrostatic equilibrium and compare how different EOS models affect stellar properties.

---

## Physical Background

Newtonian hydrostatic equilibrium is inadequate for describing neutron stars, since they are highly compact, relativistic objects in which strong gravity significantly alters the spacetime geometry. The relation between pressure, energy density, and gravity must therefore be treated within the framework of General Relativity.

The structure of neutron stars is encapsulated in the Tolman–Oppenheimer–Volkoff (TOV) equations, which generalize Newtonian gravity to relativistic stellar objects. These equations assume a spherically symmetric, static star in hydrostatic equilibrium and a cold equation of state ($T = 0$ K).

---

## The TOV Equations

The TOV equation for hydrostatic equilibrium is:

$$
\frac{dP(r)}{dr}
= -\frac{G m(r)\rho(r)}{r^2}
\left(1 + \frac{P(r)}{\rho(r)c^2}\right)
\left(1 + \frac{4\pi r^3 P(r)}{m(r)c^2}\right)
\left(1 - \frac{2Gm(r)}{rc^2}\right)^{-1}
$$

The enclosed mass satisfies:

$$
\frac{dm(r)}{dr} = \frac{4\pi r^2 \varepsilon(r)}{c^2}
$$

where $\varepsilon(r)$ is the energy density.

To close the system, an equation of state (EOS) is required:

$$
P = P(\varepsilon)
$$

or, for a polytropic EOS:

$$
P = K \varepsilon^\Gamma
$$

---

## Numerical Formulation

To solve the TOV system numerically, we transform variables into dimensionless or rescaled quantities suitable for computation. In particular:

- Energy density: MeV·fm⁻³  
- Mass: solar masses ($M_\odot$)  
- Radius: km  

The modified TOV equations used in this project are:

\[
\frac{d\bar{P}(r)}{dr}
= -1.474 \frac{\bar{\varepsilon}(r)\bar{m}(r)}{r^2}
\left(1 + \frac{\bar{P}(r)}{\bar{\varepsilon}(r)}\right)
\left(1 + \frac{11.2 \, r^3}{10^6} \frac{\bar{P}(r)}{\bar{m}(r)}\right)
\left(1 - 2.948 \frac{\bar{m}(r)}{r}\right)^{-1}
\]

\[
\frac{d\bar{m}(r)}{dr} = 11.2 \times 10^{-6} r^2 \bar{\varepsilon}(r)
\]

---

## Numerical Method

The system is solved using a fourth-order Runge–Kutta (RK4) integration scheme:

\[
\frac{dP}{dr} = f(r, P, m; \varepsilon), \quad
\frac{dm}{dr} = g(r, P, m; \varepsilon)
\]

Update equations:

\[
P_{n+1} = P_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)
\]

\[
m_{n+1} = m_n + \frac{1}{6}(l_1 + 2l_2 + 2l_3 + l_4)
\]

with:

\[
k_1 = h f(r_n, P_n, m_n), \quad l_1 = h g(r_n, P_n, m_n)
\]

\[
k_2 = h f\left(r_n + \frac{h}{2}, P_n + \frac{k_1}{2}, m_n + \frac{l_1}{2}\right), \quad
l_2 = h g\left(r_n + \frac{h}{2}, P_n + \frac{k_1}{2}, m_n + \frac{l_1}{2}\right)
\]

\[
k_3 = h f\left(r_n + \frac{h}{2}, P_n + \frac{k_2}{2}, m_n + \frac{l_2}{2}\right), \quad
l_3 = h g\left(r_n + \frac{h}{2}, P_n + \frac{k_2}{2}, m_n + \frac{l_2}{2}\right)
\]

\[
k_4 = h f(r_n + h, P_n + k_3, m_n + l_3), \quad
l_4 = h g(r_n + h, P_n + k_3, m_n + l_3)
\]

where:

\[
h = \frac{r_{\text{end}} - r_{\text{center}}}{N}
\]

---

## Numerical Setup

- Central pressure range: \( P_c \in [1, 1000] \, \text{MeV·fm}^{-3} \)
- Integration starts near \( r = 0 \) with small non-zero values to avoid singularities
- Integration stops when pressure reaches (approximately) zero, defining the stellar surface

---

## Project Structure
