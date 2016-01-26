.. _survey_design:

Survey Design
=============

One of the most important aspects of a geophysical survey is the design of the
survey. How the survey is layed out will impact the coupling with the target,
the detectability of the target, and the resolution. Therefore, it is
important to think about the transmitters, receiver, and what the sought
target is before doing a geophysical survey.

Some questions to think about that will influence the survey design:

- What am I looking for? How large is it? How deep is it?
- What geology is in my area?
- Is there a particular direction to the geology?
- What are the physical properties of my target and the other units?
- Is there ample contrast between the physical properties?
- Do I need a 2D or 3D survey?
- How much can I spend on a survey? Time? Money?

Detectability
-------------

In order for a target to be detectable, the secondary field (whether that be
the electric field, magnetic field, or voltage potential) must be larger than
the noise (geologic noise, instrument noise, etc) and it must be relatively
large enough compared to the primary field. For example, if the noise in the
primary field is anticipated to be 5% and the instrument sensitivity is 5 mV,
then the secondary field must at least be above 5 mV to be detectable but also
be more than 5% different compared to the primary field. This provides us with
two metrics: relative difference and absolute difference.

Relative difference (:math:`RD`) and absolute difference (:math:`AD`) are determined as follows:

.. math::
        RD = \frac{F^S}{F^P} * 100,
        :label: relative_detect

.. math::
        AD = F^S,
        :label: absolute_detect
     
where:

- :math:`F^S = F^T - F^P` is the secondary field
- :math:`F^P` is the primary field
- :math:`F^T` is the total field

To test whether the target is adequately detectable given a certain survey
layout, we use :ref:`forward modelling <forward_modelling>` to compute the
primary field using a model that does not contain the target and the total
field using a model that does contain the target.

Resolution
----------

While detectability is a key part in determining the usefulness of a given
survey design, it does not guarantee that we can recover the target by
:ref:`inverting <inversion>` the total field data. By inverting for the
sought-after target using synthetic modeling, we can determine if the survey
has enough resolution to recover the target.

Summary
-------

Drawbacks of survey design is that some knowledge of the sought-after target
is required. Large-scale, regional surveys will be more grid-based to cover a
great area but when trying to gather information about a particular target of
interest, it is important to have some a-priori knowledge (whether it be from
previous geophysical surveys, geological information, drilling, etc) to be
able to design an appropriate survey. In the end, spending time on survey
design will likely provide better information and recovery about the target.

For more information about survey design for specific geophysical methods, see
tthe following pages:

- :ref:`DC resistivity survey design <dcr_survey_design>`
- :ref:`Loop-loop FDEM survey design <looploopfdem_survey_design>`

        

 



