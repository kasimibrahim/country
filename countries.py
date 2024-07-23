from tkinter import *
import random as r
import controls


class Countries:
    def __init__(self, tk):
        self.tk = tk
        self.score = 0
        self.current_question = Label()
        self.current_flag = ''
        self.africa = {
            1: Countries.CountryQuestion('algeria'.lower(), tk),
            2: Countries.CountryQuestion('angola'.lower(), tk),
            3: Countries.CountryQuestion('benin'.lower(), tk),
            4: Countries.CountryQuestion('botswana'.lower(), tk),
            5: Countries.CountryQuestion('burkina faso'.lower(), tk),
            6: Countries.CountryQuestion('burundi'.lower(), tk),
            7: Countries.CountryQuestion('cape verde'.lower(), tk),
            8: Countries.CountryQuestion('cameroon'.lower(), tk),
            9: Countries.CountryQuestion('central african republic'.lower(), tk),
            10: Countries.CountryQuestion('chad'.lower(), tk),
            11: Countries.CountryQuestion('comoros'.lower(), tk),
            12: Countries.CountryQuestion('congo'.lower(), tk),
            13: Countries.CountryQuestion('democratic republic of the congo'.lower(), tk),
            14: Countries.CountryQuestion('djibouti'.lower(), tk),
            15: Countries.CountryQuestion('egypt'.lower(), tk),
            16: Countries.CountryQuestion('equatorial guinea'.lower(), tk),
            17: Countries.CountryQuestion('eritrea'.lower(), tk),
            18: Countries.CountryQuestion('eswatini'.lower(), tk),
            19: Countries.CountryQuestion('ethiopia'.lower(), tk),
            20: Countries.CountryQuestion('gabon'.lower(), tk),
            21: Countries.CountryQuestion('gambia'.lower(), tk),
            22: Countries.CountryQuestion('ghana'.lower(), tk),
            23: Countries.CountryQuestion('guinea'.lower(), tk),
            24: Countries.CountryQuestion('guinea-bissau'.lower(), tk),
            25: Countries.CountryQuestion('ivory coast'.lower(), tk),
            26: Countries.CountryQuestion('kenya'.lower(), tk),
            27: Countries.CountryQuestion('lesotho'.lower(), tk),
            28: Countries.CountryQuestion('liberia'.lower(), tk),
            29: Countries.CountryQuestion('libya'.lower(), tk),
            30: Countries.CountryQuestion('madagascar'.lower(), tk),
            31: Countries.CountryQuestion('malawi'.lower(), tk),
            32: Countries.CountryQuestion('mali'.lower(), tk),
            33: Countries.CountryQuestion('mauritania'.lower(), tk),
            34: Countries.CountryQuestion('mauritius'.lower(), tk),
            35: Countries.CountryQuestion('morocco'.lower(), tk),
            36: Countries.CountryQuestion('mozambique'.lower(), tk),
            37: Countries.CountryQuestion('namibia'.lower(), tk),
            38: Countries.CountryQuestion('niger'.lower(), tk),
            39: Countries.CountryQuestion('nigeria'.lower(), tk),
            40: Countries.CountryQuestion('rwanda'.lower(), tk),
            41: Countries.CountryQuestion('sao tome and principe'.lower(), tk),
            42: Countries.CountryQuestion('senegal'.lower(), tk),
            43: Countries.CountryQuestion('seychelles'.lower(), tk),
            44: Countries.CountryQuestion('sierra leone'.lower(), tk),
            45: Countries.CountryQuestion('somalia'.lower(), tk),
            46: Countries.CountryQuestion('south africa'.lower(), tk),
            47: Countries.CountryQuestion('south sudan'.lower(), tk),
            48: Countries.CountryQuestion('sudan'.lower(), tk),
            49: Countries.CountryQuestion('tanzania'.lower(), tk),
            50: Countries.CountryQuestion('togo'.lower(), tk),
            51: Countries.CountryQuestion('tunisia'.lower(), tk),
            52: Countries.CountryQuestion('uganda'.lower(), tk),
            53: Countries.CountryQuestion('zambia'.lower(), tk),
            54: Countries.CountryQuestion('zimbabwe'.lower(), tk)
        }
        self.asia = {
            1: Countries.CountryQuestion('afghanistan'.lower(), tk),
            2: Countries.CountryQuestion('armenia'.lower(), tk),
            3: Countries.CountryQuestion('azerbaijan'.lower(), tk),
            4: Countries.CountryQuestion('bahrain'.lower(), tk),
            5: Countries.CountryQuestion('bangladesh'.lower(), tk),
            6: Countries.CountryQuestion('bhutan'.lower(), tk),
            7: Countries.CountryQuestion('brunei'.lower(), tk),
            8: Countries.CountryQuestion('cambodia'.lower(), tk),
            9: Countries.CountryQuestion('china'.lower(), tk),
            10: Countries.CountryQuestion('cyprus'.lower(), tk),
            11: Countries.CountryQuestion('georgia'.lower(), tk),
            12: Countries.CountryQuestion('india'.lower(), tk),
            13: Countries.CountryQuestion('indonesia'.lower(), tk),
            14: Countries.CountryQuestion('iran'.lower(), tk),
            15: Countries.CountryQuestion('iraq'.lower(), tk),
            16: Countries.CountryQuestion('israel'.lower(), tk),
            17: Countries.CountryQuestion('japan'.lower(), tk),
            18: Countries.CountryQuestion('jordan'.lower(), tk),
            19: Countries.CountryQuestion('kazakhstan'.lower(), tk),
            20: Countries.CountryQuestion('kuwait'.lower(), tk),
            21: Countries.CountryQuestion('kyrgyzstan'.lower(), tk),
            22: Countries.CountryQuestion('laos'.lower(), tk),
            23: Countries.CountryQuestion('lebanon'.lower(), tk),
            24: Countries.CountryQuestion('malaysia'.lower(), tk),
            25: Countries.CountryQuestion('maldives'.lower(), tk),
            26: Countries.CountryQuestion('mongolia'.lower(), tk),
            27: Countries.CountryQuestion('myanmar'.lower(), tk),
            28: Countries.CountryQuestion('nepal'.lower(), tk),
            29: Countries.CountryQuestion('north korea'.lower(), tk),
            30: Countries.CountryQuestion('oman'.lower(), tk),
            31: Countries.CountryQuestion('pakistan'.lower(), tk),
            32: Countries.CountryQuestion('palestine'.lower(), tk),
            33: Countries.CountryQuestion('philippines'.lower(), tk),
            34: Countries.CountryQuestion('qatar'.lower(), tk),
            35: Countries.CountryQuestion('saudi arabia'.lower(), tk),
            36: Countries.CountryQuestion('singapore'.lower(), tk),
            37: Countries.CountryQuestion('south korea'.lower(), tk),
            38: Countries.CountryQuestion('sri lanka'.lower(), tk),
            39: Countries.CountryQuestion('syria'.lower(), tk),
            40: Countries.CountryQuestion('taiwan'.lower(), tk),
            41: Countries.CountryQuestion('tajikistan'.lower(), tk),
            42: Countries.CountryQuestion('thailand'.lower(), tk),
            43: Countries.CountryQuestion('timor-leste'.lower(), tk),
            44: Countries.CountryQuestion('turkey'.lower(), tk),
            45: Countries.CountryQuestion('turkmenistan'.lower(), tk),
            46: Countries.CountryQuestion('united arab emirates'.lower(), tk),
            47: Countries.CountryQuestion('uzbekistan'.lower(), tk),
            48: Countries.CountryQuestion('vietnam'.lower(), tk),
            49: Countries.CountryQuestion('yemen'.lower(), tk)
        }
        self.europe = {
            1: Countries.CountryQuestion('albania'.lower(), tk),
            2: Countries.CountryQuestion('andorra'.lower(), tk),
            3: Countries.CountryQuestion('armenia'.lower(), tk),
            4: Countries.CountryQuestion('austria'.lower(), tk),
            5: Countries.CountryQuestion('azerbaijan'.lower(), tk),
            6: Countries.CountryQuestion('belarus'.lower(), tk),
            7: Countries.CountryQuestion('belgium'.lower(), tk),
            8: Countries.CountryQuestion('bosnia and herzegovina'.lower(), tk),
            9: Countries.CountryQuestion('bulgaria'.lower(), tk),
            10: Countries.CountryQuestion('croatia'.lower(), tk),
            11: Countries.CountryQuestion('cyprus'.lower(), tk),
            12: Countries.CountryQuestion('czech republic'.lower(), tk),
            13: Countries.CountryQuestion('denmark'.lower(), tk),
            14: Countries.CountryQuestion('estonia'.lower(), tk),
            15: Countries.CountryQuestion('finland'.lower(), tk),
            16: Countries.CountryQuestion('france'.lower(), tk),
            17: Countries.CountryQuestion('georgia'.lower(), tk),
            18: Countries.CountryQuestion('germany'.lower(), tk),
            19: Countries.CountryQuestion('greece'.lower(), tk),
            20: Countries.CountryQuestion('hungary'.lower(), tk),
            21: Countries.CountryQuestion('iceland'.lower(), tk),
            22: Countries.CountryQuestion('ireland'.lower(), tk),
            23: Countries.CountryQuestion('italy'.lower(), tk),
            24: Countries.CountryQuestion('kazakhstan'.lower(), tk),
            25: Countries.CountryQuestion('kosovo'.lower(), tk),
            26: Countries.CountryQuestion('latvia'.lower(), tk),
            27: Countries.CountryQuestion('liechtenstein'.lower(), tk),
            28: Countries.CountryQuestion('lithuania'.lower(), tk),
            29: Countries.CountryQuestion('luxembourg'.lower(), tk),
            30: Countries.CountryQuestion('malta'.lower(), tk),
            31: Countries.CountryQuestion('moldova'.lower(), tk),
            32: Countries.CountryQuestion('monaco'.lower(), tk),
            33: Countries.CountryQuestion('montenegro'.lower(), tk),
            34: Countries.CountryQuestion('netherlands'.lower(), tk),
            35: Countries.CountryQuestion('north macedonia'.lower(), tk),
            36: Countries.CountryQuestion('norway'.lower(), tk),
            37: Countries.CountryQuestion('poland'.lower(), tk),
            38: Countries.CountryQuestion('portugal'.lower(), tk),
            39: Countries.CountryQuestion('romania'.lower(), tk),
            40: Countries.CountryQuestion('russia'.lower(), tk),
            41: Countries.CountryQuestion('san marino'.lower(), tk),
            42: Countries.CountryQuestion('serbia'.lower(), tk),
            43: Countries.CountryQuestion('slovakia'.lower(), tk),
            44: Countries.CountryQuestion('slovenia'.lower(), tk),
            45: Countries.CountryQuestion('spain'.lower(), tk),
            46: Countries.CountryQuestion('sweden'.lower(), tk),
            47: Countries.CountryQuestion('switzerland'.lower(), tk),
            48: Countries.CountryQuestion('turkey'.lower(), tk),
            49: Countries.CountryQuestion('ukraine'.lower(), tk),
            50: Countries.CountryQuestion('united kingdom'.lower(), tk),
            51: Countries.CountryQuestion('vatican city'.lower(), tk)
        }
        self.north_america = {
            1: Countries.CountryQuestion('antigua and barbuda'.lower(), tk),
            2: Countries.CountryQuestion('bahamas'.lower(), tk),
            3: Countries.CountryQuestion('barbados'.lower(), tk),
            4: Countries.CountryQuestion('belize'.lower(), tk),
            5: Countries.CountryQuestion('canada'.lower(), tk),
            6: Countries.CountryQuestion('costa rica'.lower(), tk),
            7: Countries.CountryQuestion('cuba'.lower(), tk),
            8: Countries.CountryQuestion('dominica'.lower(), tk),
            9: Countries.CountryQuestion('dominican republic'.lower(), tk),
            10: Countries.CountryQuestion('el salvador'.lower(), tk),
            11: Countries.CountryQuestion('grenada'.lower(), tk),
            12: Countries.CountryQuestion('guatemala'.lower(), tk),
            13: Countries.CountryQuestion('haiti'.lower(), tk),
            14: Countries.CountryQuestion('honduras'.lower(), tk),
            15: Countries.CountryQuestion('jamaica'.lower(), tk),
            16: Countries.CountryQuestion('mexico'.lower(), tk),
            17: Countries.CountryQuestion('nicaragua'.lower(), tk),
            18: Countries.CountryQuestion('panama'.lower(), tk),
            19: Countries.CountryQuestion('saint kitts and nevis'.lower(), tk),
            20: Countries.CountryQuestion('saint lucia'.lower(), tk),
            21: Countries.CountryQuestion('saint vincent and the grenadines'.lower(), tk),
            22: Countries.CountryQuestion('trinidad and tobago'.lower(), tk),
            23: Countries.CountryQuestion('united states'.lower(), tk)
        }
        self.south_america = {
            1: Countries.CountryQuestion('argentina'.lower(), tk),
            2: Countries.CountryQuestion('bolivia'.lower(), tk),
            3: Countries.CountryQuestion('brazil'.lower(), tk),
            4: Countries.CountryQuestion('chile'.lower(), tk),
            5: Countries.CountryQuestion('colombia'.lower(), tk),
            6: Countries.CountryQuestion('ecuador'.lower(), tk),
            7: Countries.CountryQuestion('guyana'.lower(), tk),
            8: Countries.CountryQuestion('paraguay'.lower(), tk),
            9: Countries.CountryQuestion('peru'.lower(), tk),
            10: Countries.CountryQuestion('suriname'.lower(), tk),
            11: Countries.CountryQuestion('uruguay'.lower(), tk),
            12: Countries.CountryQuestion('venezuela'.lower(), tk)
        }

    def shuffle(self):
        del self.current_question
        selected = r.choice(list(self.africa.keys()))
        self.current_question = self.africa[selected]
        self.current_question.show()
        self.current_flag = self.africa[selected].location

    def get_flag(self):
        return self.current_flag

    class CountryQuestion:
        def __init__(self, key, tk):
            self.key = key
            self.location = './countries/' + key + '.png'
            self.entry = Entry(tk)

        def show(self):
            # self.label.grid(row=1, column=1)
            # self.entry.grid(row=1, column=2)
            self.entry.pack()





def check_answer(image_directory, question):
    return image_directory == question.location
