##RUNS in puython 2.7 ###
# Program to convert Pounds to kilos and viceversa
 
print ('\n       Pounds - Kilos converter\n\n')
 
pounds_or_kilograms =  str(raw_input ('You know your weight in pounds or kilograms?: '))
 
if pounds_or_kilograms == str('pounds'):
        weight_pounds = float(raw_input ('Enter your weight in pounds: '))
        print 'Your weight in kilograms is ',(weight_pounds * 0.4536 ),'kilograms'
else:
        weight_kilograms = float(raw_input ('Enter your weight in kilograms: '))
        print 'Your weight in pounds is ',(weight_kilograms / 0.4536 ),'pounds'
