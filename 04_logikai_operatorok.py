"""
==	egyenlő
!=	nem egyenlő
<	kisebb
>	nagyobb
<=	kisebb vagy egyenlő
>=	nagyobb vagy egyenlő

Logikai operátorok
and	és
or	vagy
not	nem
"""
# x = -5
# y = -3
#
# if x < 0 and y < 0:
# 	print('mindkettő negatív')
#
# if x < 0 or y < 0:
# 	print('van köztük negatív')
#
# if not x <= 0:
# 	print('x pozitív')

"""
1. Feladat
Készíts egy programot, amely a felhasználótól bekér egy egész számot,
majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót."""

x = int(input("Kérlek adj meg egy egész számot! "))

if x % 2 == 0 and x > 0:
	print("A szám páros és pozitív.")
elif x % 2 != 0 and x < 0:
	print("A szám negatív és páratlan.")


"""
2. Feladat
Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi, hogy az ikrek (Henrik és Hanna) jönnek-e ma kosrazni! Például így: Jön Henrik ma kosarazni? (i/n). A program írja ki, hogy melyik állítás igaz az alábbiak közül:
- egyikük sem jön kosarazni,
- mind a ketten jönnek kosarazni,
- csak az egyikük jön kosarazni.
"""


"""
3. Feladat
Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
- csak 3-mal osztható,
- csak 4-gyel osztható,
- 3-mal és 4-gyel is osztható,
- sem 3-mal, sem 4-gyel nem osztható!
"""
