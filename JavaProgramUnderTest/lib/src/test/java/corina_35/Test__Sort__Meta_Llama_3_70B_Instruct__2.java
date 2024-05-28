package corina_35;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.List;
import org.junit.jupiter.api.Test;
import java.util.Comparator;
import java.lang.reflect.Field;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Collections;
public class Test__Sort__Meta_Llama_3_70B_Instruct__2 {
@Test
public void testSort() {
    class MyObject {
        private int value;

        public MyObject(int value) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }
    }

    List<MyObject> list = new java.util.ArrayList<>();
    list.add(new MyObject(3));
    list.add(new MyObject(1));
    list.add(new MyObject(2));

    Sort.sort(list, "value", false);

    assertEquals(1, list.get(0).getValue());
}

@Test
public void testSortDecreasing() {
    class MyObject {
        private int value;

        public MyObject(int value) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }
    }

    List<MyObject> list = new java.util.ArrayList<>();
    list.add(new MyObject(1));
    list.add(new MyObject(3));
    list.add(new MyObject(2));

    Sort.sort(list, "value", true);

    assertEquals(3, list.get(0).getValue());
}

@Test
public void testSortEmptyList() {
    class MyObject {
        private int value;

        public MyObject(int value) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }
    }

    List<MyObject> list = new java.util.ArrayList<>();

    Sort.sort(list, "value", false);

    assertEquals(0, list.size());
}

@Test
public void testSortNullValue() {
    class MyObject {
        private Integer value;

        public MyObject(Integer value) {
            this.value = value;
        }

        public Integer getValue() {
            return value;
        }
    }

    List<MyObject> list = new java.util.ArrayList<>();
    list.add(new MyObject(3));
    list.add(new MyObject(null));
    list.add(new MyObject(2));

    Sort.sort(list, "value", false);

    assertNull(list.get(0).getValue());
}

@Test
public void testSortMultipleNullValues() {
    class MyObject {
        private Integer value;

        public MyObject(Integer value) {
            this.value = value;
        }

        public Integer getValue() {
            return value;
        }
    }

    List<MyObject> list = new java.util.ArrayList<>();
    list.add(new MyObject(3));
    list.add(new MyObject(null));
    list.add(new MyObject(null));
    list.add(new MyObject(2));

    Sort.sort(list, "value", false);

    assertNull(list.get(0).getValue());
    assertNull(list.get(1).getValue());
    assertEquals(2, list.get(2).getValue().intValue());
    assertEquals(3, list.get(3).getValue().intValue());
}

}