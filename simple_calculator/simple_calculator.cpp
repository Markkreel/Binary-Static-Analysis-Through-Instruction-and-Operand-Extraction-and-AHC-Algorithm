#include <iostream>

int main() {
  char op;
  double num1, num2;

  // Input from the user
  std::cout << "Enter an operator (+, -, *, /): ";
  std::cin >> op;

  std::cout << "Enter two numbers: ";
  std::cin >> num1 >> num2;

  // Switch statement to perform operations
  switch (op) {
  case '+':
    std::cout << num1 << " + " << num2 << " = " << (num1 + num2) << std::endl;
    break;
  case '-':
    std::cout << num1 << " - " << num2 << " = " << (num1 - num2) << std::endl;
    break;
  case '*':
    std::cout << num1 << " * " << num2 << " = " << (num1 * num2) << std::endl;
    break;
  case '/':
    if (num2 == 0) {
      std::cout << "Error: Division by zero" << std::endl;
    } else {
      std::cout << num1 << " / " << num2 << " = " << (num1 / num2) << std::endl;
    }
    break;
  default:
    std::cout << "Invalid operator" << std::endl;
  }

  return 0;
}
