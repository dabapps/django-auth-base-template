django-auth-base-template
=========================

**Switchable logged in/logged out base templates for Django.**

**Author:** Jamie Matthews, [Follow me on Twitter][jamie-twitter].

[![Build Status][build-status-image]][travis]

Overview
========

Often, a web application includes some pages (corporate blogs, Terms & Conditions, FAQs etc) which should be visible to both logged in and logged out visitors. However, these pages should include different structural elements for each type of user. For example, logged out visitors might see a "Register Now!" link in the header, whereas authenticated users might see the application's navigation menus.

The DRYest way to do this is with the magic of Django's template inheritance. Everything common to both types of user should be in a global `base.html` template. Page elements only visible to logged in users should be in `logged_in_base.html`, while elements only visible to logged out users should be in `logged_out_base.html`. Both of these should extend `base.html`.

Finally, your actual site pages should extend either `logged_in_base.html` or `logged_out_base.html` depending on whether the current user is authenticated. This is where **django-auth-base-template** can help.

Installation
============

Install from PyPI:

    pip install django-auth-base-template

Add the context processor to your `TEMPLATE_CONTEXT_PROCESSORS` list:

    TEMPLATE_CONTEXT_PROCESSORS = [
        ...
        'auth_base_template.context_processors.auth_base_template',
        ...
    ]

Add two settings to identify the templates to use:

    LOGGED_IN_BASE_TEMPLATE = 'logged_in_base.html'
    LOGGED_OUT_BASE_TEMPLATE = 'logged_out_base.html'

Usage
=====

First, create a global `base.html` template for your site:

```
<!DOCTYPE html>
<html>
    <head><title>My Site</title></head>
    <body>
        <div>{% block header %}</div>
        <div>{% block content %}</div>
    </body>
</html>
```

Create `logged_out_base.html`:

```
{% extends "base.html" %}
{% block header %}
    Welcome to the site! Register <a href="/register/">here</a>
{% endblock %}
```

Create `logged_in_base.html`:

```
{% extends "base.html" %}
{% block header %}
    Welcome back, member!
{% endblock %}
```

Finally, create one of your actual site pages:

```
{% extends auth_base_template %}
{% block content %}
    Blog! You can see this whether
    you're logged in or not!
{% endblock %}
```

Done!

Changelog
=========

1.0.0
-----

* Initial release

License
=======

Copyright © DabApps.

All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this 
list of conditions and the following disclaimer in the documentation and/or 
other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[jamie-twitter]: http://twitter.com/j4mie
[travis]: http://travis-ci.org/dabapps/django-auth-base-template
[build-status-image]: https://secure.travis-ci.org/dabapps/django-auth-base-template.png
