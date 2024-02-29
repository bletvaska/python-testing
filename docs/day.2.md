# Day 2: Selenium Basics


## Morning Exercise

Vytvorte v trieda `BankAccount` metodu `.withdraw(self, amount)`, pomocou ktorej vyberiete peniaze z uctu. Jej implementácia musi prejst nasledovnymi testami:

* **ak** vyberieme z uctu 100 evry, **tak** sa zostatok znizi o `100` evry
* **ak** zadame zapornu sumu, **tak** sa vyvolá výnimka `ValueError`
* **ak** zadame iny typ ako celé číslo, **tak** sa vyvolá výnimka `TypeError`
* **ak** sa pokusime o vyber vacsieho mnozstva penazi, ako je zostatok, **tak** sa vyvolá výnimka `ValueError`
* **ak** vyberieme rovnakú sumu, ako je zostatok na ucte, **tak** vysledny zostatok bude `0`
* **ak** zadame `0`, **tak** sa vyvolá výnimka `ValueError`
* **ak** zadame `None`, **tak** sa vyvolá výnimka `TypeError`


## Organizacia Testov

**Test suites** - subor/sada testov, ktore spolu suvisia, napr.:

* testuju jednu metódu/funkciu
* testuju jednu triedu
* testuju jeden formular
* ...

v triede `BankAccount` sa nachádzajú dve metody, takze mozeme vytvorit minimalne dva test suity. okrem toho mozeme urobit samostatny suite pre testovanie spravania samotneho uctu, ako napr. zostatok po vytvoreni alebo povinnost zadania vlastnika uctu.

vytvoríme teda v priečinku `tests/` samostatný priečinok s názvom `bankaccount/`, do ktorého jednotlivé moduly vložíme. vysledna struktura bude vyzerat nasledovne:

```
tests/
├── bankaccount/
│   ├── __init__.py
│   ├── test_bankaccount.py
│   ├── test_deposit.py
│   └── test_withdraw.py
└── __init__.py
```

následne už len pripraviť jednotlive moduly a naplníme ich testami pre jednotlivé funkcie a samotnu triedu.



## Súbor `conftest.py`

* shares content between multiple test files
  * sharing fixtures
* overriding fixtures on various levels
  * generic content in top folder
  * specific content in sub folders
  * content override

V našom prípade môžeme vytvoriť súbor conftest.py v priečinku tests/bankaccount/, kde umiestnime všetky fixtures potrebné pre prácu s bankovým účtom.


# Selenium Webdriver Architecture

```
+--------------+         +-----------+         +---------+
|              |         |           |         |         |
| Test Scripts |-------->| Webdriver |-------->| Browser |
|              |         |           |         |         |
+--------------+         +-----------+         +---------+
```


## Installation

Nainstalovat budeme potrebovať dve veci:

  1. balík `selenium`
  2. selenium webdriver


### Installing Selenium Package

Nainštalujte si do svojho prostredia balíček `selenium`

Ak používate nástroj `pip`, stačí jednoducho napísať z príkazového riadku:

```bash
$ pip install selenium
```

V prostredí _PyCharm_ zasa balíček nainštalujete v nastaveniach používaného interpretera jazyka Python.


### Installing Webdriver

Nainštalujte si príslušný _WebDriver_ pre váš prehliadač.


Ak používate linuxovú distribúciu Fedora, môžete priamo z príkazového riadku nainštalovať balíček `chromedriver`. Tento obsahuje WebDriver pre prehliadač Chrome:

```bash
$ sudo dnf install chromedriver
```


Ak používate linuxovú distribúciu _Ubuntu_, z príkazového riadku nainštalujte balík `chromium-webdriver` príkazom:

```bash
$ sudo apt install chromium-webdriver
```

Ak používate _OS Windows_ a máte nainštalovaný balíčkovací systím _Chocolatey_, _WebDriver_ pre prehliadač _Chromium_ si môžete doinštalovať príkazom:

```bash
$ choco install chromedriver
```


_WebDriver_ pre ostatné systémy môžete stiahnuť a nainštalovať podľa pokynov na domovskej stránke [http://www.seleniumhq.org/download/](http://www.seleniumhq.org/download/)


**Poznámka:** Ak používate _OS Windows_, váš stiahnutý webdriver si rozbaľte do priečinku, v ktorom sa nachádza interpreter jazyka Python (súbor python.exe). Vyhnete sa tak situácii, kedy budete musieť pri každej inštancii uvádzať absolútnu cestu k nemu.


## The Basics

Začneme s jednoduchou ukážkou, v ktorej si ukážeme základy použitia webdriver-a. Aby sme videli okamžitý dôsledok jednotlivých príkazov, použijeme interaktívny interpreter jazyka Python `ipython`:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.python.org')
assert 'Python' in driver.title

element = driver.find_element(By.NAME, 'q')
element.clear()
element.send_keys('pycon sk 2022')
element.submit()

driver.close()
```


## Creating Tests with pytest

Z predchádzajúcej ukážky si vytvoríme niekoľko testov.

Vytvorte súbor `test_pythonorg.py`, ktorý bude obsahovať jednotlivé testy.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
```


Vytvorte test, pomocou ktorého overíte, či sa v názve stránky [www.python.org](https://www.python.org) nachádza slovo Python

```python
def test_when_enter_page_check_title_contains_python():
   driver = webdriver.Chrome()
   driver.get("http://www.python.org")
   assert 'Python' in driver.title
   driver.close()
```


Overte, či po zadaní kľúčového výrazu `pycon` do vyhľadávača na tejto stránke, sa na stránke zobrazí element `<h3>` s textom `Results`

```python
def test_when_search_string_entered_then_results_must_be_on_page():
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    element = driver.find_element(By.NAME, 'q')
    element.send_keys('selenium')
    element.submit() 

    results = driver.find_element(By.XPATH,
        '//*[@id="content"]/div/section/form/h3')
    assert results.text == 'Results'
    driver.close()
```


## Creating Fixtures

Pre vytvorený testcase vytvorte potrebné fixtures a podľa potreby upravte aj zvyšný kód.

```python
@pytest.fixture
def driver():
   driver = webdriver.Chrome()
   driver.get('https://www.python.org')
   yield driver
   driver.close()

def test_when_enter_page_check_title_contains_python(driver):
   assert 'Python' in driver.title

def test_when_search_string_entered_then_results_must_be_on_page(driver):
   element = driver.find_element(By.NAME, 'q')
   element.send_keys('pycon sk 2019')
   element.submit()

   results = driver.find_element(By.XPATH,
       '//*[@id="content"]/div/section/form/h3')
   assert results.text == 'Results'
```

Odoslanie formuláru môže byť samozrejme niekoľkými spôsobmi:

* pomocou nového riadka na konci vstupu:

  ```python
  element.send_keys('pycon sk 2019\n')
  ```

* pomocou explicitne zadanej klávesy po celom vstupe:

  ```python
  element.send_keys('pycon sk 2019', Keys.RETURN)
  ```

* pomocou kliknutia na tlačidlo vedľa vyhľadávacieho poľa:

  ```python
  driver.find_element(By.ID, 'submit').click()
  ```

Upravte scope pre fixture tak, aby sa prehliadač otvoril pre všetky testy len raz.

```python
@pytest.fixture(scope='module')
```


## Testing of Login Form

Otestujte prihlasovaci formular na adrese [https://www.dsl.sk/user.php?action=login](https://www.dsl.sk/user.php?action=login) Prihlasovacie meno a heslo pre otestovanie uspesneho prihlasenia je `pytester:pytester`. **Prosim nemenit!**

zistit aktualnu stranku je mozne pomocou: `driver.current_url`

* **ak** zadam spravny login a spravne heslo **tak** ma presmeruje na stranku [https://www.dsl.sk/](https://www.dsl.sk/).
* **ak** zadam nespravny login a nespravne heslo **tak** zostanem na rovnakej stranke.
* **ak** zadam login ale nespravne heslo, **tak** zostanem na rovnakej stranke.
* **ak** zadam spravny login ale nespravne heslo, **tak** zostanem na rovnakej stranke.
* **ak** zadam login ale nezadam heslo, **tak** zostanem na rovnakej stranke.
* **ak** odoslem prazdny formular, **tak** sa dostanem na rovnakej stranke.


### Riešenie

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope="module")
def driver_azet():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_when_correct_name_password_sent_then_succesfully_logged(driver_azet):
    username = driver_azet.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/form/div[1]/div/input")
    username.send_keys("pytester")
    password = driver_azet.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/form/div[2]/div/input")
    password.send_keys("pytester")
    driver_azet.find_element(By.NAME, "submit").click()
    driver_azet.find_element(By.NAME, "Neskôr").click()


    # arrange / act
    driver_azet.get("https://prihlasenie.azet.sk/")


    # assert
    assert "Azet" in driver_azet.find_element(By.XPATH, '//*[@id="app"]/header/nav/div/div[2]/div/span')


    #driver_azet.find_element(By.PARTIAL_LINK_TEXT, "Odhlásiť").click()
```


## Tips and Tricks

### Problém s nájdením Webdriver-a

Ak chromedriver nespustíte priamo z príkazového riadku, musíte pri vytváraní objektu driver-a k nemu uviesť absolútnu cestu. Tento prístup použijete vtedy, ak ste používateľom distribúcie Ubuntu:

```python
driver = webdriver.Chrome(executable_path='/path/to/webdriver')
```


### Webdriver v Headless režime

Prehliadač Chrome je možné spustiť v tzv. headless režime, kedy sa nebude spúšťať s grafickým rozhraním, ale spustí sa len v pamäti. To je veľmi výhodné v prípadoch, ak chcete testy spúšťať na pozadí bez nutnosti mať spustené grafické prostredie.

```python
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
```


## Testing Special HTML Elements

### Checkboxes

So zaškrtávacie políčkom sa pracuje ako so štandardným elementom. Bude nás akurát zaujímať, ako zistiť jeho stav (zaškrtnuté alebo nezaškrtnuté) a tiež nás bude zaujímať, ako toto políčko označiť.

Začnime teda jeho nájdením na stránke pomocou XPath-u:

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://blazedemo.com')

# search checkbox by xpath
element = driver.find_element(By.XPATH, '//input[@id="rememberMe"]')
```

Zistiť, či je alebo nie je políčko zaškrtnuté, môžeme pomocou metódy `element.is_selected()`. Vráti hodnotu True alebo False na základe toho, či je alebo nie je toto políčko zaškrtnuté.

Zaškrtnúť alebo odškrtnúť ho je zasa možné zavolaním metódy `element.click()`.


### Radio Buttons

S radio tlačidlami sa pracuje podobne ako v prípade zaškrtávacích polí. Sú to teda elementy, ktoré vieme v HTML dokumente vyhľadať pomocou ich označenia o opýtať sa, či sú alebo nie sú označené. Keďže sa však jedná o skupinu elementov, v ktorej môže byť vo výsledku označený len jeden, je ešte potrebné sa dostať k hodnote, ktorú radio button má.

Začneme teda tým, že si uvedenú množinu radio tlačidiel na stránke nájdeme pomocou XPath-u:

```python
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://www.seleniumeasy.com/test/basic-radiobutton-demo.html')

# search radio buttons by xpath
radios = driver.find_elements(By.XPATH,
   '//input[@type="radio" and @name="ageGroup"]')
```

Označiť niektorý z nich môžeme zavolať volaním metódy `.click()` na príslušnom elemente:

```python
for radio in radios:
   radio.click()
```

Ak chceme zistiť, či je element označený, budeme sa nad ním pýtať metódou `.is_selected()`. Hodnotu zo atribútu value zvoleného elementu získame volaním metódy `.get_attribute()`:

```python
for radio in radios:
   if radio.is_selected():
      print(radio.get_attribute('value'))
      break
else:
   print('No value is selected')
```


### Dropdown Menus

Pre prácu s dropdown budeme používať triedu `Select`. Pracovať je síce možné aj bez neho, ale je to potom surové a neintuitívne. Týmto spôsobom budeme mať k dispozícii metódy, ktoré môžeme rovno využiť.

```python
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://blazedemo.com')
```

Začneme tým, že vytvoríme objekt Select, ktorý bude reprezentovať práve rozbaľovacie menu (dropdown, combo box, select). Do konštruktora vstupuje objekt elementu tohto prvku, ktorý identifikujeme napr. pomocou XPath-u:

```python
# get select element based
select = Select(driver.find_element(By.XPATH,
   '//select[@name="fromPort"]'))
```

Ak sa chceme pozrieť, aké všetky možnosti (elementy `<option>`) k dispozícii máme, môžeme ich prejsť v cykle:

```python
for option in select.options:
   print(option.text)
```

Vyberať, resp. označovať jednotlivé voľby môžeme podľa

* viditeľného textu
* hodnoty
* indexu

Ukážky sa nachádzajú nižšie:

```python
# select by visible text
select.select_by_visible_text('Portland')

# select by value
select.select_by_value('Boston')

# select by index
select.select_by_index(4)
```

Ak nás naopak zaujíma, čo je zvolené, môžeme využiť dve properties:

* `select.first_selected_option` - The first selected option in this select tag (or the currently selected option in a normal select).
* `select.all_selected_options` - Returns a list of all selected options belonging to this select tag.


### Sending Keys

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.python.org')

elem = driver.find_element(By.XPATH, '//input')
elem.send_keys('pycon', Keys.RETURN)
```


## TODO

* [pytest-webdriver](https://pypi.org/project/pytest-webdriver/)


## References

* [Selenium with Python](http://selenium-python.readthedocs.io)
* [http://naucse.python.cz/lessons/intro/testing/](http://naucse.python.cz/lessons/intro/testing/)
* [Selenium WebDriver](https://www.seleniumhq.org/docs/03_webdriver.jsp)
* [Selenium Easy](https://www.seleniumeasy.com/test/basic-radiobutton-demo.html) - stránky, kde sa dá testovať Selenium

