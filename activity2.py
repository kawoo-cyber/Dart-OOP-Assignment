// Parent Class: Animal
abstract class Animal {
  void move(); // Abstract method
}

// Subclass: Bird
class Bird extends Animal {
  @override
  void move() {
    print("Flying 🦅");
  }
}

// Subclass: Fish
class Fish extends Animal {
  @override
  void move() {
    print("Swimming 🐠");
  }
}

// Subclass: Dog
class Dog extends Animal {
  @override
  void move() {
    print("Running 🐕");
  }
}

void main() {
  List<Animal> animals = [Bird(), Fish(), Dog()];

  for (var animal in animals) {
    animal.move(); // Each class has a different implementation of move()
  }
}
