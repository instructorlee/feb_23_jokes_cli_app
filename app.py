from data import Data
from joke import Joke

data_handler = Data('jokes_data') # persisting data


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
        for index in range(0, len(Joke.jokes)):
            print(f"{index + 1}: {Joke.jokes[index].text}")

    elif command == 'add':
        if param_1:
            Joke.create(param_1)

    elif command == 'delete':
        Joke.delete(int(param_1))
            
    elif command == 'update':
        Joke.update(int(param_1), param_2)

    elif command == 'quit':
        is_playing = False

    else:
        print("Invalid Command")

print( "You are one funny guy!" )     


"""
### test flow

- Remove jokes_data.json

- add a joke - add::{joke text}
- list  : should see added joke; list should begin with 1 

- add another joke - add::{joke text}
- list  : should see 2 jokes; list should begin with 1 

- update the joke - update::{joke id}::{new text}
- list  : should see updated joke; list should begin with 1 

- delete first joke - delete::{joke id}
- list  : should see second joke; list should begin with 1 
"""