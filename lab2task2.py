
zpshka=237821
traty=2123942
capitalchik=traty-zpshka
inflya=0.03
for i in range(2,10):
    zpshka*=(1+inflya)
    capitalchik = traty - zpshka
print(round(capitalchik+1))
