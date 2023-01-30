skumriq_price = float(input())
chacha_price = float(input())
palamut_amount = float(input())
safrid_amount = float(input())
midi_amount = float(input())
midi_price = 7.50

palamut_price = skumriq_price + (skumriq_price * 0.60)
safrid_price = chacha_price + (chacha_price * 0.80)
palamut_cost = palamut_amount * palamut_price
safrid_cost = safrid_amount * safrid_price
midi_cost = midi_amount * midi_price
total_cost = palamut_cost + safrid_cost + midi_cost

print(f"{total_cost:.2f}")