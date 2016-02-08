---
layout: post
title: Abbe' Value
---

# Trigonometric Ray Trace



n = 1.6

$F\_1$ = +8.00

th = 4.2

stop = 27 mm

$u'\_2$ = 30$^o$

##Front/Back Radius

$$\begin{aligned}
r_1 &= \frac{n-1}{f_1}\\
&= \frac{8.00 \times(1.6-1)}{0.53} = 9.06
\end{aligned}$$

$$\begin{aligned}
f_2 &= \frac{f_1}{1-(\frac{t_m}{n})f_1}\\
&=5.00-(\frac{9.06}{1-(\frac{0.0042}{1.6})9.06}\\
&=-4.28\\
r_2&=\frac{1-n}{f_2}\\
&= \frac{1-1.6}{-4.28} = 0.1402\ m\ 140.2\ mm
\end{aligned}$$

* Law of sines to find $\angle$d
* $\angle$c is the angle of incidence and $\angle$d the angle of refraction

  
$$\begin{aligned}
\frac{(stop - r_2)}{sin\ (d)} 
&= \frac{r_2}{sin\theta}\\\\
sin\ d &= \frac{(stop-r_2)sin\theta}{r_2}\\\\
d &= sin^{-1}[\frac{(stop-r_2)sin\theta}{r_2}]
\end{aligned}$$

* Snell’s Law to find $\angle$c
* n is 1.6 and n' is air

\begin{aligned}
n sin(c) &= n' sin(d)\\
c &= sin^{-1}(\frac{sin(d)}{n})
\end{aligned}

* $\angle$d the angle of refraction from the back surface
* $\angle$c the angle of incidence from the back surface

\begin{aligned}
d &=\frac{(stop-r_2)(sin(u'_2)}{r_2}\\
&=sin^{-1}[\frac{(27 - 140.2)sin(30)}{140.2}]\\
&=-23.82\\
c&=sin^{-1}(\frac{sin(-23.82)}{1.6})\\
&=-14.62\\
\end{aligned}

* $u_2$ angle the un-refracted ray from the back surface would make to the axis
* $l_2$ the distance from the back surface to point where the refacted ray would intersect the axis if it had not been refracted 
* $\theta_2$ the angle that the radius makes with the axis
* $u_1$ the angle the incident ray from the front surface would make to the axis if it were not refracted

\begin{aligned}
u_2&=u'_2+d-c\\
&=30+(-23.82)-(-14.62)\\
&=20.8\\
l_2-r_2 &= \frac{r_2\times sin(c)}{sin(u_2)}\\
l_2&=[\frac{140.2\times sin(-14.62)}{sin(20.8)}]+140.2\\
&=40.55
\end{aligned}

* $\theta_2$ the angle $r_2$ makes with the axis
* $u'_1$ the angle the refracted ray makes from the front surface makes witht the axis

\begin{aligned}
\theta_2&=u'_2+l_2\\
&=30+40.55\\
&=70.55\\
u'_1 &= u_2\\
&=20.8
\end{aligned}

* $l_1$

\begin{aligned}
l_l&= l_2+th\\
&=40.55+4.2\\
&=44.75
\end{aligned}

* $\angle$b the angle of refraction from the front surface
* $\angle$a the angle of incidence from the front surface

\begin{aligned}
b&=sin^{-1}[\frac\\
b&=sin^{-1}[\frac{(44.75 - 66.25)sin(20.8)}{66.25}]\\\\&=-6.62\\\\a&=sin^{-1}(sin(-6.62)\times 1.6)\\\\&= -10.63\\
\end{aligned}
