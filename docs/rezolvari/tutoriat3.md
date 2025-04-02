---
sidebar_position: 3
title: Limbaje neregulate. Lema de pompare
---

## Exercițiul E:

Soluție punctul d:
Presupunem că $D$ este regulat ($D \in REG$).

Fie $p \in REG$ lungimea pompării (numărul de stări din automat) și $s \in D$ a.î. $|s| > p$, $s = a^p b^p c^p$.
Din lema de pompare $\implies s = xyz$ a.î. $\forall i \geq 0$, cuvântul $xy^i z \in D$.

Din condiția 3 a lemei de pompare, $|xy| \leq p$, deci $x$ și $y$ conțin doar simboluri $a$. Vom lua $x = a^k, k \leq p$, $y = a^t, t > 0$, $z = a^{p-k-t} b^p c^p$.

Luăm $i = 2$. Atunci, $xy^2 z = xyyz = a^k a^{2t} a^{p-k-t} b^p c^p = a^{p+t} b^p c^p$.
Acest cuvânt nu mai este de forma $a^n b^n c^n$, deoarece numărul de $a$ este diferit de numărul de $b$ și $c$. Astfel, $xy^2 z \notin D \implies D \notin REG$.

e. $E = \{ w w^R \mid w \in \{ a, b \}^* \}$, unde $w^R$ este oglinditul lui $w$.

Solutie punctul e:

Presupunem că $E$ este regulat ($E \in REG$).

Fie $p \in REG$ lungimea pompării (nr de stari din automat) și $s \in E$ a.î. $|s| > p$, $s = w w^R$, unde $w = a^p b$.
Astfel, $s = a^p bb a^p$. Din lema de pompare $\implies s = xyz$ a.î. $\forall i \geq 0$, cuvântul $xy^iz \in E$.

Din condiția 3 a lemei de pompare, $|xy| \leq p$, deci vom lua $x = a^k, k \leq p$, $y = a^t, t > 0$, $z = a^{p-k-t} bb a^p$.

Luăm $i = 2$. Atunci, $xy^2 z = xyyz = a^k a^{2t} a^{p-k-t} bb a^p = a^{p+t} bb a^p$.
Acest cuvânt nu mai este de forma $w w^R$, deoarece $p + t \neq p$. Astfel, $xy^2 z \notin E \implies E \notin REG$.
