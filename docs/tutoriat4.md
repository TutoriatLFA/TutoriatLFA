---
sidebar_position: 5
---

# Proprietăți ale Limbajelor Formale

1. Fie limbajele $L_1, L_2, L_3$ cu proprietatea că $L_1 \cup L_2 = L_3$ și $L_2, L_3 \in \text{REG}$. Este adevărat că $L_1 \in \text{REG}$? Unde $\text{REG}$ este familia limbajelor regulate.

2. Fie limbajele $L_1$ și $L_2$ astfel încât $L_1 \cap L_2 = \emptyset$ și $L_1, L_2 \in \text{REG}$. Deci $L_3 = \Sigma^* \setminus (L_1 \cup L_2)$ este de asemenea regulat.
Afirmația este **ADEVARATĂ/FALSĂ** (încercuiți varianta corectă și apoi justificați răspunsul).

3. Fie $L_1, L_2 \in \text{REG}$. Demonstrați sau infirmați următoarea afirmație: dacă $L_1 \cdot L_2 = \Sigma^*$, atunci $L_1 = \Sigma^*$ sau $L_2 = \Sigma^*$.

4. Fie limbajele $L_1, L_2, L_3$ cu proprietatea că $L_1 \cap L_2 = L_3$ și $L_2, L_3 \in \text{REG}$. Avem așadar că $L_1 \in \text{REG}$? Unde $A$ reprezintă complementul lui $A$.  
Afirmația este **ADEVARATĂ/FALSĂ** (încercuiți varianta corectă și apoi justificați răspunsul).

5. Fie limbajele $L_1, L_2, L_3$ cu proprietatea că $L_1 - L_2 = L_3$ și $L_2, L_3 \in \text{REG}$.  
Avem așadar că $L_1 \in \text{REG}$? Unde $\text{REG}$ este familia limbajelor regulate (recunoscute de expresii regulate). $A - B$ este diferența pe mulțimi.  
Afirmația este **ADEVARATĂ/FALSĂ** (încercuiți varianta corectă și apoi justificați răspunsul).

6. Fie $L$ un limbaj regulat. Demonstrați că limbajul $\text{Prefix}(L) = \{x \mid \exists y \text{ astfel încât } xy \in L\}$ este, de asemenea, un limbaj regulat.

7. Fie limbajele $L_1, L_2, L_3, L_4$ cu proprietatea că $L_1 \cap \overline{L_2} = L_3 \cup L_4$ și $L_2, L_3, L_4 \in \text{REG}$.  
Avem așadar că $L_1 \in \text{REG}$? Unde $\overline{A}$ reprezintă complementul lui $A$.  
Afirmația este **ADEVARATĂ/FALSĂ** (încercuiți varianta corectă și apoi justificați răspunsul).

8. Fie limbajele $L_1, L_2$ cu proprietatea că $L_1 \subseteq L_2$ și $L_1 \in \text{REG}$. Avem așadar că $L_2 \in \text{REG}$? Unde $\text{REG}$ este familia limbajelor regulate.

7. Demonstrați că familia limbajelor regulate (REG) este închisă la concatenare (dacă $L_1, L_2 \in \text{REG}$, atunci $L_1 \cdot L_2 \in \text{REG}$).

8. Fie $L$ un limbaj regulat. Este complementul său $L'$ (definit ca $\Sigma^* \setminus L$) regulat? Demonstrați sau contraziceți.

9. Fie $L_1, L_2 \in \text{REG}$. Este diferența $L_1 \setminus L_2$ (definită ca $L_1 \cap L_2'$) regulată? Justificați folosind proprietățile de închidere ale REG.

10. Fie limbajele $L_1, L_2, L_3, L_4$ cu proprietatea că $L_1 \cup L_2 = L_3 \cap L_4$ și $L_2, L_3, L_4 \in \text{REG}$. Este $L_1 \in \text{REG}$?

11. Fie limbajele $L_1, L_2, L_3$ cu proprietatea că $L_1 \setminus L_2 = L_3$ și $L_2, L_3 \in \text{REG}$. Este $L_1 \in \text{REG}$?

12. Este decidabil dacă limbajele acceptate de două AFD-uri sunt egale? Justificați pe scurt.
