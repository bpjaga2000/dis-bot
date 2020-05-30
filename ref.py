import json

a=json.dumps(
    {
    "allplayers": {
        "76561198874136060": {
            "clan": "OCEAN MINT",
            "name": "karl alfred",
            "observer_slot": 6,
            "team": "T"
        },
        "76561197961138901": {
            "clan": "Invalid0",
            "name": "3rk00-Twitch",
            "observer_slot": 7,
            "team": "T"
        },
        "76561198886064875": {
            "name": "rexy^^",
            "observer_slot": 8,
            "team": "T"
        },
        "76561198120208992": {
            "name": "maestro.",
            "observer_slot": 1,
            "team": "CT"
        },
        "76561198121310094": {
            "name": "MUFKAR :yin_yang:",
            "observer_slot": 2,
            "team": "CT"
        },
        "76561198103447590": {
            "name": "Hamburgeri",
            "observer_slot": 3,
            "team": "CT"
        },
        "76561198008427776": {
            "name": "MorfiuM",
            "observer_slot": 4,
            "team": "CT"
        },
        "76561197980459971": {
            "clan": "Invalid0",
            "name": "MATTEKUZMO @ twitch.tv",
            "observer_slot": 9,
            "team": "T"
        },
        "76561198106035981": {
            "clan": "H3LTGAL1",
            "name": "OfficialK1J",
            "observer_slot": 0,
            "team": "T"
        },
        "76561198365357203": {
            "name": "BerryBoba <3",
            "observer_slot": 5,
            "team": "CT"
        }
    }
})

print(json.loads(a))
b=json.loads(a)['allplayers']
for i in b:
    print(i)
