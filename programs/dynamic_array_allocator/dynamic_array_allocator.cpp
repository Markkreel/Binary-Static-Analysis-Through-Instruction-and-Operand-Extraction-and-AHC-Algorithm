#include <iostream>

// A basic dynamic array class
template <typename T> class DynamicArray {
public:
  DynamicArray(int initialSize = 10)
      : size(initialSize), capacity(initialSize) {
    data = new T[capacity];
  }

  ~DynamicArray() { delete[] data; }

  void push_back(T value) {
    if (size == capacity) {
      resize(capacity * 2);
    }
    data[size++] = value;
  }

  T &operator[](int index) { return data[index]; }

  int getSize() const { return size; }

private:
  void resize(int newCapacity) {
    T *newData = new T[newCapacity];
    for (int i = 0; i < size; i++) {
      newData[i] = data[i];
    }
    delete[] data;
    data = newData;
    capacity = newCapacity;
  }

  T *data;
  int size;
  int capacity;
};

int main() {
  DynamicArray<int> myArray; // Create a dynamic array of integers

  // Add elements (demonstrates resizing if needed)
  for (int i = 0; i < 20; i++) {
    myArray.push_back(i * 5);
  }

  // Access and print elements
  for (int i = 0; i < myArray.getSize(); i++) {
    std::cout << myArray[i] << " ";
  }
  std::cout << std::endl;

  return 0;
}
