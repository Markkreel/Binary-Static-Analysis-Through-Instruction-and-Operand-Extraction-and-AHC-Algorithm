#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

// A simple structure to hold a row of CSV data
struct CSVRow {
  std::vector<std::string> fields;
};

int main() {
  const char *filename = "csv_parser_test.csv";
  std::ifstream file(filename);

  if (!file.is_open()) {
    std::cout << "Error opening file: " << filename << std::endl;
    return 1;
  }

  std::vector<CSVRow> rows;
  std::string line;
  while (std::getline(file, line)) {
    CSVRow row;
    std::stringstream lineStream(line);
    std::string field;

    while (std::getline(lineStream, field, ',')) {
      row.fields.push_back(field);
    }

    rows.push_back(row);
  }

  // Accessing the parsed data
  for (auto &row : rows) {
    for (auto &field : row.fields) {
      std::cout << field << " ";
    }
    std::cout << std::endl;
  }

  return 0;
}
