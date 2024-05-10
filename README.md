# Ohjelmistotekniikka, harjoitustyö

## Budjetointisovellus

Sovelluksen avulla käyttäjät voivat luoda, muokata ja poistaa omia budjettimalleja eri tarkoituksiin

## Ohjelman dokumentaatio
- [Käyttöohje](https://github.com/petronellatoikkanen/ot-harjoitustyo/tree/master/dokumentaatio/käyttöohje.md)
 - [Vaatimusmäärittely](https://github.com/petronellatoikkanen/ot-harjoitustyo/tree/master/dokumentaatio/vaatimusmaarittely.md)
 - [Arkkitehtuurikuvaus](https://github.com/petronellatoikkanen/ot-harjoitustyo/tree/master/dokumentaatio/arkkitehtuurikuvaus.md)
 - [Testaus](https://github.com/petronellatoikkanen/ot-harjoitustyo/tree/master/dokumentaatio/testaus.md)
- [Työaikakirjanpito](https://github.com/petronellatoikkanen/ot-harjoitustyo/tree/master/dokumentaatio/tuntikirjanpito.md)
 - [Changelog](https://github.com/petronellatoikkanen/ot-harjoitustyo/tree/master/dokumentaatio/changelog.md)



## Ohjelman asennus

1. Asenna riippuvuudet 

```bash
poetry install
```

2. Suorita alustustoimenpiteet 

```bash
poetry run invoke build
```

3. Käynnistä ohjelma  

```bash
poetry run invoke start
```

## Ohjelman testaus

1. Suorita testit

```bash
poetry run invoke test
```

2. Generoi testikattavuusraportti

```bash
poetry run invoke coverage-report
```
