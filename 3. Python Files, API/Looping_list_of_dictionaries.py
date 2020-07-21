weather = [
    {
        'date':'today',
        'state': 'cloudy',
        'temp': 68.5
    },
    {
        'date':'tomorrow',
        'state': 'sunny',
        'temp': 74.8
    }
]

for e in weather:
    #print(e)
    #for x,y in e.items():
    print(f"{e['date']}'s weather is {e['state']} and temerature is {e['temp']}")

# OUTPUT
# today's weather is cloudy and temerature is 68.5
# tomorrow's weather is sunny and temerature is 74.8