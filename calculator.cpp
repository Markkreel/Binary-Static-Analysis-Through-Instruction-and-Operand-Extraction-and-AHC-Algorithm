#include <iostream>

using namespace std;

int main() {
  char operation;
  double num1, num2;

  float x = 2;
  float y = 4;

  cout << "Operation (+, -, *, /): ";
  cin >> operation;

  switch (operation) {
  case '+':
    cout << x << " + " << y << " = " << x + y << endl;
    break;
  case '-':
    cout << x << " - " << y << " = " << x - y << endl;
    break;
  case '*':
    cout << x << " * " << y << " = " << x * y << endl;
    break;
  case '/':
    if (y == 0) {
      cout << "Error: Division by zero" << endl;
    } else {
      cout << x << " / " << y << " = " << x / y << endl;
    }
    break;
  default:
    cout << "Invalid operator" << endl;
  }

  return 0;
}
