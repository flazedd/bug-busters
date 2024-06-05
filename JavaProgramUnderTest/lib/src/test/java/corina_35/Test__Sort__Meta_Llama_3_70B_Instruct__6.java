package corina_35;
import java.util.Comparator;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.util.Collections;
import org.junit.jupiter.api.Test;
import java.util.List;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import java.lang.reflect.Method;
public class Test__Sort__Meta_Llama_3_70B_Instruct__6 {
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
            new Student("John", 85),
            new Student("Emily", 92),
            new Student("Michael", 78)
    );

    Sort.sort(students, "name");

    assertEquals("Emily", students.get(0).getName());
    assertEquals("John", students.get(1).getName());
    assertEquals("Michael", students.get(2).getName());
}
@Test
public void testSortEmptyList() {
    List<Object> emptyList = new java.util.ArrayList<>();

    Sort.sort(emptyList, "anyField");

    assertEquals(0, emptyList.size());
}
@Test
public void testSortInvalidField() {
    class Employee {
        private String name;
        private int age;

        public Employee(String name, int age) {
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

    List<Employee> employees = Arrays.asList(
            new Employee("Alice", 25),
            new Employee("Bob", 30),
            new Employee("Charlie", 20)
    );

    try {
        Sort.sort(employees, "invalidField");
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        // expected
    }
}
@Test
public void testSortNullList() {
    try {
        Sort.sort(null, "anyField");
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testSortSingleElementList() {
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
            new Student("John", 85)
    );

    Sort.sort(students, "grade");

    assertEquals(85, students.get(0).getGrade());
}
@Test
public void testSortListWithNullElements() {
    class Employee {
        private String name;
        private int age;

        public Employee(String name, int age) {
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

    List<Employee> employees = Arrays.asList(
            new Employee("Alice", 25),
            null,
            new Employee("Charlie", 20)
    );

    try {
        Sort.sort(employees, "age");
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testSortListWithDuplicateElements() {
    class Product {
        private String name;
        private int price;

        public Product(String name, int price) {
            this.name = name;
            this.price = price;
        }

        public String getName() {
            return name;
        }

        public int getPrice() {
            return price;
        }
    }

    List<Product> products = Arrays.asList(
            new Product("Product A", 10),
            new Product("Product B", 20),
            new Product("Product C", 10)
    );

    Sort.sort(products, "price");

    assertEquals(10, products.get(0).getPrice());
    assertEquals(10, products.get(1).getPrice());
    assertEquals(20, products.get(2).getPrice());
}
}