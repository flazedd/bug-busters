package corina_35;
import org.junit.jupiter.api.Test;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Comparator;
import java.util.Collections;
import java.util.List;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
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
public void testSort() {
    List<MyObject> data = new ArrayList<>();
    data.add(new MyObject(5));
    data.add(new MyObject(2));
    data.add(new MyObject(8));
    data.add(new MyObject(3));

    Sort.sort(data, "value", false);

    assertEquals(2, data.get(0).getValue());
    assertEquals(3, data.get(1).getValue());
    assertEquals(5, data.get(2).getValue());
    assertEquals(8, data.get(3).getValue());
}
}