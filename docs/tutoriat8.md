--- 
sidebar_position: 9 
---

# Gramatici Independente de Context (GIC)

O **gramatică independentă de context (GIC)**, cunoscută și sub denumirea de **Context-Free Grammar (CFG)**, este un tip de gramatică formală în care regulile de producție au o structură specifică. Mai exact, fiecare regulă de producție este de forma:

$A \rightarrow \alpha$

Unde:

- $A$ este un singur simbol neterminal (o variabilă).
- $\alpha$ este un șir (posibil vid) format din simboluri terminale și/sau neterminale.

Cu alte cuvinte, partea stângă a unei producții într-o GIC este întotdeauna un singur neterminal, iar partea dreaptă poate fi orice combinație de terminale și neterminale, inclusiv șirul vid ($\lambda$). Această restricție asupra părții stângi este ceea ce le diferențiază de gramaticile sensibile la context sau cele libere.

## Cum Funcționează GIC: Exemple Practice

Pentru a ilustra concret modul în care gramaticile independente de context definesc limbaje, vom explora o serie de exemple. În fiecare caz, vom vedea limbajul țintă și regulile de producție ale GIC corespunzătoare.

## Exemple de GIC și Limbajele Generate

Iată câteva exemple de limbaje și gramaticile independente de context care le generează:

1. $L = \{a^n b^n \mid n \geq 0\}$

   $S \rightarrow aSb \mid \lambda$

   Pentru a genera cuvântul $a^3b^3$:
   $S \Rightarrow aSb \Rightarrow aaSbb \Rightarrow aaaSbbb \Rightarrow aa\lambda bbb \Rightarrow a^3b^3$

2. $L = \{a^n b^n \mid n \geq 1\}$

   $S \rightarrow aSb \mid ab$

3. $L = \{ a^{2n} b^{3k} c^k d^n \mid n, k \geq 0 \}$

   $$
   \begin{align*}
   S &\rightarrow aa S d \mid X \\
   X &\rightarrow bbb X c \mid \lambda
   \end{align*}
   $$

   $\Rightarrow aa (bbb \lambda c) d$
   $\Rightarrow aa bbb c d$

## Exercitii

1. $L = \{ ww^R \mid w \in \{a,b\}^* \}$

2. $L = \{0^{2k}1^{3k}0^{5k'} \mid k, k' \geq 2\}$

3. Considerați limbajul $L = \{a^{2n+1}b^{m+2}a^n \mid m, n \geq 0\}$

4. Considerați limbajul $L = \{a^{m+n}b^k a^{m+k}b^l \mid k, m, n, l \geq 1\}$

5. Se dă următoarea gramatică independentă de context:
   $S \rightarrow SS \mid aSa \mid bSb \mid AS \mid \lambda$
   Să se aducă această gramatică la Forma Normală Chomsky.

## Pași pentru Conversia GIC în FNC (Forma Normală Chomsky)

**Pasul 1: Eliminarea Simbolului de Start din Partea Dreaptă (RHS)**
Dacă simbolul de start $S$ apare în partea dreaptă a oricărei producții din gramatică, creați o nouă producție de forma: $S_0 \rightarrow S$, unde $S_0$ este noul simbol de start.

### Pasul 2: Eliminarea Producțiilor Nule, Unitare și Inutile

- Producții Nule ($\epsilon$): Dacă o regulă conține $\epsilon$, eliminați-l modificând corespunzător celelalte reguli.
- Producții Unitare: Dacă o regulă are un singur neterminal în partea dreaptă (de ex., $A \rightarrow B$), înlocuiți-o cu producțiile lui $B$.
- Producții Inutile: Eliminați simbolurile neatinsibile sau negeneratoare din gramatică.

**Pasul 3: Înlocuirea Terminalelor în Producțiile Mixte**
Eliminați terminalele din partea dreaptă dacă acestea există împreună cu alte terminale sau neterminale. De exemplu, regula de producție $X \rightarrow xY$ poate fi descompusă astfel: $X \rightarrow ZY$, $Z \rightarrow x$.

**Pasul 4: Reducerea Producțiilor cu Mai Mult de Două Neterminale**
Eliminați partea dreaptă cu mai mult de două neterminale. De exemplu, regula de producție $X \rightarrow XYZ$ poate fi descompusă astfel: $X \rightarrow PZ$, $P \rightarrow XY$.

**Exemplu: Conversia unei GIC în FNC**
Să luăm un exemplu pentru a converti o GIC în FNC. Considerați gramatica dată $G_1$:

$S \rightarrow ASB$

$A \rightarrow aAS \mid a \mid \epsilon$

$B \rightarrow SbS \mid A \mid bb$

**Pasul 1.**
Deoarece simbolul de start $S$ apare în partea dreaptă, vom crea o nouă regulă de producție $S_0 \rightarrow S$. Prin urmare, gramatica va deveni:

$S_0 \rightarrow S$

$S \rightarrow ASB$

$A \rightarrow aAS \mid a \mid \epsilon$

$B \rightarrow SbS \mid A \mid bb$

**Pasul 2.**
Deoarece gramatica conține producția nulă $A \rightarrow \epsilon$, eliminarea acesteia din gramatică produce:

$S_0 \rightarrow S$

$S \rightarrow ASB \mid SB$

$A \rightarrow a \mid aAS \mid aS$

$B \rightarrow SbS \mid A \mid \epsilon \mid bb$

Acum, se creează producția nulă $B \rightarrow \epsilon$, eliminarea acesteia din gramatică produce:

$S_0 \rightarrow S$

$S \rightarrow AS \mid S \mid ASB \mid SB$

$A \rightarrow a \mid aAS \mid aS$

$B \rightarrow SbS \mid A \mid bb$

Acum, se creează producția unitară $B \rightarrow A$, eliminarea acesteia din gramatică produce:

$S_0 \rightarrow S$

$S \rightarrow AS \mid ASB \mid SB \mid S$

$A \rightarrow a \mid aAS \mid aS$

$B \rightarrow SbS \mid bb \mid aAS \mid aS \mid a$

De asemenea, eliminarea producției unitare $S_0 \rightarrow S$ din gramatică produce:

$S_0 \rightarrow AS \mid ASB \mid SB \mid S$

$S \rightarrow AS \mid ASB \mid SB \mid S$

$A \rightarrow aAS \mid aS \mid a$

$B \rightarrow SbS \mid bb \mid aAS \mid aS \mid a$

De asemenea, eliminarea producțiilor unitare $S \rightarrow S$ și $S_0 \rightarrow S$ din gramatică produce:

$S_0 \rightarrow AS \mid ASB \mid SB$

$S \rightarrow AS \mid ASB \mid SB$

$A \rightarrow aAS \mid aS \mid a$

$B \rightarrow SbS \mid bb \mid aAS \mid aS \mid a$

**Pasul 3.**
În regulile de producție $A \rightarrow aAS \mid aS$ și $B \rightarrow SbS \mid aAS \mid aS$, terminalele $a$ și $b$ există în partea dreaptă împreună cu neterminale. Eliminându-le din partea dreaptă:

$S_0 \rightarrow AS \mid ASB \mid SB$

$S \rightarrow AS \mid ASB \mid SB$

$A \rightarrow XAS \mid XS \mid a$

$B \rightarrow SYS \mid bb \mid XAS \mid XS \mid a$

$X \rightarrow a$

$Y \rightarrow b$

De asemenea, $B \rightarrow bb$ nu poate face parte din FNC, eliminându-l din gramatică produce:

$S_0 \rightarrow AS \mid ASB \mid SB$

$S \rightarrow AS \mid ASB \mid SB$

$A \rightarrow XAS \mid XS \mid a$

$B \rightarrow SYS \mid YY \mid XAS \mid XS \mid a$

$X \rightarrow a$

$Y \rightarrow b$

**Pasul 4:**
În regula de producție $S_0 \rightarrow ASB$, $S \rightarrow ASB$, partea dreaptă are mai mult de două simboluri, eliminându-le din gramatică produce:

$S_0 \rightarrow AS \mid PB \mid SB$

$S \rightarrow AS \mid PB \mid SB$

$A \rightarrow XAS \mid XS \mid a$

$B \rightarrow SYS \mid YY \mid XAS \mid XS \mid a$

$X \rightarrow a$

$Y \rightarrow b$

$P \rightarrow AS$

Similar, $A \rightarrow XAS$ are mai mult de două simboluri, eliminându-l din gramatică produce:

$S_0 \rightarrow AS \mid PB \mid SB$

$S \rightarrow AS \mid PB \mid SB$

$A \rightarrow RS \mid XS \mid a$

$B \rightarrow SYS \mid YY \mid RS \mid XS \mid a$

$X \rightarrow a$

$Y \rightarrow b$

$P \rightarrow AS$

$R \rightarrow XA$

Similar, $B \rightarrow SYS$ are mai mult de două simboluri, eliminându-l din gramatică produce:

$S_0 \rightarrow AS \mid PB \mid SB$

$S \rightarrow AS \mid PB \mid SB$

$A \rightarrow RS \mid XS \mid a$

$B \rightarrow TS \mid YY \mid RS \mid XS \mid a$

$X \rightarrow a$

$Y \rightarrow b$

$P \rightarrow AS$

$R \rightarrow XA$

$T \rightarrow SY$

Deci aceasta este FNC-ul necesar pentru gramatica dată.

## Exercitii FNC

1. Se dă următoarea gramatică independentă de context:
   $S \rightarrow SS \mid aSa \mid bSb \mid AS \mid \lambda$
   Să se aducă această gramatică la Forma Normală Chomsky.
