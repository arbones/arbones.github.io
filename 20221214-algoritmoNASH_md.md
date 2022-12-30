---
bibliography: references.bib
date: December 30, 2022
date-format: long
editor: visual
editor_options:
  chunk_output_type: console
execute:
  echo: false
  warning: false
header-includes:
- |
  <script  src="20221214-algoritmoNASH_md_files/libs/quarto-diagram/mermaid.min.js"></script>
  <script  src="20221214-algoritmoNASH_md_files/libs/quarto-diagram/mermaid-init.js"></script>
  <link  href="20221214-algoritmoNASH_md_files/libs/quarto-diagram/mermaid.css" rel="stylesheet" />
- |
  <script src="20221214-algoritmoNASH_md_files/libs/kePrint-0.0.1/kePrint.js"></script>
  <link href="20221214-algoritmoNASH_md_files/libs/lightable-0.0.1/lightable.css" rel="stylesheet" />
title: Fibroscan&Biopsias
toc-title: Table of contents
---

<script  src="20221214-algoritmoNASH_md_files/libs/quarto-diagram/mermaid.min.js"></script>
<script  src="20221214-algoritmoNASH_md_files/libs/quarto-diagram/mermaid-init.js"></script>
<link  href="20221214-algoritmoNASH_md_files/libs/quarto-diagram/mermaid.css" rel="stylesheet" />

<script src="20221214-algoritmoNASH_md_files/libs/kePrint-0.0.1/kePrint.js"></script>
<link href="20221214-algoritmoNASH_md_files/libs/lightable-0.0.1/lightable.css" rel="stylesheet" />


-   [[1]{.toc-section-number} Biopsias recogidas durante la
    IQ](#biopsias-recogidas-durante-la-iq){#toc-biopsias-recogidas-durante-la-iq}
    -   [[1.1]{.toc-section-number} Caracteristicas de los pacientes en
        la cohorte de pacientes
        biopsiados](#caracteristicas-de-los-pacientes-en-la-cohorte-de-pacientes-biopsiados){#toc-caracteristicas-de-los-pacientes-en-la-cohorte-de-pacientes-biopsiados}
    -   [[1.2]{.toc-section-number} Resultado
        biopsias](#resultado-biopsias){#toc-resultado-biopsias}
-   [[2]{.toc-section-number}
    Correlaciones](#correlaciones){#toc-correlaciones}
    -   [[2.1]{.toc-section-number} Correlación Biopsia \<\>
        Fibroscan](#correlación-biopsia-fibroscan){#toc-correlación-biopsia-fibroscan}
    -   [[2.2]{.toc-section-number} Correlación Biopsia \<\>
        FIB4](#correlación-biopsia-fib4){#toc-correlación-biopsia-fib4}
    -   [[2.3]{.toc-section-number} Correlación Fibroscan \<\>
        FIB4](#correlación-fibroscan-fib4){#toc-correlación-fibroscan-fib4}
-   [[3]{.toc-section-number} Predicción fibrosis
    avanzada](#predicción-fibrosis-avanzada){#toc-predicción-fibrosis-avanzada}
    -   [[3.1]{.toc-section-number} Toda la
        cohorte](#toda-la-cohorte){#toc-toda-la-cohorte}
        -   [[3.1.1]{.toc-section-number} Fibrosis con
            fibroscan](#fibrosis-con-fibroscan){#toc-fibrosis-con-fibroscan}
        -   [[3.1.2]{.toc-section-number} Fibrosis **avanzada** con
            fibroscan](#fibrosis-avanzada-con-fibroscan){#toc-fibrosis-avanzada-con-fibroscan}
        -   [[3.1.3]{.toc-section-number} Fibrosis **avanzada** con
            FIB4](#fibrosis-avanzada-con-fib4){#toc-fibrosis-avanzada-con-fib4}
    -   [[3.2]{.toc-section-number} Modelo secuencial
        EASL](#modelo-secuencial-easl){#toc-modelo-secuencial-easl}
-   [[4]{.toc-section-number} Predicción de "at-risk NASH
    [@stern2022]](#predicción-de-at-risk-nash-stern2022){#toc-predicción-de-at-risk-nash-stern2022}
    -   [[4.1]{.toc-section-number} Toda la
        cohorte](#toda-la-cohorte-1){#toc-toda-la-cohorte-1}
        -   [[4.1.1]{.toc-section-number}
            Fibroscan](#fibroscan){#toc-fibroscan}
        -   [[4.1.2]{.toc-section-number} FIB4](#fib4){#toc-fib4}
    -   [[4.2]{.toc-section-number} Modelo secuencial
        EASL](#modelo-secuencial-easl-1){#toc-modelo-secuencial-easl-1}
        -   [[4.2.1]{.toc-section-number} Clasificación usando FIB\>1.3
            (EASL-2021)](#clasificación-usando-fib1.3-easl-2021){#toc-clasificación-usando-fib1.3-easl-2021}
        -   [[4.2.2]{.toc-section-number} Clasificación con los nuevos
            puntos de
            corte](#clasificación-con-los-nuevos-puntos-de-corte){#toc-clasificación-con-los-nuevos-puntos-de-corte}
-   [[5]{.toc-section-number}
    BIBLIOGRAFIA](#bibliografia){#toc-bibliografia}

::: cell
:::

-   Se han reclutado 149 desde 2019 para la cohorte FATe de los cuales
    148 se han sometido a cirugía. 108 pacientes tienen fibroscan
    pre-intervención.\
-   Hay 97 pacientes con biopsia y fibroscan pre-intervención.
-   Se añaden 2 nuevos pacientes con fibrosis avanzada. **No son FATe**

::: cell
::: cell-output-display
<div>

```{=html}
<p>
```
```{=html}
<pre class="mermaid mermaid-js" data-tooltip-selector="#mermaid-tooltip-1">flowchart LR
A[(Pacientes&lt;br&gt;FATe reclutados&lt;br&gt;desde el 2019&lt;br&gt;n=149)]
B[Biopsias&lt;br&gt;n=129]
C[(Pacientes&lt;br&gt;con Fibroscan&lt;br&gt;pre-IQ&lt;br&gt;n=108)]
D[Pacientes&lt;br&gt;con biopsia y&lt;br&gt;fibroscan pre-IQ&lt;br&gt;n=97]
E[Total incluidos&lt;br&gt;en el análisis&lt;br&gt;n=99]
A--&gt;B
A--&gt;C
C--&gt;D
B--&gt;D
D--&gt;|Pacientes&lt;br&gt;añadidos&lt;br&gt;n=2|E
</pre>
```
::: {#mermaid-tooltip-1 .mermaidTooltip}
:::

```{=html}
</p>
```

</div>
:::
:::

-   Se añaden 2 nuevos pacientes con fibrosis avanzada. **No son FATe**.
    Solo se incluyen los datos de fibrosis, resultado biopsia, edad, IMC
    , sexo, GPT, GOT y plaquetas.

# Biopsias recogidas durante la IQ {#biopsias-recogidas-durante-la-iq number="1"}

## Caracteristicas de los pacientes en la cohorte de pacientes biopsiados {#caracteristicas-de-los-pacientes-en-la-cohorte-de-pacientes-biopsiados number="1.1"}

La fibrosis hepática se evaluó de acuerdo con los criterios de NASH
Clinical Research Network [@kleiner2005a]:\
F0: sin fibrosis, F1: fibrosis perisinusoidal o portal/periportal, F2:
fibrosis perisinusoidal y portal/periportal, F3: fibrosis en puente, y
F4: cirrosis)

::: cell
::: cell-output-display
```{=html}
<table class="table table-striped table-condensed" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption></caption>
 <thead>
  <tr>
   <th style="text-align:left;">   </th>
   <th style="text-align:center;"> [ALL] </th>
   <th style="text-align:center;"> F0-F2 </th>
   <th style="text-align:center;"> F3-F4 </th>
   <th style="text-align:center;"> p.overall </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;font-style: italic;border-bottom: 1px solid grey">  </td>
   <td style="text-align:center;font-style: italic;border-bottom: 1px solid grey"> N=98 </td>
   <td style="text-align:center;font-style: italic;border-bottom: 1px solid grey"> N=94 </td>
   <td style="text-align:center;font-style: italic;border-bottom: 1px solid grey"> N=4 </td>
   <td style="text-align:center;font-style: italic;border-bottom: 1px solid grey">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> edad </td>
   <td style="text-align:center;"> 47.5 [41.0;54.0] </td>
   <td style="text-align:center;"> 47.0 [41.0;52.8] </td>
   <td style="text-align:center;"> 58.5 [50.8;61.0] </td>
   <td style="text-align:center;"> 0.116 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> imc </td>
   <td style="text-align:center;"> 45.7 (6.12) </td>
   <td style="text-align:center;"> 46.1 (5.91) </td>
   <td style="text-align:center;"> 38.4 (7.27) </td>
   <td style="text-align:center;"> 0.125 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> CAP </td>
   <td style="text-align:center;"> 332 [297;380] </td>
   <td style="text-align:center;"> 332 [297;381] </td>
   <td style="text-align:center;"> 336 [319;352] </td>
   <td style="text-align:center;"> 0.939 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> fibroscan </td>
   <td style="text-align:center;"> 6.35 [4.90;10.4] </td>
   <td style="text-align:center;"> 6.30 [4.90;10.0] </td>
   <td style="text-align:center;"> 16.8 [10.7;26.5] </td>
   <td style="text-align:center;"> 0.012 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> nas </td>
   <td style="text-align:center;"> 1.00 [0.00;3.00] </td>
   <td style="text-align:center;"> 1.00 [0.00;3.00] </td>
   <td style="text-align:center;"> 6.50 [5.75;7.25] </td>
   <td style="text-align:center;"> 0.019 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> GOT </td>
   <td style="text-align:center;"> 24.0 [19.0;31.0] </td>
   <td style="text-align:center;"> 23.5 [19.0;29.2] </td>
   <td style="text-align:center;"> 72.0 [44.0;97.8] </td>
   <td style="text-align:center;"> 0.003 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> GPT </td>
   <td style="text-align:center;"> 25.0 [19.0;40.0] </td>
   <td style="text-align:center;"> 24.0 [18.5;39.0] </td>
   <td style="text-align:center;"> 87.5 [55.0;112] </td>
   <td style="text-align:center;"> 0.012 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> fib4 </td>
   <td style="text-align:center;"> 0.87 [0.66;1.20] </td>
   <td style="text-align:center;"> 0.84 [0.63;1.18] </td>
   <td style="text-align:center;"> 1.91 [1.69;2.27] </td>
   <td style="text-align:center;"> 0.002 </td>
  </tr>
</tbody>
</table>
```
:::
:::

## Resultado biopsias {#resultado-biopsias number="1.2"}

::: panel-tabset
### NAFLD Activity Score (NAS) {#nafld-activity-score-nas number="1.2.1"}

::: cell
::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown/unnamed-chunk-4-1.png)
:::
:::

### Fibrosis Stage {#fibrosis-stage number="1.2.2"}

::: cell
::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown/unnamed-chunk-5-1.png)
:::
:::

### Esteatosis {#esteatosis number="1.2.3"}

::: cell
::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown/unnamed-chunk-6-1.png)
:::
:::
:::

Hay un 4% de pacientes con fibrosis avanzada (grados 3-4 en la biopsia)

# Correlaciones {#correlaciones number="2"}

## Correlación Biopsia \<\> Fibroscan {#correlación-biopsia-fibroscan number="2.1"}

::: cell
::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown/unnamed-chunk-7-1.png)
:::
:::

::: cell
::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown/unnamed-chunk-8-1.png)
:::
:::

## Correlación Biopsia \<\> FIB4 {#correlación-biopsia-fib4 number="2.2"}

::: cell
::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown/unnamed-chunk-9-1.png)
:::
:::

## Correlación Fibroscan \<\> FIB4 {#correlación-fibroscan-fib4 number="2.3"}

::: cell
::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown/unnamed-chunk-10-1.png)
:::
:::

Se quita un valor de fibrosis (57.8) \>\>\>outlier???

# Predicción fibrosis avanzada {#predicción-fibrosis-avanzada number="3"}

## Toda la cohorte {#toda-la-cohorte number="3.1"}

### Fibrosis con fibroscan {#fibrosis-con-fibroscan number="3.1.1"}

**Gold standard**: Detección de fibrosis en biopsia (Fibrosis ≠ 0).\
El punto de corte se calcula a partir del indice de Youden (J)
maximizando la sensibilidad y la especificidad
($J = Sensibilidad + Especificidad − 1$)

::: cell
::: cell-output-display
```{=html}
<table class="table table-striped" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:right;"> optimal_cutpoint </th>
   <th style="text-align:right;"> acc </th>
   <th style="text-align:right;"> sensitivity </th>
   <th style="text-align:right;"> specificity </th>
   <th style="text-align:right;"> AUC </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 9.9 </td>
   <td style="text-align:right;"> 0.71 </td>
   <td style="text-align:right;"> 0.58 </td>
   <td style="text-align:right;"> 0.76 </td>
   <td style="text-align:right;"> 0.68 </td>
  </tr>
</tbody>
</table>
```
:::
:::

### Fibrosis **avanzada** con fibroscan {#fibrosis-avanzada-con-fibroscan number="3.1.2"}

**Gold standard**: Detección de fibrosis en biopsia (F3-F4).\
El punto de corte se calcula a partir del indice de Youden (J)
maximizando la sensibilidad y la especificidad
($J = Sensibilidad + Especificidad − 1$)

::: cell
::: cell-output-display
```{=html}
<table class="table table-striped" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:right;"> optimal_cutpoint </th>
   <th style="text-align:right;"> acc </th>
   <th style="text-align:right;"> sensitivity </th>
   <th style="text-align:right;"> specificity </th>
   <th style="text-align:right;"> AUC </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 9.9 </td>
   <td style="text-align:right;"> 0.71 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7 </td>
   <td style="text-align:right;"> 0.87 </td>
  </tr>
</tbody>
</table>
```
:::
:::

### Fibrosis **avanzada** con FIB4 {#fibrosis-avanzada-con-fib4 number="3.1.3"}

**Gold standard**: Detección de fibrosis en biopsia (F3-F4).\
El punto de corte se calcula a partir del indice de Youden (J)
maximizando la sensibilidad y la especificidad
($J = Sensibilidad + Especificidad − 1$)

::: cell
::: cell-output-display
```{=html}
<table class="table table-striped" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:right;"> optimal_cutpoint </th>
   <th style="text-align:right;"> acc </th>
   <th style="text-align:right;"> sensitivity </th>
   <th style="text-align:right;"> specificity </th>
   <th style="text-align:right;"> AUC </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 1.49 </td>
   <td style="text-align:right;"> 0.9 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9 </td>
   <td style="text-align:right;"> 0.95 </td>
  </tr>
</tbody>
</table>
```
:::
:::

## Modelo secuencial EASL {#modelo-secuencial-easl number="3.2"}

To enable the detection of advanced liver fibrosis in patients with
NAFLD in the primary care setting or in diabetology clinics, the EASL
has proposed a three-tiered approach for the use of NITs
[@berzigotti2021],[@canivet2022]

![Algoritmo EASL](images/easl.png){fig-align="center"}

::: cell
::: cell-output-display
```{=html}
<table class="table table-striped table-condensed" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>Clasificación de los pacientes segun el FIB4</caption>
 <thead>
  <tr>
   <th style="text-align:left;">   </th>
   <th style="text-align:center;"> &lt;1.30 </th>
   <th style="text-align:center;"> &gt;=1.30 </th>
   <th style="text-align:center;"> p.overall </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;font-style: italic;border-bottom: 1px solid grey">  </td>
   <td style="text-align:center;font-style: italic;border-bottom: 1px solid grey"> N=75 </td>
   <td style="text-align:center;font-style: italic;border-bottom: 1px solid grey"> N=18 </td>
   <td style="text-align:center;font-style: italic;border-bottom: 1px solid grey">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> fib4 </td>
   <td style="text-align:center;"> 0.76 [0.56;1.00] </td>
   <td style="text-align:center;"> 1.61 [1.48;2.15] </td>
   <td style="text-align:center;"> &lt;0.001 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> CAP </td>
   <td style="text-align:center;"> 336 [300;380] </td>
   <td style="text-align:center;"> 322 [298;375] </td>
   <td style="text-align:center;"> 0.888 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> fibroscan </td>
   <td style="text-align:center;"> 6.30 [4.85;10.0] </td>
   <td style="text-align:center;"> 7.45 [5.08;12.2] </td>
   <td style="text-align:center;"> 0.257 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> nas </td>
   <td style="text-align:center;"> 1.00 [0.00;3.00] </td>
   <td style="text-align:center;"> 2.00 [0.00;4.25] </td>
   <td style="text-align:center;"> 0.277 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Esteatosis: </td>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;"> 0.533 </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 0 </td>
   <td style="text-align:center;"> 30 (40.0%) </td>
   <td style="text-align:center;"> 5 (31.2%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 1 </td>
   <td style="text-align:center;"> 20 (26.7%) </td>
   <td style="text-align:center;"> 5 (31.2%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 2 </td>
   <td style="text-align:center;"> 19 (25.3%) </td>
   <td style="text-align:center;"> 3 (18.8%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 3 </td>
   <td style="text-align:center;"> 6 (8.00%) </td>
   <td style="text-align:center;"> 3 (18.8%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> balonizacion: </td>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;"> 0.299 </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 0 </td>
   <td style="text-align:center;"> 62 (82.7%) </td>
   <td style="text-align:center;"> 11 (68.8%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 1 </td>
   <td style="text-align:center;"> 10 (13.3%) </td>
   <td style="text-align:center;"> 4 (25.0%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 2 </td>
   <td style="text-align:center;"> 3 (4.00%) </td>
   <td style="text-align:center;"> 1 (6.25%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> inflamacion: </td>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;"> 0.095 </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 0 </td>
   <td style="text-align:center;"> 52 (69.3%) </td>
   <td style="text-align:center;"> 7 (43.8%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 1 </td>
   <td style="text-align:center;"> 18 (24.0%) </td>
   <td style="text-align:center;"> 6 (37.5%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 2 </td>
   <td style="text-align:center;"> 4 (5.33%) </td>
   <td style="text-align:center;"> 2 (12.5%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 3 </td>
   <td style="text-align:center;"> 1 (1.33%) </td>
   <td style="text-align:center;"> 1 (6.25%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> fibrosis </td>
   <td style="text-align:center;"> 0.00 [0.00;0.00] </td>
   <td style="text-align:center;"> 0.50 [0.00;1.00] </td>
   <td style="text-align:center;"> 0.009 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> fibrosis_SiNo </td>
   <td style="text-align:center;"> 16 (21.6%) </td>
   <td style="text-align:center;"> 9 (50.0%) </td>
   <td style="text-align:center;"> 0.035 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> fib.avanz </td>
   <td style="text-align:center;"> 0 (0.00%) </td>
   <td style="text-align:center;"> 4 (22.2%) </td>
   <td style="text-align:center;"> 0.001 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> at.risk.nash </td>
   <td style="text-align:center;"> 4 (5.33%) </td>
   <td style="text-align:center;"> 2 (12.5%) </td>
   <td style="text-align:center;"> 0.284 </td>
  </tr>
</tbody>
</table>
```
:::
:::

#### Representación grafica de las categorías de FIB4 y liver stiffness measurement (fibroscan) {#representación-grafica-de-las-categorías-de-fib4-y-liver-stiffness-measurement-fibroscan .unnumbered}

::: cell
::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown//vtree001.png){width="2000"}
:::
:::

#### Metricas de diagnóstico de fibrosis avanzada {#metricas-de-diagnóstico-de-fibrosis-avanzada .unnumbered}

::: cell
::: cell-output-display
```{=html}
<table class="table table-striped" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:right;"> optimal_cutpoint </th>
   <th style="text-align:right;"> acc </th>
   <th style="text-align:right;"> sensitivity </th>
   <th style="text-align:right;"> specificity </th>
   <th style="text-align:right;"> AUC </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 9.9 </td>
   <td style="text-align:right;"> 0.78 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.71 </td>
   <td style="text-align:right;"> 0.88 </td>
  </tr>
</tbody>
</table>
```
:::

::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown/unnamed-chunk-16-1.png)
:::
:::

# Predicción de "at-risk NASH [@stern2022] {#predicción-de-at-risk-nash-stern2022 number="4"}

At-risk NASH (or fibrotic NASH) is defined by the presence of NASH
(NAFLD activity score ≥4 with 1 item of each at least) and significant
fibrosis (fibrosis stage ≥2) [@sanyal2015]

## Toda la cohorte {#toda-la-cohorte-1 number="4.1"}

### Fibroscan {#fibroscan number="4.1.1"}

::: cell
::: cell-output-display
```{=html}
<table class="table table-striped" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:right;"> optimal_cutpoint </th>
   <th style="text-align:right;"> acc </th>
   <th style="text-align:right;"> sensitivity </th>
   <th style="text-align:right;"> specificity </th>
   <th style="text-align:right;"> AUC </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 9.9 </td>
   <td style="text-align:right;"> 0.74 </td>
   <td style="text-align:right;"> 0.86 </td>
   <td style="text-align:right;"> 0.73 </td>
   <td style="text-align:right;"> 0.84 </td>
  </tr>
</tbody>
</table>
```
:::
:::

### FIB4 {#fib4 number="4.1.2"}

::: cell
::: cell-output-display
```{=html}
<table class="table table-striped" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:right;"> optimal_cutpoint </th>
   <th style="text-align:right;"> acc </th>
   <th style="text-align:right;"> sensitivity </th>
   <th style="text-align:right;"> specificity </th>
   <th style="text-align:right;"> AUC </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 0.89 </td>
   <td style="text-align:right;"> 0.59 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.56 </td>
   <td style="text-align:right;"> 0.73 </td>
  </tr>
</tbody>
</table>
```
:::
:::

## Modelo secuencial EASL {#modelo-secuencial-easl-1 number="4.2"}

### Clasificación usando FIB\>1.3 (EASL-2021) {#clasificación-usando-fib1.3-easl-2021 number="4.2.1"}

::: cell
::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown//vtree002.png){width="2000"}
:::
:::

**Cutoff de fibrosis en el subgrupo FIB4\>=1.30**

::: cell
::: cell-output-display
```{=html}
<table class="table table-striped" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:right;"> optimal_cutpoint </th>
   <th style="text-align:right;"> acc </th>
   <th style="text-align:right;"> sensitivity </th>
   <th style="text-align:right;"> specificity </th>
   <th style="text-align:right;"> AUC </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 9.9 </td>
   <td style="text-align:right;"> 0.75 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.71 </td>
   <td style="text-align:right;"> 0.86 </td>
  </tr>
</tbody>
</table>
```
:::

::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown/unnamed-chunk-20-1.png)
:::
:::

### Clasificación con los nuevos puntos de corte {#clasificación-con-los-nuevos-puntos-de-corte number="4.2.2"}

#### FIB4\> 0.89, LSM\>=8 (EASL-2021) {#fib4-0.89-lsm8-easl-2021 number="4.2.2.1"}

::: cell
::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown//vtree003.png){width="2000"}
:::
:::

::: cell
::: cell-output-display
```{=html}
<table class="table table-striped table-condensed" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption></caption>
 <thead>
  <tr>
   <th style="text-align:left;">   </th>
   <th style="text-align:center;"> &lt; 0.89 </th>
   <th style="text-align:center;"> &gt;= 0.89 </th>
   <th style="text-align:center;"> p.overall </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;font-style: italic;border-bottom: 1px solid grey">  </td>
   <td style="text-align:center;font-style: italic;border-bottom: 1px solid grey"> N=49 </td>
   <td style="text-align:center;font-style: italic;border-bottom: 1px solid grey"> N=44 </td>
   <td style="text-align:center;font-style: italic;border-bottom: 1px solid grey">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> fib4 </td>
   <td style="text-align:center;"> 0.66 [0.51;0.76] </td>
   <td style="text-align:center;"> 1.22 [1.05;1.53] </td>
   <td style="text-align:center;"> &lt;0.001 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> CAP </td>
   <td style="text-align:center;"> 346 [299;387] </td>
   <td style="text-align:center;"> 330 [299;376] </td>
   <td style="text-align:center;"> 0.488 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> fibroscan </td>
   <td style="text-align:center;"> 5.90 [4.80;9.90] </td>
   <td style="text-align:center;"> 8.05 [4.97;10.4] </td>
   <td style="text-align:center;"> 0.166 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> nas </td>
   <td style="text-align:center;"> 1.00 [0.00;2.00] </td>
   <td style="text-align:center;"> 1.00 [0.00;3.75] </td>
   <td style="text-align:center;"> 0.411 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Esteatosis: </td>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;"> 0.150 </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 0 </td>
   <td style="text-align:center;"> 19 (38.8%) </td>
   <td style="text-align:center;"> 16 (38.1%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 1 </td>
   <td style="text-align:center;"> 13 (26.5%) </td>
   <td style="text-align:center;"> 12 (28.6%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 2 </td>
   <td style="text-align:center;"> 15 (30.6%) </td>
   <td style="text-align:center;"> 7 (16.7%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 3 </td>
   <td style="text-align:center;"> 2 (4.08%) </td>
   <td style="text-align:center;"> 7 (16.7%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> balonizacion: </td>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;"> 0.331 </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 0 </td>
   <td style="text-align:center;"> 42 (85.7%) </td>
   <td style="text-align:center;"> 31 (73.8%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 1 </td>
   <td style="text-align:center;"> 6 (12.2%) </td>
   <td style="text-align:center;"> 8 (19.0%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 2 </td>
   <td style="text-align:center;"> 1 (2.04%) </td>
   <td style="text-align:center;"> 3 (7.14%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> inflamacion: </td>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;"> 0.268 </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 0 </td>
   <td style="text-align:center;"> 35 (71.4%) </td>
   <td style="text-align:center;"> 24 (57.1%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 1 </td>
   <td style="text-align:center;"> 12 (24.5%) </td>
   <td style="text-align:center;"> 12 (28.6%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 2 </td>
   <td style="text-align:center;"> 2 (4.08%) </td>
   <td style="text-align:center;"> 4 (9.52%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;padding-left: 2em;" indentlevel="1"> 3 </td>
   <td style="text-align:center;"> 0 (0.00%) </td>
   <td style="text-align:center;"> 2 (4.76%) </td>
   <td style="text-align:center;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> fibrosis </td>
   <td style="text-align:center;"> 0.00 [0.00;0.00] </td>
   <td style="text-align:center;"> 0.00 [0.00;1.00] </td>
   <td style="text-align:center;"> 0.046 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> fibrosis_SiNo </td>
   <td style="text-align:center;"> 9 (18.8%) </td>
   <td style="text-align:center;"> 16 (36.4%) </td>
   <td style="text-align:center;"> 0.096 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> fib.avanz </td>
   <td style="text-align:center;"> 0 (0.00%) </td>
   <td style="text-align:center;"> 4 (9.09%) </td>
   <td style="text-align:center;"> 0.049 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> at.risk.nash </td>
   <td style="text-align:center;"> 1 (2.04%) </td>
   <td style="text-align:center;"> 5 (11.9%) </td>
   <td style="text-align:center;"> 0.091 </td>
  </tr>
</tbody>
</table>
```
:::
:::

::: cell
::: cell-output-display
```{=html}
<table class="table table-striped" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:right;"> optimal_cutpoint </th>
   <th style="text-align:right;"> acc </th>
   <th style="text-align:right;"> sensitivity </th>
   <th style="text-align:right;"> specificity </th>
   <th style="text-align:right;"> AUC </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 9.9 </td>
   <td style="text-align:right;"> 0.71 </td>
   <td style="text-align:right;"> 0.8 </td>
   <td style="text-align:right;"> 0.7 </td>
   <td style="text-align:right;"> 0.78 </td>
  </tr>
</tbody>
</table>
```
:::

::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown/unnamed-chunk-23-1.png)
:::
:::

#### FIB4\> 0.89, LSM\>= 9.9 kPa {#fib4-0.89-lsm-9.9-kpa number="4.2.2.2"}

::: cell
::: cell-output-display
![](20221214-algoritmoNASH_md_files/figure-markdown//vtree004.png){width="2000"}
:::
:::

# BIBLIOGRAFIA {#bibliografia .unnumbered number="5"}
