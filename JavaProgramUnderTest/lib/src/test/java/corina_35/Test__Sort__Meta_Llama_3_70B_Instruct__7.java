package corina_35;
import java.lang.reflect.Field;
import static org.junit.jupiter.api.Assertions.*;
import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;
import java.util.List;
import java.lang.reflect.InvocationTargetException;
import java.util.Collections;
import java.util.Arrays;
import java.util.Comparator;
public class Test__Sort__Meta_Llama_3_70B_Instruct__7 {
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
    students.add(new Student("John", 20));
    students.add(new Student("Alice", 18));
    students.add(new Student("Bob", 22));

    Sort.sort(students, "age", true);

    assertEquals(22, students.get(0).getAge());
    assertEquals(20, students.get(1).getAge());
    assertEquals(18, students.get(2).getAge());
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

        public int getSalary() {
            return salary;
        }
    }

    java.util.List<Employee> employees = new java.util.ArrayList<>();

    Sort.sort(employees, "salary", true);

    assertEquals(0, employees.size());
}

@Test
public void testSortNullField() {
    class Person {
        private String name;
        private Integer age;

        public Person(String name, Integer age) {
            this.name = name;
            this.age = age;
        }

        public Integer getAge() {
            return age;
        }
    }

    java.util.List<Person> people = new java.util.ArrayList<>();
    people.add(new Person("John", 20));
    people.add(new Person("Alice", null));
    people.add(new Person("Bob", 22));

    Sort.sort(people, "age", true);

    assertEquals(22, people.get(0).getAge());
    assertEquals(20, people.get(1).getAge());
    assertNull(people.get(2).getAge());
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
    }

    java.util.List<Person> people = new java.util.ArrayList<>();
    people.add(new Person("John", 20));
    people.add(new Person("Alice", 18));
    people.add(new Person("Bob", 22));

    try {
        Sort.sort(people, "age", true);
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        assertEquals("No method 'getAge()' exists in class " + Person.class.getName() + "!", e.getMessage());
    }
}

@Test
public void testSortEmptyListWithField() {
    class Employee {
        private String name;
        private int salary;

        public Employee(String name, int salary) {
            this.name = name;
            this.salary = salary;
        }

        public int getSalary() {
            return salary;
        }
    }

    java.util.List<Employee> employees = new java.util.ArrayList<>();

    Sort.sort(employees, "salary", true);

    assertEquals(0, employees.size());
}

@Test
public void testSortListWithDuplicateElements() {
    class Employee {
        private String name;
        private int salary;

        public Employee(String name, int salary) {
            this.name = name;
            this.salary = salary;
        }

        public int getSalary() {
            return salary;
        }
    }

    java.util.List<Employee> employees = new java.util.ArrayList<>();
    employees.add(new Employee("John", 20));
    employees.add(new Employee("Alice", 20));
    employees.add(new Employee("Bob", 22));

    Sort.sort(employees, "salary", true);

    assertEquals(22, employees.get(0).getSalary());
    assertEquals(20, employees.get(1).getSalary());
    assertEquals(20, employees.get(2).getSalary());
}

@Test
public void testSort_1() {
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

    List<Object> people = new java.util.ArrayList<>();
    people.add(new Person("John", 25));
    people.add(new Person("Alice", 30));
    people.add(new Person("Bob", 20));

    Sort.sort(people, "age", true);

    assertEquals(30, ((Person) people.get(0)).getAge());
    assertEquals(25, ((Person) people.get(1)).getAge());
    assertEquals(20, ((Person) people.get(2)).getAge());
}

@Test
public void testSort_3() {
    class Employee {
        private String name;
        private int salary;

        public Employee(String name, int salary) {
            this.name = name;
            this.salary = salary;
        }

        public int getSalary() {
            return salary;
        }
    }

    List<Object> employees = new java.util.ArrayList<>();
    employees.add(new Employee("John", 40000));
    employees.add(new Employee("Alice", 50000));
    employees.add(new Employee("Bob", 30000));

    Sort.sort(employees, "salary", true);

    assertEquals(50000, ((Employee) employees.get(0)).getSalary());
    assertEquals(40000, ((Employee) employees.get(1)).getSalary());
    assertEquals(30000, ((Employee) employees.get(2)).getSalary());
}


}