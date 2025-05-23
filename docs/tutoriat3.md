---
sidebar_position: 4
---

# Limbaje neregulate. Lema de pompare

## Cuprins

- [A. Limbaje neregulate](#a-limbaje-neregulate)
- [B. Lema de pompare - enunț](#b-lema-de-pompare---enunț)
- [C. Utilizarea lemei de pompare](#c-utilizarea-lemei-de-pompare)
- [D. Încă un exemplu](#d-încă-un-exemplu)
- [E. Exerciții](#e-exerciții)

---

## A. Limbaje neregulate

Un limbaj regulat este, prin definiție, acceptat de un automat finit. Cu toate acestea, există limbaje neregulate, adică cele care nu sunt acceptate de niciun astfel de automat.

### Exemple de limbaje neregulate

A = $\{ 0^n 1^n \mid n \geq 0 \}$

B = $\{ w \mid w \in \{0,1\}^*, w \text{ nu e palindrom} \}$

## B. Lema de pompare - enunț

Dacă A este limbaj regulat, atunci există un număr $p > 0$ astfel încât fiecare cuvânt $s$ din $A$ cu lungimea cel puțin $p$ poate fi rescris ca $s = xyz$, respectând următoarele condiții:

1. Oricare $i \geq 0$, $xy^i z \in A$,
2. $|y| > 0$,
3. $|xy| \leq p$.

Astfel, $x$ sau $z$ pot fi $\lambda$, însă, din 2, rezultă că $y$ nu poate fi niciodată $\lambda$. Dacă ar lipsi condiția 2, lema ar fi întotdeauna adevărată, indiferent de natura limbajului.

## C. Utilizarea lemei de pompare

În general, dacă ne propunem să demonstrăm că un limbaj este regulat, îl transformăm în automat finit.

Lema de pompare este utilizată atunci când trebuie să demonstrăm că un limbaj este neregulat. În continuare, vom folosi ca exemplu limbajul $A = \{ 0^n 1^n \mid n \geq 0 \}$, trecând prin toți pașii demonstrației.

### Pasul 1. Presupunem, prin reducere la absurd, că A este regulat.

### Pasul 2. Verificăm îndeplinirea condițiilor lemei.

Fie $p$ lungimea pompării. Alegem $s = 0^p 1^p$. Întrucât $s$ aparține limbajului $A$ și are lungimea mai mare decât $p$, putem rescrie $s$ ca $s = xyz$, unde, oricare $i \geq 0$, $xy^i z$ aparține lui $A$.

#### Cazul 1. y conține doar 0.

În acest caz, $xy^2 z = xyyz$ conține mai mulți 0 decât 1. Așadar, acest cuvânt nu aparține lui $A$, deci prima condiție nu este îndeplinită. Prin urmare, acest caz determină o contradicție.

Observăm, din a treia condiție a lemei de pompare, că acesta este singurul caz valid. Lungimea lui $xy$ trebuie să fie mai mică sau egală cu p, iar primele p caractere din cuvântul ales $s$ sunt 0. Prin urmare, $y$ poate fi doar o succesiune de 0.

### Pasul 3. Concluzia

Din cazul analizat anterior reiese că aplicarea condițiilor impuse de lema de pompare pe limbajul dat rezultă într-o contradicție. Prin urmare, limbajul $A$ nu este regulat.

## D. Încă un exemplu

Fie limbajul $B = \{ 0^{n^2} \mid n \geq 0 \}$. Este acesta regulat?

Presupunem că $B$ este regulat.

Fie $p$ lungimea pompării și $s$ un cuvânt din $B$, $s = 0^{p^2}$. Deoarece $s$ aparține lui $B$ și $s$ are lungimea cel puțin egală cu $p$, $s$ poate fi împărțit: $s = xyz$. Oricare $i \geq 0$, cuvântul $xy^i z$ aparține lui $B$.
Luăm $xyz$ și $xy^2 z = xyyz$ din $B$. Lungimile acestora diferă prin lungimea lui $y$. Din condiția 3 a lemei de pompare, $|xy| \leq p$, deci $|y| \leq p$. Avem $|xyz| = p^2$, iar $|xy^2 z| \leq p^2 + p$. Dar $p^2 + p < p^2 + p + 1 = (p + 1)^2$.

În plus, din condiția 2 rezultă că, $y$ fiind nevid, $|xy^2 z| > p^2$. Astfel, lungimea lui $xy^2 z$ este între $p^2$ și $(p+1)^2$, deci nu este pătrat perfect. Așadar, $xy^2 z$ nu aparține lui $B$.

În concluzie, $B nu este regulat.

## E. Exerciții

Demonstrați că următoarele limbaje sunt neregulate:

a. $A = \{ 0^{2^n} \mid n \geq 0 \}$

b. $B = \{ 1^n \mid n \text{ este prim} \}$

c. $C = \{ a^k w c w \mid w \in \{ a, b, c \}^*, k \geq 4 \}$

d. $D = \{ a^n b^n c^n \mid n \geq 1 \}$

e. $E = \{ w w^R \mid w \in \{ a, b \}^* \}$, unde $w^R$ este oglinditul lui $w$.

f. $F = \{a^n b^m \mid 10 < n < m \}$
