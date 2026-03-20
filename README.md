# E-Commerce & Digitale Geschäftsmodelle

**Interaktive Lernplattform · Master Marken- und Medienmanagement · THWS Business School**

Dozentin: Prof. Dr.-Ing. Eva Klenk

🌐 **Live:** https://swrobuts.github.io/e-comm/

---

## Struktur

```
e-comm/
├── index.html          # Kurs-Startseite (React + Tailwind)
├── data/               # Synthetische UrbanCart-Datensätze (CSV)
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   ├── sessions.csv
│   ├── reviews.csv
│   └── marketing.csv
└── generate_datasets.py  # Dataset-Generator (nur für Kursentwicklung)
```

## Datensätze (UrbanCart)

Alle Daten sind **synthetisch** und dienen ausschließlich Lehrzwecken.  
UrbanCart ist ein fiktives europäisches Online-Handelsunternehmen.

| Datei | Inhalt | Zeilen |
|-------|--------|--------|
| `customers.csv` | Kundenstamm (Region, Alter, Gerät, Premium) | 8.000 |
| `products.csv` | Produktkatalog (6 Kategorien, 41 Produkte) | 41 |
| `orders.csv` | Bestellungen 2023–2024 (Kanal, Status, Umsatz) | ~14.000 |
| `order_items.csv` | Bestellpositionen (Produkt, Menge, Preis) | ~30.000 |
| `sessions.csv` | Website-Funnel pro Kanal & Monat | 144 |
| `reviews.csv` | Produktbewertungen mit Sentiment-Label | ~5.800 |
| `marketing.csv` | Kanalperformance (Spend, CPA, ROAS) | 144 |

## Labs

| # | Thema | Schwierigkeit |
|---|-------|---------------|
| 01 | Erste Schritte mit Tableau | Einstieg |
| 02 | Kundenstruktur & Demografie | Einstieg |
| 03 | RFM-Analyse | Mittel |
| 04 | ABC-Analyse & Pareto | Mittel |
| 05 | Saisonalität & Trends | Mittel |
| 06 | Conversion Funnel | Mittel |
| 07 | Sentimentanalyse | Fortgeschritten |
| 08 | Marketing-Kanalanalyse | Fortgeschritten |
| 09 | Executive Dashboard | Fortgeschritten |

---

© THWS Business School Würzburg · Prof. Dr.-Ing. Eva Klenk
