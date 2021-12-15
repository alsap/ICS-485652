import matplotlib.pyplot as plt

dnipr_bud = [22456,22821,22698]
dnipr_mash = [10087,26059,26001]
dnipr_tz = [206,240,190]
dnipr_inv = [34,57,32]
univer_bud = [44048,44548,44348]
univer_mash = [5564,8135,8000]
univer_tz = [12,45,42]
univer_inv = [116,180,157]
x = ("0.00","0.50","1.00")

plt.plot(x,dnipr_bud,label = "Дніпрянка Будівлі")
plt.plot(x,dnipr_mash,label = "Дніпрянка Машини")
plt.plot(x,dnipr_tz,label = "Дніпрянка ТЗ")
plt.plot(x,dnipr_inv,label = "Дніпрянка Інвентар")
plt.plot(x,univer_bud,label = "Універсам 22 Будівлі")
plt.plot(x,univer_mash,label = "Універсам 22 Машини")
plt.plot(x,univer_tz,label = "Універсам 22 ТЗ")
plt.plot(x,univer_inv,label = "Універсам 22 Інвентар")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

def graf():
 plt.show()