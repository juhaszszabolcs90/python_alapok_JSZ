"""1.1 Feladat
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!"""

# question = input("Jó napod van-e? ")
# if question == "igen":
# 	print("Örülök, hogy jó napod van!")
# else:
# 	print("Sajnálom, legyen szebb napod!")



question = input("Jó napod van-e? ")
question_lowercase = question.lower()
if question_lowercase == "igen":
	print("Örülök, hogy jó napod van!")
else:
	print("Sajnálom, legyen szebb napod!")

"""1.2 Feladat
Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"""
