package corina_35;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;
import java.util.Comparator;
import java.lang.reflect.Field;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Collections;
public class Test__Sort__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testSorting() {
    class Person {
        private String name;
        private int age;

        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public String getName() {
            return name;
        }

        public int getAge() {
            return age;
        }
    }

    java.util.ArrayList<Person> people = new java.util.ArrayList<>();
    people.add(new Person("Alice", 25));
    people.add(new Person("Bob", 30));
    people.add(new Person("Charlie", 20));

    Sort.sort(people, "age", false);

    int[] expectedAges = {20, 25, 30};
    for (int i = 0; i < people.size(); i++) {
        assertEquals(expectedAges[i], people.get(i).getAge());
    }
}

@Test
public void testSortingDescending() {
    class Student {
        private String name;
        private double gpa;

        public Student(String name, double gpa) {
            this.name = name;
            this.gpa = gpa;
        }

        public String getName() {
            return name;
        }

        public double getGpa() {
            return gpa;
        }
    }

    java.util.ArrayList<Student> students = new java.util.ArrayList<>();
    students.add(new Student("John", 3.8));
    students.add(new Student("Emily", 3.4));
    students.add(new Student("Michael", 3.9));

    Sort.sort(students, "gpa", true);

    double[] expectedGpas = {3.9, 3.8, 3.4};
    for (int i = 0; i < students.size(); i++) {
        assertEquals(expectedGpas[i], students.get(i).getGpa(), 0.01);
    }
}

@Test
public void testSortingWithNullValue() {
    class Employee {
        private String name;
        private Integer salary;

        public Employee(String name, Integer salary) {
            this.name = name;
            this.salary = salary;
        }

        public String getName() {
            return name;
        }

        public Integer getSalary() {
            return salary;
        }
    }

    java.util.ArrayList<Employee> employees = new java.util.ArrayList<>();
    employees.add(new Employee("Alice", 50000));
    employees.add(new Employee("Bob", null));
    employees.add(new Employee("Charlie", 60000));

    Sort.sort(employees, "salary", false);

    Integer[] expectedSalaries = {null, 50000, 60000};
    for (int i = 0; i < employees.size(); i++) {
        assertEquals(expectedSalaries[i], employees.get(i).getSalary());
    }
}

@Test
public void testSortingWithMultipleNullValues() {
    class Book {
        private String title;
        private Integer pages;

        public Book(String title, Integer pages) {
            this.title = title;
            this.pages = pages;
        }

        public String getTitle() {
            return title;
        }

        public Integer getPages() {
            return pages;
        }
    }

    java.util.ArrayList<Book> books = new java.util.ArrayList<>();
    books.add(new Book("Book1", null));
    books.add(new Book("Book2", 200));
    books.add(new Book("Book3", null));
    books.add(new Book("Book4", 300));

    Sort.sort(books, "pages", false);

    Integer[] expectedPages = {null, null, 200, 300};
    for (int i = 0; i < books.size(); i++) {
        assertEquals(expectedPages[i], books.get(i).getPages());
    }
}

@Test
public void testSortingWithEmptyList() {
    class Product {
        private String name;
        private double price;

        public Product(String name, double price) {
            this.name = name;
            this.price = price;
        }

        public String getName() {
            return name;
        }

        public double getPrice() {
            return price;
        }
    }

    java.util.ArrayList<Product> products = new java.util.ArrayList<>();

    Sort.sort(products, "price", false);

    assertEquals(0, products.size());
}

@Test
public void testSortingWithSingleElementList() {
    class Car {
        private String model;
        private int year;

        public Car(String model, int year) {
            this.model = model;
            this.year = year;
        }

        public String getModel() {
            return model;
        }

        public int getYear() {
            return year;
        }
    }

    java.util.ArrayList<Car> cars = new java.util.ArrayList<>();
    cars.add(new Car("Toyota", 2015));

    Sort.sort(cars, "year", false);

    assertEquals(2015, cars.get(0).getYear());
}

@Test
public void testSortingWithInvalidFieldName() {
    class Teacher {
        private String name;
        private int age;

        public Teacher(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public String getName() {
            return name;
        }

        public int getAge() {
            return age;
        }
    }

    java.util.ArrayList<Teacher> teachers = new java.util.ArrayList<>();
    teachers.add(new Teacher("John", 30));
    teachers.add(new Teacher("Mary", 25));

    try {
        Sort.sort(teachers, "invalidField", false);
        fail("Expected IllegalArgumentException for invalid field name");
    } catch (IllegalArgumentException e) {
        // expected
    }
}

@Test
public void testSortingWithNonComparableType() {
    class Address {
        private String street;
        private Object nonComparable;

        public Address(String street, Object nonComparable) {
            this.street = street;
            this.nonComparable = nonComparable;
        }

        public String getStreet() {
            return street;
        }

        public Object getNonComparable() {
            return nonComparable;
        }
    }

    java.util.ArrayList<Address> addresses = new java.util.ArrayList<>();
    addresses.add(new Address("Street1", new Object()));
    addresses.add(new Address("Street2", new Object()));

    try {
        Sort.sort(addresses, "nonComparable", false);
        fail("Expected ClassCastException for non-comparable type");
    } catch (ClassCastException e) {
        // expected
    }
}















}