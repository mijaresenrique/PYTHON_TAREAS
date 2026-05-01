tipo = int(input("Tipo de cliente (1=VIP, 2=Regular): "))
monto = float(input("Ingrese monto de compra: "))

descuento = 0

if tipo == 1:  # VIP
    if monto > 100:
        descuento = monto * 0.20
    else:
        descuento = monto * 0.10
else:  # Regular
    if monto > 200:
        descuento = monto * 0.10
    else:
        descuento = monto * 0.05

total = monto - descuento

print("Descuento aplicado:", descuento)
print("Monto final a pagar:", total)