# Solving the situation when client wants to pay for a service
# - trying to pay by cash
# - trying to pay by cart
# - trying to pay by cryptocurrency

service_price = 500.00

data_EUR_rate = 19.54
data_USD_rate = 19.18
data_LEI_rate = 1
data_RUB_rate = 3.3
data_cripto_rate = 55.6

# CODE FOR CASH

client_cash_amount = float ( input ( "Enter the amount of cash = " ) )
if client_cash_amount > 0 :
    Type_of_money = input ( "Enter the currency in which you are going to pay for the purchase ( EUR , USD , LEI , RUB , cripto ) - " )
    if Type_of_money == "EUR" :
        service_cash_price_after_converting = int ( service_price / data_EUR_rate )
        client_cash_amount_after_converting = client_cash_amount / data_EUR_rate - 3 * ( client_cash_amount / data_EUR_rate / 100 )
        print ( "Your cash account after the transfer ( LEI ---> EUR ) = " , int ( client_cash_amount_after_converting ) )
        print ( "3 percent of the total amount is calculated for the ' conversion ' service ." )
    elif Type_of_money == "USD" :
        service_cash_price_after_converting = int ( service_price / data_USD_rate )
        client_cash_amount_after_converting = client_cash_amount / data_USD_rate - 3 * ( client_cash_amount / data_USD_rate / 100 ) 
        print ( "Your cash account after the transfer ( LEI ---> USD ) = " , int ( client_cash_amount_after_converting ) )
        print ( "3 percent of the total amount is calculated for the ' conversion ' service ." )
    elif Type_of_money == "LEI" :
        service_cash_price_after_converting = service_price
        print ( "This is the same currency therefore the transfer is not needed ." )
        client_cash_amount_after_converting = client_cash_amount
        print ( "Your cash ( LEI ) = " , int ( client_cash_amount_after_converting ) ) 
    elif Type_of_money == "RUB" :
        service_cash_price_after_converting = int ( service_price * data_RUB_rate )
        client_cash_amount_after_converting = client_cash_amount * data_USD_rate  - 3 * ( client_cash_amount * data_RUB_rate / 100 )
        print ( "Your cash account after the transfer ( LEI ---> RUB ) = " , int ( client_cash_amount_after_converting ) )
        print ( "3 percent of the total amount is calculated for the ' conversion ' service ." )
    elif Type_of_money == "cripto" :
        service_cash_price_after_converting = int ( service_price / data_cripto_rate )
        client_cash_amount_after_converting = client_cash_amount / data_cripto_rate - 3 * ( client_cash_amount / data_cripto_rate / 100 )
        print ( "Your money after conversion ( LEI ---> crypto ) = " , int ( client_cash_amount_after_converting ) )
        print ( "3 percent of the total amount is calculated for the ' conversion ' service ." )
    else :
        print ( "This currency is not listed in our database . Reject !!!" )
else :
    client_cash_amount <= 0
    client_cash_amount_after_converting = 0
    service_cash_price_after_converting = service_price
    print ( "This operation is impossible . Error !!!" )
# CODE FOR CART

client_cart_amount = float ( input ( "Enter the amount of cart = " ) )
if client_cart_amount > 0 :
    Type_of_money = input ( "Enter the currency in which you are going to pay for the purchase ( EUR , USD , LEI , RUB , cripto ) - " )
    if Type_of_money == "EUR" :
        service_cart_price_after_converting = int ( service_price / data_EUR_rate )
        client_cart_amount_after_converting = client_cart_amount / data_EUR_rate
        print ( "Your cart account after the transfer ( LEI ---> EUR ) = " , int ( client_cart_amount_after_converting ) )
    elif Type_of_money == "USD" :
        service_cart_price_after_converting = int ( service_price / data_USD_rate )
        client_cart_amount_after_converting = client_cart_amount / data_USD_rate
        print ( "Your cart account after the transfer ( LEI ---> USD ) = " , int ( client_cart_amount_after_converting ) )
    elif Type_of_money == "LEI" :
        service_cart_price_after_converting = service_price
        print ( "This is the same currency therefore the transfer is not needed ." )
        client_cart_amount_after_converting = client_cart_amount
        print ( "Your cart ( LEI ) = " , int ( client_cart_amount_after_converting ) )
    elif Type_of_money == "RUB" :
        service_cart_price_after_converting = int ( service_price * data_RUB_rate )
        client_cart_amount_after_converting = client_cart_amount * data_USD_rate
        print ( "Your cart account after the transfer ( LEI ---> RUB ) = " , int ( client_cart_amount_after_converting ) )
    elif Type_of_money == "cripto" :
        service_cart_price_after_converting = int ( service_price / data_cripto_rate )
        client_cart_amount_after_converting = client_cart_amount / data_cripto_rate
        print ( "Your money after conversion ( LEI ---> crypto ) = " , int ( client_cart_amount_after_converting ) )
    else :
        print ( "This currency is not listed in our database . Reject !!!" )
else :
    client_cart_amount <= 0
    client_cart_amount_after_converting = 0
    service_cart_price_after_converting = service_price
    print ( "This operation is impossible . Error !!!" )

# CODE FOR CRIPTO

client_cripto_amount = int ( input ( "Enter the amount of cripto = " ) )
if client_cripto_amount > 0 :
    service_price_after_converting = int ( service_price / data_cripto_rate )
else :
    client_cripto_amount <= 0
    print ( "This operation is impossible . Error !!!" )

# CODE FOR ORDER PAYMENT

if client_cash_amount_after_converting >= service_cash_price_after_converting :
    print ( "Can the payment be made in cash ? - " , client_cash_amount_after_converting >= service_cash_price_after_converting )
    print ( "The order is paid . Thank you for your purchase ! " )
else :
    print ( "Can the payment be made in cash ? - " , client_cash_amount_after_converting >= service_price_after_converting )
    print ( "There are not enough funds . You cannot pay for the purchase . Use another payment method , for example cart . ! " )
    if client_cash_amount_after_converting >= service_cart_price_after_converting :
        print ( "Can the payment be made in cart ? - " , client_cart_amount_after_converting >= service_cart_price_after_converting )
        print ( "The order is paid . Thank you for your purchase ! " )
    else :
        print ( "Can the payment be made in cart ? - " , client_cart_amount_after_converting >= service_cart_price_after_converting )
        print ( "There are not enough funds on the card . You cannot pay for the purchase . Use another payment method , for example cripto . ! " )
        if client_cripto_amount >= service_price_after_converting :
            print ( "Can the payment be made in cripto ? - " , client_cripto_amount >= service_price_after_converting )
            print ( "The order is paid . Thank you for your purchase ! " )
        else :
            print ( "Can the payment be made in cripto ? - " , client_cripto_amount >= service_price_after_converting )
            print ( "There are not enough funds . You cannot pay for the purchase . " )