import argparse
# NOTE: This starter code is intentionally incomplete so all tests fail.
# Students will need to define the parser, subcommands, and handlers.

# TODO: Import the argparse module

# TODO: Define the add_task function
# This function should accept 'args' and print: ✅ Task added: <description>

# TODO: Define the list_tasks function
# This function should accept 'args' and print: 📋 Listing all tasks...

# TODO: Define the main() function
# Inside main():
# - Create an ArgumentParser with a helpful description
# - Add subparsers for "add" and "list" commands
# - For "add", require a "description" argument and set its handler
# - For "list", just set the handler to list_tasks
# - Parse the arguments and call the appropriate handler (if exists)


def add_task(args) :
    print(f'✅ Task added : {args.description}')

def list_tasks(args) :
    print(f'Listing all tasks...')

def main() :
    parser = argparse.ArgumentParser(description='Tak Manager CLI')
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser('add' , help='Add new task')
    add_parser.add_argument('description' ,  help='Description of the task')
    add_parser.set_defaults(func=add_task)

    list_parser = subparsers.add_parser('list' , help='Lists all tasks')
    list_parser.set_defaults(func=list_tasks)

    args = parser.parse_args()

    if hasattr(args, 'func') :
        args.func(args)
    else :
        parser.print_help()
