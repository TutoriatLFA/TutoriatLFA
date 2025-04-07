---
sidebar_position: 5
---

# Proprietăți ale Limbajelor Formale

1. Fie $L_1=\{a^n b^n \mid n \geq 0\}$ și $L_2 = \varSigma^* \implies L_1 \cup L_2 = \varSigma^* \implies L_3 = \varSigma^*$. Deci afirmatia este **Falsă**.  

2. Deoarece $L_1 \in \text{REG}$ și $L_2 \in \text{REG}$, deci $L_1 \cup L_2 \in \text{REG}$.
   Așadar, $L_3 = \varSigma^* \setminus (L_1 \cup L_2) \in \text{REG} = \overline{L_1 \cup L_2} $ (complementul unui limbaj regulat este un limbaj regulat). Deci afirmatia este **Adevărată**.
