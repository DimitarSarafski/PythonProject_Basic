obem = int(input())
debit_purva_truba = int(input())
debit_vtora_truba = int(input())
chasove_otsusva = float(input())

pulnene_truba1 = chasove_otsusva * debit_purva_truba
pulnene_truba2 = chasove_otsusva * debit_vtora_truba

obsto = pulnene_truba1 + pulnene_truba2

if obem >= obsto:
    obsto_procenti = (obsto * 100)/obem
    truba1_procenti = ((pulnene_truba1 * 100)/obsto)
    truba2_procenti = ((pulnene_truba2 * 100) / obsto)
    print(f"The pool is {obsto_procenti:.2f}% full. Pipe 1: {truba1_procenti:.2f}%. Pipe 2: {truba2_procenti:.2f}%.")
else:
    prepulvane = obsto -obem
    print(f"For {chasove_otsusva} hours the pool overflows with {prepulvane:.2f} liters." )