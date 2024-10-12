#  1 masala
# class Odam:
#     def __init__(self, ism):
#         self.ism = ism
#     def salomlashish(self):
#         return f"Salom {self.ism}"
# while True:
#     ism2 = input("Ism kiriting :")
#     if not ism2[0].isupper():
#         print("Ismni bosh harifi katta bo'lishi kerak qayta urining ")
#     elif len(ism2) <= 3:
#         print("Ism hariflari kamida 4 tadan ko'p bo'lishi kerak qayta urining")
#     else:
#             odam2 = Odam(ism2)
#             print(odam2.salomlashish())
#             print("Dastur tugatildi")
#             break

# 2 masala
# class Odam:
#     def __init__(self, ism):
#         self.ism = ism
#     def kuylash(self):
#         return f"{self.ism}, kuylayapti ..."
#     def eshitish(self):
#         return f"{self.ism}, kuylashini eshityapti"
#     def gapirish(self):
#         return f"{self.ism}, gapiryapti"
# odam1 = Odam("Abduraxmon")
# odam2 = Odam("Azizbek")
# kuylash_1 = odam1.kuylash()
# eshitish_2 = odam2.eshitish()
# gapirish3 = odam2.gapirish()
# print(kuylash_1)
# print(eshitish_2)
# print(gapirish3)

# 3 masala
# class Odam:
#     def __init__(self, ism):
#         self.ism = ism
#
#     def yugurish(self):
#         return f"{self.ism}, yuguryapti "
#     def yiqilish(self):
#         return f"{self.ism}, yiqildi "
#
# odam1 = Odam("Salohiddin")
# yugurish = odam1.yugurish()
# yiqilish = odam1.yiqilish()
# print(yugurish)
# print(f"Oyog'i qoqilib ketdi va {yiqilish}")

# 4 masala
# class Odam:
#     def __init__(self, ism):
#         self.ism = ism
#     def tepish(self, koptok):
#         print(f"{self.ism}, kopto'kni tepdi ")
#         koptok.uchush()
#
# class Koptok:
#     def uchush(self):
#         print("Kopto'k uchdi")
#
# aziz = Odam("Aziz")
# koptok = Koptok()
# aziz.tepish(koptok)

# 5 masala
# class Vaqt:
#     def __init__(self, soat, minut, sekund):
#         self.soat = soat
#         self.minut = minut
#         self.sekund = sekund
#
#     def oshirish(self, soat=0, minut=0, sekund=0):
#         self.sekund += sekund
#         if self.sekund >= 60:
#             self.minut += self.sekund // 60
#             self.sekund %= 60
#
#         self.minut += minut
#         if self.minut >= 60:
#             self.soat += self.minut // 60
#             self.minut %= 60
#
#         self.soat += soat
#         if self.soat >= 24:
#             self.soat %= 24
#
#     def __str__(self):
#         return f"{self.soat:02}:{self.minut:02}:{self.sekund:02}"
#
# vaqt = Vaqt(10, 30, 50)
# print("Dastlabki vaqt:", vaqt)
#
# # Vaqtni oshirish
# vaqt.oshirish(soat=5)
# print("Soat oshirilgandan keyin vaqt:", vaqt)
#
# vaqt.oshirish(minut=5)
# print("Minut oshirilgandan keyin vaqt:", vaqt)
#
# vaqt.oshirish(sekund=5)
# print("Sekund oshirilgandan keyin vaqt:", vaqt)
