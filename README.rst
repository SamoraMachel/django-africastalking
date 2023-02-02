=====================
Django AfricasTalking
=====================

This SDK provides rest api implementation for the Africa's Talking APIs

Installation
-------------

To install this use
`python
pip install django-aft
`

Quick start
-----------

1. Add "africastalking" to your INSTALLED_APPS settings like this::
    
    INSTALLED_APPS = [
        ...
        'aft_sms', # for the sms services
        'aft_payment' # for the payment services
    ]

2. Add the followin configurations in your setting.py

    AFRICASTALKING = {
        "USERNAME": <your_username>,
        "API_KEY" : <your_api_key>,
        "SHORT_CODE": <your_short_code> # optional,
        "LIVE_URL": <africa's_talking_live_url> # https://api.africastalking.com/version1/,
        "SANDBOX_URL": <africa's_talking_sandbox_url> # https://api.sandbox.africastalking.com/version1/
    }

    RETRY_DURATION_IN_HOURS = # number of hours before a request is retried e.g 1


3. Include the Django Africa's Talking URLconf in your project urls.py like this

    `python
    path('sms/', include('aft_sms.urls')), # for the sms apis
    path('payment/', include('aft_payment.urls')) # for the payment apis
    `

4. Run ``python manage.py migrate`` to create the Django Africa's Talking models

5. Start the development server and visit http://127.0.0.1:8000/admin/ to create sms and payments (you'll need the Admin app enabled)

