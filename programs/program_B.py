import subprocess
import statistics


def main():
    """
    Main function that coordinates the execution of Program B.

    Program B interacts with Program A, a separate pseudo-random number generator program.
    It sends commands to Program A, retrieves random numbers, processes them,
    and outputs statistical information.

    - Sends a "Hi" command to Program A and validates the response.
    - Sends "GetRandom" commands to retrieve 100 random integers from Program A.
    - Sends a "Shutdown" command to terminate Program A gracefully.
    - Outputs the sorted list of random numbers, as well as the median and average.

    Raises:
        FileNotFoundError: If Program A cannot be found or fails to start.
        Exception: If responses from Program A do not match expected format.
    """

    # Run program A
    try:
        process = subprocess.Popen(
            ['python3', 'program_A.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    except FileNotFoundError:
        raise FileNotFoundError('Could not find or execute Program A')

    # Define a function to send commands to program A and receive responses
    def send_command(command):
        """
        Sends a command to Program A and retrieves the response.

        Args:
            command (str): The command to send to Program A. Expected commands are "Hi",
                           "GetRandom", and "Shutdown".

        Returns:
            str: The response from Program A, stripped of any surrounding whitespace.
        """

        process.stdin.write(command + '\n')
        process.stdin.flush()
        return process.stdout.readline().strip()

    # Send the Hi command to Program A and verify the correct response
    response = send_command('Hi')
    if response != 'Hi':
        raise Exception('Invalid response to "Hi" command')

    # Retrieve 100 random numbers by sending the GetRandom command to Program A 100 times
    numbers = []
    for _ in range(100):
        response = send_command('GetRandom')
        try:
            numbers.append(int(response))
        except ValueError:
            raise Exception(f'Invalid response to "GetRandom" command: {response}')

    # Send the Shutdown command to Program A to terminate it
    send_command('Shutdown')
    process.wait()

    # Sort the list of retrieved random numbers and print the sorted list to the console
    numbers = sorted(numbers)
    print(f'Sorted list of numbers: {numbers}')

    # Calculate and print the median and average of the numbers
    median = statistics.median(numbers)
    average = statistics.mean(numbers)
    print(f'Median: {median}')
    print(f'Average: {average}')


# Run program B
if __name__ == '__main__':
    main()
