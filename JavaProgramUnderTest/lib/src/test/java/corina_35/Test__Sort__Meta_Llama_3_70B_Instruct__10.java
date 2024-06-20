package corina_35;
import java.util.List;
import java.util.Arrays;
import java.util.Comparator;
import org.junit.jupiter.api.Test;
import java.lang.reflect.Field;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Collections;
import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;
public class Test__Sort__Meta_Llama_3_70B_Instruct__10 {
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

    Sort.sort(people, "age");

    assertEquals(20, people.get(0).getAge());
    assertEquals(25, people.get(1).getAge());
    assertEquals(30, people.get(2).getAge());
}
@Test
public void testSortDecreasing() {
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

    List<Student> students = Arrays.asList(
        new Student("John", 3.5),
        new Student("Emily", 3.8),
        new Student("Michael", 3.2)
    );

    Sort.sort(students, "gpa", true);

    assertEquals(3.8, students.get(0).getGpa(), 0.01);
    assertEquals(3.5, students.get(1).getGpa(), 0.01);
    assertEquals(3.2, students.get(2).getGpa(), 0.01);
}
@Test
public void testSortEmptyList() {
    List<String> emptyList = new java.util.ArrayList<>();

    Sort.sort(emptyList, "length");

    assertEquals(0, emptyList.size());
}
@Test
public void testSortSameValues() {
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
        new Student("Bob", 90),
        new Student("Charlie", 90)
    );

    Sort.sort(students, "grade");

    assertEquals(90, students.get(0).getGrade());
    assertEquals(90, students.get(1).getGrade());
    assertEquals(90, students.get(2).getGrade());
}
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

    List<Person> people = new java.util.ArrayList<>();
    people.add(new Person("John", 25));
    people.add(new Person("Alice", 30));
    people.add(new Person("Bob", 20));

    Sort.sort(people, "age", true);

    assertEquals(30, people.get(0).getAge());
    assertEquals(25, people.get(1).getAge());
    assertEquals(20, people.get(2).getAge());
}
@Test
public void testSortingByName() {
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

    List<Person> people = new java.util.ArrayList<>();
    people.add(new Person("Alice", 25));
    people.add(new Person("Bob", 30));
    people.add(new Person("Charlie", 20));

    Sort.sort(people, "name", false);

    assertEquals("Alice", people.get(0).getName());
    assertEquals("Bob", people.get(1).getName());
    assertEquals("Charlie", people.get(2).getName());
}
@Test
public void testSortingEmptyList() {
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

    List<Person> people = new java.util.ArrayList<>();

    Sort.sort(people, "age", true);

    assertEquals(0, people.size());
}
@Test
public void testSortingByNonExistingField() {
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

    List<Person> people = new java.util.ArrayList<>();
    people.add(new Person("Alice", 25));
    people.add(new Person("Bob", 30));
    people.add(new Person("Charlie", 20));

    try {
        Sort.sort(people, "nonExistingField", true);
        fail("Expected IllegalArgumentException for non-existing field");
    } catch (IllegalArgumentException e) {
        // expected
    }
}
}