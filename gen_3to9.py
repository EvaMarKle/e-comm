#!/usr/bin/env python3
"""UrbanCart Labs 03-09 – vollstaendiger Inhalt"""
import json, textwrap

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
        '<p class="ai-block__intro" data-de="Tableau ist ideal f&#252;r explorative Analyse ohne Code. Python erm&#246;glicht dieselbe Analyse automatisiert und skalierbar. Nutze diesen Prompt direkt in ChatGPT oder Claude:" data-en="Tableau is perfect for exploratory analysis without code. Python allows the same analysis automated and scalable. Use this prompt directly in ChatGPT or Claude:"></p>'
        '<div class="ai-block__stack">' + t_html + '</div>'
        '<div class="ai-block__prompt-label" data-de="Prompt f&#252;r ChatGPT / Claude" data-en="Prompt for ChatGPT / Claude"></div>'
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


# ═══════════════════════════════════════════════════════════
# LAB 03 – RFM-ANALYSE
# ═══════════════════════════════════════════════════════════
q03 = [
    Q("Was bedeutet R in RFM?", "What does R mean in RFM?",
      ["Revenue", "Recency &#8211; Tage seit letztem Kauf", "Rate", "Return"],
      ["Revenue", "Recency &#8211; days since last purchase", "Rate", "Return"],
      1, "Recency = Tage seit dem letzten Kauf. Je kleiner, desto aktiver der Kunde.",
      "Recency = days since last purchase. The smaller, the more active the customer."),
    Q("Was bedeutet F in RFM?", "What does F mean in RFM?",
      ["Finance", "Frequency &#8211; Kaufhaeufigkeit", "Filter", "Forecast"],
      ["Finance", "Frequency &#8211; purchase frequency", "Filter", "Forecast"],
      1, "Frequency = wie oft hat ein Kunde bestellt. Hohe Frequency = loyaler Kunde.",
      "Frequency = how often has a customer ordered. High frequency = loyal customer."),
    Q("Was bedeutet M in RFM?", "What does M mean in RFM?",
      ["Mobile", "Monat", "Monetary &#8211; Gesamtumsatz", "Marketing"],
      ["Mobile", "Month", "Monetary &#8211; total revenue", "Marketing"],
      2, "Monetary = Gesamtumsatz des Kunden. Hoher Wert = wertvoller Kunde.",
      "Monetary = total customer revenue. High value = valuable customer."),
    Q("Wie berechnet man Recency in Tableau?", "How to calculate Recency in Tableau?",
      ["COUNT([order_date])", "DATEDIFF('day', MAX([order_date]), DATE('2025-01-01'))", "SUM([order_date])", "MIN([order_date])"],
      ["COUNT([order_date])", "DATEDIFF('day', MAX([order_date]), DATE('2025-01-01'))", "SUM([order_date])", "MIN([order_date])"],
      1, "DATEDIFF berechnet die Differenz in Tagen zwischen dem letzten Kauf und dem Referenzdatum.",
      "DATEDIFF calculates the day difference between the last purchase and the reference date."),
    Q("Was ist ein Champion-Kunde?", "What is a champion customer?",
      ["Kauft nur einmal", "Hohe Recency, Frequency und Monetary &#8211; das beste Segment", "Unbekannt", "Viele Retouren"],
      ["Buys only once", "High Recency, Frequency and Monetary &#8211; best segment", "Unknown", "Many returns"],
      1, "Champions: kuerzlich aktiv, kauft oft, gibt viel aus. Das wertvollste Segment.",
      "Champions: recently active, buys often, spends a lot. The most valuable segment."),
    Q("Was ist ein At-Risk-Kunde?", "What is an at-risk customer?",
      ["Neuer Kunde", "Frueher wertvoll, jetzt lange nicht mehr aktiv", "Kauft nur guenstig", "Nie bestellt"],
      ["New customer", "Formerly valuable, now long inactive", "Only buys cheap", "Never ordered"],
      1, "At-Risk: war Champion oder Loyal, hat aber zuletzt nicht mehr bestellt. Reaktivierung pruefen.",
      "At-Risk: was champion or loyal, but has not ordered recently. Consider reactivation."),
    Q("Welche Tableau-Funktion zaehlt eindeutige Bestellungen?", "Which Tableau function counts unique orders?",
      ["SUM([order_id])", "COUNT([order_id])", "COUNTD([order_id])", "AVG([order_id])"],
      ["SUM([order_id])", "COUNT([order_id])", "COUNTD([order_id])", "AVG([order_id])"],
      2, "COUNTD = Count Distinct. Zaehlt jeden Wert nur einmal. Verhindert Doppelzaehlung.",
      "COUNTD = Count Distinct. Counts each value only once. Prevents double-counting."),
    Q("Was ist Churn?", "What is churn?",
      ["Ein Diagrammtyp", "Kundenabwanderung", "Ein Produktfehler", "Eine Marketingmassnahme"],
      ["A chart type", "Customer attrition", "A product defect", "A marketing measure"],
      1, "Churn = Kundenabwanderung. Churn Rate = Anteil der Kunden, die aufhoeren zu kaufen.",
      "Churn = customer attrition. Churn rate = share of customers who stop buying."),
    Q("Wie werden RFM-Scores erstellt?", "How are RFM scores created?",
      ["Manuell", "Quintile: Kunden in 5 gleiche Gruppen (1-5) einteilen", "Per ML", "Alphabetisch"],
      ["Manually", "Quintiles: divide customers into 5 equal groups (1-5)", "By ML", "Alphabetically"],
      1, "Quintile: jede Dimension in 5 Gruppen. Score 5 = beste Gruppe.",
      "Quintiles: each dimension in 5 groups. Score 5 = best group."),
    Q("Was zeigt ein Scatter Plot F (X) vs. M (Y)?", "What does a scatter plot F (X) vs. M (Y) show?",
      ["Geografische Daten", "Engagement vs. Wert pro Kunde", "Zeitverlauf", "Produktkategorien"],
      ["Geographic data", "Engagement vs. value per customer", "Time trend", "Product categories"],
      1, "F vs. M: wer kauft oft (F) und wer gibt viel aus (M). Beste Kunden rechts oben.",
      "F vs. M: who buys often (F) and who spends a lot (M). Best customers top-right."),
    Q("Was ist Hibernating?", "What is Hibernating?",
      ["Schlaeft woertlich", "Lang inaktiv, niedrige Scores in R, F, M", "Kauft nur nachts", "Saisonaler Kaeufer"],
      ["Sleeping literally", "Long inactive, low scores in R, F, M", "Only buys at night", "Seasonal buyer"],
      1, "Hibernating: lang inaktiv, niedrige Werte. Win-Back oder abschreiben.",
      "Hibernating: long inactive, low values. Win-back or write off."),
    Q("Welche Strategie gilt fuer Hibernating-Kunden?", "Which strategy for hibernating customers?",
      ["Intensiv bewerben", "Win-Back-Kampagne mit starkem Anreiz oder abschreiben", "Ignorieren", "Newsletter abmelden"],
      ["Advertise intensively", "Win-back campaign with strong incentive or write off", "Ignore", "Newsletter unsubscribe"],
      1, "Win-Back: starkes Angebot (30% Rabatt). Kein Return -> Segment bereinigen.",
      "Win-back: strong offer (30% discount). No return -> clean up segment."),
    Q("Warum ist RFM besser als reines Umsatz-Ranking?", "Why is RFM better than pure revenue ranking?",
      ["Einfacher", "Beruecksichtigt auch Aktivitaet und Loyalitaet", "Genauer", "Kein Unterschied"],
      ["Simpler", "Also considers activity and loyalty", "More precise", "No difference"],
      1, "Reiner Umsatz ignoriert Inaktivitaet. 1.000 EUR vor 3 Jahren < 500 EUR letzte Woche.",
      "Pure revenue ignores inactivity. 1,000 EUR three years ago < 500 EUR last week."),
    Q("Was ist Level of Detail (LOD) in Tableau?", "What is Level of Detail (LOD) in Tableau?",
      ["Bildschirmaufloesung", "Aggregationsebene der Berechnung im View", "Anzahl Datenpunkte", "Filtertiefe"],
      ["Screen resolution", "Aggregation level of calculation in the view", "Number of data points", "Filter depth"],
      1, "LOD bestimmt, auf welcher Ebene Tableau aggregiert. customer_id im View = Berechnung pro Kunde.",
      "LOD determines the aggregation level. customer_id in view = calculation per customer."),
    Q("Welches Feld verbindet Recency mit einem Kunden?", "Which field connects Recency to a customer?",
      ["order_id", "product_id", "customer_id", "order_date"],
      ["order_id", "product_id", "customer_id", "order_date"],
      2, "customer_id ist der Schluessel. Alle RFM-Metriken werden pro customer_id berechnet.",
      "customer_id is the key. All RFM metrics are calculated per customer_id."),
]

m03 = (
    lz([
        ("R, F und M als Kundensegmentierungs-Dimensionen verstehen", "Understand R, F and M as customer segmentation dimensions"),
        ("Berechnete Felder in Tableau (DATEDIFF, COUNTD, SUM) erstellen", "Create calculated fields in Tableau (DATEDIFF, COUNTD, SUM)"),
        ("Einen Scatter Plot zur Kundensegmentierung aufbauen", "Build a scatter plot for customer segmentation"),
        ("Segmente ableiten und Marketingmassnahmen je Segment definieren", "Derive segments and define marketing measures per segment"),
    ])
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kontext" data-en="Context"></div>'
    + '<h2 class="block__title" data-de="Warum RFM? Die 3 Dimensionen der Kundentreue" data-en="Why RFM? The 3 Dimensions of Customer Loyalty"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="Nicht alle Kunden sind gleich wertvoll. RFM ist das meistgenutzte Framework fuer Kundensegmentierung im E-Commerce &#8211; ohne Machine Learning, nur mit Bestelldaten. Du klassifizierst UrbanCarts 8.000 Kunden in Champions, Loyal, At-Risk und Hibernating." data-en="Not all customers are equally valuable. RFM is the most widely used customer segmentation framework in e-commerce &#8211; without machine learning, using only order data. You classify UrbanCart\'s 8,000 customers into Champions, Loyal, At-Risk and Hibernating."></p>'
    + concept(
        "Was ist RFM?",
        "<strong>R</strong>ecency: Wann war der letzte Kauf? (niedrig = gut) &middot; <strong>F</strong>requency: Wie oft bestellt? &middot; <strong>M</strong>onetary: Wie viel ausgegeben? Jede Dimension wird 1&#8211;5 gescort.",
        "<strong>R</strong>ecency: When was the last purchase? (low = good) &middot; <strong>F</strong>requency: How often? &middot; <strong>M</strong>onetary: How much spent? Each dimension scored 1&#8211;5.",
        "Die 5 Hauptsegmente",
        "Champions (5-5-5): kaufen jetzt, kaufen oft, geben viel aus. Loyal: treu aber nicht top. At Risk: frueher wertvoll, jetzt inaktiv. Hibernating: lang inaktiv. New: erst einmal bestellt.",
        "Champions (5-5-5): buying now, buy often, spend a lot. Loyal: faithful but not top. At Risk: formerly valuable, now inactive. Hibernating: long inactive. New: ordered only once."
    )
    + infobox("RFM-Segmente und Massnahmen", "RFM Segments and Actions", [
        ("Champions", "Loyalty-Programm, Early Access, Exklusiv behandeln"),
        ("Loyal Customers", "Up-Sell, Cross-Sell, Bewertungen anfragen"),
        ("At Risk", "Reaktivierungskampagne, persoenliche Ansprache"),
        ("Hibernating", "Win-Back mit 30% Rabatt oder abschreiben"),
        ("New Customers", "Onboarding-Serie, zweiten Kauf triggern"),
    ])
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Vorbereitung" data-en="Preparation"></div>'
    + '<h2 class="block__title" data-de="orders.csv laden" data-en="Load orders.csv"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="steps">'
    + step(1, "orders.csv verbinden", "Connect orders.csv",
           "Tableau &#8594; Verbinden &#8594; Textdatei &#8594; orders.csv. Felder pruefen: order_id, customer_id, order_date, total_revenue, status.",
           "Tableau &#8594; Connect &#8594; Text File &#8594; orders.csv. Check fields: order_id, customer_id, order_date, total_revenue, status.",
           opened=True)
    + step(2, "Level of Detail verstehen", "Understand Level of Detail",
           "customer_id auf Zeilen ziehen. Alle RFM-Felder werden dann pro Kunde berechnet. Ohne customer_id aggregiert Tableau ueber alle Kunden.",
           "Drag customer_id to Rows. All RFM fields are then calculated per customer. Without customer_id, Tableau aggregates across all customers.")
    + '</div>'
    + tbox("Referenzdatum fuer Recency: 1. Januar 2025. Dieses Datum in allen DATEDIFF-Formeln verwenden.",
           "Reference date for Recency: 1 January 2025. Use this date in all DATEDIFF formulas.")
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Analyse" data-en="Analysis"></div>'
    + '<h2 class="block__title" data-de="RFM-Felder berechnen und visualisieren" data-en="Calculate and visualise RFM fields"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="3 berechnete Felder &#8211; dann ein Scatter Plot mit Farbcodierung fuer sofortige Segmenterkennung." data-en="3 calculated fields &#8211; then a scatter plot with colour coding for instant segment recognition."></p>'
    + '<div class="steps">'
    + step(1, "Calculated Field: Recency", "Calculated Field: Recency",
           "Neues berechnetes Feld, Name: Recency. Formel: DATEDIFF('day', MAX([order_date]), DATE('2025-01-01')). Je kleiner der Wert, desto kuerzlicher war der Kauf.",
           "New calculated field, name: Recency. Formula: DATEDIFF('day', MAX([order_date]), DATE('2025-01-01')). The smaller the value, the more recent the purchase.",
           tip_de="DATEDIFF: Differenz zwischen zwei Daten. MAX([order_date]) = letzter Kauf des Kunden. DATE('2025-01-01') = Referenzdatum.",
           tip_en="DATEDIFF: difference between two dates. MAX([order_date]) = customer's last purchase. DATE('2025-01-01') = reference date.",
           opened=True)
    + step(2, "Calculated Field: Frequency", "Calculated Field: Frequency",
           "Neues berechnetes Feld, Name: Frequency. Formel: COUNTD([order_id]). Zaehlt eindeutige Bestellungen pro Kunde.",
           "New calculated field, name: Frequency. Formula: COUNTD([order_id]). Counts unique orders per customer.")
    + step(3, "Calculated Field: Monetary", "Calculated Field: Monetary",
           "Neues berechnetes Feld, Name: Monetary. Formel: SUM([total_revenue]). Gesamtumsatz pro Kunde.",
           "New calculated field, name: Monetary. Formula: SUM([total_revenue]). Total revenue per customer.")
    + step(4, "Scatter Plot: F vs. M, Farbe = Recency", "Scatter Plot: F vs. M, Colour = Recency",
           "Neues Arbeitsblatt. Frequency auf Spalten, Monetary auf Zeilen. Chart-Typ: Kreis. Recency auf Farbe (Rot-Gruen-Palette, umgekehrt: Rot = lange nicht aktiv).",
           "New worksheet. Frequency to Columns, Monetary to Rows. Chart type: Circle. Recency to Colour (Red-Green palette, reversed: Red = long inactive).",
           tip_de="Rechts oben = Champions (hohe F, hohe M). Rot = At Risk / Hibernating. Gruene Cluster links unten = New Customers.",
           tip_en="Top-right = Champions (high F, high M). Red = At Risk / Hibernating. Green clusters bottom-left = New Customers.")
    + step(5, "Dashboard und Erkenntnisse", "Dashboard and insights",
           "Neues Dashboard. Scatter Plot + KPI-Karten (Kundenanzahl pro Segment). Titel: UrbanCart Customer Segments (RFM). Was faellt auf?",
           "New dashboard. Scatter plot + KPI cards (customer count per segment). Title: UrbanCart Customer Segments (RFM). What stands out?")
    + '</div></section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kennzahlen" data-en="Key Metrics"></div>'
    + '<h2 class="block__title" data-de="RFM-Segment-Kennzahlen" data-en="RFM Segment Metrics"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="kpi-row">'
    + kpi('<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>',
          '~15&#8239;% Kunden', '~15&#8239;% customers', 'Champions', 'Hoher R, F, M Score')
    + kpi('<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>',
          '~20&#8239;% Kunden', '~20&#8239;% customers', 'At Risk', 'Frueher wertvoll, jetzt inaktiv')
    + kpi('<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
          'Ø 3&#8211;4', 'Avg. 3&#8211;4', 'Ø Bestellungen', 'Frequency Mittelwert')
    + '</div></section>'
    + quiz_sec("lab04.html", "Weiter zu Lab 04: ABC-Analyse", "Continue to Lab 04: ABC Analysis")
    + ai_bl(["Python", "pandas", "Plotly", "scikit-learn"],
            "# Prompt fuer ChatGPT / Claude:\n"
            '"Erstelle eine RFM-Analyse in Python.\n'
            "Lade orders.csv (pandas). Berechne pro customer_id:\n"
            "- R: Tage seit letztem Kauf (Referenz: 2025-01-01)\n"
            "- F: nunique(order_id)\n"
            "- M: sum(total_revenue)\n"
            "Normalisiere auf Scores 1-5 mit pd.qcut.\n"
            "Plotly Scatter: F (X), M (Y), Farbe = R.\n"
            'Beschrifte Cluster: Champions, At Risk, Hibernating."')
    + nav("lab02.html", "&#8592; Lab 02: Kundenstruktur", "&#8592; Lab 02: Demographics",
          "lab04.html", "Lab 04: ABC-Analyse &#8594;", "Lab 04: ABC Analysis &#8594;")
)

with open('lab03.html', 'w', encoding='utf-8') as f:
    f.write(page(
        "Lab 03 &#8211; RFM-Analyse",
        nb("Lab 03 von 09", "Lab 03 of 09")
        + bc("Lab 03 &#8211; RFM-Analyse", "Lab 03 &#8211; RFM Analysis")
        + hero("Lab 03 von 09 &#183; Mittel", "Lab 03 of 09 &#183; Intermediate",
               "RFM-Analyse:", "RFM Analysis:", "Kundensegmentierung", "Customer Segmentation",
               "Recency, Frequency, Monetary &#8211; das bewaehrteste Framework der Kundensegmentierung. Du berechnest RFM-Scores und identifizierst Champions, At-Risk und Hibernating-Kunden.",
               "Recency, Frequency, Monetary &#8211; the most proven customer segmentation framework. You calculate RFM scores and identify champions, at-risk and hibernating customers.",
               "60&#8211;90 Min.", "orders.csv", "03")
        + prog(2) + wrap(m03, "03"), q03))
print("lab03.html OK")


# ═══════════════════════════════════════════════════════════
# LAB 04 – ABC-ANALYSE & PARETO
# ═══════════════════════════════════════════════════════════
q04 = [
    Q("Was besagt das Pareto-Prinzip?", "What does the Pareto principle state?",
      ["Alle Produkte gleich wichtig", "80% Umsatz von 20% der Produkte", "50/50 Verteilung", "Mehr Produkte = mehr Umsatz"],
      ["All products equally important", "80% revenue from 20% of products", "50/50 distribution", "More products = more revenue"],
      1, "80/20-Regel: wenige Produkte = Grossteil des Umsatzes. Gilt auch im E-Commerce.",
      "80/20 rule: few products = majority of revenue. Applies to e-commerce too."),
    Q("Was sind A-Produkte?", "What are A-products?",
      ["Alle Produkte", "80% mit niedrigstem Umsatz", "Kumuliert 0-80% des Umsatzes", "Nur Premium"],
      ["All products", "80% with lowest revenue", "Cumulative 0-80% of revenue", "Only premium"],
      2, "A-Produkte: erste 80% des kumulierten Gesamtumsatzes. Kern des Geschaefts.",
      "A-products: first 80% of cumulative total revenue. Core business."),
    Q("Was sind C-Produkte?", "What are C-products?",
      ["Umsatzstaerkste Artikel", "Letzte 5% des kumulierten Umsatzes (95-100%)", "Hohe Marge", "Neue Produkte"],
      ["Highest revenue items", "Last 5% of cumulative revenue (95-100%)", "High margin", "New products"],
      1, "C-Produkte: sehr geringer Umsatzbeitrag. Auslistung pruefen, Listungskosten kalkulieren.",
      "C-products: very low revenue contribution. Review delisting, calculate listing costs."),
    Q("Was macht RUNNING_SUM in Tableau?", "What does RUNNING_SUM do in Tableau?",
      ["Summiert eine Zeile", "Berechnet die laufende (kumulierte) Summe", "Multipliziert", "Rundet auf"],
      ["Sums one row", "Calculates the running (cumulative) sum", "Multiplies", "Rounds up"],
      1, "RUNNING_SUM(SUM([x])) addiert von oben nach unten: jede Zeile enthaelt alle vorherigen plus aktuellen Wert.",
      "RUNNING_SUM(SUM([x])) adds from top to bottom: each row contains all previous plus current value."),
    Q("Wie erstellt man Dual-Axis in Tableau?", "How to create Dual-Axis in Tableau?",
      ["Zwei Arbeitsblatter", "Rechtsklick auf zweite Kennzahl > Dual Axis > Achsen synchronisieren", "Filter", "Export"],
      ["Two worksheets", "Right-click on second measure > Dual Axis > Synchronize axes", "Filter", "Export"],
      1, "Dual Axis: zwei Kennzahlen auf verschiedenen Achsen im selben Chart. Balken + Linie.",
      "Dual Axis: two measures on different axes in the same chart. Bar + line."),
    Q("Was ist TOTAL() in Tableau?", "What is TOTAL() in Tableau?",
      ["Zaehlt Zeilen", "Gesamtwert aller Zeilen im aktuellen View", "Filtert Daten", "Rundet auf"],
      ["Counts rows", "Total value of all rows in current view", "Filters data", "Rounds up"],
      1, "TOTAL(SUM([x])) = Gesamtsumme aller Werte im View. Fuer kumulierten Anteil in % benoetigt.",
      "TOTAL(SUM([x])) = grand total of all values in view. Needed for cumulative share in %."),
    Q("Was ist die ABC-Formel fuer Tableau?", "What is the ABC formula for Tableau?",
      ["IF x < 0.5 THEN 'A'", "IF [Kum] <= 0.8 THEN 'A' ELSEIF [Kum] <= 0.95 THEN 'B' ELSE 'C' END", "CASE WHEN", "IIF"],
      ["IF x < 0.5 THEN 'A'", "IF [Cum] <= 0.8 THEN 'A' ELSEIF [Cum] <= 0.95 THEN 'B' ELSE 'C' END", "CASE WHEN", "IIF"],
      1, "IF-Feld gibt ABC-Klasse zurueck. A=0-80%, B=80-95%, C=95-100% kumuliert.",
      "IF field returns ABC class. A=0-80%, B=80-95%, C=95-100% cumulative."),
    Q("Welches Feld verbindet order_items und products?", "Which field connects order_items and products?",
      ["order_id", "customer_id", "product_id", "order_date"],
      ["order_id", "customer_id", "product_id", "order_date"],
      2, "product_id ist der Schluessel zwischen order_items.csv und products.csv.",
      "product_id is the key between order_items.csv and products.csv."),
    Q("Wer war Vilfredo Pareto?", "Who was Vilfredo Pareto?",
      ["Tableau-Entwickler", "Ital. Oekonom, beobachtete 80/20 bei Landbesitz", "Marketingexperte", "Amazon-Gruender"],
      ["Tableau developer", "Italian economist who observed 80/20 in land ownership", "Marketing expert", "Amazon founder"],
      1, "Vilfredo Pareto (1848-1923) entdeckte: 20% der Bevoelkerung besitzen 80% des Bodens in Italien.",
      "Vilfredo Pareto (1848-1923) discovered: 20% of the population own 80% of the land in Italy."),
    Q("Warum absteigend sortieren im Pareto-Chart?", "Why sort descending in the Pareto chart?",
      ["Sieht besser aus", "Zeigt sofort wichtigste Produkte und den 80%-Knick", "Excel-Standard", "Pflicht"],
      ["Looks better", "Shows most important products and the 80% bend immediately", "Excel standard", "Required"],
      1, "Absteigende Sortierung macht das 80/20-Muster sichtbar. Der Knick zeigt die A/B-Grenze.",
      "Descending sort makes the 80/20 pattern visible. The bend shows the A/B boundary."),
    Q("Was zeigt die Linie im Pareto-Chart?", "What does the line in the Pareto chart show?",
      ["Preis", "Kumulierten Umsatzanteil in %", "Anzahl Bestellungen", "Bestand"],
      ["Price", "Cumulative revenue share in %", "Number of orders", "Stock"],
      1, "Die Linie zeigt den kumulierten Anteil am Gesamtumsatz. Bei 80% endet die A-Klasse.",
      "The line shows cumulative share of total revenue. At 80%, the A-class ends."),
    Q("Wann gilt das Pareto-Prinzip NICHT?", "When does the Pareto principle NOT apply?",
      ["Immer", "Long-Tail-Modelle (Amazon Marketplace, Spotify)", "Grosse Kataloge", "Niemals"],
      ["Always", "Long-tail models (Amazon Marketplace, Spotify)", "Large catalogues", "Never"],
      1, "Long Tail: viele Nischenprodukte mit kleinem Umsatz sind zusammen signifikant. 80/20 gilt weniger.",
      "Long tail: many niche products with small revenue are collectively significant. 80/20 applies less."),
    Q("Was ist der sinnvolle Schritt nach C-Produkt-Identifikation?", "What to do after identifying C-products?",
      ["Sofort loeschen", "Listungskosten gegen Umsatz und Marge abwaegen", "Preis verdoppeln", "Ignorieren"],
      ["Delete immediately", "Weigh listing costs against revenue and margin", "Double the price", "Ignore"],
      1, "Erst Deckungsbeitrag pruefen. Falls Marge hoch trotz niedrigem Umsatz, kann Behalten sinnvoll sein.",
      "First check contribution margin. If margin is high despite low revenue, keeping it may make sense."),
    Q("Welcher Chart-Typ zeigt Pareto am besten?", "Which chart type best shows Pareto?",
      ["Kreisdiagramm", "Heatmap", "Dual-Axis: Balken + Linie", "Scatter Plot"],
      ["Pie chart", "Heatmap", "Dual-Axis: Bar + Line", "Scatter plot"],
      2, "Pareto = Dual-Axis. Balken links (Umsatz), Linie rechts (kumulierter Anteil %).",
      "Pareto = Dual-Axis. Bar left (revenue), line right (cumulative share %)."),
    Q("Welche Farben fuer A/B/C?", "Which colours for A/B/C?",
      ["Beliebig", "A=Gruen, B=Orange, C=Rot (Ampelsystem)", "Alle blau", "Schwarz/weiss"],
      ["Arbitrary", "A=Green, B=Orange, C=Red (traffic light system)", "All blue", "Black/white"],
      1, "Ampelsystem: A=Gruen (gut), B=Orange (beobachten), C=Rot (kritisch pruefen).",
      "Traffic light: A=Green (good), B=Orange (monitor), C=Red (review critically)."),
]

m04 = (
    lz([
        ("Das Pareto-Prinzip und die ABC-Analyse verstehen", "Understand the Pareto principle and ABC analysis"),
        ("RUNNING_SUM in Tableau fuer kumulative Auswertungen nutzen", "Use RUNNING_SUM in Tableau for cumulative analyses"),
        ("Einen Dual-Axis Chart (Balken + Linie) aufbauen", "Build a Dual-Axis chart (bar + line)"),
        ("Produkte in A, B, C Klassen farbcodieren und Entscheidungen ableiten", "Colour-code products in A, B, C classes and derive decisions"),
    ])
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kontext" data-en="Context"></div>'
    + '<h2 class="block__title" data-de="80&#8239;% des Umsatzes mit 20&#8239;% der Produkte" data-en="80&#8239;% of Revenue from 20&#8239;% of Products"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="UrbanCart hat 41 Produkte. Welche davon generieren wirklich Umsatz? Die ABC-Analyse trennt die Kernprodukte von denen, die Lager und Aufmerksamkeit ohne proportionalen Umsatzbeitrag binden." data-en="UrbanCart has 41 products. Which ones actually generate revenue? ABC analysis separates core products from those tying up storage and attention without proportional revenue contribution."></p>'
    + concept(
        "Pareto-Prinzip",
        "80/20-Regel: 20% der Ursachen erklaeren 80% der Wirkung. Vilfredo Pareto entdeckte 1906: 20% der Bevoelkerung besitzen 80% des Bodens in Italien.",
        "80/20 rule: 20% of causes explain 80% of effects. Vilfredo Pareto discovered in 1906: 20% of population owns 80% of land in Italy.",
        "A / B / C Klassen",
        "A: 0-80% Umsatz (Kernprodukte, maximale Prioritaet). B: 80-95% (ergaenzend, optimieren). C: 95-100% (kritisch, Auslistung pruefen).",
        "A: 0-80% revenue (core products, maximum priority). B: 80-95% (complementary, optimise). C: 95-100% (critical, review delisting)."
    )
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Vorbereitung" data-en="Preparation"></div>'
    + '<h2 class="block__title" data-de="Datensaetze laden und verbinden" data-en="Load and connect datasets"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="steps">'
    + step(1, "order_items.csv laden", "Load order_items.csv",
           "Tableau > Verbinden > Textdatei > order_items.csv. Felder: order_item_id, order_id, product_id, quantity, unit_price, total_price.",
           "Tableau > Connect > Text File > order_items.csv. Fields: order_item_id, order_id, product_id, quantity, unit_price, total_price.",
           opened=True)
    + step(2, "products.csv hinzufuegen (Join)", "Add products.csv (Join)",
           "products.csv auf die Arbeitsflaeche ziehen. Join-Feld: product_id. Inner Join. Nun sind product_name und category verfuegbar.",
           "Drag products.csv onto canvas. Join field: product_id. Inner Join. Now product_name and category are available.",
           tip_de="products.csv enthaelt: product_id, product_name, category, price. Nach Join stehen Produktnamen im Arbeitsblatt.",
           tip_en="products.csv contains: product_id, product_name, category, price. After join, product names are available in worksheet.")
    + '</div>'
    + tbox("Im Data-Source-Tab pruefen: order_items INNER JOIN products ueber product_id.",
           "Check in Data Source tab: order_items INNER JOIN products via product_id.")
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Analyse" data-en="Analysis"></div>'
    + '<h2 class="block__title" data-de="Pareto-Diagramm aufbauen" data-en="Build the Pareto Chart"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="5 Schritte zum vollstaendigen Pareto-Diagramm mit ABC-Farbcodierung." data-en="5 steps to a complete Pareto chart with ABC colour coding."></p>'
    + '<div class="steps">'
    + step(1, "Umsatz pro Produkt (Balken, absteigend)", "Revenue per product (bar, descending)",
           "Neues Arbeitsblatt. product_name auf Zeilen. SUM([total_price]) auf Spalten. Toolbar: Absteigend sortieren. Chart-Typ: horizontaler Balken.",
           "New worksheet. product_name to Rows. SUM([total_price]) to Columns. Toolbar: Sort descending. Chart type: horizontal bar.",
           opened=True)
    + step(2, "Berechnetes Feld: Kumulierter Anteil", "Calculated field: Cumulative share",
           "Neues berechnetes Feld, Name: Kum Anteil. Formel: RUNNING_SUM(SUM([total_price])) / TOTAL(SUM([total_price])). Zahlenformat: Prozent.",
           "New calculated field, name: Cum Share. Formula: RUNNING_SUM(SUM([total_price])) / TOTAL(SUM([total_price])). Number format: Percent.",
           tip_de="RUNNING_SUM laeuft von oben nach unten. TOTAL ist die Gesamtsumme. Ergebnis: kumulierter Anteil pro Produkt.",
           tip_en="RUNNING_SUM runs top to bottom. TOTAL is the grand total. Result: cumulative share per product.")
    + step(3, "Dual-Axis erstellen", "Create Dual-Axis",
           "Kum Anteil in den Spalten-Bereich ziehen (zweite Kennzahl). Rechtsklick auf neue Achse > Dual Axis > Achsen synchronisieren. Chart-Typ fuer Kum Anteil: Linie.",
           "Drag Cum Share into Columns area (second measure). Right-click on new axis > Dual Axis > Synchronize axes. Chart type for Cum Share: Line.")
    + step(4, "ABC-Klassen berechnen", "Calculate ABC classes",
           "Berechnetes Feld, Name: ABC. Formel: IF [Kum Anteil] <= 0.8 THEN 'A' ELSEIF [Kum Anteil] <= 0.95 THEN 'B' ELSE 'C' END. Auf Farbe ziehen.",
           "Calculated field, name: ABC. Formula: IF [Cum Share] <= 0.8 THEN 'A' ELSEIF [Cum Share] <= 0.95 THEN 'B' ELSE 'C' END. Drag to Colour.",
           tip_de="Farben anpassen: A = Gruen #3D7A56, B = Orange #E87722, C = Rot #DC2626.",
           tip_en="Adjust colours: A = Green #3D7A56, B = Orange #E87722, C = Red #DC2626.")
    + step(5, "Referenzlinien bei 80% und 95%", "Reference lines at 80% and 95%",
           "Rechtsklick auf linke Achse > Referenzlinie > Wert 0.8 > Beschriftung: A/B-Grenze. Zweite Linie bei 0.95.",
           "Right-click on left axis > Reference Line > Value 0.8 > Label: A/B boundary. Second line at 0.95.")
    + '</div></section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kennzahlen" data-en="Key Metrics"></div>'
    + '<h2 class="block__title" data-de="ABC-Analyse Ergebnisse" data-en="ABC Analysis Results"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="kpi-row">'
    + kpi('<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
          '~8 Produkte', '~8 products', 'A-Produkte', 'Kern: 0-80% Umsatz')
    + kpi('<path d="M18 20V10M12 20V4M6 20v-6"/>',
          '~6 Produkte', '~6 products', 'B-Produkte', 'Ergaenzend: 80-95%')
    + kpi('<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>',
          '~27 Produkte', '~27 products', 'C-Produkte', 'Kritisch: 95-100%')
    + '</div></section>'
    + quiz_sec("lab05.html", "Weiter zu Lab 05: Saisonalitaet", "Continue to Lab 05: Seasonality")
    + ai_bl(["Python", "pandas", "Plotly", "numpy"],
            "# Prompt fuer ChatGPT / Claude:\n"
            '"Erstelle ein Pareto-Diagramm (ABC-Analyse) in Python.\n'
            "Lade order_items.csv und products.csv, merge auf product_id.\n"
            "groupby product_name, berechne SUM(total_price).\n"
            "Sortiere absteigend, berechne kumulierten Anteil (cumsum/sum).\n"
            "Faerbe Balken: A=#3D7A56, B=#E87722, C=#DC2626.\n"
            "Plotly Dual-Axis: Balken links, Linie rechts (kum. Anteil %).\n"
            'Referenzlinien bei 80% und 95%."')
    + nav("lab03.html", "&#8592; Lab 03: RFM-Analyse", "&#8592; Lab 03: RFM Analysis",
          "lab05.html", "Lab 05: Saisonalitaet &#8594;", "Lab 05: Seasonality &#8594;")
)

with open('lab04.html', 'w', encoding='utf-8') as f:
    f.write(page(
        "Lab 04 &#8211; ABC-Analyse &amp; Pareto",
        nb("Lab 04 von 09", "Lab 04 of 09")
        + bc("Lab 04 &#8211; ABC-Analyse &amp; Pareto", "Lab 04 &#8211; ABC Analysis &amp; Pareto")
        + hero("Lab 04 von 09 &#183; Mittel", "Lab 04 of 09 &#183; Intermediate",
               "ABC-Analyse &amp;", "ABC Analysis &amp;", "Pareto-Prinzip", "Pareto Principle",
               "80&#8239;% des Umsatzes kommen von 20&#8239;% der Produkte. Du baust das Pareto-Diagramm und entscheidest, welche Produkte UrbanCart behalten, optimieren oder streichen sollte.",
               "80&#8239;% of revenue comes from 20&#8239;% of products. You build the Pareto chart and decide which products to keep, optimise or discontinue.",
               "60&#8211;90 Min.", "order_items.csv &#183; products.csv", "04")
        + prog(2) + wrap(m04, "04"), q04))
print("lab04.html OK")


# ═══════════════════════════════════════════════════════════
# LAB 05 – SAISONALITAET & ZEITREIHEN
# ═══════════════════════════════════════════════════════════
q05 = [
    Q("Was ist Saisonalitaet?", "What is seasonality?",
      ["Zufaellige Schwankungen", "Wiederkehrende Muster in gleichen Perioden", "Kontinuierlicher Anstieg", "Einmaliger Ausreisser"],
      ["Random fluctuations", "Recurring patterns in the same periods", "Continuous increase", "One-time outlier"],
      1, "Saisonalitaet = periodisch wiederkehrende Muster. Im E-Commerce: Black Friday, Weihnachten.",
      "Seasonality = periodically recurring patterns. In e-commerce: Black Friday, Christmas."),
    Q("Was ist ein Trend in einer Zeitreihe?", "What is a trend in a time series?",
      ["Saisonale Schwankung", "Langfristige Richtung (steigend/fallend/stagnierend)", "Zufaelliges Rauschen", "Ausreisser"],
      ["Seasonal fluctuation", "Long-term direction (rising/falling/stagnating)", "Random noise", "Outlier"],
      1, "Trend = langfristige Richtung. Saisonalitaet = kurz- bis mittelfristiges Muster. Beides ueberlagert sich.",
      "Trend = long-term direction. Seasonality = short to medium-term pattern. Both overlap."),
    Q("Was bedeutet YoY?", "What does YoY mean?",
      ["Year of Year", "Year on Year - Vorjahresvergleich fuer denselben Zeitraum", "Years of Revenue", "Yesterday"],
      ["Year of Year", "Year on Year - prior year comparison for the same period", "Years of Revenue", "Yesterday"],
      1, "YoY vergleicht z.B. November 2024 mit November 2023. Bereinigt Saisonalitaet.",
      "YoY compares e.g. November 2024 with November 2023. Removes seasonal effects."),
    Q("Wie erstellt man YoY in Tableau?", "How to create YoY in Tableau?",
      ["Zwei Arbeitsblatter", "YEAR([order_date]) auf Farbe > zwei Linien 2023 und 2024", "Filter", "Neues Feld"],
      ["Two worksheets", "YEAR([order_date]) to Colour > two lines 2023 and 2024", "Filter", "New field"],
      1, "YEAR auf Farbe: Tableau erstellt automatisch zwei Linien fuer jedes Jahr.",
      "YEAR to Colour: Tableau automatically creates two lines for each year."),
    Q("Wie aktiviert man den Forecast in Tableau?", "How to activate the forecast in Tableau?",
      ["Rechtsklick auf Datenpunkt", "Menue Analyse > Forecast > Forecast einblenden", "Neues Arbeitsblatt", "CSV-Import"],
      ["Right-click on data point", "Menu Analysis > Forecast > Show Forecast", "New worksheet", "CSV import"],
      1, "Tableau Forecast nutzt exponentielle Glaettung. Menue Analyse > Forecast > Forecast einblenden.",
      "Tableau Forecast uses exponential smoothing. Menu Analysis > Forecast > Show Forecast."),
    Q("Was ist ein Konfidenzintervall?", "What is a confidence interval?",
      ["Der vorhergesagte Wert", "Band um den Forecast - Wahrscheinlichkeitsbereich", "Ein Filter", "Der Ist-Wert"],
      ["The predicted value", "Band around forecast - probability range", "A filter", "The actual value"],
      1, "95%-Konfidenzintervall: In 95% der Faelle liegt der Istwert innerhalb dieses Bands.",
      "95% confidence interval: In 95% of cases the actual value falls within this band."),
    Q("Warum Monat statt Tag fuer Trendanalyse?", "Why month instead of day for trend analysis?",
      ["Tage sind ungenaue Daten", "Monatsaggregation glaettet Rauschen, zeigt Muster klarer", "Weniger Daten", "Kostenguenstiger"],
      ["Days are inaccurate data", "Monthly aggregation smooths noise, shows patterns more clearly", "Less data", "Cheaper"],
      1, "Tageswerte sind verrauscht (Wochentag-Effekte). Monate zeigen Saisonalitaet klarer.",
      "Daily values are noisy (weekday effects). Months show seasonality more clearly."),
    Q("Warum gibt es einen Doppelpeak im Nov+Dez?", "Why is there a double peak in Nov+Dec?",
      ["Datenfehler", "Black Friday (Nov) und Weihnachten/Advent (Dez)", "Zufall", "Produktlancierungen"],
      ["Data error", "Black Friday (Nov) and Christmas/Advent (Dec)", "Random", "Product launches"],
      1, "Black Friday: letzter Freitag im November. Advent/Weihnachten: Dezember. Klassischer Doppelpeak.",
      "Black Friday: last Friday in November. Advent/Christmas: December. Classic double peak."),
    Q("Was ist Q4?", "What is Q4?",
      ["Erste Jahreshaelfte", "Viertes Quartal: Oktober, November, Dezember", "Zweites Quartal", "Ein Datenformat"],
      ["First half of year", "Fourth quarter: October, November, December", "Second quarter", "A data format"],
      1, "Q4 = Quartal 4 (Okt-Dez). Im E-Commerce typischerweise staerkstes Quartal.",
      "Q4 = Quarter 4 (Oct-Dec). In e-commerce typically the strongest quarter."),
    Q("Wie berechnet man YoY-Wachstum?", "How to calculate YoY growth?",
      ["Aktuelles / Vorjahr", "(Aktuelles - Vorjahr) / Vorjahr x 100", "Aktuelles - Vorjahr", "Vorjahr / Aktuelles"],
      ["Current / prior year", "(Current - Prior) / Prior x 100", "Current - Prior", "Prior / Current"],
      1, "YoY-Wachstum = (2024 - 2023) / 2023 x 100. Prozentualer Veraenderungswert.",
      "YoY growth = (2024 - 2023) / 2023 x 100. Percentage change value."),
    Q("Was ist ARIMA?", "What is ARIMA?",
      ["Ein Datenbankformat", "Autoregressive Integrated Moving Average - statistisches Zeitreihenmodell", "Tableau-Feature", "Diagrammtyp"],
      ["A database format", "Autoregressive Integrated Moving Average - statistical time series model", "Tableau feature", "Chart type"],
      1, "ARIMA: Klassisches Statistikmodell fuer Zeitreihenforecast. In Python: statsmodels.",
      "ARIMA: Classic statistical model for time series forecasting. In Python: statsmodels."),
    Q("Was ist Facebook Prophet?", "What is Facebook Prophet?",
      ["Social-Media-Tool", "Open-Source-Forecast-Bibliothek, robust fuer Saisonalitaet", "Dashboard-Tool", "KI fuer Bilder"],
      ["Social media tool", "Open-source forecast library, robust for seasonality", "Dashboard tool", "AI for images"],
      1, "Prophet: von Meta entwickelt, ideal fuer E-Commerce-Daten mit Saisonalitaet. pip install prophet.",
      "Prophet: developed by Meta, ideal for e-commerce data with seasonality. pip install prophet."),
    Q("Was ist Zeitreihen-Zerlegung?", "What is time series decomposition?",
      ["Aggregationsmethode", "Aufteilung in Trend + Saisonalitaet + Restkomponente", "Filtermethode", "Exportformat"],
      ["Aggregation method", "Decomposition into Trend + Seasonality + Residual", "Filter method", "Export format"],
      1, "Zerlegung trennt: langfristiger Trend, saisonales Muster, zufaelliges Rauschen.",
      "Decomposition separates: long-term trend, seasonal pattern, random noise."),
    Q("Was ist ein gleitender Durchschnitt?", "What is a moving average?",
      ["Durchschnitt aller Werte", "Durchschnitt der letzten N Perioden, rollt mit der Zeit", "Forecast-Wert", "Ausreissertest"],
      ["Average of all values", "Average of last N periods, rolling over time", "Forecast value", "Outlier test"],
      1, "Gleitender Durchschnitt glaettet kurzfristige Schwankungen. 3M-MA = Durchschnitt letzter 3 Monate.",
      "Moving average smooths short-term fluctuations. 3M-MA = average of last 3 months."),
    Q("Welche Granularitaet zeigt 24 Datenpunkte fuer 2023-2024?", "Which granularity shows 24 data points for 2023-2024?",
      ["Tag", "Woche", "Monat/Jahr", "Quartal"],
      ["Day", "Week", "Month/Year", "Quarter"],
      2, "Monat/Jahr: Jan 2023 bis Dez 2024 = 24 Datenpunkte. Ideal fuer Saisonalitaets-Analyse.",
      "Month/Year: Jan 2023 to Dec 2024 = 24 data points. Ideal for seasonality analysis."),
]

m05 = (
    lz([
        ("Saisonalitaet und Trend in einer E-Commerce-Zeitreihe unterscheiden", "Distinguish seasonality and trend in an e-commerce time series"),
        ("Einen YoY-Vergleich (2023 vs. 2024) in Tableau aufbauen", "Build a YoY comparison (2023 vs. 2024) in Tableau"),
        ("Den Tableau-Forecast aktivieren und Konfidenzintervall lesen", "Activate the Tableau forecast and read the confidence interval"),
        ("Saisonale Peaks (Black Friday, Weihnachten) erklaeren", "Explain seasonal peaks (Black Friday, Christmas)"),
    ])
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kontext" data-en="Context"></div>'
    + '<h2 class="block__title" data-de="Warum Zeitreihen-Analyse fuer E-Commerce entscheidend ist" data-en="Why Time Series Analysis is Critical for E-Commerce"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="Ohne Zeitreihen-Analyse kauft UrbanCart zu wenig Lagerware im Oktober und steht im Black Friday ohne Produkte da. Wer Saisonalitaet versteht, plant Lager, Personal und Budget richtig." data-en="Without time series analysis, UrbanCart buys too little stock in October and runs out on Black Friday. Understanding seasonality means planning stock, staff and budget correctly."></p>'
    + concept(
        "Trend vs. Saisonalitaet",
        "Trend = langfristige Richtung: Waechst UrbanCart ueber 2 Jahre? Saisonalitaet = wiederkehrendes Muster: Nov-Peak jedes Jahr. Beides ueberlagert sich in den Rohdaten.",
        "Trend = long-term direction: Is UrbanCart growing over 2 years? Seasonality = recurring pattern: Nov peak every year. Both overlap in raw data.",
        "YoY-Vergleich",
        "Year on Year: vergleicht denselben Monat im Vorjahr. November 2024 vs. November 2023. Saisonalitaet wird kontrolliert &#8211; das Restliche ist echter Trend.",
        "Year on Year: compares the same month in the prior year. Nov 2024 vs. Nov 2023. Seasonality is controlled &#8211; the remainder is real trend."
    )
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Vorbereitung" data-en="Preparation"></div>'
    + '<h2 class="block__title" data-de="orders.csv laden und Datum pruefen" data-en="Load orders.csv and verify date"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="steps">'
    + step(1, "orders.csv verbinden", "Connect orders.csv",
           "Tableau > Verbinden > Textdatei > orders.csv. Pruefen: order_date als Datum erkannt (Kalender-Icon, nicht Abc-Symbol).",
           "Tableau > Connect > Text File > orders.csv. Check: order_date recognised as date (calendar icon, not Abc symbol).",
           tip_de="Abc statt Kalender? Klicke auf Abc > Datum (Genau). Tableau erkennt dann Datumshierarchien.",
           tip_en="Abc instead of calendar? Click Abc > Date (Exact). Tableau then recognises date hierarchies.",
           opened=True)
    + step(2, "Granularitaet einstellen", "Set granularity",
           "Im Arbeitsblatt: Order Date auf Spalten > Rechtsklick > Monat auswaehlen (nicht Tag oder Jahr). Ergebnis: 24 Datenpunkte (Jan 2023 bis Dez 2024).",
           "In worksheet: Order Date to Columns > Right-click > Select Month (not Day or Year). Result: 24 data points (Jan 2023 to Dec 2024).")
    + '</div>'
    + tbox("Monat/Jahr zeigt 24 Datenpunkte (Jan 2023 bis Dez 2024). Ideal fuer Saisonalitaets-Analyse.",
           "Month/Year shows 24 data points (Jan 2023 to Dec 2024). Ideal for seasonality analysis.")
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Analyse" data-en="Analysis"></div>'
    + '<h2 class="block__title" data-de="Zeitreihe, YoY und Forecast" data-en="Time series, YoY and Forecast"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="3 Arbeitsblatter: Zeitreihe, YoY-Vergleich, Forecast. Dann Dashboard." data-en="3 worksheets: time series, YoY comparison, forecast. Then dashboard."></p>'
    + '<div class="steps">'
    + step(1, "Monatlicher Umsatz (Linienchart)", "Monthly revenue (line chart)",
           "Neues Arbeitsblatt. Order Date auf Spalten (Monat/Jahr). SUM([total_revenue]) auf Zeilen. Chart-Typ: Linie. Peaks im November und Dezember sichtbar?",
           "New worksheet. Order Date to Columns (Month/Year). SUM([total_revenue]) to Rows. Chart type: Line. See peaks in November and December?",
           tip_de="Peak November: Black Friday. Dezember: Weihnachten. Beides echte saisonale Effekte.",
           tip_en="Peak November: Black Friday. December: Christmas. Both real seasonal effects.",
           opened=True)
    + step(2, "YoY-Vergleich", "YoY Comparison",
           "Neues Arbeitsblatt. Order Date auf Spalten (nur Monat 1-12). SUM([total_revenue]) auf Zeilen. YEAR([order_date]) auf Farbe > 2 Linien: 2023 (grau) und 2024 (blau).",
           "New worksheet. Order Date to Columns (month 1-12 only). SUM([total_revenue]) to Rows. YEAR([order_date]) to Colour > 2 lines: 2023 (grey) and 2024 (blue).",
           tip_de="Liegt 2024 konsequent ueber 2023? Das ist echter Wachstumstrend. Gleiche Peaks = Saisonalitaet.",
           tip_en="Is 2024 consistently above 2023? That is real growth trend. Same peaks = seasonality.")
    + step(3, "Forecast aktivieren", "Activate Forecast",
           "Zurueck zur Zeitreihe (alle 24 Monate). Menue Analyse > Forecast > Forecast einblenden. Tableau ergaenzt 6 Monate (Jan-Jun 2025) als gestrichelte Linie mit Konfidenzband.",
           "Back to time series (all 24 months). Menu Analysis > Forecast > Show Forecast. Tableau adds 6 months (Jan-Jun 2025) as dashed line with confidence band.",
           tip_de="Das Konfidenzband: 95% Wahrscheinlichkeit, dass der echte Wert darin liegt. Breites Band = Unsicherheit.",
           tip_en="The confidence band: 95% probability that the real value falls within it. Wide band = uncertainty.")
    + step(4, "Dashboard zusammenbauen", "Assemble dashboard",
           "Neues Dashboard. Zeitreihe oben (gross). YoY-Vergleich unten links. Forecast unten rechts. Titel: UrbanCart Sales Trend 2023-2024 + Forecast.",
           "New dashboard. Time series top (large). YoY comparison bottom-left. Forecast bottom-right. Title: UrbanCart Sales Trend 2023-2024 + Forecast.")
    + '</div></section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kennzahlen" data-en="Key Metrics"></div>'
    + '<h2 class="block__title" data-de="Zeitreihen-Kennzahlen" data-en="Time Series Metrics"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="kpi-row">'
    + kpi('<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
          'Q4 staerkstes Quartal', 'Q4 strongest quarter', 'Saisonalitaet', 'Nov + Dez = Doppelpeak')
    + kpi('<path d="M18 20V10M12 20V4M6 20v-6"/>',
          '+12&#8239;% YoY', '+12&#8239;% YoY', 'YoY-Wachstum', 'Trend 2023 > 2024')
    + kpi('<path d="M5 12h14M12 5l7 7-7 7"/>',
          'Jan&#8211;Jun 2025', 'Jan&#8211;Jun 2025', 'Forecast-Horizont', '6 Monate mit 95%-Band')
    + '</div></section>'
    + quiz_sec("lab06.html", "Weiter zu Lab 06: Conversion Funnel", "Continue to Lab 06: Conversion Funnel")
    + ai_bl(["Python", "pandas", "Prophet", "Plotly"],
            "# Prompt fuer ChatGPT / Claude:\n"
            '"Erstelle eine Zeitreihen-Analyse mit Forecast.\n'
            "Lade orders.csv (pandas), parse order_date als datetime.\n"
            "Aggregiere auf Monatsumsatz: resample('ME').sum().\n"
            "Erstelle mit Plotly:\n"
            "1. YoY: 2023 (#9CA3AF gestrichelt) vs 2024 (#005B9A)\n"
            "2. Prophet Forecast: 6 Monate (Jan-Jun 2025)\n"
            "   Linie in #E87722, Konfidenzband transparent\n"
            'Beschrifte Peaks: Nov 2023 / Nov 2024 als Black Friday."')
    + nav("lab04.html", "&#8592; Lab 04: ABC-Analyse", "&#8592; Lab 04: ABC Analysis",
          "lab06.html", "Lab 06: Conversion Funnel &#8594;", "Lab 06: Conversion Funnel &#8594;")
)

with open('lab05.html', 'w', encoding='utf-8') as f:
    f.write(page(
        "Lab 05 &#8211; Saisonalitaet &amp; Zeitreihen",
        nb("Lab 05 von 09", "Lab 05 of 09")
        + bc("Lab 05 &#8211; Saisonalitaet &amp; Zeitreihen", "Lab 05 &#8211; Seasonality &amp; Time Series")
        + hero("Lab 05 von 09 &#183; Mittel", "Lab 05 of 09 &#183; Intermediate",
               "Saisonalitaet &amp;", "Seasonality &amp;", "Zeitreihen", "Time Series",
               "Umsatzdaten ueber zwei Jahre &#8211; Trends erkennen, Peaks erklaeren, die Zukunft vorhersagen. Du nutzt Tableaus Forecast-Funktion und lernst YoY-Vergleiche aufzubauen.",
               "Revenue data over two years &#8211; recognise trends, explain peaks, predict the future. You use Tableau's forecast function and learn to build YoY comparisons.",
               "60&#8211;90 Min.", "orders.csv", "05")
        + prog(2) + wrap(m05, "05"), q05))
print("lab05.html OK")


# ═══════════════════════════════════════════════════════════
# LAB 06 – CONVERSION FUNNEL
# ═══════════════════════════════════════════════════════════
q06 = [
    Q("Was ist ein Conversion Funnel?", "What is a conversion funnel?",
      ["Ein Produktfilter", "Die Abfolge von Nutzer-Schritten von Besuch bis Kauf", "Ein Diagrammtyp", "Ein Marketingkanal"],
      ["A product filter", "The sequence of user steps from visit to purchase", "A chart type", "A marketing channel"],
      1, "Funnel = Trichter. Jede Stufe verliert Nutzer. Analyse zeigt wo und warum.",
      "Funnel = funnel. Each step loses users. Analysis shows where and why."),
    Q("Was ist die Conversion Rate?", "What is the conversion rate?",
      ["Klickanzahl", "Anteil der Besucher die eine gewuenschte Aktion ausfuehren (z.B. kaufen)", "Umsatz pro Produkt", "Anzahl Sessions"],
      ["Click count", "Share of visitors who complete a desired action (e.g. purchase)", "Revenue per product", "Number of sessions"],
      1, "Conversion Rate = Kaeufer / Besucher x 100. E-Commerce-Durchschnitt: 1-3%.",
      "Conversion Rate = buyers / visitors x 100. E-commerce average: 1-3%."),
    Q("Was ist Drop-off?", "What is drop-off?",
      ["Ein Produktrueckgabe", "Nutzer verlassen den Funnel ohne die naechste Stufe zu erreichen", "Ein Fehler im System", "Ein Marketingbegriff"],
      ["A product return", "Users leaving the funnel without reaching the next step", "A system error", "A marketing term"],
      1, "Drop-off = Absprung an einer Funnel-Stufe. Hoher Drop-off = Problem auf dieser Seite.",
      "Drop-off = abandonment at a funnel step. High drop-off = problem on that page."),
    Q("Welche sessions.csv-Spalte zeigt die Funnel-Stufe?", "Which sessions.csv column shows the funnel stage?",
      ["session_id", "channel", "funnel_stage", "device"],
      ["session_id", "channel", "funnel_stage", "device"],
      2, "funnel_stage enthaelt: landing, product, cart, checkout, purchase.",
      "funnel_stage contains: landing, product, cart, checkout, purchase."),
    Q("Was ist die typische E-Commerce Conversion Rate?", "What is the typical e-commerce conversion rate?",
      ["20-30%", "10-15%", "1-3%", "50%"],
      ["20-30%", "10-15%", "1-3%", "50%"],
      2, "Durchschnitt E-Commerce: 1-3%. Alles darueber ist sehr gut. Mobile oft weniger als Desktop.",
      "E-commerce average: 1-3%. Anything above is very good. Mobile often less than desktop."),
    Q("Was ist Cart Abandonment?", "What is cart abandonment?",
      ["Voller Warenkorb", "Nutzer legt Artikel in den Warenkorb, kauft aber nicht", "Produkt nicht verfuegbar", "Versandkosten"],
      ["Full shopping cart", "User adds items to cart but does not purchase", "Product unavailable", "Shipping costs"],
      1, "Cart Abandonment Rate ca. 70-80%. Haeufige Gruende: unerwartete Kosten, Registrierungspflicht.",
      "Cart abandonment rate approx. 70-80%. Common reasons: unexpected costs, forced registration."),
    Q("Wie visualisiert man einen Funnel in Tableau?", "How to visualise a funnel in Tableau?",
      ["Liniendiagramm", "Balkendiagramm sortiert nach Funnel-Reihenfolge", "Kreisdiagramm", "Heatmap"],
      ["Line chart", "Bar chart sorted by funnel order", "Pie chart", "Heatmap"],
      1, "Funnel in Tableau: Balken mit funnel_stage auf Zeilen (richtige Reihenfolge!), COUNTD sessions auf Spalten.",
      "Funnel in Tableau: Bar chart with funnel_stage on Rows (correct order!), COUNTD sessions on Columns."),
    Q("Was zeigt der Checkout-Drop-off?", "What does the checkout drop-off show?",
      ["Produkte ohne Bestand", "Nutzer die im Checkout-Prozess abbrechen (Zahlung, Adresse)", "Marketing-Effizienz", "Versandzeit"],
      ["Products out of stock", "Users abandoning during checkout (payment, address)", "Marketing efficiency", "Shipping time"],
      1, "Checkout Drop-off: komplizierter Prozess, keine bevorzugte Zahlmethode, Sicherheitsbedenken.",
      "Checkout drop-off: complicated process, no preferred payment method, security concerns."),
    Q("Was ist A/B-Testing?", "What is A/B testing?",
      ["Zwei Produkte vergleichen", "Kontrollierter Vergleich zweier Varianten um die bessere zu bestimmen", "ABC-Analyse", "Zwei Datensaetze mergen"],
      ["Comparing two products", "Controlled comparison of two variants to determine the better one", "ABC analysis", "Merging two datasets"],
      1, "A/B-Test: Version A vs. B mit zufaelliger Nutzerzuteilung. Statistisch signifikante Unterschiede = Gewinner.",
      "A/B test: version A vs. B with random user assignment. Statistically significant differences = winner."),
    Q("Was ist Bounce Rate im Funnel-Kontext?", "What is bounce rate in a funnel context?",
      ["Retouren-Quote", "Anteil Nutzer die nach 1 Seite abspringen (Landing-Stufe)", "Conversion Rate", "Click Rate"],
      ["Return rate", "Share of users leaving after 1 page (landing stage)", "Conversion rate", "Click rate"],
      1, "Bounce Rate = Landing Drop-off. Nutzer sehen Landing Page, klicken nicht weiter. Ziel < 50%.",
      "Bounce Rate = landing drop-off. Users see landing page, do not click further. Target < 50%."),
    Q("Was verbessert die Checkout Conversion?", "What improves checkout conversion?",
      ["Mehr Produkte zeigen", "Gastbestellung ermoeglichen, Zahlmethoden erweeitern, Vertrauen staerken", "Preis erhoehen", "Weniger Bilder"],
      ["Show more products", "Enable guest checkout, expand payment methods, build trust", "Raise prices", "Fewer images"],
      1, "Top-Massnahmen: Gastbestellung, Ratenzahlung/PayPal, SSL-Siegel, klare Rueckgabe-Infos.",
      "Top measures: guest checkout, instalment/PayPal, SSL seal, clear return information."),
    Q("Wie berechnet man Drop-off-Rate?", "How to calculate drop-off rate?",
      ["(Stufe A - Stufe B) * 100", "(Stufe A - Stufe B) / Stufe A x 100", "Stufe B / Stufe A x 100", "Stufe A + Stufe B"],
      ["(Step A - Step B) * 100", "(Step A - Step B) / Step A x 100", "Step B / Step A x 100", "Step A + Step B"],
      1, "Drop-off-Rate = (Eingang - Ausgang) / Eingang x 100. Zeigt prozentualen Verlust.",
      "Drop-off rate = (entry - exit) / entry x 100. Shows percentage loss."),
    Q("Was ist der Unterschied zwischen Session und Nutzer?", "What is the difference between session and user?",
      ["Kein Unterschied", "Session = ein Besuch, Nutzer = eine Person (kann mehrere Sessions haben)", "Nutzer = Session", "Session ist groesser"],
      ["No difference", "Session = one visit, User = one person (can have multiple sessions)", "User = session", "Session is larger"],
      1, "Ein Nutzer kann mehrere Sessions haben. Sessions zaehlen Besuche, Nutzer zaehlen Personen.",
      "A user can have multiple sessions. Sessions count visits, users count people."),
    Q("Welches device hat typischerweise niedrigere Conversion?", "Which device typically has lower conversion?",
      ["Desktop", "Mobile", "Tablet", "Alle gleich"],
      ["Desktop", "Mobile", "Tablet", "All the same"],
      1, "Mobile: kleinerer Screen, Ablenkungen, schwierigere Dateneingabe. Conversion ca. 50% von Desktop.",
      "Mobile: smaller screen, distractions, harder data entry. Conversion approx. 50% of desktop."),
    Q("Was ist der Hauptvorteil von Funnel-Analyse?", "What is the main advantage of funnel analysis?",
      ["Zeigt Umsatz", "Identifiziert den genauen Schritt mit dem groessten Optimierungspotenzial", "Ersetzt A/B-Testing", "Zeigt Produkte"],
      ["Shows revenue", "Identifies the exact step with greatest optimisation potential", "Replaces A/B testing", "Shows products"],
      1, "Funnel zeigt: Wo verliere ich die meisten Nutzer? Dort ansetzen = groesster ROI.",
      "Funnel shows: where do I lose most users? Addressing that = greatest ROI."),
]

m06 = (
    lz([
        ("Den Conversion Funnel verstehen und in Tableau visualisieren", "Understand the conversion funnel and visualise it in Tableau"),
        ("Drop-off-Raten pro Funnel-Stufe berechnen", "Calculate drop-off rates per funnel stage"),
        ("Unterschiede nach Geraet und Kanal identifizieren", "Identify differences by device and channel"),
        ("Optimierungsmassnahmen fuer kritische Stellen ableiten", "Derive optimisation measures for critical steps"),
    ])
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kontext" data-en="Context"></div>'
    + '<h2 class="block__title" data-de="Warum verliert UrbanCart 97% seiner Besucher?" data-en="Why does UrbanCart lose 97% of its visitors?"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="Der durchschnittliche E-Commerce-Shop konvertiert 1-3% seiner Besucher. 97-99% verlassen die Seite ohne zu kaufen. Die Funnel-Analyse zeigt: An welcher Stelle brechen die meisten ab &#8211; und warum?" data-en="The average e-commerce shop converts 1-3% of visitors. 97-99% leave without buying. Funnel analysis shows: at which step do most drop off &#8211; and why?"></p>'
    + concept(
        "Was ist ein Funnel?",
        "Ein Trichter: viele Besucher oben, wenige Kaeufer unten. Jede Stufe verliert Nutzer. Stufen: Landing > Produkt > Warenkorb > Checkout > Kauf.",
        "A funnel: many visitors at top, few buyers at bottom. Each step loses users. Stages: Landing > Product > Cart > Checkout > Purchase.",
        "Drop-off vs. Conversion",
        "Drop-off-Rate = Verlustquote an einer Stufe. Conversion Rate = Anteil der Besucher die kaufen. Ziel: Drop-off minimieren, Conversion maximieren.",
        "Drop-off rate = loss rate at a step. Conversion rate = share of visitors who buy. Goal: minimise drop-off, maximise conversion."
    )
    + infobox("Typische Drop-off-Raten im E-Commerce", "Typical Drop-off Rates in E-Commerce", [
        ("Landing > Produkt", "~40% Absprung (Bounce Rate)"),
        ("Produkt > Warenkorb", "~60% Absprung (kein Kauf-Intent)"),
        ("Warenkorb > Checkout", "~70% Absprung (Cart Abandonment)"),
        ("Checkout > Kauf", "~30% Absprung (Zahlungsprobleme)"),
    ])
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Vorbereitung" data-en="Preparation"></div>'
    + '<h2 class="block__title" data-de="sessions.csv laden" data-en="Load sessions.csv"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="steps">'
    + step(1, "sessions.csv verbinden", "Connect sessions.csv",
           "Tableau > Verbinden > Textdatei > sessions.csv. Felder pruefen: session_id, user_id, channel, device, funnel_stage, session_date.",
           "Tableau > Connect > Text File > sessions.csv. Check fields: session_id, user_id, channel, device, funnel_stage, session_date.",
           tip_de="funnel_stage enthaelt die Werte: landing, product, cart, checkout, purchase. Das ist unsere Kernvariable.",
           tip_en="funnel_stage contains: landing, product, cart, checkout, purchase. That is our core variable.",
           opened=True)
    + step(2, "Funnel-Reihenfolge sicherstellen", "Ensure funnel order",
           "funnel_stage ist ein Text-Feld. Tableau sortiert es alphabetisch &#8211; das ist falsch. Rechtsklick auf funnel_stage > Benutzerdefinierte Sortierung > manuell festlegen: landing, product, cart, checkout, purchase.",
           "funnel_stage is a text field. Tableau sorts it alphabetically &#8211; that is wrong. Right-click on funnel_stage > Custom sort > set manually: landing, product, cart, checkout, purchase.")
    + '</div>'
    + tbox("Die korrekte Reihenfolge ist entscheidend fuer den Funnel. Alphabetisch wuerde 'cart' vor 'landing' kommen &#8211; das ergibt keinen Sinn.",
           "Correct order is critical for the funnel. Alphabetically 'cart' would come before 'landing' &#8211; that makes no sense.")
    + '</section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Analyse" data-en="Analysis"></div>'
    + '<h2 class="block__title" data-de="Funnel aufbauen und Drop-offs analysieren" data-en="Build funnel and analyse drop-offs"></h2>'
    + '<div class="block__rule"></div>'
    + '<p class="block__lead" data-de="4 Schritte zum vollstaendigen Funnel-Dashboard mit Drop-off-Analyse nach Geraet." data-en="4 steps to a complete funnel dashboard with device-level drop-off analysis."></p>'
    + '<div class="steps">'
    + step(1, "Funnel-Balkendiagramm", "Funnel bar chart",
           "Neues Arbeitsblatt. funnel_stage auf Zeilen (korrekte Reihenfolge!). COUNTD([session_id]) auf Spalten. Chart-Typ: Balken. Absteigend sortieren.",
           "New worksheet. funnel_stage to Rows (correct order!). COUNTD([session_id]) to Columns. Chart type: Bar. Sort descending.",
           tip_de="Der Balken wird kleiner: viele Sessions landen, wenige kaufen. Das ist der Funnel-Trichter.",
           tip_en="The bar gets smaller: many sessions land, few purchase. That is the funnel.",
           opened=True)
    + step(2, "Drop-off-Rate berechnen", "Calculate drop-off rate",
           "Berechnetes Feld: Drop-off Rate = (Vorherige Stufe - Aktuelle Stufe) / Vorherige Stufe x 100. Alternativ: Tableau Table Calculations nutzen (WINDOW_SUM).",
           "Calculated field: Drop-off Rate = (Previous Stage - Current Stage) / Previous Stage x 100. Alternatively: use Tableau Table Calculations (WINDOW_SUM).")
    + step(3, "Aufteilen nach Geraet", "Break down by device",
           "Neues Arbeitsblatt. device auf Farbe ziehen. Funnel nach device aufgeteilt: Wo ist Mobile schwaecher als Desktop?",
           "New worksheet. Drag device to Colour. Funnel split by device: where is Mobile weaker than Desktop?",
           tip_de="Mobile zeigt typischerweise schlechtere Conversion im Checkout-Schritt: kleinerer Screen, schwierigere Eingabe.",
           tip_en="Mobile typically shows worse conversion at checkout: smaller screen, harder data entry.")
    + step(4, "Dashboard: Funnel + Geraet + Kanal", "Dashboard: Funnel + Device + Channel",
           "Neues Dashboard. Hauptfunnel gross oben. Geraete-Vergleich unten links. Kanal-Vergleich unten rechts. Titel: UrbanCart Conversion Funnel Analysis.",
           "New dashboard. Main funnel large at top. Device comparison bottom-left. Channel comparison bottom-right. Title: UrbanCart Conversion Funnel Analysis.")
    + '</div></section>'
    + '<section class="block sr">'
    + '<div class="block__eyebrow" data-de="Kennzahlen" data-en="Key Metrics"></div>'
    + '<h2 class="block__title" data-de="Funnel-Kennzahlen" data-en="Funnel Metrics"></h2>'
    + '<div class="block__rule"></div>'
    + '<div class="kpi-row">'
    + kpi('<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
          '~2&#8239;% Conversion', '~2&#8239;% Conversion', 'Overall Conversion', 'Landing > Purchase')
    + kpi('<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>',
          '~70&#8239;% Cart Abandon', '~70&#8239;% Cart Abandon', 'Groesster Drop-off', 'Warenkorb > Checkout')
    + kpi('<rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>',
          'Mobile -50&#8239;%', 'Mobile -50&#8239;%', 'Geraete-Luecke', 'vs. Desktop Conversion')
    + '</div></section>'
    + quiz_sec("lab07.html", "Weiter zu Lab 07: Sentiment-Analyse", "Continue to Lab 07: Sentiment Analysis")
    + ai_bl(["Python", "pandas", "Plotly", "plotly.express"],
            "# Prompt fuer ChatGPT / Claude:\n"
            '"Erstelle eine Conversion Funnel Analyse in Python.\n'
            "Lade sessions.csv (pandas). Zaehle COUNTD(session_id) pro funnel_stage.\n"
            "Reihenfolge: landing > product > cart > checkout > purchase.\n"
            "Berechne Drop-off-Rate: (Stufe[n-1] - Stufe[n]) / Stufe[n-1] x 100.\n"
            "Erstelle Plotly Funnel Chart (px.funnel) in Orange #E87722.\n"
            "Zweiter Chart: Funnel aufgeteilt nach device (Mobile vs. Desktop).\n"
            'Zeige Conversion Rate (purchase / landing x 100) als KPI."')
    + nav("lab05.html", "&#8592; Lab 05: Saisonalitaet", "&#8592; Lab 05: Seasonality",
          "lab07.html", "Lab 07: Sentiment-Analyse &#8594;", "Lab 07: Sentiment Analysis &#8594;")
)

with open('lab06.html', 'w', encoding='utf-8') as f:
    f.write(page(
        "Lab 06 &#8211; Conversion Funnel",
        nb("Lab 06 von 09", "Lab 06 of 09")
        + bc("Lab 06 &#8211; Conversion Funnel &amp; Drop-off", "Lab 06 &#8211; Conversion Funnel &amp; Drop-off")
        + hero("Lab 06 von 09 &#183; Mittel", "Lab 06 of 09 &#183; Intermediate",
               "Conversion Funnel", "Conversion Funnel", "&amp; Drop-off-Analyse", "&amp; Drop-off Analysis",
               "Warum verlassen 97% der Besucher den Shop ohne zu kaufen? Du analysierst den Conversion Funnel von UrbanCart und identifizierst die kritischen Absprungpunkte.",
               "Why do 97% of visitors leave without buying? You analyse UrbanCart's conversion funnel and identify the critical drop-off points.",
               "60&#8211;90 Min.", "sessions.csv", "06")
        + prog(2) + wrap(m06, "06"), q06))
print("lab06.html OK")


# ═══════════════════════════════════════════════════════════
# LAB 07 – SENTIMENT-ANALYSE
# ═══════════════════════════════════════════════════════════
