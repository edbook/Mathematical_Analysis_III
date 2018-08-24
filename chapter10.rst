LAPLACE–UMMYNDUN
================

Skilgreiningar og reiknireglur
-------------------------------

Skilgreiningar og reiknireglur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera fall sem skilgreint er á
:math:`{{\mathbb  R}}_+=\{t\in {{\mathbb  R}}; t\geq 0\}` með gildi í
:math:`{{\mathbb  C}}` og gerum ráð fyrir að :math:`f` sé heildanlegt á
sérhverju lokuðu og takmörkuðu bili :math:`[0,b]`.

*Laplace–mynd* :math:`f`, sem við táknum með :math:`{\mathcal{L}}f` eða
:math:`{\mathcal{L}}\{f\}`, er skilgreind með formúlunni

.. math::

  {\mathcal{L}}f(s)=\int_0^ \infty e^{-st}f(t)\, dt.

  

Skilgreiningarmengi fallsins :math:`{\mathcal{L}}f` samanstendur af öllum
tvinntölum :math:`s` þannig að heildið í hægri hliðinni sé samleitið.

*Laplace-ummyndun* er vörpunin :math:`{\mathcal{L}}` sem úthlutar falli
:math:`f` Laplace-mynd sinni :math:`{\mathcal{L}}f`.

  

Skilgreining
^^^^^^^^^^^^

Við segjum að fallið :math:`f:{{\mathbb  R}}_+\to {{\mathbb  C}}` sé af
:hover:`veldisvísisgerð` ef til eru jákvæðir fastar
:math:`M` og :math:`c` þannig að

.. math::

  |f(t)|\leq Me^{c t}, \qquad t\in {{\mathbb  R}}_+.

  

--------------

Ef :math:`f` er heildanlegt á sérhverju takmörkuðu bili :math:`[0,b]` og
uppfyllir ójöfnuna, þá er :math:`{\mathcal{L}}f` skilgreint fyrir öll
:math:`s\in {{\mathbb  C}}` með :math:`{{\operatorname{Re\, }}}s >c`. Við fáum að auki vaxtartakmarkanir á :math:`{\mathcal{L}}f`,

.. math::

  |{\mathcal{L}}f(s) |\leq \int_0^\infty e^{-{{\operatorname{Re\, }}}st} Me^{c t} \, dt =
   \dfrac M{{{\operatorname{Re\, }}}\,  s-c}, \qquad {{\operatorname{Re\, }}}\,  s>c.


  

Það er augljóst að Laplace-ummyndun er línuleg vörpun, en það þýðir að

.. math:: {\mathcal{L}}\{\alpha f+\beta g\}(s)=\alpha{\mathcal{L}}\{f\}(s)+\beta{\mathcal{L}}\{g\}(s)

ef :math:`f` og :math:`g` eru föll af veldisvísisgerð, :math:`\alpha`
og :math:`\beta` eru tvinntölur og :math:`s\in {{\mathbb  C}}` liggur í
skilgreiningarmengi fallanna :math:`{\mathcal{L}}\{f\}` og
:math:`{\mathcal{L}}\{g\}`.

Við þurfum að leiða út nokkrar reiknireglur fyrir Laplace-ummyndun. Sú
fyrsta segir okkur að Laplace-myndir falla af veldisvísisgerð séu fáguð
föll og hún segir okkur einnig að afleiður af Laplace-myndum af slíkum
föllum séu einnig Laplace myndir:

  

Setning
^^^^^^^

Látum :math:`f:{{\mathbb  R}}_+\to {{\mathbb  C}}` vera fall sem er
heildanlegt á sérhverju bili :math:`[0,b]` til eru jákvæðir fastar
:math:`M` og :math:`c` þannig að
:math:`|f(t)|\leq Me^{c t}, t\in {{\mathbb  R}}_+`.

Þá er :math:`{\mathcal{L}}f` fágað á menginu
:math:`\{s\in {{\mathbb  C}};{{\operatorname{Re\, }}}s>c\}` og

.. math::

  \dfrac{d^k}{ds^k}{\mathcal{L}}\{f\}(s)=
   (-1)^k{\mathcal{L}}\{t^kf(t)\}(s), \qquad {{\operatorname{Re\, }}}s>c.


  

--------------

Nokkur mikilvæg dæmi
~~~~~~~~~~~~~~~~~~~~

Reiknum nú út nokkrar Laplace-myndir:

Ef :math:`\alpha\in {{\mathbb  R}}` og :math:`\alpha>-1`, þá er

.. math::

  \begin{aligned}
   {\mathcal{L}}\{t^\alpha\}(s)
   &=\int_0^\infty e^{-st}t^\alpha \, dt =
   \dfrac 1{s^{\alpha+1}} \int_0^\infty e^{-st}(st)^\alpha \, s dt \\
   &=
   \dfrac 1{s^{\alpha+1}} \int_0^\infty e^{-\tau}\tau^\alpha \,  d\tau =
   \dfrac {\Gamma(\alpha+1)}{s^{\alpha+1}}.\end{aligned}

Ef :math:`{\alpha}` er heiltala, þá verður þessi formúla

.. math::

  {\mathcal{L}}\{t^\alpha\}(s)
   =\dfrac {\alpha!}{s^{\alpha+1}}.

Fyrir sérhvert :math:`\alpha\in {{\mathbb  C}}` gildir

.. math::

  {\mathcal{L}}\{e^{\alpha t}\}(s)=
   \int_0^{\infty}e^{-st}e^{\alpha t}\, dt =
   \int_0^{\infty}e^{-(s-\alpha)t}\, dt =
   \left[\dfrac {-e^{-(s-\alpha)t}} {s-\alpha}\right]_0^{\infty}=
   \dfrac 1{s-\alpha},

og í framhaldi af þessu fáum við

.. math::

  \begin{aligned}
   {\mathcal{L}}\{\cos\beta t\}(s) &=
   \frac 12 {\mathcal{L}}\{e^{i\beta t}\}(s) +\frac 12{\mathcal{L}}\{e^{-i\beta t}\}(s)\\
   &=\frac 12\left[\dfrac 1{s-i\beta}+\dfrac 1{s+i\beta}\right]
   =\dfrac s{s^2+\beta^2},\\
   {\mathcal{L}}\{\sin\beta t\}(s) &=
   \frac 1{2i}{\mathcal{L}}\{e^{i\beta t}\}(s) -\frac 1{2i}{\mathcal{L}}\{e^{-i\beta t}\}(s)\\
   &=\frac 1{2i}\left[\dfrac 1{s-i\beta}-\dfrac 1{s+i\beta}\right]
   =\dfrac {\beta}{s^2+\beta^2},\\
   {\mathcal{L}}\{\cosh \beta t\}(s) &= 
   \frac 12 {\mathcal{L}}\{e^{\beta t}\}(s) +\frac 12{\mathcal{L}}\{e^{-\beta t}\}(s)\\
   &=\frac 12\left[\dfrac 1{s-\beta}+\dfrac 1{s+\beta}\right]
   =\dfrac s{s^2-\beta^2},\\
   {\mathcal{L}}\{\sinh \beta t\}(s) &= 
   \frac 1{2}{\mathcal{L}}\{e^{\beta t}\}(s) -\frac 1{2}{\mathcal{L}}\{e^{-i\beta t}\}(s)\\
   &=\frac 1{2}\left[\dfrac 1{s-\beta}-\dfrac 1{s+\beta}\right]
   =\dfrac \beta{s^2-\beta^2}.\end{aligned}

Við höfum almenna reiknireglu:

Setning
^^^^^^^

:math:`{\mathcal{L}}\{e^{\alpha t}f\}(s) = {\mathcal{L}}\{f\}(s-\alpha)`.

--------------

Útreikninga okkar hér að framan getum við nú tekið saman í litla töflu:

.. math::

  \begin{aligned}
   {\mathcal{L}}\{e^{\alpha t}t^{\beta}\}(s)
   &=\dfrac{\Gamma(\beta+1)}{(s-\alpha)^{\beta+1}},\\
   {\mathcal{L}}\{e^{\alpha t}\cos \beta t\}(s)
   &=\dfrac{s-\alpha}{(s-\alpha)^2+\beta^2},\\
   {\mathcal{L}}\{e^{\alpha t}\sin \beta t\}(s)
   &=\dfrac{\beta}{(s-\alpha)^2+\beta^2},\\
   {\mathcal{L}}\{e^{\alpha t}\cosh \beta t\}(s)
   &=\dfrac{s-\alpha}{(s-\alpha)^2-\beta^2},\\
   {\mathcal{L}}\{e^{\alpha t}\sinh \beta t\}(s)
   &=\dfrac{\beta}{(s-\alpha)^2-\beta^2}.\end{aligned}

Laplace-ummyndun er eintæk vörpun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _set:10.1.2:

Setning
^^^^^^^

Gerum ráð fyrir að föllin :math:`f,g\in C({{\mathbb  R}}_+)` séu bæði af
veldisvísisgerð og að til sé fasti :math:`c` þannig að

.. math:: {\mathcal{L}}f(s)={\mathcal{L}}g(s), \qquad s\in {{\mathbb  C}}, \quad {{\operatorname{Re\, }}}s\geq c.

Þá er :math:`f(t)=g(t)` fyrir öll :math:`t\in {{\mathbb  R}}_+`.

--------------

Þessa setningu má einnig orða þannig að Laplace-ummyndun er eintæk
vörpun á mengi allra samfelldra falla af veldisvísisgerð. 

Ef við sjáum
að eitthvert fall :math:`F(s)` er Laplace-mynd af samfelldu falli
:math:`f`, þá segir setningin okkur að :math:`f` er ótvírætt ákvarðað og
við köllum þá :math:`f` *andhverfa Laplace-mynd* af fallinu :math:`F` og
skrifum :math:`f(t)={\mathcal{L}}^{-1}\{F\}(t)`.

Heaviside-fallið
~~~~~~~~~~~~~~~~

Fallið :math:`H:{{\mathbb  R}}\to {{\mathbb  R}}`, sem skilgreint er með

.. math::

  H(t)=\begin{cases} 1, &t\geq 0,\\ 0, & t<0,\end{cases}

  

kallast *Heaviside–fall*. Athugum að hliðrun
þess :math:`H_a(t)=H(t-a)` uppfyllir

.. math::

  H_a(t)=\begin{cases} 1, &t\geq a,\\ 0, & t<a,\end{cases}

  

og því er Laplace-mynd þess

.. math::

  {\mathcal{L}}H_a(s)= \int_a^{\infty} e^{-st}\, dt= \dfrac{e^{-as}} s, \qquad a>0.


  

Við fáum reyndar almenna reiknireglu:

Setning
^^^^^^^

Látum :math:`f:{{\mathbb  R}}_+\to {{\mathbb  C}}` vera fall af
veldisvísisgerð. Þá gildir um sérhvert :math:`a\geq 0` að

.. math:: {\mathcal{L}}\{H(t-a)f(t-a)\}(s) = e^{-as}{\mathcal{L}}\{f\}(s).

þar sem fallið :math:`t\mapsto H(t-a)f(t-a)` tekur gildið :math:`0`
fyrir öll :math:`t<a`.

Laplace-ummyndun af vigur- og fylkjagildum vörpunum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`u=(u_1,\dots,u_m): {{\mathbb  R}}_+\to {{\mathbb  C}}^m` er
vigurgilt fall á jákvæða raunásnum, þá skilgreinum við Laplace-mynd
:math:`u` með því að taka Laplace-mynd af hnitaföllunum,

.. math:: {\mathcal{L}}u(s)=({\mathcal{L}}u_1,\dots,{\mathcal{L}}u_m).

Við förum eins að við að skilgreina Laplace-mynd af
:math:`p\times m`-fylkjagildu falli :math:`U=(u_{jk})_{j,k=1}^{p,m}`,
þar sem við skilgreinum :math:`{\mathcal{L}}U(s)` sem :math:`p\times m`
fylkjagilda fallið

.. math:: {\mathcal{L}}U(s)=({\mathcal{L}}u_{jk}(s))_{j,k=1}^{p,m}.

Ef :math:`A` er :math:`p\times m` fylki, þá er

.. math::

  {\mathcal{L}}\{Au\}(s)=A{\mathcal{L}}u(s).


  

Þessa reglu sönnum við með því að líta á :math:`v=Au`,
:math:`v_j=a_{j1}u_1+\cdots+a_{jm}u_m` og notfæra okkur að
Laplace-ummyndunin er línuleg vörpun. Það gefur okkur
:math:`{\mathcal{L}}v_j(s)=a_{j1}{\mathcal{L}}u_1(s)+\cdots+a_{jm}{\mathcal{L}}u_m(s)`.
Vinstri hliðin í þessari jöfnu er þáttur númer :math:`j` í vinstri hlið
jöfnunnar, en hægri hliðin er þáttur númer :math:`j` í hægri hlið
hennar.

Ef hins :math:`A` er eitthvert :math:`q\times p` fylki, þá fæst reglan

.. math::

  {\mathcal{L}}\{AU\}(s)=A{\mathcal{L}}U(s).


  

Upphafsgildisverkefni
---------------------

Upphafsgildisverkefni
~~~~~~~~~~~~~~~~~~~~~

Nú skulum við snúa okkur að kjarna málsins, en það er að taka fall
:math:`f\in C^ 1({{\mathbb  R}}_+)` af veldisvísisgerð og reikna út heildið

.. math::

  \begin{aligned}
   \int_0^ b e^{-st}f{{^{\prime}}}(t)\, dt &=
   \left[e^{-st}f(t)\right]_0^ b+
   \int_0^ b se^{-st}f(t)\, dt \\
   &=
   s\int_0^ b e^{-st}f(t)\, dt -f(0)+e^{-sb}f(b).\end{aligned}

Ef :math:`{{\operatorname{Re\, }}}s` er nógu stórt, þá getum við látið
:math:`b\to \infty` og fáum því

.. math::

  {\mathcal{L}}\{f{{^{\prime}}}\}(s)=s{\mathcal{L}}\{f\}(s)-f(0).


  

Ef við gerum ráð fyrir að :math:`f\in C^2({{\mathbb  R}}_+)` og að bæði
:math:`f` og :math:`f{{^{\prime}}}` séu af veldisvísisgerð, þá fáum
við með því að beita þessari formúlu tvisvar að

.. math::

  {\mathcal{L}}\{f{{^{\prime\prime}}}\}(s)=s{\mathcal{L}}\{f{{^{\prime}}}\}(s)-f{{^{\prime}}}(0)=s^ 2{\mathcal{L}}\{f\}(s)
   -sf(0)-f{{^{\prime}}}(0),


  

og með þrepun fáum við síðan:

Setning
^^^^^^^

Ef :math:`f\in C^ m({{\mathbb  R}}_+)` og
:math:`f, f{{^{\prime}}}, f{{^{\prime\prime}}}, \dots, f^{(m-1)}`, eru af veldisvísisgerð, þá er
:math:`{\mathcal{L}}\{f^{(m)}\}(s)` skilgreint fyrir öll
:math:`s\in {{\mathbb  C}}` með :math:`{{\operatorname{Re\, }}}s` nógu
stórt og

.. math::

  {\mathcal{L}}\{f^{(m)}\}(s)=s^
   m{\mathcal{L}}\{f\}(s)-s^{m-1}f(0)-\cdots-sf^{(m-2)}(0)-f^{(m-1)}(0).

  

--------------

Áður en við snúum okkur að því að leysa afleiðujöfnuhneppi með
Laplace-ummyndun, skulum við líta á veldisvísisfylkið:

Setning
^^^^^^^

Um sérhvert :math:`m\times m` fylki :math:`A` gildir

.. math::

  {\mathcal{L}}\{e^{tA}\}(s) = (sI-A)^{-1}.


  

--------------

Green–fallið og földun
----------------------

Green–fallið og földun
~~~~~~~~~~~~~~~~~~~~~~

Lítum nú á afleiðujöfnu með fastastuðla

.. math::

  P(D)u=(a_mD^m+\cdots+a_1D+a_0)u=f(t),

  

með upphafsskilyrðunum

.. math::

  u(a)=b_0, u{{^{\prime}}}(a)=b_1,\  \dots,  \  u^{(m-1)}(a)=b_{m-1}.

  

Með því að hliðra til tímaásnum, þ.e. skipta á fallinu :math:`u(t)` og
:math:`u(t-a)`, þá getum við gert ráð fyrir að :math:`a=0`.

Við höfum sýnt fram á að fallið :math:`u_p` sem uppfyllir
:math:`P(D)u=f(t)`, með óhliðruðu upphafsskilyrðunum
:math:`b_0=\cdots=b_{m-1}=0` er gefið með formúlunni

.. math::

  u_p(t)=\int_0^tG(t,\tau) f(\tau)\, d\tau,

  

þar sem :math:`G` er Green–fall virkjans :math:`P(D)`. Við skulum nú
reikna út :math:`U_p(s)={\mathcal{L}}\{u_p\}(s)`. Vegna þess að
upphafsgildin eru öll :math:`0`, þá er

.. math::

  {\mathcal{L}}\{u_p{{^{\prime}}}\}(s)=sU_p(s), \quad 
   {\mathcal{L}}\{u_p{{^{\prime\prime}}}\}(s)=s^2U_p(s),\dots,
   {\mathcal{L}}\{u_p^{(m)}\}(s)=s^mU_p(s).

Þetta gefur okkur að

.. math:: {\mathcal{L}}\{P(D)u_p\}(s)=(a_ms^m+\cdots+a_1s+a_0)U_p(s)={\mathcal{L}}f(s),

sem er greinilega jafnan

.. math:: P(s)U_p(s)={\mathcal{L}}f(s),

og við fáum

  

.. math:: {\mathcal{L}}\{u_p\}(s)=\dfrac {{\mathcal{L}}f(s)}{P(s)}.

Nú er Green–fallið :math:`G(t,\tau)=g(t-\tau)`, þar sem :math:`g`
uppfyllir

.. math::

  P(D)g=0, \  g(0)=g{{^{\prime}}}(0)=\cdots=g^{(m-2)}(0)=0, \ g^{(m-1)}(0)=\dfrac 1{a_m}.

Ef við setjum :math:`U(s)={\mathcal{L}}g(s)`, þá fáum við

.. math::

  \begin{aligned}
   {\mathcal{L}}\{g{{^{\prime}}}\}(s) &= s{\mathcal{L}}\{g\}(s)-g(0)=sU(s),\\
   {\mathcal{L}}\{g{{^{\prime\prime}}}\}(s) &= s^2{\mathcal{L}}\{g\}(s)-sg(0)-g{{^{\prime}}}(0)\\
   &=s^2U(s),\\
   &\qquad \vdots\qquad\qquad\vdots\qquad\qquad \vdots\\
   {\mathcal{L}}\{g^{(m-1)}\}(s) &=
   s^{m-1}{\mathcal{L}}\{g\}(s)-s^{m-2}g(0)-\cdots-g^{(m-2)}(0)\\
   &=s^{m-1}U(s),\\
   {\mathcal{L}}\{g^{(m)}\}(s) &=
   s^m{\mathcal{L}}\{g\}(s)-s^{m-1}g(0)-\cdots-g^{(m-1)}(0)\\
   &=s^mU(s)-\dfrac 1{a_m}.\end{aligned}

Við tökum nú Laplace-myndina af báðum hliðum jöfnunnar :math:`P(D)g=0`
og fáum

.. math:: (a_ms^mU(s)-1)+a_{m-1}s^{m-1}U(s)+\cdots+a_1sU(s)+a_0U(s)=0,

og við fáum :math:`P(s)U(s)=1`, sem jafngildir

  

.. math:: {\mathcal{L}}g(s)=\dfrac 1{P(s)}.

Við höfum því sýnt fram á að

.. math::

  {\mathcal{L}}\left\{\int_0^tg(t-\tau)f(\tau)\, d\tau\right\}(s)= {\mathcal{L}}\{u_p\}(s)=
   {\mathcal{L}}\{g\}(s){\mathcal{L}}\{f\}(s).

Þessi formúla er engin tilviljun, því við höfum:

  

Setning
^^^^^^^

Ef :math:`f` og :math:`g` eru föll af veldisvísisgerð og heildanleg á
sérhverju bili :math:`[0,b]`, þá er

.. math::

  {\mathcal{L}}\left\{\int_0^tf(t-\tau)g(\tau)\, d\tau\right\}(s)=
   {\mathcal{L}}\{f\}(s){\mathcal{L}}\{g\}(s).

--------------

Athugið að

.. math::

  \int_0^t f(t-\tau)g(\tau) \, d\tau=
   \int_0^t f(\tau)g(t-\tau) \, d\tau.

Með því að velja :math:`g(t)=1` og nota að :math:`{\mathcal{L}}\{1\}=1/s`,
þá fæst:

Fylgisetning
^^^^^^^^^^^^

Ef :math:`f` er af veldisvísisgerð og heildanlegt á sérhverju bili
:math:`[0,b]`, þá er

.. math::

  {\mathcal{L}}\left\{\int_0^t f(\tau) \, d\tau\right\}(s) = \dfrac 1s
   {\mathcal{L}}\{f\}(s).


  

--------------

:hover:`Földun,földun` tveggja falla
:math:`f, g: {{\mathbb  R}}\to {{\mathbb  C}}` er skilgreind með
formúlunni

.. math:: f\ast g(t)=\int_{-\infty}^{+\infty}f(t-\tau)g(\tau) \, d\tau,

og talan :math:`t` liggur í skilgreiningarmengi :math:`f\ast g` ef heildið
er samleitið. 

Ef :math:`f` er til dæmis heildanlegt á
:math:`{{\mathbb  R}}` og :math:`g` er takmarkað, þá er földunin vel
skilgreind fyrir öll :math:`t\in {{\mathbb  R}}`. 

Ef föllin :math:`f` og
:math:`g` eru bæði skilgreind og heildanleg á :math:`{{\mathbb  R}}_+`,
þá getum við framlengt skilgreiningarsvæði þeirra yfir í allt
:math:`{{\mathbb  R}}` með því að setja :math:`f(t)=g(t)=0` fyrir öll
:math:`t<0`. 

Þá er :math:`f\ast g(t)` skilgreint fyrir öll
:math:`t\in {{\mathbb  R}}` og

.. math:: f\ast g(t)= \int_0^tf(t-\tau)g(\tau)\, d\tau.

Við getum því umritað síðustu setningu í

  

.. math:: {\mathcal{L}}\{f\ast g\}={\mathcal{L}}\{f\}{\mathcal{L}}\{g\}.


