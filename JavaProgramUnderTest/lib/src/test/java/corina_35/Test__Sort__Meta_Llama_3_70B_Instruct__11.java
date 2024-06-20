package corina_35;
import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.Comparator;
import java.lang.reflect.Field;
import java.util.Collections;
import static org.junit.jupiter.api.Assertions.*;
import java.lang.reflect.InvocationTargetException;
import java.util.List;
import org.junit.jupiter.api.Test;
public class Test__Sort__Meta_Llama_3_70B_Instruct__11 {
@Test
public void testSort() {
    class Student {
        private String name;
        private int age;

        public Student(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public int getAge() {
            return age;
        }
    }

    java.util.List<Student> students = new java.util.ArrayList<>();
    students.add(new Student("Alice", 20));
    students.add(new Student("Bob", 18));
    students.add(new Student("Charlie", 22));

    Sort.sort(students, "age", true);

    assertEquals(22, students.get(0).getAge());
    assertEquals(20, students.get(1).getAge());
    assertEquals(18, students.get(2).getAge());
}
@Test
public void testSortByName() {
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
    }

    java.util.List<Person> people = new java.util.ArrayList<>();
    people.add(new Person("Bob", 20));
    people.add(new Person("Alice", 18));
    people.add(new Person("Charlie", 22));

    Sort.sort(people, "name", false);

    assertEquals("Alice", people.get(0).getName());
    assertEquals("Bob", people.get(1).getName());
    assertEquals("Charlie", people.get(2).getName());
}
@Test
public void testSortEmptyList() {
    class Student {
        private String name;
        private int age;

        public Student(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public int getAge() {
            return age;
        }
    }

    java.util.List<Student> students = new java.util.ArrayList<>();

    Sort.sort(students, "age", true);

    assertEquals(0, students.size());
}
@Test
public void testSortListWithInvalidField() {
    class Student {
        private String name;
        private int age;

        public Student(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public int getAge() {
            return age;
        }
    }

    java.util.List<Student> students = new java.util.ArrayList<>();
    students.add(new Student("Alice", 20));
    students.add(new Student("Bob", 18));
    students.add(new Student("Charlie", 22));

    try {
        Sort.sort(students, "invalidField", true);
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        // expected
    }
}
@Test
public void testSortListWithMultipleSameValues() {
    class Student {
        private String name;
        private int age;

        public Student(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public int getAge() {
            return age;
        }
    }

    java.util.List<Student> students = new java.util.ArrayList<>();
    students.add(new Student("Alice", 20));
    students.add(new Student("Bob", 20));
    students.add(new Student("Charlie", 22));

    Sort.sort(students, "age", true);

    assertEquals(22, students.get(0).getAge());
    assertEquals(20, students.get(1).getAge());
    assertEquals(20, students.get(2).getAge());
}
@Test
public void testSortListWithDifferentClasses() {
    class Student {
        private String name;
        private int age;

        public Student(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public int getAge() {
            return age;
        }
    }

    class Teacher {
        private String name;
        private int age;

        public Teacher(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public int getAge() {
            return age;
        }
    }

    java.util.List<Object> people = new java.util.ArrayList<>();
    people.add(new Student("Alice", 20));
    people.add(new Teacher("Bob", 18));
    people.add(new Student("Charlie", 22));

    try {
        Sort.sort(people, "age", true);
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        // expected
    }
}
@Test
public void testSortListWithEmptyGetterName() {
    class Student {
        private String name;
        private int age;

        public Student(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public int getAge() {
            return age;
        }
    }

    java.util.List<Student> students = new java.util.ArrayList<>();
    students.add(new Student("Alice", 20));
    students.add(new Student("Bob", 18));
    students.add(new Student("Charlie", 22));

    try {
        Sort.sort(students, "", true);
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        // expected
    }
}
@Test
public void testSortListWithNullList() {
    try {
        Sort.sort(null, "age", true);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
}