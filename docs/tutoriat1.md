
# DFA/NFA

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
1. Construiți un DFA care acceptă **reuniunea** limbajelor:  
    - $L_1 = \{ (ab)^n \mid n \geq 0 \}$  
    - $L_2 = \{ b^n \mid n \geq 0 \}$
2. Construiți un DFA care acceptă **intersecția** limbajelor:
    - $L_1 = \{ a^n b^m \mid n \geq 2, m \geq 1 \}$  
    - $L_2 = \{ a ^n b^m \mid n \geq 1, m \geq 0\}$

### 6. NFA pentru operații pe limbaje
Construiți un $\lambda$-NFA care acceptă **concatenarea** limbajelor:  
- $L_1 = \{ (ab)^n \mid n \geq 0 \}$  
- $L_2 = \{ c^n \mid n \gt 0 \}$

### 7. NFA pentru verificarea subșirului
Construiți un NFA care verifică dacă, într-o propoziție dată, cuvintele `"ana"` și `"mere"` apar în această ordine (nu neapărat consecutive).

### 9. Construcție Lambda-NFA pentru verificarea formei cuvintelor
Să se construiască un $\lambda$-NFA care verifică dacă cuvântul primit este de forma:  
$$
L_1 = \{a+b==c \mid a \in L_2, b \in L_2, c \in L_2\},  
$$  
unde:  
$$
L_2 = \{1 \sdot \{1, 0\}^*\},  
$$  
iar alfabetul este $\{1, 0, +, =\}$.  

**Exemple de cuvinte acceptate**:  
- `110+10==1110`  
- `1+0+100==101`  
