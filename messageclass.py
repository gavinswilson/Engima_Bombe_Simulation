from enigma.machine import EnigmaMachine

if __name__ == "__main__":
    print("This runs only when module.py is executed directly, not when imported.")

class Message:
    """
    Class to hold a message with its associated metadata and provide methods for encryption and decryption using an Enigma machine.
   
    """
    # Class variables (shared by all instances)
    fullciphertext = ""
    ciphertext = ""
    split_ciphertext = ""
    plaintext = ""
    indicator_setting = ""
    message_indicator_setting = ""
    indicator_setting_enc = ""
    indicator_setting_dec = ""
    date = ""
    time = ""
    interception_time = ""
    from_list = ""
    to_list = ""
    frequency = 0
    ringsettings = ''
    rotors = ''
    reflector = ''
    plugboardsettings = ''
    rotorposition = ''
    number_of_rotors = 0
    number_of_letters = 0
    discriminant = ''

    enigma = None
                           
                        
    def __init__(self):
        self.plaintext = None

    def decrypt(self):
        """
        Standard decryption procedure: take the first 6 characters with the daily settings and decrypt them into a repeated 3 letter phrase.
        Thich becomes the main message's indicator setting. 
        Then set the machine to the message's indicator setting and decrypt the rest of the ciphertext into plaintext.
   
        """
        self.split_ciphertext_parts()
        # get message and enrypted indicator
        self.enigma.set_display(self.rotorposition)
        #set to the given indicator setting from the unecrypted preamble and decrypt the encrypted indicator setting
        self.indicator_setting_dec = self.enigma.process_text(self.indicator_setting_enc)
        #6 character string which is repeated 3 letter indicator setting.
        self.message_indicator_setting = self.indicator_setting_dec[:3]
        # take the first set
        self.enigma.set_display(self.message_indicator_setting)
        # reset enigma to the new indicator settings using the daily settings and decrypt the rest of the ciphertext
        self.plaintext = self.enigma.process_text(self.ciphertext) 
    
    def split_ciphertext_parts(self):
        """
        Splits the full ciphertext into its component parts, In german wartime code, the first 6 letters of the full ciphertext are the encrypted indicator setting, and the rest is the actual ciphertext.
        """
        self.ciphertext = self.fullciphertext[6:]
        self.indicator_setting_enc = self.fullciphertext[:6]

    def split_ciphertext(self):
        # Split the full ciphertext into groups of 5 letters for viewing
        self.split_ciphertext = ' '.join(self.fullciphertext[i:i+5] for i in range(0, len(self.fullciphertext), 5))
    
    def check_number_of_letters(self):
        if self.number_of_letters == len(self.fullciphertext):
            return True
        else:            
            print(f"Warning: Number of letters specified ({self.number_of_letters}) does not match actual number of letters in full ciphertext ({len(self.fullciphertext)}).")
            return False
    def setup_enigma_machine(self):
        # Set up the Enigma machine with the daily settings
        self.enigma = EnigmaMachine.from_key_sheet(
            rotors=self.rotors,
            reflector=self.reflector,
            ring_settings=self.ringsettings,
            plugboard_settings=self.plugboardsettings
        )
    #---------------------------------------------------------------------------------------------------------------------------------
    # test-set-up for verification
    #---------------------------------------------------------------------------------------------------------------------------------


    def testsetup_bletchley_decrypt(self):
        #message settings
        self.set_date('1941-02-01')
        
        self.set_fullciphertext('mmbkbpfnzomyppcslpvbvcbzzljyweihfpbltafyxnpwftccldhxpgeusbwlatixmtunsefjhqaybiakbrxsuhwmvxjdrenwjwxukypld')
        
        self.set_frequency(7.035)
        self.set_interception_time('1941-02-01 12:15')
        
        self.set_from_list('U-123')
        self.set_to_list('Kriegsmarine HQ')
        self.set_time('12:00')
        self.set_number_of_letters(len(self.fullciphertext))    
        self.set_discriminant('QXT')
        self.set_indicator_setting('AQL')
        
        # daily settings
        self.set_rotors('VI I III')
        self.set_reflector('B')
        self.set_ringsettings('1 1 1')
        self.set_plugboardsettings('bq cr di ej kw mt os px uz gh')
        self.set_rotorposition(self.indicator_setting)
        self.setup_enigma_machine()



    #---------------------------------------------------------------------------------------------------------------------------------
    # Message Settings
    #---------------------------------------------------------------------------------------------------------------------------------
    
    def set_ciphertext(self, ciphertext): self.ciphertext = ciphertext
    def get_ciphertext(self): return self.ciphertext
    def set_fullciphertext(self, ciphertext): self.fullciphertext = ciphertext.upper()
    def get_fullciphertext(self): return self.fullciphertext
    def set_plaintext(self, plaintext): self.plaintext = plaintext
    def get_plaintext(self): return self.plaintext
    def set_indicator_setting(self, indicator_setting): self.indicator_setting = indicator_setting
    def get_indicator_setting(self): return self.indicator_setting
    def set_indicator_setting_enc(self, indicator_setting_enc): self.indicator_setting_enc = indicator_setting_enc
    def get_indicator_setting_enc(self): return self.indicator_setting_enc
    def set_indicator_setting_dec(self, indicator_setting_dec): self.indicator_setting_dec = indicator_setting_dec
    def get_indicator_setting_dec(self): return self.indicator_setting_dec
    def set_date(self, date): self.date = date
    def get_date(self): return self.date
    def set_time(self, time): self.time = time
    def get_time(self): return self.time
    def set_interception_time(self, interception_time): self.interception_time = interception_time
    def get_interception_time(self): return self.interception_time
    def set_from_list(self, from_list): self.from_list = from_list
    def get_from_list(self): return self.from_list
    def set_to_list(self, to_list): self.to_list = to_list
    def get_to_list(self): return self.to_list
    def set_frequency(self, frequency): self.frequency = frequency
    def get_frequency(self): return self.frequency
    def set_discriminant(self, discriminant): self.discriminant = discriminant
    def get_discriminant(self): return self.discriminant
    def set_number_of_letters(self, number_of_letters): self.number_of_letters = number_of_letters
    def get_number_of_letters(self): return self.number_of_letters
    
    
    
    #---------------------------------------------------------------------------------------------------------------------------------
    # machines daily settings
    #---------------------------------------------------------------------------------------------------------------------------------
    
    def set_ringsettings(self, ringsettings): self.ringsettings = ringsettings
    def get_ringsettings(self): return self.ringsettings
    def set_rotors(self, rotors): self.rotors = rotors
    def get_rotors(self): return self.rotors
    def set_reflector(self, reflector): self.reflector = reflector
    def get_reflector(self): return self.reflector
    def set_plugboardsettings(self, plugboardsettings): self.plugboardsettings = plugboardsettings
    def get_plugboardsettings(self): return self.plugboardsettings
    def set_rotorposition(self, rotorposition): self.rotorposition = rotorposition
    def get_rotorposition(self): return self.rotorposition


    #---------------------------------------------------------------------------------------------------------------------------------
    # Data printing functions
    #---------------------------------------------------------------------------------------------------------------------------------

    def printmessage(self, style):
        self.split_ciphertext()
        if style == "BletchleyPark":
            print(f"-------------- START --------------")
            print(f"Date: {self.date}")
            print(f"-------------- INTERCEPT OPERATORS ADDITIONS --------------")
            print(f"Frequency: {self.frequency} MHz")
            print(f"Interception Time: {self.interception_time}")
            print(f"-------------- UNENCIPHERED PREAMBLE --------------")
            print(f"Call Signs: From {self.from_list} To {self.to_list}")
            print(f"Time of origin: {self.time}")
            print(f"Number of Letters: {self.number_of_letters}")            
            print(f"Single or Multi-part: Part x of y")
            print(f"Discriminant: QXT")           
            print(f"Indicator Setting: {self.indicator_setting}")
            print(f"-------------- ENCIPHERED TEXT --------------")
            print(f"{self.split_ciphertext}")
            print(f"-------------- MACHINE SETTINGS --------------")
            print(f"Ring Settings: {self.ringsettings}")
            print(f"Rotors: {self.rotors}")
            print(f"Reflector: {self.reflector}")
            print(f"Plugboard Settings: {self.plugboardsettings}")
            print(f"-------------- MESSAGE INFORMATION --------------")
            print(f"Complete Ciphertext: {self.fullciphertext}")
            print(f"Encrypted Indicator Setting: {self.indicator_setting_enc}")
            print(f"Ciphertext: {self.ciphertext}")
            print(f"Decrypted Indicator Setting: {self.indicator_setting_dec}")
            print(f"Recovered Indicator Setting: {self.message_indicator_setting}")
            print(f"Plaintext: {self.plaintext}")
            print(f"-------------- END OF MESSAGE --------------")