---
sidebar_position: 3
---

# Transformări de Automate și Verificarea Acceptării

## Cuprins

- [A. Transformarea AFN → AFN](#a-transformarea-afn--afd)
- [B. Verificarea Acceptării Cuvintelor](#b-verificarea-acceptării-cuvintelor)
- [C. Lucrul cu λ-Tranziții](#c-lucrul-cu-λ-tranziții)

---

## A. Transformarea AFN → AFD

### Pas 1: Algoritmul Subseturilor

#### Definiții și Principii:

- **Stările AFD** = submulțimi de stări AFN
- **Tranzițiile** se calculează ca reuniuni de tranziții AFN
- **Stări finale în AFD** = submulțimile care conțin cel puțin o stare finală din AFN

#### Exemplu Pas cu Pas:

Fie următorul AFN:

| **Component**  | **Detalii**                                                                                                                                                                                                                                         |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stări          | q0, q1, q2                                                                                                                                                                                                                                          |
| Alfabet        | \{a, b\}                                                                                                                                                                                                                                            |
| Tranziții      | $\delta(q0, \mathrm{a}) = \{q0, q1\}$ <br/> $\delta(q0, \mathrm{b}) = \{q0\}$ <br/> $\delta(q1, \mathrm{a}) = \emptyset$ <br/> $\delta(q1, \mathrm{b}) = \{q2\}$ <br/> $\delta(q2, \mathrm{a}) = \{q2\}$ <br/> $\delta(q2, \mathrm{b}) = \emptyset$ |
| Stare inițială | q0                                                                                                                                                                                                                                                  |
| Stări finale   | $\{q2\}$                                                                                                                                                                                                                                            |

**Tabel de tranziții pentru AFN:**

| AFN | a           | b           |
| --- | ----------- | ----------- |
| q0  | $\{q0,q1\}$ | $\{q0\}$    |
| q1  | $\emptyset$ | $\{q2\}$    |
| q2  | $\{q2\}$    | $\emptyset$ |

#### Construirea AFD:

1. Începem cu starea inițială din AFN: $\{q0\}$
2. Calculăm tranzițiile:

   | Stare AFD        | Cu simbolul a    | Cu simbolul b |
   | ---------------- | ---------------- | ------------- |
   | $\{q0\}$         | $\{q0, q1\}$     | $\{q0\}$      |
   | $\{q0, q1\}$     | $\{q0, q1\}$     | $\{q0, q2\}$  |
   | $\{q0, q2\}$     | $\{q0, q1, q2\}$ | $\{q0\}$      |
   | $\{q0, q1, q2\}$ | $\{q0, q1, q2\}$ | $\{q0, q2\}$  |

3. Stările AFD:
   - A = $\{q0\}$
   - B = $\{q0, q1\}$
   - C = $\{q0, q2\}$ (stare finală)
   - D = $\{q0, q1, q2\}$ (stare finală)

**Tabel de tranziții pentru AFD:**

| AFD              | a   | b   |
| ---------------- | --- | --- |
| A=$\{q0\}$       | B   | A   |
| B=$\{q0,q1\}$    | B   | C   |
| C=$\{q0,q2\}$    | D   | A   |
| D=$\{q0,q1,q2\}$ | D   | C   |

**Exercițiu 1:**

Transformați următorul AFN în AFD:

- Stări: p, q, r
- Alfabet: $\{a, b\}$
- Tranziții:
  - $\delta(p, \mathrm{a}) = \{p, q\}$
  - $\delta(p, \mathrm{b}) = \{p\}$
  - $\delta(q, \mathrm{a}) = \{r\}$
  - $\delta(q, \mathrm{b}) = \emptyset$
  - $\delta(r, \mathrm{a}) = \emptyset$
  - $\delta(r, \mathrm{b}) = \{q\}$
- Stare inițială: p
- Stări finale: $\{r\}$

**Exercițiu 2:**

Transformați în AFD următorul AFN:

- Stări: s, t, u
- Alfabet: $\{0, 1\}$
- Tranziții:
  - $\delta(s, 0) = \{s, t\}$
  - $\delta(s, 1) = \{s\}$
  - $\delta(t, 0) = \emptyset$
  - $\delta(t, 1) = \{u\}$
  - $\delta(u, 0) = \{u\}$
  - $\delta(u, 1) = \emptyset$
- Stare inițială: s
- Stări finale: $\{u\}$

**Exercițiu 3:**
Explicați diferențele posibile în stările intermediare ale AFD rezultat atunci când alfabetul conține mai mult de două simboluri.

**Exercițiu 4:**
Construiți un AFN cu trei stări și transformați-l în AFD, evidențiind care submulțimi din AFD sunt stări finale.

---

## B. Verificarea Acceptării Cuvintelor

### Pas 1: Procesul de Acceptare în AFD

#### Principii de bază:

- Urmărim un singur drum posibil
- Acceptăm cuvântul dacă ajungem într-o stare finală după consumarea întregului input

#### Exemplu 1:

Fie un AFD cu stări $\{S, T, U\}$, starea inițială S și stări finale $\{U\}$:

- $\delta(S, \mathrm{a}) = T$
- $\delta(S, \mathrm{b}) = S$
- $\delta(T, \mathrm{a}) = U$
- $\delta(T, \mathrm{b}) = S$
- $\delta(U, \mathrm{a}) = U$
- $\delta(U, \mathrm{b}) = T$

**Verificare "bba":**

1. Pornire din S
2. Citire b: S → S
3. Citire b: S → S
4. Citire a: S → T
5. Final: T (nu este stare finală) → cuvântul nu este acceptat

#### Exemplu 2:

**Verificare "babbaba":**

1. Pornire din S
2. b: S → S
3. a: S → T
4. b: T → S
5. b: S → S
6. a: S → T
7. b: T → S
8. a: S → T
9. Final: T (nu este stare finală) → cuvântul nu este acceptat

**Exercițiu:**

Comparați procesul de acceptare pentru cuvântul "aba" pe AFD și AFN de mai sus.

**Exercițiu 2:**
Scrieți un cuvânt de lungime minimă care este respins de AFD-ul de mai sus și precizați traseul de parcurgere a stărilor.

**Exercițiu 3:**
Propuneți un AFD care acceptă doar cuvintele care conțin cel puțin două litere consecutive identice și justificați de ce alte cuvinte sunt respinse.

## C. Lucrul cu λ-Tranziții

### Pas 1: λ-Închideri

#### Definiție:

λ-închiderea unui set de stări Q este mulțimea tuturor stărilor accesibile din Q folosind doar λ-tranziții, inclusiv stările din Q.

#### Formula λ-închiderii:

Pentru o stare q:

- $\lambda^*(q)$ include q
- Dacă $p \in \lambda^*(q)$ și există o λ-tranziție de la p la r, atunci $r \in \lambda^*(q)$

#### Exemplu de calcul:

Fie un AFN-λ cu stările $\{q0, q1, q2, q3, q4, q5, q6\}$ și λ-tranziții:

- $\lambda(q0) = \{q2, q3\}$
- $\lambda(q2) = \{q4\}$
- $\lambda(q3) = \{q5, q6\}$
- $\lambda(q4) = \lambda(q5) = \lambda(q6) = \lambda(q1) = \emptyset$

λ-închiderea lui q0 este:

- $\lambda^*(q0) = \{q0, q2, q3, q4, q5, q6\}$

**Exercițiu 6:**

Calculați λ-închiderile pentru toate stările din următorul AFN-λ:

- Stări: $\{s, t, u, v\}$
- λ-tranziții:
  - $\lambda(s) = \{t\}$
  - $\lambda(t) = \{u\}$
  - $\lambda(u) = \{v\}$
  - $\lambda(v) = \emptyset$

**Exercițiu 7:**
Modelați un AFN-λ care să aibă tranziții λ multiple plecând din aceeași stare și descrieți λ-închiderile.

**Exercițiu 8:**
Construiți un AFN-λ care acceptă doar cuvintele de formă $(ab)^n$ și arătați concret etapele transformării în AFN fără λ.

### Pas 2: Transformarea AFN-λ → AFN

#### Etape:

1. **λ-Completion:** Adăugarea tranzițiilor simulate

   - Pentru fiecare stare q și simbol a:
   - $\delta'(q, a) = \delta(q, a) \cup \left(\bigcup_{p \in \lambda^*(q)} \delta(p, a)\right)$

2. **λ-Transition Removal:** Eliminarea λ-tranzițiilor

3. **Final State Adjustment:** O stare q devine finală dacă $\lambda^*(q)$ conține vreo stare finală din AFN-λ

#### Exemplu:

Fie un AFN-λ cu stările $\{q0, q1, q2\}$, starea inițială q0, stare finală q2 și tranzițiile:

- $\delta(q0, \mathrm{a}) = \{q1\}$
- $\delta(q0, \lambda) = \{q2\}$
- $\delta(q1, \mathrm{b}) = \{q2\}$
- $\delta(q2, \mathrm{a}) = \{q0\}$

**Calculul λ-închiderilor:**

- $\lambda^*(q0) = \{q0, q2\}$
- $\lambda^*(q1) = \{q1\}$
- $\lambda^*(q2) = \{q2\}$

**Tranzițiile în AFN rezultat:**

- $\delta'(q0, \mathrm{a}) = \{q1, q0\}$ (combinând $\delta(q0, \mathrm{a})$ și $\delta(q2, \mathrm{a})$)
- $\delta'(q0, \mathrm{b}) = \emptyset$
- $\delta'(q1, \mathrm{a}) = \emptyset$
- $\delta'(q1, \mathrm{b}) = \{q2\}$
- $\delta'(q2, \mathrm{a}) = \{q0\}$
- $\delta'(q2, \mathrm{b}) = \emptyset$

**Stări finale noi:** $\{q0, q2\}$ (deoarece $q2 \in \lambda^*(q0)$)

### Pas 3: Transformarea AFN-λ → AFD

#### Metodă directă:

1. Calculăm λ-închiderea stării inițiale pentru a obține starea inițială a AFD
2. Pentru fiecare stare nouă S a AFD și fiecare simbol a:
   - $\delta_{AFD}(S, \mathrm{a}) = \lambda^*\left(\bigcup_{q \in S} \delta_{AFN-\lambda}(q, \mathrm{a})\right)$

**Exercițiu Final:**

Transformați un AFN-λ în AFD folosind metoda directă:

- Stări: $\{w, x, y, z\}$
- Alfabetul: $\{0, 1\}$
- Tranziții:
  - $\delta(w, 0) = \{x\}$
  - $\delta(w, \lambda) = \{y\}$
  - $\delta(x, 1) = \{y\}$
  - $\delta(x, \lambda) = \{z\}$
  - $\delta(y, 0) = \{w\}$
  - $\delta(y, 1) = \{z\}$
  - $\delta(z, 1) = \{z\}$
- Stare inițială: w
- Stări finale: $\{z\}$
