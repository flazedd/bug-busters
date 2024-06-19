package biblestudy_68;
import java.util.*;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Queue__Meta_Llama_3_70B_Instruct__9 {
@Test
public void testEnqueueAndDequeue() {
    Queue queue = new Queue();
    queue.enqueue("Hello");
    queue.enqueue("World");
    assertEquals("Hello", queue.dequeue());
}
@Test
public void testRemove() {
    Queue queue = new Queue();
    queue.enqueue("Hello");
    queue.enqueue("World");
    queue.enqueue("Hello");
    assertEquals(2, queue.remove("Hello"));
    assertEquals(1, queue.getNumberItems());
}
@Test
public void testRefreshElement() {
    Queue queue = new Queue();
    queue.enqueue("Hello");
    queue.enqueue("World");
    queue.refreshElement("Hello");
    assertEquals("World", queue.dequeue());
    assertEquals("Hello", queue.dequeue());
}
@Test
public void testMaxCapacityExceeded() {
    Queue queue = new Queue(2);
    queue.enqueue("Hello");
    queue.enqueue("World");
    queue.enqueue("Again");
    assertTrue(queue.maxCapacityExceeded());
}
@Test
public void testGetPeakNumberItems() {
    Queue queue = new Queue();
    queue.enqueue("Hello");
    queue.enqueue("World");
    queue.enqueue("Again");
    assertEquals(3, queue.getPeakNumberItems());
    queue.dequeue();
    assertEquals(3, queue.getPeakNumberItems());
}
@Test
public void testIsEmpty() {
    Queue queue = new Queue();
    assertTrue(queue.isEmpty());
    queue.enqueue("Hello");
    assertFalse(queue.isEmpty());
}
@Test
public void testGetObjects() {
    Queue queue = new Queue();
    queue.enqueue("Hello");
    queue.enqueue("World");
    queue.enqueue("Again");
    Vector objects = queue.getObjects();
    assertEquals(3, objects.size());
    assertTrue(objects.contains("Hello"));
    assertTrue(objects.contains("World"));
    assertTrue(objects.contains("Again"));
}
@Test
public void testToString() {
    Queue queue = new Queue();
    queue.enqueue("Hello");
    queue.enqueue("World");
    String toString = queue.toString();
    assertTrue(toString.contains("numItems=2"));
    assertTrue(toString.contains("maxNumItems=2"));
    assertTrue(toString.contains("maxCapacity=-1"));
    assertTrue(toString.contains("getObjects()=[Hello, World]"));
}
}