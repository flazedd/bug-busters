package biblestudy_68;
import java.util.*;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Queue__Meta_Llama_3_70B_Instruct__10 {
@Test
public void testEnqueueDequeue() {
    Queue queue = new Queue();
    queue.enqueue("Hello");
    queue.enqueue("World");
    assertEquals("Hello", queue.dequeue());
}
@Test
public void testRefreshElement() {
    Queue queue = new Queue();
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    queue.enqueue("Apple");
    queue.refreshElement("Apple");
    assertEquals("Banana", queue.dequeue());
    assertEquals("Apple", queue.dequeue());
}
@Test
public void testRemove() {
    Queue queue = new Queue();
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    queue.enqueue("Apple");
    queue.remove("Apple");
    assertEquals("Banana", queue.dequeue());
    assertTrue(queue.isEmpty());
}
@Test
public void testGetObjects() {
    Queue queue = new Queue();
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    queue.enqueue("Orange");
    Vector objects = queue.getObjects();
    assertEquals(3, objects.size());
    assertTrue(objects.contains("Apple"));
    assertTrue(objects.contains("Banana"));
    assertTrue(objects.contains("Orange"));
}
@Test
public void testMaxCapacityExceeded() {
    Queue queue = new Queue(2);
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    assertTrue(queue.maxCapacityExceeded());
}
@Test
public void testGetPeakNumberItems() {
    Queue queue = new Queue();
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    queue.enqueue("Orange");
    queue.dequeue();
    assertEquals(3, queue.getPeakNumberItems());
}
@Test
public void testIsEmpty() {
    Queue queue = new Queue();
    assertTrue(queue.isEmpty());
    queue.enqueue("Apple");
    assertFalse(queue.isEmpty());
}
@Test
public void testGetNumberItems() {
    Queue queue = new Queue();
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    assertEquals(2, queue.getNumberItems());
    queue.dequeue();
    assertEquals(1, queue.getNumberItems());
}
}