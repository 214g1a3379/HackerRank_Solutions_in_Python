def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    if sum(bill)//2==b:
        print("Bon Appetit")
    else:
        print(b-(sum(bill)//2))
