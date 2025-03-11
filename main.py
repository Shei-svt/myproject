def cal_pago(num_piezas, pre_uni):
    monto_tot = num_piezas * pre_uni
    
    if monto_tot > 500000:
        inver_empre = monto_tot * 0.55
        pres_banco = monto_tot * 0.30
        credi_fab = monto_tot * 0.15
    else:
        inver_empre = monto_tot * 0.70
        pres_banco = 0
        credi_fab = monto_tot * 0.30
    
    inter_fab = credi_fab * 0.20
    tot_cred_fab = credi_fab + inter_fab
    
    print("\nResumen de Pago:")
    print(f"Número de piezas a comprar: {num_piezas}")
    print(f"Precio unitario de cada pieza: ${pre_uni:,.2f}")
    print(f"Monto total de la compra: ${monto_tot:,.2f}")
    print(f"Inversión de la empresa: ${inver_empre:,.2f}")
    print(f"Préstamo del banco: ${pres_banco:,.2f}")
    print(f"Crédito al fabricante (incluyendo intereses): ${tot_cred_fab:,.2f}")
    
    return {
        "monto_total": monto_tot,
        "inversion_empresa": inver_empre,
        "prestamo_banco": pres_banco,
        "credito_fabricante": tot_cred_fab
    }

num_piezas = int(input("Ingrese el número de piezas a comprar: "))
pre_uni = float(input("Ingrese el precio unitario de la pieza: "))
cal_pago(num_piezas, pre_uni)
