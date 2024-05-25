package corina_35;
import java.util.List;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Field;
import java.util.Collections;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Comparator;
import org.junit.jupiter.api.Test;
public class Test__Sort__Meta_Llama_3_70B_Instruct__1 {
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

    List<Person> people = new java.util.ArrayList<>();
    people.add(new Person("John", 25));
    people.add(new Person("Alice", 30));
    people.add(new Person("Bob", 20));

    Sort.sort(people, "age", false);

    assertEquals(20, people.get(0).getAge());
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
}

}