Chapter of examples (tutorial)
=======

Section
-------

Subsection
~~~~~~~~~~

Text

Extensions
----------

MathJax
~~~~~~~

In text :math:`2` or

.. math::
	4+4+3


Sage-cell extensions 
--------------------

For the pdf-version the applets can be changed for static images.

R
~~~~

.. sagecell::
    :lang: R

    4+4
    
Sage
~~~~

Sage example by `Marshall Hampton <http://wiki.sagemath.org/interact/graphics#Curves_of_Pursuit>`_.

.. sagecell::

    html('<h2>Tangent line grapher</h2>')
    @interact
    def tangent_line(f = input_box(default=sin(x)), xbegin = slider(0,10,1/10,0), xend = slider(0,10,1/10,10), x0 = slider(0, 1, 1/100, 1/2)):
        prange = [xbegin, xend]
        x0i = xbegin + x0*(xend-xbegin)
        var('x')
        df = diff(f)
        tanf = f(x0i) + df(x0i)*(x-x0i)
        fplot = plot(f, prange[0], prange[1])
        print 'Tangent line is y = ' + tanf._repr_()
        tanplot = plot(tanf, prange[0], prange[1], rgbcolor = (1,0,0))
        fmax = f.find_local_maximum(prange[0], prange[1])[0]
        fmin = f.find_local_minimum(prange[0], prange[1])[0]
        show(fplot + tanplot, xmin = prange[0], xmax = prange[1], ymax = fmax, ymin = fmin)

Octave
~~~~~~

.. warning::
	Plotting in Octave is not working at the moment

.. sagecell::
    :lang: octave

    A = [ 1, 1, 2; 3, 5, 8; 13, 21, 34 ]
    B = rand (3, 2)
    A*B

Hoverrole Extension
~~~~~~~~~~~~~~~~~~~
Þetta er texti um :hover:`stærðfræðigreiningu` og :hover:`afleiðujöfnur, deildajafna`. Fleiri hugtök: :hover:`heildi`, :hover:`ferill`, :hover:`vörpun`.

Auto-generated list of translated terms:

.. hoverlist::

Sphinx ScrollDepth Extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This extension tracks how far users have scrolled on the page. When a new section is scrolled into view a Google Analytics event is fired. These events can be seen in real time in the Javascript console (Chrome: CTRL+Shift+I OR Options-> More Tools -> Developer Tools).

Don't forget to replace the tracking code snippet with your own. Your tracking code can be found at analytics.google.com under Admin-> Tracking Info-> Tracking Code.

Tracking PDF-downloads
~~~~~~~~~~~~~~~~~~~~~~
File downloads can be easily tracked with Google Analytics. See example below.

The following code:

.. code-block:: html
    
    .. raw:: html

        <a href="_static/NAME.pdf" onclick="var that=this;ga('send','event','Download','PDF',this.href);setTimeout(function(){location.href=that.href;},400);console.log('PDF-download tracked');return false;">PDF-útgáfa</a>

Results in the link below with Google Analytics tracking. Try opening the Javascript Console (Chrome: CTRl+Shift+I) and clicking the link.

.. raw:: html

    <a href="_static/NAME.pdf" onclick="var that=this;ga('send','event','Download','PDF',this.href);setTimeout(function(){location.href=that.href;},400);console.log('PDF-download tracked');return false;">PDF-útgáfa</a>


  
