package biblestudy_68;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import java.util.*;
public class Test__Queue__Meta_Llama_3_70B_Instruct__12 {
@Test
public void testEnqueueDequeue() {
    Queue queue = new Queue();
    queue.enqueue("Hello");
    queue.enqueue("World");
    assertEquals("Hello", queue.dequeue());
}
@Test
public void testRemove() {
    Queue queue = new Queue();
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    queue.enqueue("Apple");
    assertEquals(2, queue.remove("Apple"));
    assertEquals(1, queue.getNumberItems());
}
@Test
public void testRefreshElement() {
    Queue queue = new Queue();
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    queue.refreshElement("Apple");
    assertEquals("Banana", queue.dequeue());
    assertEquals("Apple", queue.dequeue());
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
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    queue.enqueue("Cherry");
    Vector objects = queue.getObjects();
    assertEquals(3, objects.size());
    assertTrue(objects.contains("Apple"));
    assertTrue(objects.contains("Banana"));
    assertTrue(objects.contains("Cherry"));
}
@Test
public void testGetPeakNumberItems() {
    Queue queue = new Queue();
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    queue.enqueue("Cherry");
    assertEquals(3, queue.getPeakNumberItems());
    queue.dequeue();
    assertEquals(3, queue.getPeakNumberItems());
}
@Test
public void testToString() {
    Queue queue = new Queue();
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    String toString = queue.toString();
    assertTrue(toString.contains("numItems=2"));
    assertTrue(toString.contains("maxNumItems=2"));
    assertTrue(toString.contains("maxCapacity=-1"));
    assertTrue(toString.contains("getObjects()=[Apple, Banana]"));
}
@Test
public void testMultipleEnqueueAndDequeue() {
    Queue queue = new Queue();
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    queue.enqueue("Cherry");
    assertEquals("Apple", queue.dequeue());
    queue.enqueue("Date");
    assertEquals("Banana", queue.dequeue());
    assertEquals("Cherry", queue.dequeue());
    assertEquals("Date", queue.dequeue());
    assertTrue(queue.isEmpty());
}
}