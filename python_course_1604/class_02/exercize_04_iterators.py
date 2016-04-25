'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Please modify below function to implement quit and skip command to behava as
# speicified in the function documentation.


def execute_commands(commands):
    """ Executes given commands.

    If 'ping' command is given then it prints 'pong'
    In all other it prints 'error'

    The function exits when given sequence of commands terminates.

    Please use both continue and break to complete this exercize
    """

    iterator = iter(commands)

    while True:
        # HINT: implement iteration here
        try:
            command = next(iterator)
        except StopIteration:
            break

        if command == 'ping':
            print('pong')
        else:
            print('error')
