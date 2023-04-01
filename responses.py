import random


def get_response() -> str:
    responses = \
        ["@callmedaddy420#4175 is a bum",
         "@callmedaddy420#4175 kys",
         "@callmedaddy420#4175 suck my balls",
         "@callmedaddy420#4175 you're 3rd https://tenor.com/view/littleman17-fortnite-dance-gif-24840201"
         ]

    return responses[random.randint(0, 3)]
