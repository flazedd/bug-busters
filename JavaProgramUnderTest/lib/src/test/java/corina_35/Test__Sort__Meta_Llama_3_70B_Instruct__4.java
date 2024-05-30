package corina_35;
import java.util.List;
import java.lang.reflect.Field;
import org.junit.jupiter.api.Test;
import java.util.Comparator;
import java.util.Collections;
import java.util.Arrays;
import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Sort__Meta_Llama_3_70B_Instruct__4 {
@Test
    public void testSort() {
        class Person {
            private String name;
            private int age;

            public Person(String name, int age) {
                this.name = name;
                this.age = age;
            }

            public int getAge() {
                return age;
            }
        }

        java.util.List<Person> people = new java.util.ArrayList<>();
        people.add(new Person("John", 25));
        people.add(new Person("Alice", 30));
        people.add(new Person("Bob", 20));

        Sort.sort(people, "age", true);

        assertEquals(30, people.get(0).getAge());
        assertEquals(25, people.get(1).getAge());
        assertEquals(20, people.get(2).getAge());
    }
@Test
    public void testSortStudents() {
        class Student {
            private String name;
            private double gpa;

            public Student(String name, double gpa) {
                this.name = name;
                this.gpa = gpa;
            }

            public double getGpa() {
                return gpa;
            }
        }

        java.util.List<Student> students = new java.util.ArrayList<>();
        students.add(new Student("Alice", 3.7));
        students.add(new Student("Bob", 3.3));
        students.add(new Student("Charlie", 3.9));

        Sort.sort(students, "gpa", false);

        assertEquals(3.3, students.get(0).getGpa(), 0.01);
        assertEquals(3.7, students.get(1).getGpa(), 0.01);
        assertEquals(3.9, students.get(2).getGpa(), 0.01);
    }
@Test
    public void testSortEmptyList() {
        java.util.List<String> emptyList = new java.util.ArrayList<>();

        Sort.sort(emptyList, "length", false);

        assertEquals(0, emptyList.size());
    }
@Test
    public void testSortNullList() {
        try {
            Sort.sort(null, "field", false);
            assert false; // should throw NullPointerException
        } catch (NullPointerException e) {
            // expected
        }
    }
@Test
    public void testSortListWithNullElements() {
        class Person {
            private String name;
            private int age;

            public Person(String name, int age) {
                this.name = name;
                this.age = age;
            }

            public int getAge() {
                return age;
            }
        }

        java.util.List<Person> people = new java.util.ArrayList<>();
        people.add(new Person("John", 25));
        people.add(null);
        people.add(new Person("Alice", 30));

        try {
            Sort.sort(people, "age", true);
            assert false; // should throw NullPointerException
        } catch (NullPointerException e) {
            // expected
        }
    }
@Test
    public void testSortListWithMultipleNullElements() {
        class Person {
            private String name;
            private int age;

            public Person(String name, int age) {
                this.name = name;
                this.age = age;
            }

            public int getAge() {
                return age;
            }
        }

        java.util.List<Person> people = new java.util.ArrayList<>();
        people.add(null);
        people.add(new Person("John", 25));
        people.add(null);
        people.add(new Person("Alice", 30));

        try {
            Sort.sort(people, "age", true);
            assert false; // should throw NullPointerException
        } catch (NullPointerException e) {
            // expected
        }
    }
@Test
    public void testSortListWithSingleElement() {
        class Person {
            private String name;
            private int age;

            public Person(String name, int age) {
                this.name = name;
                this.age = age;
            }

            public int getAge() {
                return age;
            }
        }

        java.util.List<Person> people = new java.util.ArrayList<>();
        people.add(new Person("John", 25));

        Sort.sort(people, "age", true);

        assertEquals(25, people.get(0).getAge());
    }
@Test
    public void testSortListWithDuplicateElements() {
        class Person {
            private String name;
            private int age;

            public Person(String name, int age) {
                this.name = name;
                this.age = age;
            }

            public int getAge() {
                return age;
            }
        }

        java.util.List<Person> people = new java.util.ArrayList<>();
        people.add(new Person("John", 25));
        people.add(new Person("Alice", 25));
        people.add(new Person("Bob", 30));

        Sort.sort(people, "age", true);

        assertEquals(30, people.get(0).getAge());
        assertEquals(25, people.get(1).getAge());
        assertEquals(25, people.get(2).getAge());
    }
}