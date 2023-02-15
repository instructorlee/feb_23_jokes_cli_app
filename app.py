jokes = [
    {
        'text': "Why did the chicken cross the road? To get to the ther side.",
    },
    {
        'text': "Why do golfers carry 2 pairs of socks? In case they get a hole in one.",
    }
]

is_playing = True

while ( is_playing ):
    line_input = input('command-> ').strip() #add::why did the chicken ....... #update::2::New JOke.......

    line_parts = line_input.split('::')

    # Last Thursday Office Hour
    command = line_parts[0]
    param_1 = line_parts[1] if len(line_parts) > 1 else None # null
    param_2 = line_parts[2] if len(line_parts) > 2 else None

    if command == 'list': 
        for index, joke in enumerate(jokes):
            print(f"{index}: {joke['text']}")

    elif command == 'add':
        if param_1:
            jokes.append({'text': param_1})

    elif command == 'delete':
        del(jokes[int(param_1) - 1])
            
    elif command == 'update':
        jokes[int(param_1) - 1] = {'text': param_2}

    elif command == 'quit':
        is_playing = False

    else:
        print("Invalid Command")

print( "You are one funny guy!" )     
