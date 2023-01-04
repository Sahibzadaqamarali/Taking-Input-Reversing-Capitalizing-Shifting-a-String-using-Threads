import threading

class InputThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.string = None
  
  def run(self):
    try:
      # Get input from the user
      self.string = input("Enter a string: ")
    except Exception as e:
      print("Exception occurred in InputThread:", e)

class ReverseThread(threading.Thread):
  def __init__(self, input_thread):
    threading.Thread.__init__(self)
    self.input_thread = input_thread
  
  def run(self):
    # Reverse the string from the input thread
    reversed_string = self.input_thread.string[::-1]
    print("Reversed string:", reversed_string)

class CapitalThread(threading.Thread):
  def __init__(self, input_thread):
    threading.Thread.__init__(self)
    self.input_thread = input_thread
  
  def run(self):
    # Capitalize the string from the input thread
    capitalized_string = self.input_thread.string.upper()
    print("Capitalized string:", capitalized_string)

class ShiftThread(threading.Thread):
  def __init__(self, input_thread):
    threading.Thread.__init__(self)
    self.input_thread = input_thread
  
  def run(self):
    # Shift the characters in the string from the input thread by two
    shifted_string = ""
    for c in self.input_thread.string:
      shifted_string += chr(ord(c) + 2)
    print("Shifted string:", shifted_string)

# Create the input thread
input_thread = InputThread()

# Create the other threads and pass the input thread as an argument
reverse_thread = ReverseThread(input_thread)
capital_thread = CapitalThread(input_thread)
shift_thread = ShiftThread(input_thread)

# Start the input thread
input_thread.start()

# Wait for the input thread to finish
input_thread.join()

# Start the other threads
reverse_thread.start()
capital_thread.start()
shift_thread.start()

# Wait for the other threads to finish
reverse_thread.join()
capital_thread.join()
shift_thread.join()
