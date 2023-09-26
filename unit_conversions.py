## Converting between units via python functions

### Miles to Kilometers
def mi_to_km(x) :
    convert = round(1.60934*x, 2)
    return convert

### Kilometers to Miles
def km_to_mi(x) :
    convert = round(0.621371*x, 2)
    return convert

### Fahrenheit to Celsius
def f_to_c(x) :
    convert = round((x-32) * (5/9), 2)
    return convert

### Celsius to Fahrenheit
def c_to_f(x) :
    convert = round((x * 9/5) + 32, 2)
    return convert

### Kilograms to Pounds
def kg_to_lbs(x) :
    convert = round(2.20462*x, 2)
    return convert

### Pounds to Kilograms
def lbs_to_kg(x) :
    convert = round(0.453592*x, 2)
    return convert
