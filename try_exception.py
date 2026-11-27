def withdraw_money(amount, bal):
    try:
        if amount <=0:
            raise "Amount should be greater than 0"
        bal = bal - amount
        print(bal)
    except ValueError as e:
        print("Oops Invalid input",e)
    finally:
        print("Done")

withdraw_money(200,1000)
    