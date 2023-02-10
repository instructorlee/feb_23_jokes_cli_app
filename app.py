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

    """
    line_parts.append('')
    line_parts.append('')  
    """

    command = line_parts[0]
    param_1 = line_parts[1] if len(line_parts) > 1 else None # null
    param_2 = line_parts[2] if len(line_parts) > 2 else None


    if command == 'list': # list
        pass

    elif command == 'add': # implement
        pass

    elif command == 'delete':
        pass

    elif command == 'update':
        pass

    elif command == 'quit':
        is_playing = False

    else:
        print("Invalid Command")


"""
    - add, list, update, delete
    - print "invalid command"
    - Use the 'pass' keyword to replace future functionality.

    IF Statements
"""

print( "You are one funny guy!" )     

"""
 swtich(command) {

     case 'list':
         cde

    case 'edit':
        code
 }

"""