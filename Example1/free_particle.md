# Free Particle

An important question to ask is: what is the probability to find a free particle within a $\Delta x$ region in space? 

This is crucial for measurements, since we would never measure ALL space at the same time, but instead, our instrument will measure a section of $x$ space 

##### 1. Most easy equation `works`

$$\hat H\left|k\right> = -\frac{\hbar^2}{2m} \frac{\partial^2\left|k\right>}{\partial x^2}
= -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2}\left(\frac{1}{\sqrt{2\pi}}e^{ikx} \right)$$

$$= \frac{\hbar^2k^2}{2m} \left(\frac{1}{\sqrt{2\pi}}e^{ikx} \right)  = \frac{p^2}{2m}\left|k\right>$$

The probability of finding it within a $\Delta x$, at **any** place in space, is the same.

*Thus when the particle has a well-defined momentum ($\hbar k$),  the probability of finding it anywhere in space is the same.*


***Localization*** of the particle can be obtained by considering not just a single value of momentum ($\hbar k$), but a range of values.  
Consider the superposition of waves with a range of momenta given by 
$p=p_0 \pm \Delta p$ $\hspace{0.25cm}$ or $\hspace{0.25cm}$ $\hbar k = \hbar(k_0 \pm \Delta k)$


Since the momentum varies continuolsy, we use an integration for the superposition of waves, all equally weigthed:   

$$\Psi_{\Delta k}(x) = \frac{2N\sin(\Delta kx)}{x} e^{ik_ox}$$

where $N$ is a normalization constant and is equal to $N=\frac{1}{2\sqrt{\pi\Delta k}}$


To understand this new wavefunction, we plot its Real and Imaginary components separately.   


##### 2. Some equation `not works`

###### Test 1

`input`

```
$$\left[\hat P, \hat H \right] = \hat P \cdot \hat H - \hat H \cdot \hat P$$ 
```

`output` from dcc.Markdown, accidently put `<a>` tag into equation, so mathjax cannot render it

```
$$\left<a href="">\hat P, \hat H \right</a> = \hat P \cdot \hat H - \hat H \cdot \hat P$$
```

`rendered` (not work)

$$\left[\hat P, \hat H \right] = \hat P \cdot \hat H - \hat H \cdot \hat P$$ 

###### Test 2

`input`

```
$$\Psi^*_k(x) \Psi_k(x) \Delta x = \left|\Psi_k(x)\right|^2 \Delta x 
= \left(\frac{1}{\sqrt{2\pi}} e^{ikx}\right)^*\frac{1}{\sqrt{2\pi}} e^{ikx} \Delta x = \frac{1}{2\pi} \Delta x $$
```

`output` from dcc.Markdown, accidently put `<em>` tag into equation, so mathjax cannot render it

```
$$\Psi^<em>_k(x) \Psi_k(x) \Delta x = \left|\Psi_k(x)\right|^2 \Delta x = \left(\frac{1}{\sqrt{2\pi}} e^{ikx}\right)^</em>\frac{1}{\sqrt{2\pi}} e^{ikx} \Delta x = \frac{1}{2\pi} \Delta x $$
```

`rendered` (not work)

$$\Psi^*_k(x) \Psi_k(x) \Delta x = \left|\Psi_k(x)\right|^2 \Delta x = \left(\frac{1}{\sqrt{2\pi}} e^{ikx}\right)^*\frac{1}{\sqrt{2\pi}} e^{ikx} \Delta x = \frac{1}{2\pi} \Delta x $$


##### 3. Graph axis works