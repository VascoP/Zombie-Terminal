import os

class InputMenu(object):
    def __init__(self, question, minlen):
        self.question = question
        self.minlen = minlen
        self.answer = None
        
        
    def show(self):
        print self.question + "\n"
        self.prompt()

           
    def prompt(self):
        self.answer = raw_input("> ")
        if len(self.answer) < self.minlen:
            os.system('clear')
            print "Too short!\n"
            self.show()
        else:
            self.confirm()
            

    def confirm(self):
        print "Your input is '%s'. Is this correct? (y/n)" % self.answer
        confirmation = raw_input("> ")
        
        if confirmation == "y":
            return self.answer
        elif confirmation == "n":
            os.system('clear')
            self.show()
        else:
            os.system('clear')
            self.confirm()


    def get_answer(self):
        return self.answer



class OptionsMenu(object):
    def __init__(self, question, options):
        self.question = question
        self.options = options
        self.choice = None


    def show(self):
        print self.question + "\n"
        for (index, option) in enumerate(self.options):
            print "[%d] %s" % (index, option)
        print ""
        self.prompt()


    def prompt(self):
        try:
            self.choice = int(raw_input("> "))
        except:
            self.choice = None

        if self.choice >= 0 and self.choice < len(self.options):
            self.confirm()
        else:
            os.system('clear')
            print "Choose a valid option!\n"
            self.show()


    def confirm(self):
        print "You chose '%s'. Is this correct? (y/n)" % self.options[self.choice]
        confirmation = raw_input("> ")

        if confirmation == "y":
            return self.options[self.choice]
        elif confirmation == "n":
            os.system('clear')
            self.show()
        else:
            os.system('clear')
            self.confirm()


    def get_answer(self):
        return self.options[self.choice]