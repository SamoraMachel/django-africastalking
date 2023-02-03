=====================
Django AfricasTalking
=====================

This SDK provides rest api implementation for the Africa's Talking APIs

Installation
-------------

To install this use ::

    pip install https://github.com/SamoraMachel/django-africastalking/archive/main.zip


Quick start
-----------

1. Add "africastalking" to your INSTALLED_APPS settings like this ::
    
    INSTALLED_APPS = [
        ...
        'aft_sms', # for the sms services
        'aft_payment' # for the payment services
    ]

2. Add the following configurations in your setting.py ::

    AFRICASTALKING = {
        "USERNAME": <your_username>,
        "API_KEY" : <your_api_key>,
        "SHORT_CODE": <your_short_code> # optional,
        "LIVE_URL": <africa's_talking_live_url> # https://api.africastalking.com/version1/,
        "SANDBOX_URL": <africa's_talking_sandbox_url> # https://api.sandbox.africastalking.com/version1/,
        "RETRY_DURATION": <integer_value_representing_number_hours_before_a_request_is_retried>
    }

3. Inside you ``app.urls`` add the configuration function :: 
   
    from aft_config import configure_aft
    configure_aft()

4. Include the Django Africa's Talking URLconf in your project urls.py like this ::

    path('sms/', include('aft_sms.urls')), # for the sms apis
    path('payment/', include('aft_payment.urls')) # for the payment apis

5. Run ``python manage.py migrate`` to create the Django Africa's Talking models

6. Start the development server and visit http://127.0.0.1:8000/admin/ to create sms and payments (you'll need the Admin app enabled)

