from tkinter import *
import random as r
import controls


class Countries:
    def __init__(self, tk):
        self.tk = tk
        self.score = 0
        self.current_question = Label()
        self.current_flag = ''
        self.shorthand = {
            'dz': 'algeria',
            'ao': 'angola',
            'bj': 'benin',
            'bw': 'botswana',
            'bf': 'burkina faso',
            'bi': 'burundi',
            'cv': 'cape verde',
            'cm': 'cameroon',
            'cf': 'central african republic',
            'td': 'chad',
            'km': 'comoros',
            'cg': 'congo',
            'cd': 'democratic republic of the congo',
            'dj': 'djibouti',
            'eg': 'egypt',
            'gq': 'equatorial guinea',
            'er': 'eritrea',
            'sz': 'eswatini',
            'et': 'ethiopia',
            'ga': 'gabon',
            'gm': 'gambia',
            'gh': 'ghana',
            'gn': 'guinea',
            'gw': 'guinea-bissau',
            'ci': 'ivory coast',
            'ke': 'kenya',
            'ls': 'lesotho',
            'lr': 'liberia',
            'ly': 'libya',
            'mg': 'madagascar',
            'mw': 'malawi',
            'ml': 'mali',
            'mr': 'mauritania',
            'mu': 'mauritius',
            'ma': 'morocco',
            'mz': 'mozambique',
            'na': 'namibia',
            'ne': 'niger',
            'ng': 'nigeria',
            'rw': 'rwanda',
            'st': 'sao tome and principe',
            'sn': 'senegal',
            'sc': 'seychelles',
            'sl': 'sierra leone',
            'so': 'somalia',
            'za': 'south africa',
            'ss': 'south sudan',
            'sd': 'sudan',
            'tz': 'tanzania',
            'tg': 'togo',
            'tn': 'tunisia',
            'ug': 'uganda',
            'zm': 'zambia',
            'zw': 'zimbabwe',
            'af': 'afghanistan',
            'am': 'armenia',
            'az': 'azerbaijan',
            'bh': 'bahrain',
            'bd': 'bangladesh',
            'bt': 'bhutan',
            'bn': 'brunei',
            'kh': 'cambodia',
            'cn': 'china',
            'cy': 'cyprus',
            'ge': 'georgia',
            'in': 'india',
            'id': 'indonesia',
            'ir': 'iran',
            'iq': 'iraq',
            'il': 'israel',
            'jp': 'japan',
            'jo': 'jordan',
            'kz': 'kazakhstan',
            'kw': 'kuwait',
            'kg': 'kyrgyzstan',
            'la': 'laos',
            'lb': 'lebanon',
            'my': 'malaysia',
            'mv': 'maldives',
            'mn': 'mongolia',
            'mm': 'myanmar',
            'np': 'nepal',
            'kp': 'north korea',
            'om': 'oman',
            'pk': 'pakistan',
            'ps': 'palestine',
            'ph': 'philippines',
            'qa': 'qatar',
            'sa': 'saudi arabia',
            'sg': 'singapore',
            'kr': 'south korea',
            'lk': 'sri lanka',
            'sy': 'syria',
            'tw': 'taiwan',
            'tj': 'tajikistan',
            'th': 'thailand',
            'tl': 'timor-leste',
            'tr': 'turkey',
            'tm': 'turkmenistan',
            'ae': 'united arab emirates',
            'uz': 'uzbekistan',
            'vn': 'vietnam',
            'ye': 'yemen',
            'al': 'albania',
            'ad': 'andorra',
            'at': 'austria',
            'by': 'belarus',
            'be': 'belgium',
            'ba': 'bosnia and herzegovina',
            'bg': 'bulgaria',
            'hr': 'croatia',
            'cz': 'czech republic',
            'dk': 'denmark',
            'ee': 'estonia',
            'fi': 'finland',
            'fr': 'france',
            'de': 'germany',
            'gr': 'greece',
            'hu': 'hungary',
            'is': 'iceland',
            'ie': 'ireland',
            'it': 'italy',
            'xk': 'kosovo',
            'lv': 'latvia',
            'li': 'liechtenstein',
            'lt': 'lithuania',
            'lu': 'luxembourg',
            'mt': 'malta',
            'md': 'moldova',
            'mc': 'monaco',
            'me': 'montenegro',
            'nl': 'netherlands',
            'mk': 'north macedonia',
            'no': 'norway',
            'pl': 'poland',
            'pt': 'portugal',
            'ro': 'romania',
            'ru': 'russia',
            'sm': 'san marino',
            'rs': 'serbia',
            'sk': 'slovakia',
            'si': 'slovenia',
            'es': 'spain',
            'se': 'sweden',
            'ch': 'switzerland',
            'ua': 'ukraine',
            'gb': 'united kingdom',
            'va': 'vatican city',
            'ag': 'antigua and barbuda',
            'bs': 'bahamas',
            'bb': 'barbados',
            'bz': 'belize',
            'ca': 'canada',
            'cr': 'costa rica',
            'cu': 'cuba',
            'dm': 'dominica',
            'do': 'dominican republic',
            'sv': 'el salvador',
            'gd': 'grenada',
            'gt': 'guatemala',
            'ht': 'haiti',
            'hn': 'honduras',
            'jm': 'jamaica',
            'mx': 'mexico',
            'ni': 'nicaragua',
            'pa': 'panama',
            'kn': 'saint kitts and nevis',
            'lc': 'saint lucia',
            'vc': 'saint vincent and the grenadines',
            'tt': 'trinidad and tobago',
            'us': 'united states',
            'ar': 'argentina',
            'bo': 'bolivia',
            'br': 'brazil',
            'cl': 'chile',
            'co': 'colombia',
            'ec': 'ecuador',
            'gy': 'guyana',
            'py': 'paraguay',
            'pe': 'peru',
            'sr': 'suriname',
            'uy': 'uruguay',
            've': 'venezuela'
        }

        self.africa = {
            1: Countries.CountryQuestion('dz'.lower(), tk),
            2: Countries.CountryQuestion('ao'.lower(), tk),
            3: Countries.CountryQuestion('bj'.lower(), tk),
            4: Countries.CountryQuestion('bw'.lower(), tk),
            5: Countries.CountryQuestion('bf'.lower(), tk),
            6: Countries.CountryQuestion('bi'.lower(), tk),
            7: Countries.CountryQuestion('cv'.lower(), tk),
            8: Countries.CountryQuestion('cm'.lower(), tk),
            9: Countries.CountryQuestion('cf'.lower(), tk),
            10: Countries.CountryQuestion('td'.lower(), tk),
            11: Countries.CountryQuestion('km'.lower(), tk),
            12: Countries.CountryQuestion('cg'.lower(), tk),
            13: Countries.CountryQuestion('cd'.lower(), tk),
            14: Countries.CountryQuestion('dj'.lower(), tk),
            15: Countries.CountryQuestion('eg'.lower(), tk),
            16: Countries.CountryQuestion('gq'.lower(), tk),
            17: Countries.CountryQuestion('er'.lower(), tk),
            18: Countries.CountryQuestion('sz'.lower(), tk),
            19: Countries.CountryQuestion('et'.lower(), tk),
            20: Countries.CountryQuestion('ga'.lower(), tk),
            21: Countries.CountryQuestion('gm'.lower(), tk),
            22: Countries.CountryQuestion('gh'.lower(), tk),
            23: Countries.CountryQuestion('gn'.lower(), tk),
            24: Countries.CountryQuestion('gw'.lower(), tk),
            25: Countries.CountryQuestion('ci'.lower(), tk),
            26: Countries.CountryQuestion('ke'.lower(), tk),
            27: Countries.CountryQuestion('ls'.lower(), tk),
            28: Countries.CountryQuestion('lr'.lower(), tk),
            29: Countries.CountryQuestion('ly'.lower(), tk),
            30: Countries.CountryQuestion('mg'.lower(), tk),
            31: Countries.CountryQuestion('mw'.lower(), tk),
            32: Countries.CountryQuestion('ml'.lower(), tk),
            33: Countries.CountryQuestion('mr'.lower(), tk),
            34: Countries.CountryQuestion('mu'.lower(), tk),
            35: Countries.CountryQuestion('ma'.lower(), tk),
            36: Countries.CountryQuestion('mz'.lower(), tk),
            37: Countries.CountryQuestion('na'.lower(), tk),
            38: Countries.CountryQuestion('ne'.lower(), tk),
            39: Countries.CountryQuestion('ng'.lower(), tk),
            40: Countries.CountryQuestion('rw'.lower(), tk),
            41: Countries.CountryQuestion('st'.lower(), tk),
            42: Countries.CountryQuestion('sn'.lower(), tk),
            43: Countries.CountryQuestion('sc'.lower(), tk),
            44: Countries.CountryQuestion('sl'.lower(), tk),
            45: Countries.CountryQuestion('so'.lower(), tk),
            46: Countries.CountryQuestion('za'.lower(), tk),
            47: Countries.CountryQuestion('ss'.lower(), tk),
            48: Countries.CountryQuestion('sd'.lower(), tk),
            49: Countries.CountryQuestion('tz'.lower(), tk),
            50: Countries.CountryQuestion('tg'.lower(), tk),
            51: Countries.CountryQuestion('tn'.lower(), tk),
            52: Countries.CountryQuestion('ug'.lower(), tk),
            53: Countries.CountryQuestion('zm'.lower(), tk),
            54: Countries.CountryQuestion('zw'.lower(), tk)

        }
        self.asia = {
            1: Countries.CountryQuestion('af'.lower(), tk),
            2: Countries.CountryQuestion('am'.lower(), tk),
            3: Countries.CountryQuestion('az'.lower(), tk),
            4: Countries.CountryQuestion('bh'.lower(), tk),
            5: Countries.CountryQuestion('bd'.lower(), tk),
            6: Countries.CountryQuestion('bt'.lower(), tk),
            7: Countries.CountryQuestion('bn'.lower(), tk),
            8: Countries.CountryQuestion('kh'.lower(), tk),
            9: Countries.CountryQuestion('cn'.lower(), tk),
            10: Countries.CountryQuestion('cy'.lower(), tk),
            11: Countries.CountryQuestion('ge'.lower(), tk),
            12: Countries.CountryQuestion('in'.lower(), tk),
            13: Countries.CountryQuestion('id'.lower(), tk),
            14: Countries.CountryQuestion('ir'.lower(), tk),
            15: Countries.CountryQuestion('iq'.lower(), tk),
            16: Countries.CountryQuestion('il'.lower(), tk),
            17: Countries.CountryQuestion('jp'.lower(), tk),
            18: Countries.CountryQuestion('jo'.lower(), tk),
            19: Countries.CountryQuestion('kz'.lower(), tk),
            20: Countries.CountryQuestion('kw'.lower(), tk),
            21: Countries.CountryQuestion('kg'.lower(), tk),
            22: Countries.CountryQuestion('la'.lower(), tk),
            23: Countries.CountryQuestion('lb'.lower(), tk),
            24: Countries.CountryQuestion('my'.lower(), tk),
            25: Countries.CountryQuestion('mv'.lower(), tk),
            26: Countries.CountryQuestion('mn'.lower(), tk),
            27: Countries.CountryQuestion('mm'.lower(), tk),
            28: Countries.CountryQuestion('np'.lower(), tk),
            29: Countries.CountryQuestion('kp'.lower(), tk),
            30: Countries.CountryQuestion('om'.lower(), tk),
            31: Countries.CountryQuestion('pk'.lower(), tk),
            32: Countries.CountryQuestion('ps'.lower(), tk),
            33: Countries.CountryQuestion('ph'.lower(), tk),
            34: Countries.CountryQuestion('qa'.lower(), tk),
            35: Countries.CountryQuestion('sa'.lower(), tk),
            36: Countries.CountryQuestion('sg'.lower(), tk),
            37: Countries.CountryQuestion('kr'.lower(), tk),
            38: Countries.CountryQuestion('lk'.lower(), tk),
            39: Countries.CountryQuestion('sy'.lower(), tk),
            40: Countries.CountryQuestion('tw'.lower(), tk),
            41: Countries.CountryQuestion('tj'.lower(), tk),
            42: Countries.CountryQuestion('th'.lower(), tk),
            43: Countries.CountryQuestion('tl'.lower(), tk),
            44: Countries.CountryQuestion('tr'.lower(), tk),
            45: Countries.CountryQuestion('tm'.lower(), tk),
            46: Countries.CountryQuestion('ae'.lower(), tk),
            47: Countries.CountryQuestion('uz'.lower(), tk),
            48: Countries.CountryQuestion('vn'.lower(), tk),
            49: Countries.CountryQuestion('ye'.lower(), tk)
        }
        self.europe = {
            1: Countries.CountryQuestion('al'.lower(), tk),
            2: Countries.CountryQuestion('ad'.lower(), tk),
            3: Countries.CountryQuestion('am'.lower(), tk),
            4: Countries.CountryQuestion('at'.lower(), tk),
            5: Countries.CountryQuestion('az'.lower(), tk),
            6: Countries.CountryQuestion('by'.lower(), tk),
            7: Countries.CountryQuestion('be'.lower(), tk),
            8: Countries.CountryQuestion('ba'.lower(), tk),
            9: Countries.CountryQuestion('bg'.lower(), tk),
            10: Countries.CountryQuestion('hr'.lower(), tk),
            11: Countries.CountryQuestion('cy'.lower(), tk),
            12: Countries.CountryQuestion('cz'.lower(), tk),
            13: Countries.CountryQuestion('dk'.lower(), tk),
            14: Countries.CountryQuestion('ee'.lower(), tk),
            15: Countries.CountryQuestion('fi'.lower(), tk),
            16: Countries.CountryQuestion('fr'.lower(), tk),
            17: Countries.CountryQuestion('ge'.lower(), tk),
            18: Countries.CountryQuestion('de'.lower(), tk),
            19: Countries.CountryQuestion('gr'.lower(), tk),
            20: Countries.CountryQuestion('hu'.lower(), tk),
            21: Countries.CountryQuestion('is'.lower(), tk),
            22: Countries.CountryQuestion('ie'.lower(), tk),
            23: Countries.CountryQuestion('it'.lower(), tk),
            24: Countries.CountryQuestion('kz'.lower(), tk),
            25: Countries.CountryQuestion('xk'.lower(), tk),
            26: Countries.CountryQuestion('lv'.lower(), tk),
            27: Countries.CountryQuestion('li'.lower(), tk),
            28: Countries.CountryQuestion('lt'.lower(), tk),
            29: Countries.CountryQuestion('lu'.lower(), tk),
            30: Countries.CountryQuestion('mt'.lower(), tk),
            31: Countries.CountryQuestion('md'.lower(), tk),
            32: Countries.CountryQuestion('mc'.lower(), tk),
            33: Countries.CountryQuestion('me'.lower(), tk),
            34: Countries.CountryQuestion('nl'.lower(), tk),
            35: Countries.CountryQuestion('mk'.lower(), tk),
            36: Countries.CountryQuestion('no'.lower(), tk),
            37: Countries.CountryQuestion('pl'.lower(), tk),
            38: Countries.CountryQuestion('pt'.lower(), tk),
            39: Countries.CountryQuestion('ro'.lower(), tk),
            40: Countries.CountryQuestion('ru'.lower(), tk),
            41: Countries.CountryQuestion('sm'.lower(), tk),
            42: Countries.CountryQuestion('rs'.lower(), tk),
            43: Countries.CountryQuestion('sk'.lower(), tk),
            44: Countries.CountryQuestion('si'.lower(), tk),
            45: Countries.CountryQuestion('es'.lower(), tk),
            46: Countries.CountryQuestion('se'.lower(), tk),
            47: Countries.CountryQuestion('ch'.lower(), tk),
            48: Countries.CountryQuestion('tr'.lower(), tk),
            49: Countries.CountryQuestion('ua'.lower(), tk),
            50: Countries.CountryQuestion('gb'.lower(), tk),
            51: Countries.CountryQuestion('va'.lower(), tk)
        }
        self.north_america = {
            1: Countries.CountryQuestion('ag'.lower(), tk),
            2: Countries.CountryQuestion('bs'.lower(), tk),
            3: Countries.CountryQuestion('bb'.lower(), tk),
            4: Countries.CountryQuestion('bz'.lower(), tk),
            5: Countries.CountryQuestion('ca'.lower(), tk),
            6: Countries.CountryQuestion('cr'.lower(), tk),
            7: Countries.CountryQuestion('cu'.lower(), tk),
            8: Countries.CountryQuestion('dm'.lower(), tk),
            9: Countries.CountryQuestion('do'.lower(), tk),
            10: Countries.CountryQuestion('sv'.lower(), tk),
            11: Countries.CountryQuestion('gd'.lower(), tk),
            12: Countries.CountryQuestion('gt'.lower(), tk),
            13: Countries.CountryQuestion('ht'.lower(), tk),
            14: Countries.CountryQuestion('hn'.lower(), tk),
            15: Countries.CountryQuestion('jm'.lower(), tk),
            16: Countries.CountryQuestion('mx'.lower(), tk),
            17: Countries.CountryQuestion('ni'.lower(), tk),
            18: Countries.CountryQuestion('pa'.lower(), tk),
            19: Countries.CountryQuestion('kn'.lower(), tk),
            20: Countries.CountryQuestion('lc'.lower(), tk),
            21: Countries.CountryQuestion('vc'.lower(), tk),
            22: Countries.CountryQuestion('tt'.lower(), tk),
            23: Countries.CountryQuestion('us'.lower(), tk)
        }
        self.south_america = {
            1: Countries.CountryQuestion('ar'.lower(), tk),
            2: Countries.CountryQuestion('bo'.lower(), tk),
            3: Countries.CountryQuestion('br'.lower(), tk),
            4: Countries.CountryQuestion('cl'.lower(), tk),
            5: Countries.CountryQuestion('co'.lower(), tk),
            6: Countries.CountryQuestion('ec'.lower(), tk),
            7: Countries.CountryQuestion('gy'.lower(), tk),
            8: Countries.CountryQuestion('py'.lower(), tk),
            9: Countries.CountryQuestion('pe'.lower(), tk),
            10: Countries.CountryQuestion('sr'.lower(), tk),
            11: Countries.CountryQuestion('uy'.lower(), tk),
            12: Countries.CountryQuestion('ve'.lower(), tk)
        }

    def get_flag(self):
        return self.current_flag

    class CountryQuestion:
        def __init__(self, key, tk):
            self.key = key
            self.location = ('./countries/' + key + '.png').strip()
            self.entry = Entry(tk)
            self.answered = False

        def show(self):
            # self.label.grid(row=1, column=1)
            # self.entry.grid(row=1, column=2)
            self.entry.pack()

        def get_answer(self):
            return self.entry.get()

        def disable(self):
            self.entry.config(state='disabled')
            self.answered = True

        def attempt(self):
            return self.answered

        def get_entry(self):
            return self.entry


def check_answer(image_directory, question):
    return image_directory == question.location
