import math
import sys

class ScientificCalculator:
    """Scientific Calculator with basic operations"""
    
    @staticmethod
    def square_root(x):
        """Calculate square root of x"""
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(x)
    
    @staticmethod
    def factorial(x):
        """Calculate factorial of x"""
        if x < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if not isinstance(x, int) and not x.is_integer():
            raise ValueError("Factorial is only defined for integers")
        return math.factorial(int(x))
    
    @staticmethod
    def natural_log(x):
        """Calculate natural logarithm (base e) of x"""
        if x <= 0:
            raise ValueError("Natural logarithm is only defined for positive numbers")
        return math.log(x)
    
    @staticmethod
    def power(x, b):
        """Calculate x raised to power b"""
        return math.pow(x, b)


def display_menu():
    """Display calculator menu"""
    print("\n" + "="*50)
    print("Scientific Calculator")
    print("="*50)
    print("1. Square Root (√x)")
    print("2. Factorial (x!)")
    print("3. Natural Logarithm (ln(x))")
    print("4. Power (x^b)")
    print("5. Exit")
    print("="*50)


def main():
    """Main function to run calculator"""
    calc = ScientificCalculator()
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '5':
                print("\nThank you for using Scientific Calculator!")
                sys.exit(0)
            
            if choice == '1':
                x = float(input("Enter number: "))
                result = calc.square_root(x)
                print(f"\n√{x} = {result}")
            
            elif choice == '2':
                x = float(input("Enter number: "))
                result = calc.factorial(x)
                print(f"\n{int(x)}! = {result}")
            
            elif choice == '3':
                x = float(input("Enter number: "))
                result = calc.natural_log(x)
                print(f"\nln({x}) = {result}")
            
            elif choice == '4':
                x = float(input("Enter base (x): "))
                b = float(input("Enter exponent (b): "))
                result = calc.power(x, b)
                print(f"\n{x}^{b} = {result}")
            
            else:
                print("\nInvalid choice! Please enter 1-5.")
        
        except ValueError as e:
            print(f"\nError: {e}")
        except KeyboardInterrupt:
            print("\n\nExiting calculator...")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
