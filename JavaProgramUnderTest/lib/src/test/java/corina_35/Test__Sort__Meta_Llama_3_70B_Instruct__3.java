package corina_35;
import java.lang.reflect.InvocationTargetException;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.Comparator;
import java.lang.reflect.Method;
import java.lang.reflect.Field;
import java.util.List;
import java.util.Collections;
public class Test__Sort__Meta_Llama_3_70B_Instruct__3 {
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

    Person[] peopleArray = new Person[] {
            new Person("Alice", 25),
            new Person("Bob", 30),
            new Person("Charlie", 20)
    };

    List<Person> people = java.util.Arrays.asList(peopleArray);

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

    Student[] studentsArray = new Student[] {
            new Student("John", 3.8),
            new Student("Emily", 3.2),
            new Student("Michael", 3.9)
    };

    List<Student> students = java.util.Arrays.asList(studentsArray);

    Sort.sort(students, "gpa", true);

    assertEquals(3.9, students.get(0).getGpa(), 0.01);
    assertEquals(3.8, students.get(1).getGpa(), 0.01);
    assertEquals(3.2, students.get(2).getGpa(), 0.01);
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

    List<Employee> employees = java.util.Arrays.asList();

    Sort.sort(employees, "salary");

    assertEquals(0, employees.size());
}
@Test
public void testSortNoGetterMethod() {
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

    Person[] peopleArray = new Person[] {
            new Person("Alice", 25),
            new Person("Bob", 30),
            new Person("Charlie", 20)
    };

    List<Person> people = java.util.Arrays.asList(peopleArray);

    try {
        Sort.sort(people, "age");
        fail("Expected IllegalArgumentException for no getter method");
    } catch (IllegalArgumentException e) {
        // expected
    }
}
@Test
public void testSortMultipleFields() {
    class Student {
        private String name;
        private int grade;
        private double gpa;

        public Student(String name, int grade, double gpa) {
            this.name = name;
            this.grade = grade;
            this.gpa = gpa;
        }

        public String getName() {
            return name;
        }

        public int getGrade() {
            return grade;
        }

        public double getGpa() {
            return gpa;
        }
    }

    Student[] studentsArray = new Student[] {
            new Student("John", 11, 3.8),
            new Student("Emily", 12, 3.2),
            new Student("Michael", 11, 3.9)
    };

    List<Student> students = java.util.Arrays.asList(studentsArray);

    Sort.sort(students, "grade");
    assertEquals(11, students.get(0).getGrade());
    assertEquals(11, students.get(1).getGrade());
    assertEquals(12, students.get(2).getGrade());

    Sort.sort(students, "gpa");
    assertEquals(3.2, students.get(0).getGpa(), 0.01);
    assertEquals(3.8, students.get(1).getGpa(), 0.01);
    assertEquals(3.9, students.get(2).getGpa(), 0.01);
}
@Test
public void testSortPrivateField() {
    class Person {
        private String name;
        private int age;

        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        private String getName() {
            return name;
        }

        private int getAge() {
            return age;
        }
    }

    Person[] peopleArray = new Person[] {
            new Person("Alice", 25),
            new Person("Bob", 30),
            new Person("Charlie", 20)
    };

    List<Person> people = java.util.Arrays.asList(peopleArray);

    try {
        Sort.sort(people, "age");
        fail("Expected IllegalArgumentException for private field");
    } catch (IllegalArgumentException e) {
        // expected
    }
}
@Test
    public void testSorting() {
        class TestData {
            private int value;

            public TestData(int value) {
                this.value = value;
            }

            public int getValue() {
                return value;
            }
        }

        TestData[] testDataArray = new TestData[]{new TestData(5), new TestData(2), new TestData(8)};
        List<TestData> data = Arrays.asList(testDataArray);
        Sort.sort(data, "value");
        assertEquals(2, data.get(0).getValue());
        assertEquals(5, data.get(1).getValue());
        assertEquals(8, data.get(2).getValue());
    }
@Test
public void testSortMethod() {
    List<MyClass> list = new java.util.ArrayList<>();
    list.add(new MyClass(5));
    list.add(new MyClass(2));
    list.add(new MyClass(8));

    Sort.sort(list, "value", false);

    assertEquals(2, list.get(0).getValue());
    assertEquals(5, list.get(1).getValue());
    assertEquals(8, list.get(2).getValue());
}

class MyClass {
    private int value;

    public MyClass(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}

}