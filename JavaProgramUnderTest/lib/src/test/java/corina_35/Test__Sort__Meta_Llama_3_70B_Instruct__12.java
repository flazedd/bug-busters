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
public class Test__Sort__Meta_Llama_3_70B_Instruct__12 {
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
        people.add(new Person("John", 25));
        people.add(new Person("Alice", 30));
        people.add(new Person("Bob", 20));

        Sort.sort(people, "name", false);

        assertEquals("Alice", people.get(0).getName());
        assertEquals("Bob", people.get(1).getName());
        assertEquals("John", people.get(2).getName());
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

            public int getAge() {
                return age;
            }
        }

        java.util.List<Person> people = new java.util.ArrayList<>();

        Sort.sort(people, "age", true);

        assertEquals(0, people.size());
    }
@Test
public void testSorting() {
    class TestData {
        private int id;
        public TestData(int id) { this.id = id; }
        public int getId() { return id; }
    }

    List<TestData> data = new java.util.ArrayList<>();
    data.add(new TestData(3));
    data.add(new TestData(1));
    data.add(new TestData(2));

    Sort.sort(data, "id");

    assertEquals(1, data.get(0).getId());
    assertEquals(2, data.get(1).getId());
    assertEquals(3, data.get(2).getId());
}
@Test
public void testSortingDecreasing() {
    class TestData {
        private int id;
        public TestData(int id) { this.id = id; }
        public int getId() { return id; }
    }

    List<TestData> data = new java.util.ArrayList<>();
    data.add(new TestData(1));
    data.add(new TestData(3));
    data.add(new TestData(2));

    Sort.sort(data, "id", true);

    assertEquals(3, data.get(0).getId());
    assertEquals(2, data.get(1).getId());
    assertEquals(1, data.get(2).getId());
}
@Test
public void testSortingWithNullValue() {
    class TestData {
        private Integer id;
        public TestData(Integer id) { this.id = id; }
        public Integer getId() { return id; }
    }

    List<TestData> data = new java.util.ArrayList<>();
    data.add(new TestData(3));
    data.add(new TestData(1));
    data.add(new TestData(null));
    data.add(new TestData(2));

    Sort.sort(data, "id");

    assertNull(data.get(0).getId());
    assertEquals(1, data.get(1).getId());
    assertEquals(2, data.get(2).getId());
    assertEquals(3, data.get(3).getId());
}
@Test
public void testSortingEmptyList() {
    class TestData {
        private int id;
        public TestData(int id) { this.id = id; }
        public int getId() { return id; }
    }

    List<TestData> data = new java.util.ArrayList<>();

    Sort.sort(data, "id");

    assertEquals(0, data.size());
}
@Test
public void testSortingListWithOneElement() {
    class TestData {
        private int id;
        public TestData(int id) { this.id = id; }
        public int getId() { return id; }
    }

    List<TestData> data = new java.util.ArrayList<>();
    data.add(new TestData(1));

    Sort.sort(data, "id");

    assertEquals(1, data.get(0).getId());
    assertEquals(1, data.size());
}
}