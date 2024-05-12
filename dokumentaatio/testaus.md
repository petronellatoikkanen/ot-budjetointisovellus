# Testaus

## Sovelluksen testaus
- Sovelluksen testaus on jaettu services ja repositories tasolla. UserService-luokkaa testataan TestUserService-luokalla ja BudgetinService-luokkaa TestBudgetinService-luokalla. Vastaavasti UserRepository-luokkaa testataan TestUserRepository-luokalla ja BudgetingRepository-luokkaa TestBudgetinRepository-luokalla.

## Testauskattavuus
- Sovelluksen testikattavuus on 82%, huomioiden repositories, entities sekä services kansioiden sisällön. 


Lisäksi järjestelmää on testattu manuaalisesti ohjelman asennuksen ja käynnistyksen jälkeen. Ohjelmaan on jäänyt ongelma kustannuksien listaamisesta budjetointinäkymässä. 

Testit saa ajettua komennolla poetry run invoke test ja testiraportin komennolla poetry run invoke coverage-report



