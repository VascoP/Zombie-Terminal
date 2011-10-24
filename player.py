from menu import InputMenu, OptionsMenu
import os

class Player(object):
    def __init__(self):
        self.name = None
        self.job = None
        

    def give_name(self):
        menu = InputMenu("What is your name?", 3)
        menu.show()
        self.name = menu.get_answer()
        os.system('clear')


    def give_job(self):
        menu = OptionsMenu("You've just arrived at your house. You had to leave early from work due to the emergency quarantine.\n\nWhat is your job?", ["Engineer", "Doctor", "Policeman", "Professional athlete"])
        menu.show()
        self.job = menu.get_answer()
        os.system('clear')
    
        if self.job == "Engineer":
            self.intel = 100
            self.health = 100
            self.physical = 10
        elif self.job == "Doctor":
            self.intel = 50
            self.health = 150
            self.physical = 10
        elif self.job == "Policeman":
            self.intel = 30
            self.health = 100
            self.physical = 80
        elif self.job == "Professional athlete":
            self.intel = 10
            self.health = 100
            self.physical = 100


    def job_description(self):
        if self.job == "Engineer":
            print "You are an engineer, you can easily learn new skills and you can repair almost anything."
        elif self.job == "Doctor":
            print "You are a doctor, you are very healthy and you can heal yourself much faster then normal."
        elif self.job == "Policeman":
            print "You are a policeman, you can easily identify dangerous situations and you have access to firearms."
        elif self.job == "Professional athlete":
            print "You are a professional athlete, your reactions fast, you are strong and you have great stamina."
        