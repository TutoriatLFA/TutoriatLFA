
## Exerciții cu Automate Finite Deterministe (DFA)

### 1. Construcție DFA pentru cuvinte specifice
1. Proiectați un DFA care acceptă **exact** cuvântul: `finit`.  
2. Construiți un DFA care acceptă **fie** cuvântul `finit`, **fie** cuvântul `final`.  
3. Proiectați un DFA care recunoaște oricare dintre cuvintele: `finit`, `final` sau `limbaj`.

---

### 2. DFA pentru subșiruri specificate (alfabet: ${0,1}$)
1. Construiți un DFA care acceptă toate cuvintele ce conțin **subșirul** `0`.  
2. Proiectați un DFA pentru cuvinte care includ **subșirul** `00`.  
3. Sintezați un DFA care identifică cuvintele cu **subșirul** `101`.

---

### 3. DFA pentru sufixe specificate (alfabet: ${0,1}$)
1. Construiți un DFA care acceptă cuvinte care **se termină cu** `1`.  
2. Proiectați un DFA care recunoaște cuvinte cu **sufixul** `11`.

---

### 4. DFA pentru verificarea divizibilității
Proiectați un DFA care analizează reprezentarea binară a unui număr și acceptă **doar** numerele divizibile cu $8$.

---

### 5. DFA pentru operații pe limbaje
Construiți un DFA care acceptă **reuniunea** limbajelor:  
- $L_1 = \{ (ab)^n \mid n \geq 0 \}$  
- $L_2 = \{ b^n \mid n \geq 0 \}$

### 6. NFA pentru operații pe limbaje
Construiți un $\lambda\ NFA care acceptă **reuniunea** limbajelor:  
- $L_1 = \{ (ab)^n \mid n \geq 0 \}$  
- $L_2 = \{ b^n \mid n \geq 0 \}$