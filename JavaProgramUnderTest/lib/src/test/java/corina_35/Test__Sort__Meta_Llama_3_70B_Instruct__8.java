package corina_35;
import java.lang.reflect.Method;
import java.util.Comparator;
import java.util.List;
import java.util.Arrays;
import java.lang.reflect.Field;
import org.junit.jupiter.api.Test;
import java.util.Collections;
import static org.junit.jupiter.api.Assertions.*;
import java.lang.reflect.InvocationTargetException;
public class Test__Sort__Meta_Llama_3_70B_Instruct__8 {
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

    List<Person> people = new java.util.ArrayList<>();
    people.add(new Person("John", 25));
    people.add(new Person("Alice", 30));
    people.add(new Person("Bob", 20));

    Sort.sort(people, "age");

    assertEquals(20, people.get(0).getAge());
    assertEquals(25, people.get(1).getAge());
    assertEquals(30, people.get(2).getAge());
}
@Test
public void testSortDescending() {
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
public void testSortEmptyList() {
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

    Sort.sort(people, "age");

    assertEquals(0, people.size());
}
@Test
public void testSortNullField() {
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

    try {
        Sort.sort(people, "nonExistingField");
        assert false; // Should not reach this line
    } catch (IllegalArgumentException e) {
        assertEquals("No such field 'nonExistingField' exists in class " + Person.class.getName() + "!", e.getMessage().replace(" exists", "' exists"));
    }
}
@Test
public void testSortNullList() {
    try {
        Sort.sort(null, "age");
        assert false; // Should not reach this line
    } catch (NullPointerException e) {
        assertEquals("Cannot invoke \"java.util.List.size()\" because \"data\" is null", e.getMessage());
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

        public String getName() {
            return name;
        }

        public int getAge() {
            return age;
        }
    }

    List<Person> people = new java.util.ArrayList<>();
    people.add(new Person("John", 25));
    people.add(null);
    people.add(new Person("Bob", 20));

    try {
        Sort.sort(people, "age");
        assert false; // Should not reach this line
    } catch (NullPointerException e) {
        assertEquals("Cannot invoke \"Object.getClass()\" because \"obj\" is null", e.getMessage());
    }
}
@Test
public void testSortListWithNonComparableElements() {
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

    Sort.sort(people, "name"); // No exception is thrown
}
@Test
    public void testSortNew() {
        class MyClass {
            private int value;

            public MyClass(int value) {
                this.value = value;
            }

            public int getValue() {
                return value;
            }
        }

        java.util.List<MyClass> list = new java.util.ArrayList<MyClass>();
        list.add(new MyClass(5));
        list.add(new MyClass(3));
        list.add(new MyClass(8));
        list.add(new MyClass(1));
        list.add(new MyClass(4));

        Sort.sort(list, "value");

        assertEquals(1, list.get(0).getValue());
    }
}