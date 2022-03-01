================
Mux Video XBlock
================

XBlock for the easy integration of the `Mux <https://mux.com>`__ video platform with `Open edX <https://open.edx.org>`__. This XBlock is extremely lightweight, because it inherits from the official `lti-consumer XBlock <https://github.com/openedx/xblock-lti-consumer>`__. A couple settings simplify the configuration of the XBlock, such that instructors do not have to fiddle with many LTI parameters.

Installation
============

::

    pip install -e git+https://github.com/strata-kk/mux-videos-xblock

In the Open edX Studio, go to Settings -> Advanced Settings -> Advanced modules and add "mux" to the list. You should now be able to add "Mux video" advanced units to your course.

Configuration
=============

The following optional settings may be added to your LMS/CMS for a smoother integration.

``LTI_DEFAULT_PASSPORT_ID``
---------------------------

Default: ``""`` (empty string)

Default ID of the LTI passport to use in all LTI applications.

``LTI_DEFAULT_MUX_PASSPORT_ID``
-------------------------------

Default: ``""`` (empty string)

Default ID of the LTI passport to use in all Mux LTI applications.

``LTI_DEFAULT_PRODUCER_LAUNCH_URL``
-----------------------------------

Default: ``"/lti/1.1/launch"`` (empty string)

Default launch url of the LTI producer. Note that if you want to include the LTI producer in an iframe, then the LTI producer must be running in a subdomain of the LMS and the CMS.

License
=======

The code in this repository is licensed under version 3 of the AGPL unless otherwise noted. See the LICENSE.txt file for details.
