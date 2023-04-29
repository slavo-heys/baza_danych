'''
Program do zarządzania bazą danych
autor: Slavo Heys

'''

import pandas as pd
import os
import time
import termtables
import re

# sprawdz czy istnieje plik 'baza_danych.csv', jeśli nie to stwórz go
try:
    df = pd.read_csv('baza_danych.csv')
    # usuń kolumnę 'Unnamed: 0'
    df = df.drop('Unnamed: 0', axis=1)
except FileNotFoundError:
    df = pd.DataFrame(
        columns=['data', 'imie', 'nazwisko', 'pesel', 'wiek', 'plec', 'miasto', 'kod', 'ulica', 'nr_budynku',
                 'nr_mieszkania', 'tel_stacjonarny', 'tel_komórkowy', 'email', 'dodatkowe_informacje'])


# --------------------------------------------------------------------------------
# Program główny
class Program:
    def __init__(self):
        self.menu()

    def menu(self):
        # wyczyść ekran
        os.system('cls')

        # wyświetl menu
        print('-' * 50)
        print('Witaj w programie do zarządzania bazą danych!')
        print('-' * 50)
        print('1. Dodaj nowy rekord')
        print('2. Wyświetl wszystkie rekordy')
        print('3. Wyszukaj rekord')
        print('4. Usuń rekord\n')
        print('00 - Wyjście')
        print('-' * 50)

        self.wybor = input('Wybierz opcję: ')

        if self.wybor == '1':
            self.dodaj()
        elif self.wybor == '2':
            self.wyswietl()
        elif self.wybor == '3':
            self.wyszukaj()
        elif self.wybor == '4':
            self.usun()
        elif self.wybor == '00':
            os.system('cls')
            exit()
        else:
            print('Nie ma takiej opcji! Za 5 sekund wrócisz do menu.')
            time.sleep(5)
            self.menu()

    def dodaj(self):
        self.red = "\u0030"  # unicode for 0
        self.green = "\u00B2"
        os.system('cls')
        print('-' * 50)
        print('Dodawanie nowego rekordu')
        print('-' * 50)
        # dzisejsza data i godzina
        self.data = time.strftime('%Y-%m-%d %H:%M')
        # --------------------------------------------------------------------------------
        self.imie = input('Podaj imię: ')
        if self.imie != '':
            # sprawdz czy imię jest poprawne
            if not self.imie.isalpha():
                print('Imię jest niepoprawne!')
                time.sleep(2)
                self.dodaj()
            # pierwsza litera imienia z dużej litery
            self.imie = self.imie.capitalize()

        self.nazwisko = input('Podaj nazwisko: ')
        if self.nazwisko != '':
            # sprawdz czy nazwisko jest poprawne
            if not self.nazwisko.isalpha():
                print('Nazwisko jest niepoprawne!')
                time.sleep(2)
                self.dodaj()
            # pierwsza litera nazwiska z dużej litery
            self.nazwisko = self.nazwisko.capitalize()
        # --------------------------------------------------------------------------------
        self.pesel = input('Podaj lub PESEL: ')
        if self.pesel != '':
            # sprawdz PESEL jest poprawny
            if not self.pesel.isdigit():
                print('PESEL jest niepoprawny!')
                time.sleep(2)
                self.dodaj()
            # sprawdz czy PESEL ma odpowiednią długość
            if len(self.pesel) != 11:
                print('PESEL jest niepoprawny!')
                time.sleep(2)
                self.dodaj()
            # sprawdz płeć na podstawie PESEL
            if int(self.pesel[9]) % 2 == 0:
                self.plec = 'Kobieta'
            else:
                self.plec = 'Mężczyzna'
            # oblicz na podstawie PESEL wiek
            if len(self.pesel) == 11:
                # pobierz aktualny rok
                self.aktualny_rok = time.strftime('%Y')
                # pobierz z pesele 2 pierwsze cyfry i oblicz wiek
                self.pesel_rok = self.pesel[0:2]
                if self.pesel_rok == '00' or self.pesel_rok == '01' or self.pesel_rok == '02' or self.pesel_rok == '03' \
                        or self.pesel_rok == '04' or self.pesel_rok == '05' or self.pesel_rok == '06' \
                        or self.pesel_rok == '07' or self.pesel_rok == '08' or self.pesel_rok == '09' or \
                        self.pesel_rok == '10' or self.pesel_rok == '11' or self.pesel_rok == '12' or \
                        self.pesel_rok == '13' or self.pesel_rok == '14' or self.pesel_rok == '15' or \
                        self.pesel_rok == '16' or self.pesel_rok == '17' or self.pesel_rok == '18' or \
                        self.pesel_rok == '19' or self.pesel_rok == '20' or self.pesel_rok == '21' or \
                        self.pesel_rok == '22' or self.pesel_rok == '23':

                    self.pesel_rok = '20' + self.pesel_rok
                else:
                    self.pesel_rok = '19' + self.pesel_rok

                self.wiek = int(self.aktualny_rok) - int(self.pesel_rok)
                print(f'Wiek: {self.wiek}, płeć: {self.plec}')
            # sprawdz czy wiek jest poprawny
            if int(self.wiek) < 0 or int(self.wiek) > 110:
                print('Wiek jest niepoprawny!')
                time.sleep(2)
                self.dodaj()
        else:
            self.pesel = ''
            self.wiek = ''
            self.plec = ''
        # --------------------------------------------------------------------------------
        self.miasto = input('Podaj miasto: ')
        if self.miasto != '':
            # pierwsza litera miasta z dużej litery
            self.miasto = self.miasto.capitalize()
        else:
            self.miasto = ''

        self.kod = input('Podaj kod pocztowy: ')
        if self.kod != '':
            # sprawdz czy kod pocztowy ma odpowiednią długość
            if len(self.kod) != 6:
                print('Kod pocztowy jest niepoprawny!')
                time.sleep(2)
                self.dodaj()
        else:
            self.kod = ''
        # --------------------------------------------------------------------------------
        self.ulica = input('Podaj ulicę: ')
        # --------------------------------------------------------------------------------
        self.nr_budynku = input('Podaj numer budynku: ')
        # --------------------------------------------------------------------------------
        self.nr_mieszkania = input('Podaj numer mieszkania: ')
        # --------------------------------------------------------------------------------
        self.tel_stacjonarny = input('Podaj numer telefonu stacjonarnego: ')
        # sprawdz czy numer telefonu stacjonarnego jest poprawny
        if self.tel_stacjonarny != '':
            if not self.tel_stacjonarny.isdigit():
                print('Numer telefonu stacjonarnego jest niepoprawny!')
                time.sleep(2)
                self.dodaj()
        else:
            self.tel_stacjonarny = ''
        # --------------------------------------------------------------------------------
        self.tel_komorkowy = input('Podaj numer telefonu komórkowego: ')
        if self.tel_komorkowy != '':
            # sprawdz czy numer telefonu komórkowego jest poprawny
            if not self.tel_komorkowy.isdigit():
                print('Numer telefonu komórkowego jest niepoprawny!')
                time.sleep(2)
                self.dodaj()
                # sprawdz czy numer telefonu komórkowego ma odpowiednią długość
            if len(self.tel_komorkowy) != 9:
                print('Numer telefonu komórkowego jest niepoprawny!')
                time.sleep(2)
                self.dodaj()
            # zmień format numeru telefonu komórkowego
            self.tel_komorkowy = self.tel_komorkowy[:3] + '-' + self.tel_komorkowy[3:6] + '-' + self.tel_komorkowy[6:]
        else:
            self.tel_komorkowy = ''
        # --------------------------------------------------------------------------------
        self.email = input('Podaj adres email: ')
        if self.email != '':
            # sprawdz czy adres email jest poprawny
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
                print('Adres email jest niepoprawny!')
                time.sleep(2)
                self.dodaj()
        else:
            self.email = ''
        # --------------------------------------------------------------------------------
        self.dodatkowe_informacje = input('Podaj dodatkowe informacje: ')
        # --------------------------------------------------------------------------------
        # dodaj rekord do DataFrame
        df.loc[len(df)] = [self.data, self.imie, self.nazwisko, self.pesel, self.wiek, self.plec, self.miasto, self.kod,
                           self.ulica,
                           self.nr_budynku, self.nr_mieszkania, self.tel_stacjonarny, self.tel_komorkowy, self.email,
                           self.dodatkowe_informacje]

        # zapisz DataFrame do pliku
        df.to_csv('baza_danych.csv')

        # sprawdz czy rekord został dodany
        if self.imie in df.values:
            print('Rekord został dodany!')
            time.sleep(2)
        else:
            print('Rekord nie został dodany!')
            time.sleep(2)
            self.menu()

        # zapytaj czy dodać kolejny rekord
        self.kolejny = input('Czy chcesz dodać kolejny rekord? (t/n): ')
        if self.kolejny == 't':
            self.dodaj()
        else:
            self.menu()

    # --------------------------------------------------------------------------------
    def wyswietl(self):
        os.system('cls')
        print('Wyświetlanie wszystkich rekordów')
        print('\n')
        data = []
        self.header = ['data zapisu', 'imie', 'nazwisko', 'pesel', 'wiek', 'pleć', 'miasto', 'kod', 'ulica',
                       'nr_budynku',
                       'nr_mieszkania', 'tel_stacjonarny', 'tel_komórkowy', 'email', 'dodatkowe_informacje']
        # wyświetl DataFrame w tabeli texttable
        for i in range(len(df)):
            dane_tabeli = [df.loc[i][0], df.loc[i][1], df.loc[i][2], df.loc[i][3], df.loc[i][4], df.loc[i][5],
                           df.loc[i][6], df.loc[i][7], df.loc[i][8], df.loc[i][9], df.loc[i][10], df.loc[i][11],
                           df.loc[i][12], df.loc[i][13], df.loc[i][14]]
            data.append(dane_tabeli)
        table = termtables.to_string(data, header=self.header)
        print(table)
        print('\n')
        input('Naciśnij ENTER aby wrócić do menu.')
        self.menu()

    # --------------------------------------------------------------------------------
    def wyszukaj(self):
        os.system('cls')
        print('Wyszukiwanie rekordów')
        print('\n')
        self.wyszukiwanie = input('Podaj dane do wyszukania (imie, nazwisko, pesel, tel komórkowy, email: ')
        # sprawdz czy podano dane do wyszukania
        if self.wyszukiwanie == '':
            print('Nie podano danych do wyszukania!')
            time.sleep(2)
            self.wyszukaj()
        else:
            # sprawdź czy podano imię
            if self.wyszukiwanie in df['imie'].values:
                print('Wyniki wyszukiwania dla imienia: ' + self.wyszukiwanie)
                print('\n')
                # wyszukaj imię
                for i in range(len(df)):
                    if df.loc[i][1] == self.wyszukiwanie:
                        print(df.loc[i])
                        print('\n')
            # sprawdź czy podano nazwisko
            elif self.wyszukiwanie in df['nazwisko'].values:
                print('Wyniki wyszukiwania dla nazwiska: ' + self.wyszukiwanie)
                print('\n')
                # wyszukaj nazwisko
                for i in range(len(df)):
                    if df.loc[i][2] == self.wyszukiwanie:
                        print(df.loc[i])
                        print('\n')
            # sprawdź czy podano pesel
            elif self.wyszukiwanie in df['pesel'].values:
                print('Wyniki wyszukiwania dla peselu: ' + self.wyszukiwanie)
                print('\n')
                # wyszukaj pesel
                for i in range(len(df)):
                    if df.loc[i][3] == self.wyszukiwanie:
                        print(df.loc[i])
                        print('\n')
            # sprawdź czy podano numer telefonu komórkowego
            elif self.wyszukiwanie in df['tel_komorkowy'].values:
                print('Wyniki wyszukiwania dla numeru telefonu komórkowego: ' + self.wyszukiwanie)
                print('\n')
                # wyszukaj numer telefonu komórkowego
                for i in range(len(df)):
                    if df.loc[i][12] == self.wyszukiwanie:
                        print(df.loc[i])
                        print('\n')
            # sprawdź czy podano adres email
            elif self.wyszukiwanie in df['email'].values:
                print('Wyniki wyszukiwania dla adresu email: ' + self.wyszukiwanie)
                print('\n')
                # wyszukaj adres email
                for i in range(len(df)):
                    if df.loc[i][13] == self.wyszukiwanie:
                        print(df.loc[i])
                        print('\n')
            else:
                print('Nie znaleziono rekordów!')
                time.sleep(2)
                self.menu()
        input('Naciśnij ENTER aby wrócić do menu.')

    # --------------------------------------------------------------------------------
    def usun(self):
        pass


# start programu
Program()
