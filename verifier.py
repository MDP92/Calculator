
class Verifier:

    def AllowedButtons(button):

        switcher = {
                '(':True,
                ')':True,
                '+':True,
                '-':True,
                '*':True,
                '/':True,
                '.':True,
                '0':True,
                '1':True,
                '2':True,
                '3':True,
                '4':True,
                '5':True,
                '6':True,
                '7':True,
                '8':True,
                '9':True,
                # Keypad desktop PC
                '<96>':True,
                '<97>':True,
                '<98>':True,
                '<99>':True,
                '<100>':True,
                '<101>':True,
                '<102>':True,
                '<103>':True,
                '<104>':True,
                '<105>':True,
                # Keypad laptop PC
                'Key.insert':True,
                'Key.end':True,
                'Key.down':True,
                'Key.page_down':True,
                'Key.left':True,
                '<12>':True,
                'Key.right':True,
                'Key.home':True,
                'Key.up':True,
                'Key.page_up':True,
                
                'Key.backspace':True,
                'Key.shift':'shift'
             }
        return switcher.get(button,"Invalid button, press another one")


    def KeypadCast(string):
        if (string == '<96>') or (string == 'Key.insert'):
            string = '0'
        elif (string == '<97>') or (string == 'Key.end'):
            string = '1'
        elif (string == '<98>') or (string == 'Key.down'):
            string = '2'
        elif (string == '<99>') or (string == 'Key.page_down'):
            string = '3'
        elif (string == '<100>') or (string == 'Key.left'):
            string = '4'
        elif (string == '<101>') or (string == '<12>'):
            string = '5'
        elif (string == '<102>') or (string == 'Key.right'):
            string = '6'
        elif (string == '<103>') or (string == 'Key.home'):
            string = '7'
        elif (string == '<104>') or (string == 'Key.up'):
            string = '8'
        elif (string == '<105>') or (string == 'Key.page_up'):
            string = '9'
        return string
