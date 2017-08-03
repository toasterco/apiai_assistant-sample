|Logo|

===============================
 apiai_assistant sample project
===============================

|GitHub-Status| |GitHub-Stars| |GitHub-Forks|

|LICENCE|

``apiaiassistant-sample`` is a very basic sample use of the `apiai_assistant <https://pypi.python.org/pypi/apiai_assistant>`__ library.

------------------------------------------

.. contents:: Table of contents
   :backlinks: top
   :local:


Installation
============

.. code:: sh

    pip install -r requirements.txt -t .


Points of interests
===================

- `Processing the API.ai request <https://github.com/toasterco/apiaiassistant-sample/blob/master/handlers/assistant_webhook.py#L16>`__

- `Declaring the Assistant instance <https://github.com/toasterco/apiaiassistant-sample/blob/master/agent/__init__.py#L5>`__

- `Start intent <https://github.com/toasterco/apiaiassistant-sample/blob/master/agent/actions/start.py#L5>`__

- `Animal Info intent <https://github.com/toasterco/apiaiassistant-sample/blob/master/agent/actions/animal_info.py#L24>`__

- `Animal Wiki Corpus <https://github.com/toasterco/apiaiassistant-sample/blob/master/corpora/animal_wiki_corpus.json>`__

Usage
=====

Creating the API.ai agent
~~~~~~~~~~~~~~~~~~~~~~~~~

Download apiaiassistant-sample.zip

Initial Setup

- Navigate to `API.ai <https://api.ai/>`__

- Sign up for free (we recommend doing it with a Google account)

- Click on the **Integrations** tab on the left hand side

- Toggle **Actions on Google** and follow the setup wizard

Import the agent

- Click **Create Agent** at the top left below the logo (or the '+' sign)

- Input an agent name and click **Save**

- Click on gear icon right of your agent's name at the top left, below the logo

- Click on the third tab, **Export and Import**

- Click **RESTORE FROM ZIP**

- **SELECT FILE** and select the apiaiassistant-sample ZIP file you downloaded from this repo

- Type "RESTORE" and then click **Restore**

- Click **Done**


Setting up fulfillment
~~~~~~~~~~~~~~~~~~~~~~

Using the existing deployed webhook

- Click on the **Fulfillment** tab

- Toggle **Enabled**

- Fill the form with the following data

.. code::

    URL: https://apiaiassistant-sample.appspot.com/webhooks/assistant
    HEADERS:
      key: magickey
      value: catwikisample

- Click **Save**


Using your own deployed webhook

- Clone this repo

- Install the `Cloud SDK <https://cloud.google.com/sdk/downloads>`__

- Run:
      :code:`gcloud config set account $YOUR_AOG_ACCOUNT`

      :code:`gcloud config set project $YOUR_AOG_PROJECT`

- Navigate to the root of the cloned repo and run :code:`gcloud app deploy app.yaml`

- Now follow the steps above but use the url of your own webhook when filling the fulfillment form


Testing the agent
~~~~~~~~~~~~~~~~~

At this point you can already test the agent throught the API.ai console (the input box at the top right of the page)

To test the agent and have it available as the dev version on your own Assistant device, do the following

- Click on the **Integrations** tab on the right hand side

- Click on the **Actions on Google** integration

- Click **Update**

- Click **Visit Console**

- Now on the Actions on Google console, click **TEST**

- You can now invoke the agent from the Dialog box


FAQ and Known Issues
====================


- I don't have a :code:`$YOUR_AOG_ACCOUNT`

  ``$YOUR_AOG_ACCOUNT is the account you used to sign up for API.ai and the one you used to enable the Actions on Google integration``

- I don't have a :code:`$YOUR_AOG_PROJECT`

  ``$YOUR_AOG_PROJECT is the Actions on Google project created when setting up the Actions on Google integration``

- I can't see the basic card rich response on API.ai

  ``API.ai doesn't send capabilities in the POST payload when testing the agent through the API.ai console``

- How can I use it on my Assistant device (Google Home, phone, other devices)

  ``The logged in user on your Assistant device must be part of the Actions on Google project``

If you come across any other difficulties, browse/open issues
`here <https://github.com/toasterco/apiaiassistant-sample/issues?q=is%3Aissue>`__.

Contributions
=============

All source code is hosted on `GitHub <https://github.com/ToasterCo/apiaiassistant-sample>`__.
Contributions are welcome.

See the
`CONTRIBUTING <https://raw.githubusercontent.com/toasterco/apiaiassistant-sample/master/CONTRIBUTING.md>`__
file for more information.


LICENCE
=======

Open Source : |LICENCE|

.. |Logo| image:: https://raw.githubusercontent.com/toasterco/apiaiassistant/master/images/apiaiassistant-logo.png
   :height: 180px
   :width: 180 px
   :alt: apiaiassistant logo

.. |GitHub-Status| image:: https://img.shields.io/github/tag/toasterco/apiaiassistant.svg?maxAge=2592000
   :target: https://github.com/toasterco/apiaiassistant/releases

.. |GitHub-Forks| image:: https://img.shields.io/github/forks/toasterco/apiaiassistant.svg
   :target: https://github.com/toasterco/apiaiassistant/network

.. |GitHub-Stars| image:: https://img.shields.io/github/stars/toasterco/apiaiassistant.svg
   :target: https://github.com/toasterco/apiaiassistant/stargazers

.. |LICENCE| image:: https://img.shields.io/pypi/l/apiaiassistant.svg
   :target: https://raw.githubusercontent.com/toasterco/apiaiassistant/master/LICENCE
