#Задание №3

#На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег. Одна лодка может выдержать не более m килограмм,
#при этом в лодку помещается не более 2 человек. Определите, какое минимальное число лодок нужно, чтобы перевезти на другой берег всех рыбаков 
#В первую строку вводится число m (1 ≤ m ≤ 10e6) - максимальная масса, которую может выдержать одна лодка.
#Во вторую строку вводится число n (1 ≤ n ≤ 100) - количество рыбаков.
#В следующие N строк вводится по одному числу Ai (1 ≤ Ai ≤ m) - вес каждого путешественника.
#Программа должна вывести одно число - минимальное количество лодок, необходимое для переправки всех рыбаков на противоположный берег.


boat_cargo  = int(input('Максимальная масса, которую может выдержать одна лодка: '))

  
while boat_cargo < 1:
        print('Максимальная масса не может быть мельше 1 !!!') 
        boat_cargo  = int(input('Максимальная масса, которую может выдержать одна лодка: '))
while boat_cargo > 10e9:
        print('Максимальная масса не может быть больше 10e6 !!!') 
        boat_cargo  = int(input('Максимальная масса, которую может выдержать одна лодка: '))

#(1 ≤ n ≤ 100) - количество рыбаков.
fishermen = int(input('Укажите колличество рыбаков: '))

while fishermen < 1:
     print('Колличество рыбаков не может быть меньше 1 !!!')
     fishermen = int(input('Укажите колличество рыбаков: '))   
while fishermen > 100:
     print('Колличество рыбаком не может быть больше 100 !!!')
     fishermen = int(input('Укажите колличество рыбаков: '))
     

    
fishermen_cargo = []
boat = []
for i in range(fishermen):
    x = int(input(f'Введите массу {i+1} рыбока: '))
    while x < 1:
         print('Масса одного рыбака не может быть мень 1 !!! ')  
         x = int(input(f'Введите массу {i+1} рыбока: ')) 
    while x > boat_cargo:
         print(f'Масса одного рыбака не может быть больше {boat_cargo} !!! ')  
         x = int(input(f'Введите массу {i+1} рыбока: '))      
    fishermen_cargo.append(x)
    
 
for i in range(len(fishermen_cargo)):
    if fishermen_cargo[i] + min(fishermen_cargo) <= boat_cargo :
        boat += [[fishermen_cargo[i], min(fishermen_cargo)]]
        fishermen_cargo[i] += boat_cargo 
        fishermen_cargo[fishermen_cargo.index(min(fishermen_cargo))] += boat_cargo 
    else:
        if fishermen_cargo[i] > boat_cargo :
            continue
        else:
            boat += [[fishermen_cargo[i]]]

print(f'Минимальное количество лодок: {len(boat)}')