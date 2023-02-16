from data import Data
from joke import Joke

data_handler = Data('jokes_data') # persisting data

jokes = data_handler.get()

Joke.load()

is_playing = True

while ( is_playing ):
    line_input = input('command-> ').strip() #add::why did the chicken ....... #update::2::New JOke.......

    line_parts = line_input.split('::')

    # Last Thursday Office Hour
    command = line_parts[0]
    param_1 = line_parts[1] if len(line_parts) > 1 else None # null
    param_2 = line_parts[2] if len(line_parts) > 2 else None

    if command == 'list': 
        for index, joke in enumerate(Joke.jokes):
            print(f"{index}: {joke['text']}")

    elif command == 'add':
        if param_1:
            Joke.create(param_1)

    elif command == 'delete':
        del(jokes[int(param_1) - 1])
        data_handler.save(jokes)
            
    elif command == 'update':
        jokes[int(param_1) - 1] = {'text': param_2}
        data_handler.save(jokes)

    elif command == 'quit':
        is_playing = False

    else:
        print("Invalid Command")

print( "You are one funny guy!" )     
