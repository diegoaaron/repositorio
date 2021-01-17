# contactenación de cadenas
# supongamos que deseamos crear una cadena que diga: "suscribete a ______"

youtuber = "Kylie Ying"

# algunas formas de hacerlo es:
print("suscribete a " + youtuber)
print("suscribete a {}".format(youtuber))
print("suscribete a {youtuber}")

adj = input("adjetivo: ")
verb1 = input("verbo: ")
verb2 = input("verbo: ")
famous_person = input("Persona famosa: ")

madlib = f"Programar es muy {adj}! Esto me emociona mucho porque \
Yo amo {verb1}. Mantente hidratado y {verb2} como {famous_person}!"

print(madlib)