# Transformări de Automate și Verificarea Acceptării

## A. Transformarea AFN → AFD (50 minute)

### Pas 1: Algoritmul Subseturilor

**Definiții:**

- Stările AFD = submulțimi de stări AFN.
- Tranzițiile se calculează ca reuniuni de tranziții AFN.

**Exemplu Pas cu Pas:**

Fie următorul AFN:

- Stări: q0, q1, q2
- Tranziții: 
  - $\delta(q0, a) = \{q0, q1\}$
  - $\delta(q0, b) = \{q0\}$
  - $\delta(q1, a) = \emptyset$
  - $\delta(q1, b) = \{q2\}$
  - $\delta(q2, a) = \{q2\}$
  - $\delta(q2, b) = \emptyset$
- Stare inițială: q0
- Stări finale: $\{q2\}$

**Construirea AFD:**

1. Începem cu starea inițială din AFN: $\{q0\}$
2. Calculăm tranzițiile:
   - $\delta(\{q0\}, a) = \{q0, q1\}$
   - $\delta(\{q0\}, b) = \{q0\}$
   - $\delta(\{q0, q1\}, a) = \{q0, q1\}$
   - $\delta(\{q0, q1\}, b) = \{q0, q2\}$
   - $\delta(\{q0, q2\}, a) = \{q0, q1, q2\}$
   - $\delta(\{q0, q2\}, b) = \{q0\}$
   - $\delta(\{q0, q1, q2\}, a) = \{q0, q1, q2\}$
   - $\delta(\{q0, q1, q2\}, b) = \{q0, q2\}$

3. Stările AFD:
   - A = $\{q0\}$
   - B = $\{q0, q1\}$
   - C = $\{q0, q2\}$
   - D = $\{q0, q1, q2\}$

4. Stări finale: C, D (conțin q2, care este stare finală în AFN)

**Tabel de tranziții:**

| AFN  | a      | b    |
|------|--------|------|
| q0   | $\{q0,q1\}$| $\{q0\}$ |
| q1   | $\emptyset$      | $\{q2\}$ |
| q2   | $\{q2\}$   | $\emptyset$    |

| AFD | a | b |
|-----|---|---|
| A=$\{q0\}$ | B | A |
| B=$\{q0,q1\}$ | B | C |
| C=$\{q0,q2\}$ | D | A |
| D=$\{q0,q1,q2\}$ | D | C |

**Exercițiu Interactiv:**

Transformați următorul AFN în AFD:
- Stări: p, q, r
- Alfabet: $\{a, b\}$
- Tranziții:
  - $\delta(p, a) = \{p, q\}$
  - $\delta(p, b) = \{p\}$
  - $\delta(q, a) = \{r\}$
  - $\delta(q, b) = \emptyset$
  - $\delta(r, a) = \emptyset$
  - $\delta(r, b) = \{q\}$
- Stare inițială: p
- Stări finale: $\{r\}$

## B. Verificarea Acceptării Cuvintelor (30 minute)

### Pas 1: Procesul de Acceptare în AFD

**Exemplu:** Verificarea cuvântului "bba" pe un AFD:

Fie un AFD cu stări $\{S, T, U\}$, starea inițială S și stări finale $\{U\}$:
- $\delta(S, a) = T$
- $\delta(S, b) = S$
- $\delta(T, a) = U$
- $\delta(T, b) = S$
- $\delta(U, a) = U$
- $\delta(U, b) = T$

Verificare "bba":
1. Pornire din S
2. Citire b: S → S
3. Citire b: S → S
4. Citire a: S → T
5. Final: T (nu este stare finală) → cuvântul nu este acceptat

**Exemplu:** Verificarea cuvântului "babbaba":
1. Pornire din S
2. b: S → S
3. a: S → T
4. b: T → S
5. b: S → S
6. a: S → T
7. b: T → S
8. a: S → T
9. Final: T (nu este stare finală) → cuvântul nu este acceptat

### Pas 2: Procesul de Acceptare în AFN

**Exemplu:** Verificarea cuvântului "bba" pe AFN:

Fie un AFN cu stări $\{q0, q1, q2\}$, starea inițială q0 și stări finale $\{q2\}$:
- $\delta(q0, b) = \{q0, q1\}$
- $\delta(q0, a) = \{q0\}$
- $\delta(q1, b) = \{q2\}$
- $\delta(q1, a) = \emptyset$
- $\delta(q2, b) = \emptyset$
- $\delta(q2, a) = \{q2\}$

Verificare "bba" (toate căile posibile):
1. Pornire din q0
2. Citire b: q0 → $\{q0, q1\}$
   - Din q0, citire b: → $\{q0, q1\}$
   - Din q1, citire a: → $\emptyset$ (cale blocată)
   - Din q0, citire a: → $\{q0\}$
3. Citire a: q0 → $\{q0\}$
4. Final: $\{q0\}$ (nu conține stare finală) → cuvântul nu este acceptat

**Exercițiu:**
Comparați procesul de acceptare pentru cuvântul "aba" pe AFD și AFN de mai sus.

## C. Lucrul cu λ-Tranziții (40 minute)

### Pas 1: λ-Închideri

**Definiție:** Mulțimea de stări accesibile dintr-o stare dată folosind doar λ-tranziții.

**Exemplu de calcul:**

Fie un AFN-λ cu stările $\{q0, q1, q2, q3, q4, q5, q6\}$ și λ-tranziții:
- $\lambda(q0) = \{q2, q3\}$
- $\lambda(q2) = \{q4\}$
- $\lambda(q3) = \{q5, q6\}$
- $\lambda(q4) = \lambda(q5) = \lambda(q6) = \lambda(q1) = \emptyset$

Atunci λ-închiderea lui q0 este:
- $\lambda^*(q0) = \{q0, q2, q3, q4, q5, q6\}$

**Exercițiu:**
Calculați λ-închiderea pentru fiecare stare dintr-un AFN-λ dat.

### Pas 2: Transformarea AFN-λ → AFN

**Etape:**

1. **λ-Completion:** Adăugarea tranzițiilor simulate.
   - Pentru fiecare stare q și simbol a, $\delta'(q, a) = \delta(q, a) \cup (\cup\{\delta(p, a) | p \in \lambda^*(q)\})$

2. **λ-Transition Removal:** Eliminarea λ-tranzițiilor.

**Exemplu:**
Fie un AFN-λ cu stările $\{q0, q1, q2\}$, starea inițială q0, stare finală q2 și tranzițiile:
- $\delta(q0, a) = \{q1\}$
- $\delta(q0, \lambda) = \{q2\}$
- $\delta(q1, b) = \{q2\}$
- $\delta(q2, a) = \{q0\}$

Transformare în AFN:
1. $\lambda^*(q0) = \{q0, q2\}$
2. $\lambda^*(q1) = \{q1\}$
3. $\lambda^*(q2) = \{q2\}$

Tranzițiile noi:
- $\delta'(q0, a) = \{q1, q0\}$ (deoarece $q2 \in \lambda^*(q0)$ și $\delta(q2, a) = \{q0\}$)
- $\delta'(q0, b) = \emptyset$
- $\delta'(q1, a) = \emptyset$
- $\delta'(q1, b) = \{q2\}$
- $\delta'(q2, a) = \{q0\}$
- $\delta'(q2, b) = \emptyset$

Stări finale noi: $\{q0, q2\}$ (deoarece $q2 \in \lambda^*(q0)$)

### Pas 3: Transformarea AFN-λ → AFD

**Subset Construction cu λ-Închideri:**

1. Starea inițială a AFD = λ-închiderea stării inițiale a AFN-λ.
2. Tranzițiile se calculează prin combinarea λ-închiderilor.

**Exemplu:**
Pentru AFN-λ-ul de mai sus:

1. Starea inițială în AFD: A = $\lambda^*(q0) = \{q0, q2\}$
2. Calculăm tranzițiile:
   - $\delta(A, a) = \lambda^*(\delta(q0, a) \cup \delta(q2, a)) = \lambda^*(\{q1, q0\}) = \{q0, q1, q2\}$
   - $\delta(A, b) = \lambda^*(\delta(q0, b) \cup \delta(q2, b)) = \lambda^*(\emptyset) = \emptyset$

Continuați construcția AFD-ului folosind acest algoritm.

**Exercițiu final:**
Transformați un AFN-λ în AFD folosind metoda directă (subseturi + λ-închideri).
