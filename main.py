def calcular_pago(numero_piezas, precio_unitario):
    monto_total = numero_piezas * precio_unitario
    
    if monto_total > 500000:
        inversion_empresa = monto_total * 0.55
        prestamo_banco = monto_total * 0.30
        credito_fabricante = monto_total * 0.15
    else:
        inversion_empresa = monto_total * 0.70
        prestamo_banco = 0
        credito_fabricante = monto_total * 0.30
    
    interes_fabricante = credito_fabricante * 0.20
    total_credito_fabricante = credito_fabricante + interes_fabricante
    
    print("\nResumen de Pago:")
    print(f"Número de piezas a comprar: {numero_piezas}")
    print(f"Precio unitario de cada pieza: ${precio_unitario:,.2f}")
    print(f"Monto total de la compra: ${monto_total:,.2f}")
    print(f"Inversión de la empresa: ${inversion_empresa:,.2f}")
    print(f"Préstamo del banco: ${prestamo_banco:,.2f}")
    print(f"Crédito al fabricante (incluyendo intereses): ${total_credito_fabricante:,.2f}")
    
    return {
        "monto_total": monto_total,
        "inversion_empresa": inversion_empresa,
        "prestamo_banco": prestamo_banco,
        "credito_fabricante": total_credito_fabricante
    }

# Ejemplo de uso
numero_piezas = int(input("Ingrese el número de piezas a comprar: "))
precio_unitario = float(input("Ingrese el precio unitario de la pieza: "))
calcular_pago(numero_piezas, precio_unitario)
