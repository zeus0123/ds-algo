from sendgrid import SendGridAPIClient

message = {
    'personalizations': [
        {
            'to': [
                {
                    'email': 'trishan.ghosh@tifinag.com'
                }
            ],
            'subject': 'Sending with Twilio SendGrid is Fun'
        }
    ],
    'from': {
        'email': 'salesteam@wealthcarecapital.com'
    },
    'content': [
        {
            'type': 'text/plain',
            'value': 'and easy to do anywhere, even with Python'
        }
    ],
    "headers": {
        "List-Unsubscribe-Post": "List-Unsubscribe=One-Click",
        "List-Unsubscribe": "<mailto:unsubscribetrishan.ghosh@tifinag.com>, <https://qa.myclout.com>"
    }
}
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))