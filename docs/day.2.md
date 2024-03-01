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

Zatiaľ sme v rámci orgranizácie kódu len oddelili kód aplikácie od testov. Samotné súbory s testami však budú postupom času rásť, pretože pre otestovanie jednej vlastnosti môžeme vytvoriť mnoho malých jednotkových testov. Keď následne testy všetkých vlastností uložíme do jedného modulu, môže sa jednať o modul so stovkami drobných jednotkových testov. Navigácia v takom module môže byť veľmi komplikovaná.

Aby sme sa v týchto testoch nestratili, budeme ich trhať do menších modulov, ktoré budeme nazývať **sady testov** (z angl. **test suites**). Do takejto sady budeme ukladať testy, ktoré spolu súvisia, napr.:

* testujú jednu metódu/funkciu
* testujú jednu triedu
* testujú jeden formular
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

V našom prípade môžeme vytvoriť súbor `conftest.py` v priečinku `tests/bankaccount/`, kde umiestnime všetky fixtures potrebné pre prácu s bankovým účtom.

Pre následné použitie týchto fixtures netreba vytvoriť nič špeciálne - stačí ich len použiť:

```python
def test_when_account_is_created_then_balance_is_0(account):
  assert account.balance == 0
```

Fixture s názvom `account` nie je potrebné ani explicitne importovať.


# Selenium Webdriver Architecture

```
+--------------+         +-----------+         +---------+
|              |         |           |         |         |
| Test Scripts |-------->| Webdriver |-------->| Browser |
|              |         |           |         |         |
+--------------+         +-----------+         +---------+
```


## Inštalácia

Do svojho prostredia je potrebné nainštalovať balík s názvom `selenium`.

Ak používate nástroj `pip`, stačí jednoducho napísať z príkazového riadku:

```bash
$ pip install selenium
```

Ak používate nástroj `poetry`, tak balík pridáte do zoznamu balíkov príkazom:

```bash
$ poetry add selenium
```

V prostredí _PyCharm_ zasa balíček nainštalujete v nastaveniach používaného interpretera jazyka Python.

**Poznámka:** Ak používate `selenium` v staršej verzii ako `4.10`, okrem balíka `selenium` potrebujete nainštalovať aj webdriver pre príslušný prehliadač. Toto však od verzie `4.10` nie je nutné, nakoľko si ho `selenium` nainštaluje samo. Tým sa vyhneme aj prípadným problémom pri spúšťaní príslušného webdrivera, ak systém nevie nájsť jeho spustiteľnú binárku priamo v ceste.


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
element.send_keys('pycon sk 2024')
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


Vytvorte test, ktorý overí, či sa na stránke nachádza vyhľadávací panel.

```python
def test_when_on_homepage_then_searchbar_is_present(homepage):
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    homepage.find_element(By.ID, 'id-search-field')
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

## Rýchlosť vykonávaných testov

* trvá to dlho
* najdlhšie trvá spustenie prehliadača
* cieľ - spustiť prehliadač iba raz na začiatku testovania a na jeho konci ho zatvoriť
* docielime to pomocou vhodných fixtures
* predvolene je scope pre fixture nastavený ako `function` - vykoná sa pre kažú jednu funkciu. pre nás bude výhodnejšie použiť scope `module` - pri otvorení modulu a teda sady testov.

Upravte scope pre fixture tak, aby sa prehliadač otvoril pre všetky testy len raz.

```python
@pytest.fixture(scope='module')
```


## Fixture so závislosťou na inom fixture

Aktuálny fixture s názvom `driver()` nie je veľmi univerzálny, pretože spustí prehliadač priamo s konrétnou stránkou. Ak by sme ale chceli testovať viacero stránok, museli by sme pre kažú jednu vytvoriť samostatný fixture.

Miesto toho môžeme pripraviť obecný fixture s názvom `browser()`, ktorý otvorí len prehliadač a následne ďalší fixture s názvom `homepage()`, ktorého parametrom bude ten obecný, ktorý len otvorí príslušnú (domovskú) stránku.

Tieto dve fixtures môžu vyzerať takto:

```python
@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.close()

@pytest.fixture()
def homepage(browser):
    browser.get('https://www.python.org')
    yield browser
```

Fixture `browser()` môže byť uložený v súbore `conftest.py` a fixture `homepage()` môže byť uložený v príslušnom module.


## Tips and Tricks

### Webdriver v Headless režime

Prehliadač Chrome je možné spustiť v tzv. headless režime, kedy sa nebude spúšťať s grafickým rozhraním, ale spustí sa len v pamäti. To je veľmi výhodné v prípadoch, ak chcete testy spúšťať na pozadí bez nutnosti mať spustené grafické prostredie.

```python
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
```

V headless režime je možné spustiť aj prehliadač Firefox. V jeho prípade bude spustenie driver-a vyzerať nasledovne:

```python
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
```




## Označovanie skupiny testov

Zatiaľ sme dokázali označkovať len samostatný test. Označkovať však vieme aj sadu testov. To vieme urobiť priamo v module pridaním globálnej premennej `pytestmark` napríklad v module `test_withdraw.py` takto:

```python
pytestmark = [
  pytest.mark.bankaccount,
  pytest.mark.withdraw
]
```

To nám pridáva možnosť spúšťať napríklad všetky testy pre bankový účet pomocou značky `bankaccount`. Ale rovnako tak môžeme spustiť len testy týkajúce sa operácie výberu peňazí z účtu pomocou značky `withdraw`.

Samozrejme netreba zabudnúť tieto značky pridať do konfiguračného súboru `pyproject.toml`.


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


## References

* [Selenium with Python](http://selenium-python.readthedocs.io)
* [http://naucse.python.cz/lessons/intro/testing/](http://naucse.python.cz/lessons/intro/testing/)
* [Selenium WebDriver](https://www.seleniumhq.org/docs/03_webdriver.jsp)
* [Selenium Easy](https://www.seleniumeasy.com/test/basic-radiobutton-demo.html) - stránky, kde sa dá testovať Selenium
* [Welcome to the-internet](http://the-internet.herokuapp.com/) - ukazkove stranky s html elementami dobre na stestovanie


## TODO

* [pytest-webdriver](https://pypi.org/project/pytest-webdriver/)

* testovať inú stránku ako [www.python.org](https://www.python.org)
  * ukázať test niečoho sofistikovanejšieho, ako len vyhľadávať niečo na stránke
  * niečo, kde bude mať význam ukázať závislosť jednotlivých fixtures
  * možno ukázať fixture s prihlásením používateľa

* možno používať ako webdriver Firefox
  * je pomalší :-D

* ako je to s uspávaním a pauzami?
