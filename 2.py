which_one = int(input("What month (1-12)? "))
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
 
if 1 <= which_one <= 12:
    print("The month is", months[which_one - 1 ])
#------------------------------------------------------------------------------#
def mult(a, b):
    if b == 0:
        return 0
    rest = mult(a, b - 1)
    value = a + rest
    return value
print("3 * 2 = ", mult(3, 2))
