import subprocess
from subprocess import *
from time import sleep
from verifier import Verifier

# Check if the required package is installed;
# if not, install it and wait the end of the process
try:
    from pynput import keyboard
except ImportError:
    print("The required package is not installed, wait until the installation procedure is completed")
    subprocess.call('pip install pynput==1.6.8 -qq', shell=True)

    checkInstalledPackage = False
    while checkInstalledPackage == False:
        sleep(0.5)
        try:
            from pynput import keyboard
            checkInstalledPackage = True
            print("Done")
            print()
        except ImportError:
            pass


class Calculator():

    # Keypad encoding
    keypadButtons = ['<96>','<97>','<98>','<99>','<100>','<101>','<102>','<103>','<104>','<105>',
                              'Key.insert','Key.end','Key.down','Key.page_down','Key.left','<12>','Key.right',
                              'Key.home','Key.up','Key.page_up']


    insertedString = None

    def __init__(self):
        self.buffer = []
        self.openBrackets = []
        self.closeBrackets = []

    def onPress(self, key):
        #print("The pressed key is:", format(key)) --> Display the encoding of the buttons

        inputString = format(key)
        inputString = inputString.replace("'", "")

        allowedButton = Verifier.AllowedButtons(inputString)
        if allowedButton == True:
            if inputString in self.keypadButtons:
                inputString = Verifier.KeypadCast(inputString)

            ###################################
            # Check of 8 particular condition #
            ###################################

            # Add the bracket to the relevant list to allow the counting inside the expression
            if inputString == '(':
                self.openBrackets.append(inputString)
                self.buffer.append(inputString)

                self.DisplayExpression()

            elif inputString == ')':
                if len(self.openBrackets) > len(self.closeBrackets):
                    self.closeBrackets.append(inputString)
                    self.buffer.append(inputString)

                    self.DisplayExpression()
                    self.DisplayRealTimeValue()

            elif inputString == '*':
                self.buffer.append(inputString)
                # Max number of '*' allowed: 2; to calculate the exponentiation
                try:
                    if self.buffer[-1] == '*' and self.buffer[-2] == '*' and self.buffer[-3] == '*':
                        del self.buffer[-1]
                except IndexError:
                    pass

                self.DisplayExpression()

            elif inputString == '+':
                self.buffer.append(inputString)
                # Max number of '+' allowed: 1
                try:
                    if self.buffer[-1] == '+' and self.buffer[-2] == '+':
                        del self.buffer[-1]
                except IndexError:
                    pass

                self.DisplayExpression()

            elif inputString == '-':
                self.buffer.append(inputString)
                # Max number of '-' allowed: 1
                try:
                    if self.buffer[-1] == '-' and self.buffer[-2] == '-':
                        del self.buffer[-1]
                except IndexError:
                    pass

                self.DisplayExpression()

            elif inputString == '/':
                self.buffer.append(inputString)
                # Max number of '/' allowed: 1; for the floating point numbers
                try:
                    if self.buffer[-1] == '/' and self.buffer[-2] == '/':
                        del self.buffer[-1]
                except IndexError:
                    pass

                self.DisplayExpression()

            elif inputString == '.':
                self.buffer.append(inputString)
                # Max number of '.' allowed: 1; for the floating point numbers
                try:
                    if self.buffer[-1] == '.' and self.buffer[-2] == '.':
                        del self.buffer[-1]
                except IndexError:
                    pass

                self.DisplayExpression()

            elif inputString == 'Key.backspace':
                try:
                    del self.buffer[-1]
                except IndexError:
                    self.buffer = []
                finally:
                    self.DisplayExpression()
                    self.DisplayRealTimeValue()

            else:
                self.buffer.append(inputString)

                self.DisplayExpression()
                self.DisplayRealTimeValue()

        elif (str(key) == "Key.enter"):
            self.DisplayFinalValue()
            self.buffer = []

        elif str(key) == "Key.esc":
            print("End process")
            subprocess.Popen('cls', shell=True)
            return False

        elif allowedButton == 'shift':
            pass

        else:
            # Tell to the User that the pressed button isn't allowed
            print(allowedButton)

    def RunCalculator(self):
        print("Type an expression to start to calculate")
        print("Press ENTER to calculate the final value, BACKSPACE to delete the last inserted value and ESC to quit")
        print("Type '.' for the floating point number, type '**' for the exponentiation notation")
        print("The floating point results are rounded at 4 decimal digits")
        print("")
        with keyboard.Listener(
            on_press=self.onPress) as listener:
                listener.join()

    def DisplayExpression(self):
        mergeList = [''.join(self.buffer[0:len(self.buffer)])]
        self.insertedString = mergeList[0]
        print(f"Expression: {self.insertedString}")
        return self.insertedString

    def DisplayRealTimeValue(self):
        try:
            realTimeResult = round(eval(self.insertedString),4)
            print(f"Real time result: {realTimeResult}")
            return realTimeResult
        except SyntaxError:
            print("Real time value not available, please complete the expression")


    def DisplayFinalValue(self):
        try:
            finalResult = round(eval(self.insertedString),4)
            print("----------------------------------")
            print(f"Final expression: {self.insertedString}")
            print(f"Final result: {finalResult}")
            print("Type an expression to calculate it")
            print("----------------------------------")
            return finalResult
        except (SyntaxError, TypeError):
            print("Inserted expression not complete, try again")
