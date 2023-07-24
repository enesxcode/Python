storeitemsdata=[ ] 
store_items=0 
    
while store_items!=6:
 print('*****Ernest Store*****')
 store_items=input('Choose Options \n 1. Buy Item: \n 2. View Curt: \n 3. Remove Curt Item: \n 4. Make Purchase: \n 5. About Us: \n 6. Exit App \n\n Provide Options Number:')
  
 store_items=int(store_items) 
  
 items=0
 
 if store_items==1:
     lists_items=input('Buy Item''\n''Provide Product:')
     listss=int(input('Enter Quantity:'))
     listsss=float(input('Provide Price:'))
     lists_data={'Product':lists_items,'Quantity':listss,'Price':listsss}
     
     if not any(i['Product']==lists_items for i in storeitemsdata):
       storeitemsdata.count(lists_data)<=0
       storeitemsdata.append(lists_data)
       print('Item Add Saved Successfully')
     else:
      print('Item Already Available')
      
     
 elif store_items==2:
    if len(storeitemsdata)<=0:
         print('No Items In Curt')
    else:
        print('Items In Cart')
        for i in storeitemsdata:
            print(i)
    
     
 elif store_items==3:
     if len(storeitemsdata)<=0:
         print('No Item To Remove')    
     else:
      lists_items=input('Enter Your Remove Item:')
      for i in storeitemsdata:
       if i['Product']==lists_items: 
         storeitemsdata.remove(i) 
         print('Item Removed Successfully')
       else:
           print('Item Not In Cart')
        
         
 elif store_items==4:
     if not storeitemsdata:
         print('No Item To Purchase')
         continue
     listss=float(input('Make Purchase''\n''Total Amount:'))
     listsss=float(input('Enter Payment:'))
     if listss==listsss:
         totalamount=0
         total_amount=listss*listsss
         totalamount+=total_amount
         print('Total Amount:$',totalamount,'\n''Payment Successfully''\n''Thank You For Shopping With Us')
         storeitemsdata.clear()
     else:
         print('Payment Failed!''\n'"We apologize for the inconvenience, but it seems that there was an issue with your payment. Our team is working diligently to resolve the problem. Please double-check your payment details and try again. If the problem persists, don't hesitate to reach out to our customer support, and we'll be more than happy to assist you with completing your payment successfully. Thank you for your patience.")
         
          
 elif store_items==5:
      print('About US''\n''Welcome to our shopping store, your one-stop destination for all your needs. We pride ourselves on offering a curated selection of high-quality products that cater to every taste and style. With exceptional customer service and unbeatable prices, we strive to make your shopping experience truly delightful. Happy shopping with us!')
      
       
 elif store_items==6:
     break
 else:
     print('Invalid Option Input')                      
     