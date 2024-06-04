package corina_35;
import java.util.Comparator;
import java.lang.reflect.InvocationTargetException;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import java.util.Collections;
import static org.junit.jupiter.api.Assertions.*;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.List;
public class Test__Sort__Meta_Llama_3_70B_Instruct__5 {
@Test
public void testSort() {
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

    List<Person> people = Arrays.asList(
            new Person("Alice", 25),
            new Person("Bob", 30),
            new Person("Charlie", 20)
    );

    Sort.sort(people, "age", true);

    assertEquals(30, people.get(0).getAge());
    assertEquals(25, people.get(1).getAge());
    assertEquals(20, people.get(2).getAge());
}
@Test
public void testSortByName() {
    class Book {
        private String title;
        private String author;

        public Book(String title, String author) {
            this.title = title;
            this.author = author;
        }

        public String getTitle() {
            return title;
        }

        public String getAuthor() {
            return author;
        }
    }

    List<Book> books = Arrays.asList(
            new Book("To Kill a Mockingbird", "Harper Lee"),
            new Book("The Great Gatsby", "F. Scott Fitzgerald"),
            new Book("Pride and Prejudice", "Jane Austen")
    );

    Sort.sort(books, "title");

    assertEquals("Pride and Prejudice", books.get(0).getTitle());
    assertEquals("The Great Gatsby", books.get(1).getTitle());
    assertEquals("To Kill a Mockingbird", books.get(2).getTitle());
}
@Test
public void testSortWithNullValues() {
    class Student {
        private String name;
        private Integer grade;

        public Student(String name, Integer grade) {
            this.name = name;
            this.grade = grade;
        }

        public String getName() {
            return name;
        }

        public Integer getGrade() {
            return grade;
        }
    }

    List<Student> students = Arrays.asList(
            new Student("Alice", 90),
            new Student("Bob", null),
            new Student("Charlie", 80),
            new Student("David", null)
    );

    Sort.sort(students, "grade", true);

    assertEquals(90, (int) students.get(0).getGrade());
    assertEquals(80, (int) students.get(1).getGrade());
    assertNull(students.get(2).getGrade());
    assertNull(students.get(3).getGrade());
}
@Test
public void testSortEmptyList() {
    class Employee {
        private String name;
        private int salary;

        public Employee(String name, int salary) {
            this.name = name;
            this.salary = salary;
        }

        public String getName() {
            return name;
        }

        public int getSalary() {
            return salary;
        }
    }

    List<Employee> employees = Collections.emptyList();

    Sort.sort(employees, "salary");

    assertEquals(0, employees.size());
}
@Test
public void testSortListWithOneElement() {
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

    List<Product> products = Collections.singletonList(new Product("Apple", 10.99));

    Sort.sort(products, "price");

    assertEquals("Apple", products.get(0).getName());
    assertEquals(10.99, products.get(0).getPrice(), 0.01);
}
@Test
public void testSortListWithDuplicateValues() {
    class Item {
        private String name;
        private int quantity;

        public Item(String name, int quantity) {
            this.name = name;
            this.quantity = quantity;
        }

        public String getName() {
            return name;
        }

        public int getQuantity() {
            return quantity;
        }
    }

    List<Item> items = Arrays.asList(
            new Item("Book", 2),
            new Item("Pencil", 3),
            new Item("Book", 2),
            new Item("Pen", 1)
    );

    Sort.sort(items, "quantity", true);

    assertEquals(3, items.get(0).getQuantity());
    assertEquals(2, items.get(1).getQuantity());
    assertEquals(2, items.get(2).getQuantity());
    assertEquals(1, items.get(3).getQuantity());
}
@Test
public void testSortListWithNonExistingField() {
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

    List<Person> people = Arrays.asList(
            new Person("Alice", 25),
            new Person("Bob", 30),
            new Person("Charlie", 20)
    );

    try {
        Sort.sort(people, "nonExistingField");
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        // expected
    }
}
@Test
public void testSortListWithNullObject() {
    class Student {
        private String name;
        private int grade;

        public Student(String name, int grade) {
            this.name = name;
            this.grade = grade;
        }

        public String getName() {
            return name;
        }

        public int getGrade() {
            return grade;
        }
    }

    List<Student> students = Arrays.asList(
            new Student("Alice", 90),
            null,
            new Student("Charlie", 80)
    );

    try {
        Sort.sort(students, "grade", true);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
}