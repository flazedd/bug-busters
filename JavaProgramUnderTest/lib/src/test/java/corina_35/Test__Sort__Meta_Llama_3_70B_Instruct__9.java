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
public class Test__Sort__Meta_Llama_3_70B_Instruct__9 {
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

    java.util.ArrayList<Person> people = new java.util.ArrayList<>();
    people.add(new Person("Alice", 25));
    people.add(new Person("Bob", 30));
    people.add(new Person("Charlie", 20));

    Sort.sort(people, "age", true);

    assertEquals(30, people.get(0).getAge());
    assertEquals(25, people.get(1).getAge());
    assertEquals(20, people.get(2).getAge());
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

        public int getAge() {
            return age;
        }
    }

    java.util.ArrayList<Person> people = new java.util.ArrayList<>();
    people.add(new Person("Charlie", 20));
    people.add(new Person("Bob", 30));
    people.add(new Person("Alice", 25));

    Sort.sort(people, "name");

    assertEquals("Alice", people.get(0).getName());
    assertEquals("Bob", people.get(1).getName());
    assertEquals("Charlie", people.get(2).getName());
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

    java.util.ArrayList<Person> people = new java.util.ArrayList<>();

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

    java.util.ArrayList<Person> people = new java.util.ArrayList<>();
    people.add(new Person("Alice", 25));
    people.add(new Person("Bob", 30));
    people.add(new Person("Charlie", 20));

    try {
        Sort.sort(people, "nonExistingField");
        fail("Expected IllegalArgumentException for non-existing field");
    } catch (IllegalArgumentException e) {
        // expected
    }
}
@Test
public void testSortNullObject() {
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
    people.add(null);
    people.add(new Person("Charlie", 20));

    try {
        Sort.sort(people, "age");
        fail("Expected NullPointerException for null object in list");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testSortMultipleFields() {
    class Person {
        private String name;
        private int age;
        private String occupation;

        public Person(String name, int age, String occupation) {
            this.name = name;
            this.age = age;
            this.occupation = occupation;
        }

        public String getName() {
            return name;
        }

        public int getAge() {
            return age;
        }

        public String getOccupation() {
            return occupation;
        }
    }

    java.util.ArrayList<Person> people = new java.util.ArrayList<>();
    people.add(new Person("Alice", 25, "Doctor"));
    people.add(new Person("Bob", 30, "Engineer"));
    people.add(new Person("Charlie", 20, "Teacher"));

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

    java.util.ArrayList<Person> people = new java.util.ArrayList<>();
    people.add(new Person("Alice", 25));
    people.add(new Person("Bob", 30));
    people.add(new Person("Charlie", 20));

    Sort.sort(people, "age", true);

    assertEquals(30, people.get(0).getAge());
    assertEquals(25, people.get(1).getAge());
    assertEquals(20, people.get(2).getAge());
}
@Test
public void testSortByNameDescending() {
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
    people.add(new Person("Charlie", 20));
    people.add(new Person("Bob", 30));
    people.add(new Person("Alice", 25));

    Sort.sort(people, "name", true);

    assertEquals("Charlie", people.get(0).getName());
    assertEquals("Bob", people.get(1).getName());
    assertEquals("Alice", people.get(2).getName());
}
}