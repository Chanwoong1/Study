import fah_converter

if __name__ == "__main__" :
    print('Enter a celsius value : 42.6')
    celsius = 42.6
    
    fahrenheit = fah_converter.convert_c_to_f(celsius)
    print("That's,", fahrenheit, "degrees Fahrenheit.")