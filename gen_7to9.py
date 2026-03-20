#!/usr/bin/env python3
"""UrbanCart Labs 07-09 – vollstaendiger Inhalt"""
import json

with open('_thws_svg.txt') as f:
    SVG = f.read().strip()

JS = r"""
function setLang(l){document.documentElement.lang=l;document.querySelectorAll('[data-de]').forEach(el=>{const v=el.getAttribute('data-'+l);if(v!==null)el.innerHTML=v;});document.querySelectorAll('.lang-btn').forEach(b=>b.classList.toggle('is-active',b.textContent.toLowerCase()===l));localStorage.setItem('lang',l);if(typeof buildQuiz==='function')buildQuiz();}
(function(){const obs=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible');}),{threshold:.06});document.querySelectorAll('.sr').forEach(el=>obs.observe(el));})();
function lang(){return document.documentElement.lang||'de';}
let _ans={};
function buildQuiz(){const l=lang(),c=document.getElementById('quiz-questions');if(!c)return;c.innerHTML='';_ans={};updateProgress();QUESTIONS.forEach((q,qi)=>{const d=document.createElement('div');d.className='question';d.innerHTML='<div class="question__meta"><span class="question__num">'+(l==='de'?'Frage':'Question')+' '+(qi+1)+' / 15</span></div><div class="question__text">'+q.q[l]+'</div><div class="question__opts">'+q.opts[l].map((o,oi)=>'<button class="opt" onclick="answer('+qi+','+oi+')" id="opt-'+qi+'-'+oi+'"><span class="opt__key">'+('ABCD'[oi])+'</span>'+o+'</button>').join('')+'</div><div class="feedback" id="fb-'+qi+'" style="display:none"></div>';c.appendChild(d);});}
function answer(qi,oi){if(_ans[qi]!==undefined)return;_ans[qi]=oi;const l=lang(),q=QUESTIONS[qi],ok=oi===q.correct;for(let i=0;i<4;i++){const b=document.getElementById('opt-'+qi+'-'+i);b.disabled=true;if(i===q.correct)b.classList.add('is-correct');else if(i===oi)b.classList.add('is-wrong');}const fb=document.getElementById('fb-'+qi);fb.style.display='block';fb.className='feedback '+(ok?'is-correct':'is-wrong');fb.innerHTML=(ok?'&#10003;':'&#10007;')+' '+q.explain[l];updateProgress();if(Object.keys(_ans).length===QUESTIONS.length)showResult();}
function updateProgress(){const done=Object.keys(_ans).length,pct=(done/QUESTIONS.length*100).toFixed(0);const pt=document.getElementById('quiz-progress'),pf=document.getElementById('quiz-fill');if(pt)pt.textContent=done+' / 15';if(pf)pf.style.width=pct+'%';}
function showResult(){const score=Object.entries(_ans).filter(([i,a])=>a===QUESTIONS[+i].correct).length;const l=lang(),el=document.getElementById('quiz-result');el.classList.add('is-visible');document.getElementById('quiz-score').textContent=score;document.getElementById('quiz-msg').textContent=score>=13?(l==='de'?'Ausgezeichnet!':'Excellent!'):score>=10?(l==='de'?'Gut gemacht.':'Well done.'):(l==='de'?'Nochmal!':'Try again!');}
function resetQuiz(){document.getElementById('quiz-result').classList.remove('is-visible');buildQuiz();}
(function(){const l=localStorage.getItem('lang')||'de';setLang(l);})();
"""

CHECK = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="var(--green)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;margin-top:3px"><polyline points="20 6 9 17 4 12"/></svg>'
CLK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
FIL = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>'
QZ = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>'
DL = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>'
ARW = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>'
MON = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>'
BACK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>'
FWD = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
INFO = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>'


def nb(b_de, b_en):
    return (
        '<nav class="navbar"><div class="navbar__inner">'
        '<a href="index.html" class="navbar__logo-link">'
        '<svg class="navbar__logo" viewBox="0 0 274.3 91.2" xmlns="http://www.w3.org/2000/svg">' + SVG + '</svg>'
        '<div class="navbar__divider"></div>'
        '<span class="navbar__module" data-de="E-Commerce Labs" data-en="E-Commerce Labs"></span></a>'
        '<span class="navbar__badge" data-de="' + b_de + '" data-en="' + b_en + '"></span>'
        '<div class="navbar__right">'
        "<button class=\"lang-btn is-active\" onclick=\"setLang('de')\">DE</button>"
        "<button class=\"lang-btn\" onclick=\"setLang('en')\">EN</button>"
        '</div></div></nav>'
    )


def bc(lde, len_):
    return (
        '<nav class="breadcrumb"><div class="breadcrumb__inner">'
        '<div class="breadcrumb__item"><a href="index.html" data-de="Kurs&#252;bersicht" data-en="Course Overview"></a></div>'
        '<span class="breadcrumb__sep">&#8250;</span>'
        '<div class="breadcrumb__item"><a href="urbancart.html">UrbanCart</a></div>'
        '<span class="breadcrumb__sep">&#8250;</span>'
        '<div class="breadcrumb__item is-current" data-de="' + lde + '" data-en="' + len_ + '"></div>'
        '</div></nav>'
    )


def hero(kck_de, kck_en, h1de, h1en, emde, emen, subde, suben, dur, data, num):
    return (
        '<header class="lab-hero"><div class="lab-hero__inner"><div>'
        '<div class="lab-hero__kicker" data-de="' + kck_de + '" data-en="' + kck_en + '"></div>'
        '<h1 class="lab-hero__title"><span data-de="' + h1de + '" data-en="' + h1en + '"></span>'
        ' <em data-de="' + emde + '" data-en="' + emen + '"></em></h1>'
        '<p class="lab-hero__subtitle" data-de="' + subde + '" data-en="' + suben + '"></p>'
        '<div class="lab-hero__meta">'
        '<div class="lab-hero__meta-item">' + CLK + '<span><strong>' + dur + '</strong></span></div>'
        '<div class="lab-hero__meta-item">' + FIL + '<span><strong>' + data + '</strong></span></div>'
        '<div class="lab-hero__meta-item">' + QZ + '<span><strong data-de="15 Quiz-Fragen" data-en="15 quiz questions"></strong></span></div>'
        '</div></div><div class="lab-hero__num">' + num + '</div></div></header>'
    )


def prog(a):
    steps = [("Kontext","Context"),("Vorbereitung","Setup"),("Analyse","Analysis"),
             ("Visualisierung","Visualisation"),("Quiz","Quiz"),("KI","AI")]
    out = '<div class="lab-progress"><div class="lab-progress__inner">'
    for i, (de, en) in enumerate(steps):
        cls = "prog-step is-done" if i < a else ("prog-step is-active" if i == a else "prog-step")
        dot = ('<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">'
               '<polyline points="20 6 9 17 4 12"/></svg>') if i < a else str(i+1)
        out += '<div class="' + cls + '"><div class="prog-step__icon">' + dot + '</div><span data-de="' + de + '" data-en="' + en + '"></span></div>'
    return out + '</div></div>'


def sb(active):
    labs = [
        ("01","lab01.html","Erste Schritte mit Tableau"),
        ("02","lab02.html","Kundenstruktur &amp; Demografie"),
        ("03","lab03.html","RFM-Analyse"),
        ("04","lab04.html","ABC-Analyse &amp; Pareto"),
        ("05","lab05.html","Saisonalit&#228;t &amp; Zeitreihen"),
        ("06","lab06.html","Conversion Funnel"),
        ("07","lab07.html","Sentiment-Analyse"),
        ("08","lab08.html","Marketing-ROI"),
        ("09","lab09.html","Executive Dashboard"),
    ]
    items = ''.join(
        '<a href="' + h + '" class="sidebar-link' + (' is-active' if n == active else '') + '">'
        '<span style="font-size:10px;font-weight:800;color:var(--orange);width:22px;flex-shrink:0">' + n + '</span>' + t + '</a>'
        for n, h, t in labs
    )
    return (
        '<aside class="lab-sidebar">'
        '<div class="sidebar-section">'
        '<div class="sidebar-title" data-de="Alle Labs" data-en="All Labs"></div>'
        '<nav class="sidebar-nav">' + items + '</nav></div>'
        '<div class="sidebar-section">'
        '<div class="sidebar-data-card">'
        '<div class="sidebar-data-card__title">UrbanCart</div>'
        '<div class="sidebar-data-row"><span class="sidebar-data-row__label" data-de="Bestellungen" data-en="Orders"></span><span class="sidebar-data-row__value">14.355</span></div>'
        '<div class="sidebar-data-row"><span class="sidebar-data-row__label" data-de="Kunden" data-en="Customers"></span><span class="sidebar-data-row__value">8.000</span></div>'
        '<div class="sidebar-data-row"><span class="sidebar-data-row__label" data-de="Zeitraum" data-en="Period"></span><span class="sidebar-data-row__value">2023&#8211;2024</span></div>'
        '</div>'
        '<a href="https://github.com/swrobuts/e-comm/tree/main/data" target="_blank" rel="noopener" class="sidebar-download">' + DL +
        '<span data-de="Datens&#228;tze laden" data-en="Download datasets"></span></a>'
        '<a href="urbancart.html" style="display:flex;align-items:center;gap:8px;font-size:12px;font-weight:700;color:var(--blue);margin-top:8px;padding:8px 0">'
        '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
        '<span data-de="Webshop ansehen" data-en="View webshop"></span></a>'
        '</div></aside>'
    )


def lz(items):
    r = ''.join(
        '<li style="display:flex;gap:8px;align-items:flex-start;margin-bottom:4px">' + CHECK +
        '<span data-de="' + de + '" data-en="' + en + '"></span></li>'
        for de, en in items
    )
    return (
        '<section class="block sr">'
        '<div class="block__eyebrow" data-de="Lernziele" data-en="Learning Objectives"></div>'
        '<h2 class="block__title" data-de="Was lernst du in diesem Lab?" data-en="What will you learn?"></h2>'
        '<div class="block__rule"></div>'
        '<ul style="font-size:14px;color:var(--gray-600);line-height:1.9;list-style:none;padding:0;margin-top:8px">' + r + '</ul>'
        '</section>'
    )


def step(n, tde, ten, bde, ben, tip_de='', tip_en='', opened=False):
    tip = ('<div class="step__tip" data-de="' + tip_de + '" data-en="' + (tip_en or tip_de) + '"></div>') if tip_de else ''
    op = ' open' if opened else ''
    return (
        '<details class="step"' + op + '>'
        '<summary class="step__summary"><div class="step__num">' + str(n) + '</div>'
        '<div class="step__title" data-de="' + tde + '" data-en="' + ten + '"></div>'
        '<div class="step__arrow">' + ARW + '</div></summary>'
        '<div class="step__body"><p data-de="' + bde + '" data-en="' + ben + '"></p>' + tip + '</div>'
        '</details>'
    )


def tbox(de, en):
    return (
        '<div class="tableau-box"><div class="tableau-box__header">' + MON +
        '<span class="tableau-box__tag">Tableau Public</span></div>'
        '<div class="tableau-box__body" data-de="' + de + '" data-en="' + en + '"></div></div>'
    )


def concept(lt, lde, len_, rt, rde, ren):
    return (
        '<div class="concept-box sr">'
        '<div class="concept-item"><div class="concept-item__title" style="color:var(--blue)">' + INFO + ' ' + lt + '</div>'
        '<div class="concept-item__text" data-de="' + lde + '" data-en="' + len_ + '"></div></div>'
        '<div class="concept-item"><div class="concept-item__title" style="color:var(--orange)">' + INFO + ' ' + rt + '</div>'
        '<div class="concept-item__text" data-de="' + rde + '" data-en="' + ren + '"></div></div>'
        '</div>'
    )


def infobox(tde, ten, items):
    rows = ''.join(
        '<div class="infobox__item"><div class="infobox__item__title">' + t +
        '</div><div class="infobox__item__sub">' + s + '</div></div>'
        for t, s in items
    )
    return (
        '<div class="infobox sr">'
        '<div class="infobox__title" data-de="' + tde + '" data-en="' + ten + '"></div>'
        '<div class="infobox__grid">' + rows + '</div></div>'
    )


def kpi(svg, vde, ven, lbl, dfn):
    return (
        '<div class="kpi">'
        '<svg class="kpi__icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">' + svg + '</svg>'
        '<div class="kpi__value" data-de="' + vde + '" data-en="' + ven + '"></div>'
        '<div class="kpi__label">' + lbl + '</div>'
        '<div class="kpi__def">' + dfn + '</div></div>'
    )


def quiz_sec(nhref, nde, nen):
    return (
        '<section class="block">'
        '<div class="block__eyebrow" data-de="Wissenstest" data-en="Knowledge Test"></div>'
        '<h2 class="block__title" data-de="Quiz &middot; 15 Fragen" data-en="Quiz &middot; 15 Questions"></h2>'
        '<div class="block__rule"></div>'
        '<div class="quiz-section"><div class="quiz-header">'
        '<p class="quiz-header__sub" data-de="Beantworte alle Fragen &#8211; sofortiges Feedback nach jeder Antwort." data-en="Answer all questions &#8211; immediate feedback after each answer."></p>'
        '<p class="quiz-progress-text" id="quiz-progress">0 / 15</p>'
        '<div class="quiz-progress-bar"><div class="quiz-progress-fill" id="quiz-fill"></div></div>'
        '</div><div id="quiz-questions"></div>'
        '<div class="quiz-result" id="quiz-result">'
        '<div class="quiz-result__score" id="quiz-score">0</div>'
        '<div class="quiz-result__of">/15</div>'
        '<div class="quiz-result__label" data-de="Punkte" data-en="Points"></div>'
        '<div class="quiz-result__msg" id="quiz-msg"></div>'
        '<a href="' + nhref + '" class="quiz-result__next"><span data-de="' + nde + '" data-en="' + nen + '"></span>' + FWD + '</a>'
        '<button class="quiz-result__retry" onclick="resetQuiz()">'
        '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 .49-3.5"/></svg>'
        '<span data-de="Nochmal versuchen" data-en="Try again"></span></button>'
        '</div></div></section>'
    )


def ai_bl(tags, prompt):
    t_html = ''.join('<span class="ai-block__tag">' + t + '</span>' for t in tags)
    return (
        '<section class="block sr"><div class="ai-block">'
        '<div class="ai-block__eyebrow" data-de="KI &amp; Python &#8212; Ausblick" data-en="AI &amp; Python &#8212; Outlook"></div>'
        '<h3 class="ai-block__title" data-de="Von Tableau zu Python: Wie sieht das automatisiert aus?" data-en="From Tableau to Python: How does automation work?"></h3>'
        '<p class="ai-block__intro" data-de="Tableau ist ideal fuer explorative Analyse ohne Code. Python ermoeglicht dieselbe Analyse automatisiert und skalierbar. Nutze diesen Prompt direkt in ChatGPT oder Claude:" data-en="Tableau is perfect for exploratory analysis without code. Python allows the same analysis automated and scalable. Use this prompt directly in ChatGPT or Claude:"></p>'
        '<div class="ai-block__stack">' + t_html + '</div>'
        '<div class="ai-block__prompt-label" data-de="Prompt fuer ChatGPT / Claude" data-en="Prompt for ChatGPT / Claude"></div>'
        '<pre>' + prompt + '</pre>'
        "<div class=\"ai-block__context\" data-de=\"Referenz: <a href='https://whi-dashboard.butscher.cloud/' target='_blank' rel='noopener'>whi-dashboard.butscher.cloud</a> &#8212; Plotly Dash, interaktiv.\" data-en=\"Reference: <a href='https://whi-dashboard.butscher.cloud/' target='_blank' rel='noopener'>whi-dashboard.butscher.cloud</a> &#8212; Plotly Dash, interactive.\"></div>"
        '</div></section>'
    )


def nav(phref, pde, pen, nhref, nde, nen):
    return (
        '<div class="lab-nav">'
        '<a href="' + phref + '" class="lab-nav__back">' + BACK + '<span data-de="' + pde + '" data-en="' + pen + '"></span></a>'
        '<a href="' + nhref + '" class="lab-nav__next"><span data-de="' + nde + '" data-en="' + nen + '"></span>' + FWD + '</a>'
        '</div>'
    )


def wrap(main, sbn):
    return '<div style="max-width:1200px;margin:0 auto"><div class="lab-layout"><main class="lab-main">' + main + '</main>' + sb(sbn) + '</div></div>'


def page(title, body, q):
    return (
        '<!DOCTYPE html>\n<html lang="de">\n<head>\n'
        '<meta charset="UTF-8"/>\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n'
        '<title>' + title + ' &middot; E-Commerce &amp; Digitale Gesch&#228;ftsmodelle &middot; THWS</title>\n'
        '<link rel="stylesheet" href="design-system.css"/>\n'
        '</head>\n<body>\n<div class="topbar"></div>\n'
        + body +
        '\n<script>\nconst QUESTIONS=' + json.dumps(q, ensure_ascii=False) + ';\n' + JS + '\n</script>\n'
        '</body>\n</html>'
    )


def Q(qde, qen, ode, oen, c, ede, een):
    return {"q": {"de": qde, "en": qen}, "opts": {"de": ode, "en": oen}, "correct": c,
            "explain": {"de": ede, "en": een}}


# ===========================================================
# LAB 07 – SENTIMENT-ANALYSE & CUSTOMER VOICE
# ===========================================================
q07 = [
    Q("Was ist Sentiment-Analyse?", "What is sentiment analysis?",
      ["Umsatzanalyse", "Klassifikation von Texten als positiv, neutral oder negativ", "Kundendemografie", "Produktanalyse"],
      ["Revenue analysis", "Classification of texts as positive, neutral or negative", "Customer demographics", "Product analysis"],
      1, "Sentiment-Analyse extrahiert die emotionale Tonalitaet aus Text: positiv, neutral oder negativ.",
      "Sentiment analysis extracts the emotional tone from text: positive, neutral or negative."),
    Q("Was ist NPS?", "What is NPS?",
      ["Net Profit Score", "Net Promoter Score: Weiterempfehlungsbereitschaft 0-10", "Negative Product Sales", "New Purchase Score"],
      ["Net Profit Score", "Net Promoter Score: willingness to recommend 0-10", "Negative Product Sales", "New Purchase Score"],
      1, "NPS: Wie wahrscheinlich empfiehlst du uns? 0-6=Detraktoren, 7-8=Passive, 9-10=Promotoren.",
      "NPS: How likely to recommend us? 0-6=Detractors, 7-8=Passives, 9-10=Promoters."),
    Q("Wie berechnet man NPS?", "How to calculate NPS?",
      ["Promotoren + Detraktoren", "Promotoren% minus Detraktoren%", "Durchschnitt aller Scores", "Passive x 2"],
      ["Promoters + Detractors", "Promoters% minus Detractors%", "Average of all scores", "Passives x 2"],
      1, "NPS = Promotoren% - Detraktoren%. Passive werden ignoriert. Bereich: -100 bis +100.",
      "NPS = Promoters% - Detractors%. Passives are ignored. Range: -100 to +100."),
    Q("Was enthaelt reviews.csv?", "What does reviews.csv contain?",
      ["Produktpreise", "Kundenbewertungen: review_text, rating, product_name, sentiment", "Bestelldaten", "Sessiondaten"],
      ["Product prices", "Customer reviews: review_text, rating, product_name, sentiment", "Order data", "Session data"],
      1, "reviews.csv: review_id, customer_id, product_name, rating (1-5), review_text, sentiment.",
      "reviews.csv: review_id, customer_id, product_name, rating (1-5), review_text, sentiment."),
    Q("Was ist der Unterschied Rating vs. Sentiment?", "What is the difference between rating and sentiment?",
      ["Kein Unterschied", "Rating=Zahl (1-5 Sterne), Sentiment=Texttonalitaet (positiv/negativ)", "Rating ist besser", "Sentiment ist genauer"],
      ["No difference", "Rating=number (1-5 stars), Sentiment=text tone (positive/negative)", "Rating is better", "Sentiment is more precise"],
      1, "Rating: explizite Zahl. Sentiment: aus Freitext extrahierte Tonalitaet. Beides zusammen ist maechtig.",
      "Rating: explicit number. Sentiment: tone extracted from free text. Both together are powerful."),
    Q("Was zeigt eine Wordcloud?", "What does a word cloud show?",
      ["Genaue Zahlen", "Haeufige Begriffe in Texten durch Schriftgroesse visualisiert", "Zeitverlaeufe", "Geografische Daten"],
      ["Precise numbers", "Frequent terms in texts visualised by font size", "Time trends", "Geographic data"],
      1, "Wordcloud: grosse Woerter = haeufig. Gut fuer explorativen Ueberblick.",
      "Word cloud: large words = frequent. Good for exploratory overview."),
    Q("Was ist VADER?", "What is VADER?",
      ["Ein Datenbankformat", "Lexikonbasiertes Sentiment-Tool fuer Englisch (pip install vaderSentiment)", "Tableau-Feature", "ML-Modell"],
      ["A database format", "Lexicon-based sentiment tool for English (pip install vaderSentiment)", "Tableau feature", "ML model"],
      1, "VADER: schnell, kein Training noetig, gut fuer kurze Social-Media-Texte und Reviews.",
      "VADER: fast, no training needed, good for short social media texts and reviews."),
    Q("Was bedeutet ein negativer Sentiment-Peak fuer ein Produkt?", "What does a negative sentiment peak mean for a product?",
      ["Produkt ist beliebt", "Moegliches Qualitaetsproblem oder unerfuellte Erwartung", "Zu guenstig", "Gut fuer Marketing"],
      ["Product is popular", "Possible quality issue or unmet expectation", "Too cheap", "Good for marketing"],
      1, "Negativer Peak: sofortige Ursachenforschung. Batch-Problem? Fehlbeschreibung? Lieferproblem?",
      "Negative peak: immediate root cause analysis. Batch issue? Wrong description? Delivery problem?"),
    Q("Welcher Tableau-Chart zeigt Sentiment-Verteilung pro Produkt?", "Which Tableau chart shows sentiment distribution per product?",
      ["Liniendiagramm", "Gestapelter Balken (100%): positiv/neutral/negativ pro Produkt", "Kreisdiagramm", "Scatter Plot"],
      ["Line chart", "Stacked bar (100%): positive/neutral/negative per product", "Pie chart", "Scatter plot"],
      1, "100%-gestapelter Balken: Anteile je Produkt vergleichbar machen. Farben: Gruen/Grau/Rot.",
      "100%-stacked bar: makes shares comparable per product. Colours: Green/Grey/Red."),
    Q("Wie filtert man negative Reviews in Tableau?", "How to filter negative reviews in Tableau?",
      ["Alle anzeigen", "Filter auf sentiment=negative oder rating <= 2 setzen", "Reviews loeschen", "Manuell lesen"],
      ["Show all", "Set filter on sentiment=negative or rating <= 2", "Delete reviews", "Read manually"],
      1, "Filter auf sentiment: Nur negative anzeigen. Dann review_text lesen fuer Ursachenanalyse.",
      "Filter on sentiment: show only negative. Then read review_text for root cause analysis."),
    Q("Was ist Topic Modeling?", "What is topic modelling?",
      ["Ein Diagrammtyp", "KI-Methode um wiederkehrende Themen in Texten zu finden", "Ein Filterbegriff", "Produktkategorisierung"],
      ["A chart type", "AI method to find recurring themes in texts", "A filter term", "Product categorisation"],
      1, "Topic Modeling (LDA): findet Themen wie Lieferung, Qualitaet, Preis automatisch in Reviews.",
      "Topic modelling (LDA): automatically finds themes like delivery, quality, price in reviews."),
    Q("Was ist der Vorteil von Sentiment gegenueber reinem Rating?", "What is the advantage of sentiment over pure rating?",
      ["Kein Vorteil", "Sentiment erkennt auch 5-Sterne-Reviews mit negativen Kommentaren", "Rating ist praeziser", "Gleich"],
      ["No advantage", "Sentiment also detects 5-star reviews with negative comments", "Rating is more precise", "Same"],
      1, "Ironie: 5 Sterne aber 'Nie wieder!' -> Sentiment erkennt das als negativ, Rating nicht.",
      "Irony: 5 stars but 'Never again!' -> Sentiment detects this as negative, rating does not."),
    Q("Welches Feld gruppiert Reviews nach Produkt?", "Which field groups reviews by product?",
      ["review_id", "customer_id", "product_name", "sentiment"],
      ["review_id", "customer_id", "product_name", "sentiment"],
      2, "product_name auf Zeilen, COUNTD(review_id) auf Spalten: Bewertungsanzahl pro Produkt.",
      "product_name to Rows, COUNTD(review_id) to Columns: review count per product."),
    Q("Was zeigt ein Rating-Histogramm (1-5)?", "What does a rating histogram (1-5) show?",
      ["Umsatzverteilung", "Haeufigkeit jedes Bewertungs-Scores", "Zeitverlauf", "Geografisch"],
      ["Revenue distribution", "Frequency of each rating score", "Time trend", "Geographic"],
      1, "Rating-Histogramm: polarisiert das Produkt (viele 1 und 5) oder konsistent gut/schlecht?",
      "Rating histogram: is the product polarising (many 1 and 5) or consistently good/bad?"),
    Q("Was ist Transformer-basierte Sentiment-Analyse?", "What is transformer-based sentiment analysis?",
      ["Eine alte Methode", "KI-Modell (BERT, GPT) das Kontext und Ironie versteht", "Dasselbe wie VADER", "Nur fuer Deutsch"],
      ["An old method", "AI model (BERT, GPT) that understands context and irony", "Same as VADER", "Only for German"],
      1, "BERT/RoBERTa: versteht Kontext und Ironie. Genauer als VADER, aber benoetigt mehr Ressourcen.",
      "BERT/RoBERTa: understands context and irony. More accurate than VADER but needs more resources."),
]

m07 = (
    lz([
        ("Sentiment-Analyse und NPS als Methoden verstehen", "Understand sentiment analysis and NPS as methods"),
        ("Rating-Verteilung und Sentiment pro Produkt in Tableau visualisieren", "Visualise rating distribution and sentiment per product in Tableau"),
        ("Kritische Produkte mit negativem Sentiment identifizieren", "Identify critical products with negative sentiment"),
        ("Qualitative Insights aus Review-Texten ableiten", "Derive qualitative insights from review texts"),
    ])
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kontext" data-en="Context"></div>'
    + '<h2 class="block__title" data-de="Was sagen deine Kunden wirklich?" data-en="What do your customers really say?"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="Sterne-Ratings zeigen die Zahl. Review-Texte zeigen den Grund. UrbanCart hat 5.857 Bewertungen &#8211; darin stecken Produktprobleme, Lieferissues und echte Begeisterung. Sentiment-Analyse macht das messbar und vergleichbar." data-en="Star ratings show the number. Review texts show the reason. UrbanCart has 5,857 reviews &#8211; they contain product problems, delivery issues and genuine enthusiasm. Sentiment analysis makes that measurable and comparable."></p>'
    + concept(
        "Was ist Sentiment?",
        "Tonalitaet eines Textes: positiv (begeistert, zufrieden), neutral (sachlich), negativ (frustriert, enttaeuscht). Wird aus dem Freitext extrahiert &#8211; unabhaengig vom Sterne-Rating.",
        "Tone of a text: positive (enthusiastic, satisfied), neutral (factual), negative (frustrated, disappointed). Extracted from free text &#8211; independent of the star rating.",
        "Rating vs. NPS",
        "Rating (1-5): explizit, einfach. NPS (0-10): Weiterempfehlung. NPS unterscheidet Promotoren (9-10), Passive (7-8) und Detraktoren (0-6). NPS = Promotoren% - Detraktoren%.",
        "Rating (1-5): explicit, simple. NPS (0-10): recommendation. NPS distinguishes promoters (9-10), passives (7-8) and detractors (0-6). NPS = Promoters% - Detractors%."
    )
    + infobox("Typische Sentiment-Themen in E-Commerce Reviews", "Typical Sentiment Topics in E-Commerce Reviews", [
        ("Lieferung (30%)", "Schnell, spaet, beschaedigt, Paketdienst"),
        ("Qualitaet (25%)", "Material, Verarbeitung, wie beschrieben"),
        ("Preis/Leistung (20%)", "Guenstig, zu teuer, gut investiert"),
        ("Kundenservice (15%)", "Freundlich, nicht erreichbar, Kulanz"),
        ("Verpackung (10%)", "Gut verpackt, Plastikmuell, Geschenkverpackung"),
    ])
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Vorbereitung" data-en="Preparation"></div>'
    + '<h2 class="block__title" data-de="reviews.csv laden" data-en="Load reviews.csv"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="steps">'
    + step(1, "reviews.csv verbinden", "Connect reviews.csv",
           "Tableau > Verbinden > Textdatei > reviews.csv. Felder pruefen: review_id, customer_id, product_name, rating, review_text, sentiment.",
           "Tableau > Connect > Text File > reviews.csv. Check fields: review_id, customer_id, product_name, rating, review_text, sentiment.",
           tip_de="sentiment ist bereits vorklassifiziert (positive/neutral/negative). In der Praxis wuerde man NLP-Tools einsetzen.",
           tip_en="sentiment is already pre-classified (positive/neutral/negative). In practice you would use NLP tools.",
           opened=True)
    + step(2, "Datenqualitaet pruefen", "Check data quality",
           "COUNTD([review_id]) pruefen: 5.857. Wie viele pro Kategorie? Welche Produkte haben die meisten Reviews? Welches Sentiment dominiert?",
           "Check COUNTD([review_id]): 5,857. How many per category? Which products have the most reviews? Which sentiment dominates?")
    + '</div>'
    + tbox("Tableau kann review_text nicht direkt analysieren (kein NLP). Wir nutzen das vorberechnete sentiment-Feld fuer die Visualisierung.",
           "Tableau cannot directly analyse review_text (no NLP). We use the pre-calculated sentiment field for visualisation.")
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Analyse" data-en="Analysis"></div>'
    + '<h2 class="block__title" data-de="Sentiment-Dashboard aufbauen" data-en="Build the Sentiment Dashboard"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="4 Arbeitsblatter: Rating-Verteilung, Sentiment pro Produkt, Negativtrend, Kritische Reviews." data-en="4 worksheets: rating distribution, sentiment per product, negative trend, critical reviews."></p>'
    + '<div class="steps">'
    + step(1, "Rating-Histogramm (1-5 Sterne)", "Rating histogram (1-5 stars)",
           "Neues Arbeitsblatt. rating auf Spalten, COUNTD([review_id]) auf Zeilen. Chart-Typ: Balken. Farbe: Orange (#E87722) fuer 4-5, Grau fuer 3, Rot fuer 1-2.",
           "New worksheet. rating to Columns, COUNTD([review_id]) to Rows. Chart type: Bar. Colour: Orange (#E87722) for 4-5, Grey for 3, Red for 1-2.",
           tip_de="Polarisiertes Muster (viele 1 und 5) = gespalten. U-Form deutet auf Qualitaetsinkonsistenz hin.",
           tip_en="Polarised pattern (many 1 and 5) = divided. U-shape indicates quality inconsistency.",
           opened=True)
    + step(2, "Sentiment-Verteilung pro Produkt (100%-Balken)", "Sentiment distribution per product (100% bar)",
           "Neues Arbeitsblatt. product_name auf Zeilen. sentiment auf Farbe (Gruen=positiv, Grau=neutral, Rot=negativ). SUM([Number of Records]) auf Spalten. Darstellung: 100%-gestapelter Balken.",
           "New worksheet. product_name to Rows. sentiment to Colour (Green=positive, Grey=neutral, Red=negative). SUM([Number of Records]) to Columns. Display: 100% stacked bar.",
           tip_de="Sortiere nach negativem Anteil: Problempotenzial sofort sichtbar.",
           tip_en="Sort by negative share: problem potential immediately visible.")
    + step(3, "Negative Reviews gefiltert anzeigen", "Show filtered negative reviews",
           "Neues Arbeitsblatt. Filter: sentiment = negative. product_name auf Zeilen, review_text auf Text. So sieht man direkt was Kunden kritisieren.",
           "New worksheet. Filter: sentiment = negative. product_name to Rows, review_text to Text. You directly see what customers criticise.",
           tip_de="review_text lesen: Was sind die konkreten Beschwerden? Lieferung? Material? Passform? Das sind Handlungsfelder.",
           tip_en="Read review_text: what are the specific complaints? Delivery? Material? Fit? These are action areas.")
    + step(4, "Dashboard zusammenbauen", "Assemble dashboard",
           "Neues Dashboard. Rating-Histogramm oben links. Sentiment-Balken gross rechts. Negative Reviews-Liste unten. Titel: UrbanCart Customer Voice Dashboard.",
           "New dashboard. Rating histogram top-left. Sentiment bar large right. Negative reviews list bottom. Title: UrbanCart Customer Voice Dashboard.")
    + '</div></section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kennzahlen" data-en="Key Metrics"></div>'
    + '<h2 class="block__title" data-de="Sentiment-Kennzahlen" data-en="Sentiment Metrics"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="kpi-row">'
    + kpi('<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>',
          '5.857 Reviews', '5,857 reviews', 'Gesamt-Reviews', 'reviews.csv')
    + kpi('<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>',
          '~68% positiv', '~68% positive', 'Positiver Sentiment', 'Anteil positiver Reviews')
    + kpi('<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>',
          '~15% negativ', '~15% negative', 'Negativer Sentiment', 'Optimierungspotenzial')
    + '</div></section>'
    + quiz_sec("lab08.html", "Weiter zu Lab 08: Marketing-ROI", "Continue to Lab 08: Marketing ROI")
    + ai_bl(["Python", "pandas", "VADER", "WordCloud", "Plotly"],
            "# Prompt fuer ChatGPT / Claude:\n"
            '"Erstelle eine Sentiment-Analyse fuer E-Commerce Reviews.\n'
            "Lade reviews.csv (pandas).\n"
            "1. Rating-Histogramm: Plotly Balken, Farben: 4-5=#E87722, 3=#9CA3AF, 1-2=#DC2626\n"
            "2. Sentiment-Verteilung pro Produkt: 100% Stacked Bar\n"
            "   Farben: positiv=#3D7A56, neutral=#9CA3AF, negativ=#DC2626\n"
            "3. WordCloud aus negativen review_text (pip install wordcloud)\n"
            "   Stoerwoerter entfernen, Top-50 Woerter anzeigen\n"
            'NPS berechnen: Promotoren% - Detraktoren% (rating 9-10 vs 0-6)."')
    + nav("lab06.html", "&#8592; Lab 06: Conversion Funnel", "&#8592; Lab 06: Conversion Funnel",
          "lab08.html", "Lab 08: Marketing-ROI &#8594;", "Lab 08: Marketing ROI &#8594;")
)

with open('lab07.html', 'w', encoding='utf-8') as f:
    f.write(page(
        "Lab 07 &#8211; Sentiment-Analyse &amp; Customer Voice",
        nb("Lab 07 von 09", "Lab 07 of 09")
        + bc("Lab 07 &#8211; Sentiment-Analyse", "Lab 07 &#8211; Sentiment Analysis")
        + hero("Lab 07 von 09 &#183; Fortgeschritten", "Lab 07 of 09 &#183; Advanced",
               "Sentiment-Analyse &amp;", "Sentiment Analysis &amp;", "Customer Voice", "Customer Voice",
               "Was sagen deine Kunden wirklich? Du analysierst 5.857 UrbanCart-Bewertungen nach Tonalitaet, identifizierst Problemprodukte und entwickelst datenbasierte Qualitaetsempfehlungen.",
               "What do your customers really say? You analyse 5,857 UrbanCart reviews by tone, identify problem products and develop data-driven quality recommendations.",
               "60&#8211;90 Min.", "reviews.csv", "07")
        + prog(3) + wrap(m07, "07"), q07))
print("lab07.html OK")


# ===========================================================
# LAB 08 – MARKETING-ROI & KANALANALYSE
# ===========================================================
q08 = [
    Q("Was ist Marketing-ROI?", "What is Marketing ROI?",
      ["Kosten des Marketings", "Return on Investment: Gewinn/Umsatz durch Marketingausgaben im Verhaeltnis zu Kosten", "Anzahl Klicks", "Impressionen"],
      ["Marketing costs", "Return on Investment: profit/revenue from marketing relative to costs", "Number of clicks", "Impressions"],
      1, "ROI = (Umsatz - Kosten) / Kosten x 100. Zeigt: Wie viel Euro Umsatz bringt 1 Euro Marketing?",
      "ROI = (Revenue - Cost) / Cost x 100. Shows: how much revenue does 1 Euro of marketing generate?"),
    Q("Was ist CPA?", "What is CPA?",
      ["Cost per Action: Kosten pro gewuenschter Aktion (z.B. Kauf)", "Click per Ad", "Customer Product Analysis", "Channel Performance Average"],
      ["Cost per Action: cost per desired action (e.g. purchase)", "Click per Ad", "Customer Product Analysis", "Channel Performance Average"],
      0, "CPA = Cost per Acquisition. Marketingkosten / Anzahl Kaeufern. Je niedriger, desto effizienter.",
      "CPA = Cost per Acquisition. Marketing cost / number of buyers. The lower, the more efficient."),
    Q("Welche Kanaele stehen in marketing.csv?", "Which channels are in marketing.csv?",
      ["Nur Social Media", "SEA, Social, E-Mail, Organic, Direct, Affiliate", "Nur SEA", "Nur E-Mail"],
      ["Only social media", "SEA, Social, Email, Organic, Direct, Affiliate", "Only SEA", "Only email"],
      1, "marketing.csv enthaelt: channel, campaign_id, spend, clicks, conversions, revenue, date.",
      "marketing.csv contains: channel, campaign_id, spend, clicks, conversions, revenue, date."),
    Q("Was ist CTR?", "What is CTR?",
      ["Cost to Revenue", "Click-Through-Rate: Anteil der Impressionen die zu Klicks fuehren", "Customer Tracking Rate", "Channel Transfer Rate"],
      ["Cost to Revenue", "Click-Through Rate: share of impressions that lead to clicks", "Customer Tracking Rate", "Channel Transfer Rate"],
      1, "CTR = Klicks / Impressionen x 100. Misst die Relevanz einer Werbeanzeige.",
      "CTR = clicks / impressions x 100. Measures the relevance of an ad."),
    Q("Was ist ROAS?", "What is ROAS?",
      ["Return on Ad Spend: Umsatz / Werbeausgaben", "Rate of Ad Sales", "Revenue of All Segments", "Return of Average Score"],
      ["Return on Ad Spend: Revenue / Ad Spend", "Rate of Ad Sales", "Revenue of All Segments", "Return of Average Score"],
      0, "ROAS = Revenue / Ad Spend. ROAS von 4 = 4 Euro Umsatz pro 1 Euro Werbeausgaben.",
      "ROAS = Revenue / Ad Spend. ROAS of 4 = 4 Euro revenue per 1 Euro ad spend."),
    Q("Was ist Attribution?", "What is attribution?",
      ["Produktzuordnung", "Zuordnung des Kauferfolgs zu einem oder mehreren Marketingkanaelen", "Ein Diagrammtyp", "Filtermethode"],
      ["Product assignment", "Assigning purchase success to one or more marketing channels", "A chart type", "Filter method"],
      1, "Attribution: Welcher Kanal hat den Kauf beeinflusst? Last-Click, First-Click oder Multi-Touch.",
      "Attribution: which channel influenced the purchase? Last-click, first-click or multi-touch."),
    Q("Was ist Last-Click Attribution?", "What is last-click attribution?",
      ["Erster Kontaktpunkt bekommt Credit", "Letzter Klick vor dem Kauf bekommt 100% des Credits", "Gleichmaessige Verteilung", "KI-basiert"],
      ["First touchpoint gets credit", "Last click before purchase gets 100% of the credit", "Equal distribution", "AI-based"],
      1, "Last-Click: einfach zu messen, ueberschaetzt letzte Kanaele (oft Direct/Organic), unterschaetzt fruehe.",
      "Last-click: easy to measure, overvalues last channels (often direct/organic), undervalues early ones."),
    Q("Welcher Kanal hat typischerweise hoechsten ROI?", "Which channel typically has the highest ROI?",
      ["SEA (immer teuer)", "E-Mail-Marketing (guenstig, hohe Conversion bei bestehenden Kunden)", "Social Media", "Display Ads"],
      ["SEA (always expensive)", "Email marketing (cheap, high conversion with existing customers)", "Social media", "Display ads"],
      1, "E-Mail: niedrige Kosten, hohe Conversion bei Bestandskunden. ROI oft 40:1 oder hoeher.",
      "Email: low cost, high conversion with existing customers. ROI often 40:1 or higher."),
    Q("Was ist ein Kanal-Mix?", "What is a channel mix?",
      ["Nur ein Kanal", "Die Verteilung des Marketingbudgets ueber verschiedene Kanaele", "Produkt-Sortiment", "Zahlungsmethoden"],
      ["Only one channel", "Distribution of marketing budget across different channels", "Product range", "Payment methods"],
      1, "Kanal-Mix: welcher Anteil Budget geht in SEA, Social, E-Mail etc. Diversifikation reduziert Risiko.",
      "Channel mix: what share of budget goes to SEA, social, email etc. Diversification reduces risk."),
    Q("Was zeigt eine Bubble Chart fuer Kanalanalyse?", "What does a bubble chart show for channel analysis?",
      ["Zeitverlauf", "3 Dimensionen: X=Spend, Y=Revenue, Groesse=Conversions oder ROI", "Anteile", "Geografisch"],
      ["Time trend", "3 dimensions: X=Spend, Y=Revenue, Size=Conversions or ROI", "Shares", "Geographic"],
      1, "Bubble Chart: Spend vs. Revenue, Groesse = Conversions. Oben links = guenstig+umsatzstark = Effizienz-Gewinner.",
      "Bubble chart: Spend vs. Revenue, size = Conversions. Top-left = cheap+high revenue = efficiency winner."),
    Q("Wie berechnet man CPA in Tableau?", "How to calculate CPA in Tableau?",
      ["SUM([spend])", "SUM([spend]) / SUM([conversions])", "AVG([spend])", "COUNT([channel])"],
      ["SUM([spend])", "SUM([spend]) / SUM([conversions])", "AVG([spend])", "COUNT([channel])"],
      1, "CPA = Gesamtausgaben / Gesamtconversions. Berechnetes Feld in Tableau.",
      "CPA = Total spend / Total conversions. Calculated field in Tableau."),
    Q("Was ist Multi-Touch-Attribution?", "What is multi-touch attribution?",
      ["Nur letzter Klick zaehlt", "Mehrere Kontaktpunkte der Customer Journey erhalten anteiligen Credit", "Nur erster Klick", "Keiner bekommt Credit"],
      ["Only last click counts", "Multiple touchpoints in the customer journey receive proportional credit", "Only first click", "No one gets credit"],
      1, "Multi-Touch: realistischer als Last-Click. Linear, Time-Decay oder Algorithmic-Modelle.",
      "Multi-touch: more realistic than last-click. Linear, time-decay or algorithmic models."),
    Q("Was bedeutet organischer Traffic?", "What does organic traffic mean?",
      ["Bezahlter Traffic", "Besucher die ohne Werbung durch Suche, direkt oder Social kommen", "Affiliate-Traffic", "E-Mail-Klicks"],
      ["Paid traffic", "Visitors who come without advertising through search, direct or social", "Affiliate traffic", "Email clicks"],
      1, "Organic: kein direkter Werbekosten. Entsteht durch SEO, Content, Markenbekanntheit. Hoher CLV.",
      "Organic: no direct ad cost. Created by SEO, content, brand awareness. High CLV."),
    Q("Was ist Frequency Capping?", "What is frequency capping?",
      ["Einkaufsfrequenz", "Begrenzung wie oft dieselbe Person eine Werbeanzeige sieht", "E-Mail-Haeufigkeit", "Click-Limit"],
      ["Purchase frequency", "Limit on how often the same person sees an ad", "Email frequency", "Click limit"],
      1, "Frequency Capping verhindert Ad Fatigue: Nutzer sehen eine Anzeige zu oft und ignorieren sie.",
      "Frequency capping prevents ad fatigue: users see an ad too often and start ignoring it."),
    Q("Welcher Chart zeigt Budget-Effizienz am besten?", "Which chart best shows budget efficiency?",
      ["Kreisdiagramm", "Scatter/Bubble: Spend (X) vs. Revenue (Y), Groesse = Conversions", "Linie", "Tabelle"],
      ["Pie chart", "Scatter/Bubble: Spend (X) vs. Revenue (Y), Size = Conversions", "Line", "Table"],
      1, "Scatter/Bubble: zeigt Effizienz-Cluster sofort. Kanaele oben links = guenstig und effektiv.",
      "Scatter/bubble: shows efficiency clusters immediately. Channels top-left = cheap and effective."),
]

m08 = (
    lz([
        ("Marketing-ROI, CPA und ROAS als Kennzahlen verstehen", "Understand Marketing ROI, CPA and ROAS as metrics"),
        ("Kanalperformance in Tableau vergleichen (Balken, Bubble Chart)", "Compare channel performance in Tableau (bar, bubble chart)"),
        ("Budget-Effizienz pro Kanal bewerten und Empfehlungen ableiten", "Evaluate budget efficiency per channel and derive recommendations"),
        ("Das Konzept der Attribution verstehen", "Understand the concept of attribution"),
    ])
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kontext" data-en="Context"></div>'
    + '<h2 class="block__title" data-de="Welcher Kanal bringt das meiste fuer sein Geld?" data-en="Which channel delivers most for its money?"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="UrbanCart investiert in 6 Kanaele: SEA, Social Media, E-Mail, Organic, Direct und Affiliate. Nicht jeder Euro ist gleich viel wert. Die Marketing-ROI-Analyse zeigt, wo das Budget am effizientesten eingesetzt wird &#8211; und wo nicht." data-en="UrbanCart invests in 6 channels: SEA, Social Media, Email, Organic, Direct and Affiliate. Not every Euro is worth the same. Marketing ROI analysis shows where the budget is used most efficiently &#8211; and where it is not."></p>'
    + concept(
        "ROI vs. ROAS",
        "ROI = (Umsatz - Kosten) / Kosten x 100. ROAS = Umsatz / Werbeausgaben. ROAS von 4 = 4 Euro Umsatz pro 1 Euro Spend. CPA = Kosten / Conversions.",
        "ROI = (Revenue - Cost) / Cost x 100. ROAS = Revenue / Ad Spend. ROAS of 4 = 4 Euro revenue per 1 Euro spend. CPA = Cost / Conversions.",
        "Attribution",
        "Welcher Kanal hat den Kauf ausgeloest? Last-Click: letzter Klick bekommt 100%. Multi-Touch: alle Kontaktpunkte erhalten anteiligen Credit.",
        "Which channel triggered the purchase? Last-click: last click gets 100%. Multi-touch: all touchpoints receive proportional credit."
    )
    + infobox("Die 6 UrbanCart-Kanaele", "The 6 UrbanCart Channels", [
        ("SEA", "Search Engine Advertising (Google Ads). Hoch-Intent, aber teuer (CPC)"),
        ("Social Media", "Instagram, Facebook Ads. Gut fuer Awareness, variable Conversion"),
        ("E-Mail", "Newsletter an Bestandskunden. Guenstig, hohe Conversion"),
        ("Organic", "SEO, Content, direkte Suche. Kein direkter Cost, aber Aufwand"),
        ("Direct", "Direkte URL-Eingabe, Bookmarks. Starke Markenbekanntheit"),
        ("Affiliate", "Partnerprogramme. Performance-basiert, nur bei Conversion bezahlt"),
    ])
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Vorbereitung" data-en="Preparation"></div>'
    + '<h2 class="block__title" data-de="marketing.csv laden" data-en="Load marketing.csv"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="steps">'
    + step(1, "marketing.csv verbinden", "Connect marketing.csv",
           "Tableau > Verbinden > Textdatei > marketing.csv. Felder: channel, campaign_id, spend, clicks, conversions, revenue, date.",
           "Tableau > Connect > Text File > marketing.csv. Fields: channel, campaign_id, spend, clicks, conversions, revenue, date.",
           tip_de="spend = Marketingausgaben in Euro. conversions = Kaeufern. revenue = generierter Umsatz.",
           tip_en="spend = marketing spend in Euro. conversions = buyers. revenue = generated revenue.",
           opened=True)
    + step(2, "Berechnete Felder erstellen", "Create calculated fields",
           "3 berechnete Felder: ROI = (SUM([revenue])-SUM([spend]))/SUM([spend])*100. CPA = SUM([spend])/SUM([conversions]). ROAS = SUM([revenue])/SUM([spend]).",
           "3 calculated fields: ROI = (SUM([revenue])-SUM([spend]))/SUM([spend])*100. CPA = SUM([spend])/SUM([conversions]). ROAS = SUM([revenue])/SUM([spend]).",
           tip_de="Diese 3 Felder sind der Kern des Marketing-Dashboards. Erstelle sie als berechnete Felder bevor du Arbeitsblatter baust.",
           tip_en="These 3 fields are the core of the marketing dashboard. Create them as calculated fields before building worksheets.")
    + '</div>'
    + tbox("marketing.csv hat 144 Zeilen (6 Kanaele x 24 Monate). Ueberschaubar, aber aussagekraeftig.",
           "marketing.csv has 144 rows (6 channels x 24 months). Manageable but meaningful.")
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Analyse" data-en="Analysis"></div>'
    + '<h2 class="block__title" data-de="Marketing-Dashboard aufbauen" data-en="Build the Marketing Dashboard"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="4 Visualisierungen: Kanalvergleich, Bubble Chart, ROI-Zeitreihe, Budget-Allokation." data-en="4 visualisations: channel comparison, bubble chart, ROI time series, budget allocation."></p>'
    + '<div class="steps">'
    + step(1, "Kanalvergleich: ROI pro Kanal (Balken)", "Channel comparison: ROI per channel (bar)",
           "Neues Arbeitsblatt. channel auf Zeilen, [ROI] auf Spalten. Absteigend sortieren. Farbe: Gruen bei ROI > 200%, Orange bei 100-200%, Rot bei < 100%.",
           "New worksheet. channel to Rows, [ROI] to Columns. Sort descending. Colour: Green for ROI > 200%, Orange for 100-200%, Red for < 100%.",
           tip_de="Welcher Kanal hat den hoechsten ROI? Welcher kostet mehr als er bringt?",
           tip_en="Which channel has the highest ROI? Which costs more than it brings?",
           opened=True)
    + step(2, "Bubble Chart: Spend vs. Revenue", "Bubble Chart: Spend vs. Revenue",
           "Neues Arbeitsblatt. SUM([spend]) auf Spalten (X), SUM([revenue]) auf Zeilen (Y). SUM([conversions]) auf Groesse. channel auf Farbe und Beschriftung. Chart-Typ: Kreis.",
           "New worksheet. SUM([spend]) to Columns (X), SUM([revenue]) to Rows (Y). SUM([conversions]) to Size. channel to Colour and Label. Chart type: Circle.",
           tip_de="Oben links = guenstig und umsatzstark = ideal. Unten rechts = teuer und schwacher Umsatz = pruefen.",
           tip_en="Top-left = cheap and high revenue = ideal. Bottom-right = expensive and weak revenue = review.")
    + step(3, "ROI-Zeitreihe pro Kanal", "ROI time series per channel",
           "Neues Arbeitsblatt. date auf Spalten (Monat/Jahr), [ROI] auf Zeilen, channel auf Farbe. Liniendiagramm. Welcher Kanal verbessert sich ueber Zeit?",
           "New worksheet. date to Columns (Month/Year), [ROI] to Rows, channel to Colour. Line chart. Which channel improves over time?")
    + step(4, "Budget-Allokation (Treemap)", "Budget allocation (Treemap)",
           "Neues Arbeitsblatt. channel auf Detail und Farbe, SUM([spend]) auf Groesse. Chart-Typ: Treemap. Zeigt Budgetverteilung als Flaeche.",
           "New worksheet. channel to Detail and Colour, SUM([spend]) to Size. Chart type: Treemap. Shows budget distribution as area.")
    + '</div></section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kennzahlen" data-en="Key Metrics"></div>'
    + '<h2 class="block__title" data-de="Marketing-KPIs" data-en="Marketing KPIs"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="kpi-row">'
    + kpi('<line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
          'ROAS Ø 3,8', 'ROAS avg. 3.8', 'Gesamt-ROAS', '3,80 Euro pro 1 Euro Spend')
    + kpi('<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
          'E-Mail #1', 'Email #1', 'Bester Kanal ROI', 'Niedrigster CPA, hoechster ROI')
    + kpi('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/>',
          'SEA hoechster Spend', 'SEA highest spend', 'Groesster Budgetblock', 'Pruefe ROAS vs. E-Mail')
    + '</div></section>'
    + quiz_sec("lab09.html", "Weiter zu Lab 09: Executive Dashboard", "Continue to Lab 09: Executive Dashboard")
    + ai_bl(["Python", "pandas", "Plotly", "plotly.express"],
            "# Prompt fuer ChatGPT / Claude:\n"
            '"Erstelle ein Marketing-ROI-Dashboard in Python.\n'
            "Lade marketing.csv (pandas).\n"
            "Berechne pro channel:\n"
            "- ROI = (revenue - spend) / spend * 100\n"
            "- CPA = spend / conversions\n"
            "- ROAS = revenue / spend\n"
            "Erstelle mit Plotly:\n"
            "1. Balken: ROI pro Kanal (absteigend, Farbe nach ROI-Stufe)\n"
            "2. Bubble Chart: Spend (X) vs. Revenue (Y), Groesse=Conversions, Farbe=channel\n"
            "3. Treemap: Budget-Allokation nach channel (Groesse=spend)\n"
            'Farben: Orange #E87722, Blau #005B9A."')
    + nav("lab07.html", "&#8592; Lab 07: Sentiment-Analyse", "&#8592; Lab 07: Sentiment Analysis",
          "lab09.html", "Lab 09: Executive Dashboard &#8594;", "Lab 09: Executive Dashboard &#8594;")
)

with open('lab08.html', 'w', encoding='utf-8') as f:
    f.write(page(
        "Lab 08 &#8211; Marketing-ROI &amp; Kanalanalyse",
        nb("Lab 08 von 09", "Lab 08 of 09")
        + bc("Lab 08 &#8211; Marketing-ROI &amp; Kanalanalyse", "Lab 08 &#8211; Marketing ROI &amp; Channel Analysis")
        + hero("Lab 08 von 09 &#183; Fortgeschritten", "Lab 08 of 09 &#183; Advanced",
               "Marketing-ROI &amp;", "Marketing ROI &amp;", "Kanalanalyse", "Channel Analysis",
               "Welcher Kanal bringt das meiste fuer sein Geld? Du vergleichst ROI, CPA und ROAS aller 6 UrbanCart-Kanaele und optimierst die Budget-Allokation.",
               "Which channel delivers most for its money? You compare ROI, CPA and ROAS for all 6 UrbanCart channels and optimise budget allocation.",
               "60&#8211;90 Min.", "marketing.csv", "08")
        + prog(3) + wrap(m08, "08"), q08))
print("lab08.html OK")


# ===========================================================
# LAB 09 – EXECUTIVE DASHBOARD & DATA STORYTELLING
# ===========================================================
q09 = [
    Q("Was ist ein Executive Dashboard?", "What is an executive dashboard?",
      ["Technisches System-Monitoring", "Komprimierte Entscheidungsgrundlage fuer Fuehrungskraefte (max. 1 Seite)", "Ein Bericht fuer IT", "Detaillierter Datenbericht"],
      ["Technical system monitoring", "Compressed decision basis for executives (max. 1 page)", "A report for IT", "Detailed data report"],
      1, "Executive Dashboard: maximal 5-7 KPIs, eine Seite, sofort verstaendlich. Keine Details.",
      "Executive dashboard: maximum 5-7 KPIs, one page, immediately understandable. No details."),
    Q("Was ist Data Storytelling?", "What is data storytelling?",
      ["Daten erfinden", "Daten in eine verstaendliche Erzzaehlung mit Kontext und Empfehlungen einbetten", "Ein Diagrammtyp", "Eine Datenbank"],
      ["Inventing data", "Embedding data in an understandable narrative with context and recommendations", "A chart type", "A database"],
      1, "Data Storytelling: Kontext + Daten + Visualisierung + Empfehlung. Ziel: Entscheidungen ausloesen.",
      "Data storytelling: context + data + visualisation + recommendation. Goal: trigger decisions."),
    Q("Was ist das SCR-Framework?", "What is the SCR framework?",
      ["Sales Conversion Rate", "Situation, Complication, Resolution: Struktur fuer Datenpraesentation", "Security Control Review", "Scatter Chart Report"],
      ["Sales conversion rate", "Situation, Complication, Resolution: structure for data presentations", "Security control review", "Scatter chart report"],
      1, "SCR: Situation (Kontext), Complication (Problem), Resolution (Empfehlung). McKinsey-Standard.",
      "SCR: Situation (context), Complication (problem), Resolution (recommendation). McKinsey standard."),
    Q("Wie viele KPIs sollte ein Executive Dashboard haben?", "How many KPIs should an executive dashboard have?",
      ["So viele wie moeglich", "Maximal 5-7 (7 plus/minus 2 Regel)", "Genau 10", "Mindestens 20"],
      ["As many as possible", "Maximum 5-7 (7 plus/minus 2 rule)", "Exactly 10", "At least 20"],
      1, "Millers Gesetz: 7 +/- 2 Informationseinheiten gleichzeitig verarbeitbar. Weniger = besser.",
      "Miller's Law: 7 +/- 2 units of information processable simultaneously. Less = better."),
    Q("Was ist ein KPI-Trend-Indikator?", "What is a KPI trend indicator?",
      ["Ein Balkendiagramm", "Symbol das Richtung zeigt: Pfeil hoch/runter, Farbe gruen/rot", "Eine Tabelle", "Ein Filter"],
      ["A bar chart", "Symbol showing direction: arrow up/down, colour green/red", "A table", "A filter"],
      1, "Trend-Indikator: sofortige visuelle Aussage. Gruen+Pfeil hoch = gut. Rot+Pfeil runter = Handlungsbedarf.",
      "Trend indicator: immediate visual statement. Green+arrow up = good. Red+arrow down = action needed."),
    Q("Was bedeutet 'Insight' in der Datenpraesentation?", "What does 'insight' mean in data presentation?",
      ["Eine Zahl", "Eine Erkenntnis mit Implikation: was bedeutet die Zahl und was sollte man tun?", "Ein Diagramm", "Ein Filter"],
      ["A number", "A finding with implication: what does the number mean and what should be done?", "A chart", "A filter"],
      1, "Insight = Befund + Bedeutung + Empfehlung. Nicht: Umsatz stieg 12%. Sondern: Warum, und was jetzt?",
      "Insight = finding + meaning + recommendation. Not: revenue grew 12%. But: why, and what now?"),
    Q("Welche Labs fliessen ins Executive Dashboard?", "Which labs feed into the executive dashboard?",
      ["Nur Lab 01", "Alle 8 Labs: Umsatz, Kunden, RFM, ABC, Saisonalitaet, Funnel, Sentiment, Marketing", "Nur Labs 1-3", "Nur Lab 09"],
      ["Only Lab 01", "All 8 labs: revenue, customers, RFM, ABC, seasonality, funnel, sentiment, marketing", "Only labs 1-3", "Only lab 09"],
      1, "Executive Dashboard = Synthese aller Analysen. Pro Themenbereich ein KPI + Trend.",
      "Executive dashboard = synthesis of all analyses. One KPI + trend per topic area."),
    Q("Was ist ein Dashboard-Filter in Tableau?", "What is a dashboard filter in Tableau?",
      ["Daten loeschen", "Interaktives Element: klicke auf ein Element > alle anderen Charts filtern sich mit", "Ein Berechnetes Feld", "Ein Export"],
      ["Delete data", "Interactive element: click one element > all other charts filter along", "A calculated field", "An export"],
      1, "Dashboard-Filter: klicke auf Region > alle KPIs zeigen nur diese Region. Interaktivitaet ohne Code.",
      "Dashboard filter: click on region > all KPIs show only that region. Interactivity without code."),
    Q("Was ist ein Sparkline?", "What is a sparkline?",
      ["Ein grosses Liniendiagramm", "Miniatur-Liniendiagramm ohne Achsen direkt neben einer KPI-Zahl", "Ein Balken", "Eine Tabelle"],
      ["A large line chart", "Miniature line chart without axes directly next to a KPI number", "A bar", "A table"],
      1, "Sparkline: zeigt Trend auf kleinstem Raum. Ideal fuer KPI-Karten im Executive Dashboard.",
      "Sparkline: shows trend in the smallest space. Ideal for KPI cards in executive dashboard."),
    Q("Was ist Conditional Formatting in Tableau?", "What is conditional formatting in Tableau?",
      ["Farben zufaellig waehlen", "Farbe oder Form abhaengig vom Wert: rot wenn unter Ziel, gruen wenn ueber Ziel", "Ein Filter", "Export-Option"],
      ["Choose colours randomly", "Colour or shape depending on value: red if below target, green if above", "A filter", "Export option"],
      1, "Conditional Formatting: IF [KPI] < [Ziel] THEN 'Rot' ELSE 'Gruen'. Sofortige visuelle Aussage.",
      "Conditional formatting: IF [KPI] < [Target] THEN 'Red' ELSE 'Green'. Immediate visual statement."),
    Q("Was ist der Unterschied Dashboard vs. Report?", "What is the difference between a dashboard and a report?",
      ["Kein Unterschied", "Dashboard: interaktiv, Echtzeit, Monitoring. Report: statisch, Zeitpunkt, Detail", "Report ist besser", "Dashboard ist groesser"],
      ["No difference", "Dashboard: interactive, real-time, monitoring. Report: static, point in time, detail", "Report is better", "Dashboard is larger"],
      1, "Dashboard: laufendes Monitoring, Trends, Alerts. Report: detaillierte Analyse zu einem Zeitpunkt.",
      "Dashboard: ongoing monitoring, trends, alerts. Report: detailed analysis at a point in time."),
    Q("Welche Farbe zeigt Handlungsbedarf im Dashboard?", "Which colour signals action needed in a dashboard?",
      ["Blau", "Gruen", "Rot", "Gelb"],
      ["Blue", "Green", "Red", "Yellow"],
      2, "Ampelsystem: Rot = Handlungsbedarf, Orange/Gelb = Beobachten, Gruen = OK. Universal verstaendlich.",
      "Traffic light: Red = action needed, Orange/Yellow = monitor, Green = OK. Universally understood."),
    Q("Was ist ein KPI-Ziel (Target)?", "What is a KPI target?",
      ["Irgendeine Zahl", "Vorab definierter Sollwert gegen den der Istwert verglichen wird", "Der Maximalwert", "Der Durchschnitt"],
      ["Any number", "Pre-defined target value against which the actual value is compared", "The maximum value", "The average"],
      1, "Ohne Target kein Sinn: 500.000 Euro Umsatz gut oder schlecht? Nur mit Ziel vergleichbar.",
      "Without target no sense: 500,000 Euro revenue good or bad? Only comparable with a target."),
    Q("Was ist Daten-Hierarchie in Tableau?", "What is data hierarchy in Tableau?",
      ["Tabellen-Struktur", "Drill-Down: Jahr > Quartal > Monat > Tag mit einem Klick", "Sortierung", "Filter"],
      ["Table structure", "Drill-down: Year > Quarter > Month > Day with one click", "Sorting", "Filter"],
      1, "Hierarchie: klicke auf '+' neben dem Datum > naechste Detailstufe. Vom Ueberblick ins Detail.",
      "Hierarchy: click '+' next to the date > next detail level. From overview to detail."),
    Q("Was ist der letzte Schritt vor dem Prasentieren eines Dashboards?", "What is the last step before presenting a dashboard?",
      ["Mehr Daten hinzufuegen", "Stakeholder-Test: Kann die Zielgruppe das Dashboard in 30 Sekunden lesen?", "Farben aendern", "Mehr Charts hinzufuegen"],
      ["Add more data", "Stakeholder test: can the audience read the dashboard in 30 seconds?", "Change colours", "Add more charts"],
      1, "30-Sekunden-Test: Wenn die Kernaussage nicht sofort klar ist, ist das Dashboard zu komplex.",
      "30-second test: if the core message is not immediately clear, the dashboard is too complex."),
]

m09 = (
    lz([
        ("Ein Executive Dashboard aus allen 8 Lab-Analysen aufbauen", "Build an executive dashboard from all 8 lab analyses"),
        ("Data Storytelling mit dem SCR-Framework anwenden", "Apply data storytelling with the SCR framework"),
        ("Dashboard-Filter und Interaktivitaet in Tableau einrichten", "Set up dashboard filters and interactivity in Tableau"),
        ("KPIs mit Zielwerten und Conditional Formatting versehen", "Add target values and conditional formatting to KPIs"),
    ])
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kontext" data-en="Context"></div>'
    + '<h2 class="block__title" data-de="Das finale Lab: Alles zusammenfuehren" data-en="The final lab: bringing it all together"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="In den Labs 01&#8211;08 hast du UrbanCart aus 8 Perspektiven analysiert: Umsatz, Kunden, RFM, Pareto, Saisonalitaet, Funnel, Sentiment, Marketing. Jetzt baust du daraus ein Executive Dashboard fuer die Geschaeftsfuehrung &#8211; verdichtet auf das Wesentliche, mit klaren Empfehlungen." data-en="In labs 01&#8211;08 you analysed UrbanCart from 8 perspectives: revenue, customers, RFM, Pareto, seasonality, funnel, sentiment, marketing. Now you build an executive dashboard for management &#8211; condensed to the essentials, with clear recommendations."></p>'
    + concept(
        "Executive Dashboard",
        "Maximal 1 Seite. 5-7 KPIs. Sofort verstaendlich. Keine Rohdaten. Kein technisches Jargon. Zielgruppe: Fuehrungskraefte ohne Daten-Hintergrund die in 30 Sekunden entscheiden muessen.",
        "Maximum 1 page. 5-7 KPIs. Immediately understandable. No raw data. No technical jargon. Target audience: executives without a data background who need to decide in 30 seconds.",
        "Data Storytelling (SCR)",
        "Situation: Was ist der Kontext? Complication: Was ist das Problem/die Chance? Resolution: Was ist die Empfehlung? Diese Struktur gilt fuer jede Praesentation vor Fuehrungskraeften.",
        "Situation: what is the context? Complication: what is the problem/opportunity? Resolution: what is the recommendation? This structure applies to every presentation before executives."
    )
    + infobox("Die 8 Kernerkenntnisse aus den Labs", "The 8 Key Insights from the Labs", [
        ("Lab 01 (Umsatz)", "Gesamtumsatz, Bestellanzahl, AOV, November-Peak (Black Friday)"),
        ("Lab 02 (Kunden)", "CLV, Mobile-Anteil 62%, Top-Region identifiziert"),
        ("Lab 03 (RFM)", "~15% Champions, ~20% At-Risk: Reaktivierung priorisieren"),
        ("Lab 04 (Pareto)", "~30% der Produkte = 80% Umsatz: C-Produkte auslagern"),
        ("Lab 05 (Zeitreihe)", "Q4 staerkstes Quartal, +12% YoY-Wachstum, Forecast positiv"),
        ("Lab 06 (Funnel)", "~2% Conversion, 70% Cart Abandonment = groesste Hebel"),
        ("Lab 07 (Sentiment)", "68% positiv, 15% negativ: konkrete Produktprobleme identifiziert"),
        ("Lab 08 (Marketing)", "E-Mail hoechster ROI, SEA hoechster Spend: Budget umschichten?"),
    ])
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Vorbereitung" data-en="Preparation"></div>'
    + '<h2 class="block__title" data-de="Alle Datensaetze laden" data-en="Load all datasets"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="steps">'
    + step(1, "Alle Datenquellen verbinden", "Connect all data sources",
           "Neues Tableau-Workbook. Verbinde nacheinander: orders.csv, customers.csv, order_items.csv, marketing.csv, reviews.csv, sessions.csv. Jede als eigene Datenquelle.",
           "New Tableau workbook. Connect sequentially: orders.csv, customers.csv, order_items.csv, marketing.csv, reviews.csv, sessions.csv. Each as its own data source.",
           tip_de="In Tableau Public koennen mehrere Datenquellen in einem Workbook existieren. Unten links: Datenquellen-Leiste.",
           tip_en="In Tableau Public, multiple data sources can exist in one workbook. Bottom-left: data sources bar.",
           opened=True)
    + step(2, "KPIs aus Labs 01-08 sammeln", "Collect KPIs from labs 01-08",
           "Liste die 7 wichtigsten KPIs: Gesamtumsatz (Lab01), Unique Customers (Lab02), At-Risk % (Lab03), Top-A-Produkte (Lab04), YoY-Wachstum (Lab05), Conversion Rate (Lab06), Sentiment-Score (Lab07), ROAS (Lab08).",
           "List the 7 most important KPIs: Total Revenue (Lab01), Unique Customers (Lab02), At-Risk % (Lab03), Top-A products (Lab04), YoY growth (Lab05), Conversion Rate (Lab06), Sentiment score (Lab07), ROAS (Lab08).")
    + '</div>'
    + tbox("Tipp: Erstelle fuer jeden KPI ein separates Arbeitsblatt mit nur einer Zahl (Text-Chart). Dann auf dem Dashboard zusammenfuehren.",
           "Tip: Create a separate worksheet for each KPI with just one number (Text chart). Then combine on the dashboard.")
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Analyse" data-en="Analysis"></div>'
    + '<h2 class="block__title" data-de="Executive Dashboard Schritt fuer Schritt" data-en="Executive Dashboard Step by Step"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="4 Schritte zum finalen Executive Dashboard mit Storytelling-Struktur." data-en="4 steps to the final executive dashboard with storytelling structure."></p>'
    + '<div class="steps">'
    + step(1, "7 KPI-Karten erstellen", "Create 7 KPI cards",
           "Je Kennzahl: Neues Arbeitsblatt, Berechnetes Feld oder Measure direkt, auf Text ziehen, Zahlenformat anpassen. Titel = KPI-Name. Kein weiterer Schnickschnack.",
           "Per metric: new worksheet, calculated field or measure directly, drag to text, adjust number format. Title = KPI name. No further embellishments.",
           tip_de="Conditional Formatting: Calculated Field 'KPI-Status': IF [Wert] >= [Ziel] THEN 'gruen' ELSE 'rot'. Auf Hintergrundfarbe ziehen.",
           tip_en="Conditional formatting: Calculated field 'KPI status': IF [value] >= [target] THEN 'green' ELSE 'red'. Drag to background colour.",
           opened=True)
    + step(2, "Trend-Miniatur pro KPI (Sparkline)", "Trend miniature per KPI (sparkline)",
           "Pro KPI ein Liniendiagramm ohne Achsen, ohne Titel: Masse klein (60px hoch). Zeigt nur die Richtung. Direkt neben der KPI-Zahl auf dem Dashboard platzieren.",
           "Per KPI one line chart without axes, without title: size small (60px high). Shows direction only. Place directly next to the KPI number on the dashboard.")
    + step(3, "Dashboard layouten und filtern", "Layout and filter the dashboard",
           "Neues Dashboard. KPI-Karten oben (7er-Reihe). Hauptchart Mitte: monatlicher Umsatz mit Forecast. Unten: Funnel (links) und Marketing-Bubble (rechts). Filter: Zeitraum und Kanal.",
           "New dashboard. KPI cards at top (row of 7). Main chart centre: monthly revenue with forecast. Bottom: funnel (left) and marketing bubble (right). Filter: time period and channel.",
           tip_de="Dashboard-Filter: Klick auf Kanal in der Bubble Chart filtert automatisch den Umsatzchart.",
           tip_en="Dashboard filter: clicking on a channel in the bubble chart automatically filters the revenue chart.")
    + step(4, "Storytelling-Titel und Annotations", "Storytelling title and annotations",
           "Haupttitel: UrbanCart Executive Review Q4 2024. Subtitel: 3 Hauptbefunde + Empfehlung. Annotationen direkt an kritischen Punkten (November-Peak, Cart-Abandonment-Luecke).",
           "Main title: UrbanCart Executive Review Q4 2024. Subtitle: 3 main findings + recommendation. Annotations directly at critical points (November peak, cart abandonment gap).")
    + '</div></section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kennzahlen" data-en="Key Metrics"></div>'
    + '<h2 class="block__title" data-de="Executive Summary: UrbanCart 2023-2024" data-en="Executive Summary: UrbanCart 2023-2024"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="kpi-row">'
    + kpi('<line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
          '+12% YoY', '+12% YoY', 'Umsatzwachstum', '2024 vs. 2023, Q4 staerkste')
    + kpi('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/>',
          '8.000 Kunden', '8,000 customers', 'Kundenbasis', '~15% Champions, ~20% At-Risk')
    + kpi('<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
          '2% Conv.', '2% Conv.', 'Conversion Rate', '70% Cart Abandon = Hebel #1')
    + '</div></section>'
    + quiz_sec("index.html", "Zurueck zur Kursuebersicht", "Back to Course Overview")
    + ai_bl(["Python", "pandas", "Plotly", "Dash", "dash-bootstrap-components"],
            "# Prompt fuer ChatGPT / Claude:\n"
            '"Erstelle ein vollstaendiges Executive Dashboard in Plotly Dash.\n'
            "Lade alle 6 CSV-Dateien von UrbanCart.\n"
            "Zeige auf einer Seite:\n"
            "- 7 KPI-Cards mit Trend-Indikator (Pfeil hoch/runter, Farbe gruen/rot)\n"
            "- Hauptchart: monatl. Umsatz 2023+2024 mit Forecast (Prophet)\n"
            "- Funnel Chart: Conversion-Stufen\n"
            "- Bubble Chart: Marketing-Spend vs. Revenue\n"
            "Dropdown-Filter: Zeitraum und Kanal.\n"
            "Farbschema: Orange #E87722, Blau #005B9A, responsive Layout.\n"
            'pip install dash dash-bootstrap-components plotly pandas prophet"')
    + nav("lab08.html", "&#8592; Lab 08: Marketing-ROI", "&#8592; Lab 08: Marketing ROI",
          "index.html", "Zur Kursuebersicht &#8594;", "Course Overview &#8594;")
)

with open('lab09.html', 'w', encoding='utf-8') as f:
    f.write(page(
        "Lab 09 &#8211; Executive Dashboard &amp; Data Storytelling",
        nb("Lab 09 von 09", "Lab 09 of 09")
        + bc("Lab 09 &#8211; Executive Dashboard", "Lab 09 &#8211; Executive Dashboard")
        + hero("Lab 09 von 09 &#183; Fortgeschritten", "Lab 09 of 09 &#183; Advanced",
               "Executive Dashboard &amp;", "Executive Dashboard &amp;", "Data Storytelling", "Data Storytelling",
               "Das Finale: Du kombinierst alle 8 Analysen zu einem Executive Dashboard fuer die UrbanCart-Geschaeftsfuehrung &#8211; verdichtet, entscheidungsreif, professionell.",
               "The finale: you combine all 8 analyses into an executive dashboard for UrbanCart management &#8211; condensed, decision-ready, professional.",
               "90&#8211;120 Min.", "Alle Datensaetze", "09")
        + prog(3) + wrap(m09, "09"), q09))
print("lab09.html OK")

print("\nAlle Labs fertig. Validiere JS...")
import subprocess
for lab in ["lab07.html", "lab08.html", "lab09.html"]:
    r = subprocess.run(
        ["node", "--eval",
         f'const fs=require("fs");const c=fs.readFileSync("{lab}","utf8");'
         'const s=(c.match(/<script>([\\s\\S]*?)<\\/script>/)||["",""])[1];'
         'try{new Function(s);process.stdout.write("JS OK\\n");}catch(e){process.stdout.write("ERR: "+e.message+"\\n");}'],
        capture_output=True, text=True, cwd="/home/node/openclaw/e-comm"
    )
    print(f"{lab}: {r.stdout.strip()}")
