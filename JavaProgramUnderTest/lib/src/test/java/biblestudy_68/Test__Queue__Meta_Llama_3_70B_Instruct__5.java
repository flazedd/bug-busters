package biblestudy_68;
import java.util.*;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
public class Test__Queue__Meta_Llama_3_70B_Instruct__5 {
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
public void testMaxCapacityExceeded() {
    Queue queue = new Queue(2);
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    queue.enqueue("Cherry");
    assertTrue(queue.maxCapacityExceeded());
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
public void testToString() {
    Queue queue = new Queue();
    queue.enqueue("Apple");
    queue.enqueue("Banana");
    String queueString = queue.toString();
    assertTrue(queueString.contains("numItems=2"));
    assertTrue(queueString.contains("maxNumItems=2"));
    assertTrue(queueString.contains("maxCapacity=-1"));
    assertTrue(queueString.contains("getObjects()=[Apple, Banana]"));
}
}