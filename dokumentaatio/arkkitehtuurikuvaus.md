# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen pakkausrakenne koostuu pakkauksista ui (käyttöliittymä), services (sovelluslogiikka), repositories (pysyväistallennus) ja entities (tietokohteet)

## Käyttöliittymä

Sovelluksessa on käytössä kolme näkymää, login_view, create_user_view ja budgeting_view, ja näiden näyttämisestä huolehtii luokka UI.

## Tietojen tallennus

UserRepository ja BudgetingRepository huolehtivat tietojen hallinnasta. Tiedon tallennus tehdään SQLite-tietokantaan tauluihin Users, Budgets ja Expenses.
Tietokannat alustetaan poetry run invoke build -komennolla.

## Päätoiminnallisuudet

Sovelluksen päätoiminnallisuuksia ovat uuden käyttäjän luominen sekä sisään- ja uloskirjautuminen. 
Budjetointinäkymässä on lista käyttäjän budjeteista sekä niiden olemassa olevista kuluista. Lisäksi käyttäjä voi luoda uusia budjetteja ja kuluja uusiin sekä jo olemassa oleviin budjetteihin.

