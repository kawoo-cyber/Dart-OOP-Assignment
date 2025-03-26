// Parent Class: Smartphone
class Smartphone {
  String brand;
  String model;
  double price;

  // Constructor
  Smartphone(this.brand, this.model, this.price);

  // Method to display details
  void displayInfo() {
    print("Brand: $brand, Model: $model, Price: \$${price}");
  }
}

// Child Class 1: AndroidPhone
class AndroidPhone extends Smartphone {
  String osVersion;

  AndroidPhone(String brand, String model, double price, this.osVersion)
      : super(brand, model, price);

  @override
  void displayInfo() {
    super.displayInfo();
    print("OS: Android $osVersion");
  }
}

// Child Class 2: iPhone
class iPhone extends Smartphone {
  String iosVersion;

  iPhone(String brand, String model, double price, this.iosVersion)
      : super(brand, model, price);

  @override
  void displayInfo() {
    super.displayInfo();
    print("OS: iOS $iosVersion");
  }
}

void main() {
  var samsung = AndroidPhone("Samsung", "Galaxy S23", 999.99, "13.0");
  var apple = iPhone("Apple", "iPhone 15", 1199.99, "17.0");

  samsung.displayInfo();
  print("------------------");
  apple.displayInfo();
}
