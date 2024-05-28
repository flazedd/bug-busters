package biblestudy_68;
import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Queue__Meta_Llama_3_70B_Instruct__3 {
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
    queue.enqueue("Hello");
    assertTrue(queue.maxCapacityExceeded());
}

@Test
public void testGetPeakNumberItems() {
    Queue queue = new Queue();
    queue.enqueue("Hello");
    queue.enqueue("World");
    queue.enqueue("Hello");
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
    queue.enqueue("Hello");
    Vector objects = queue.getObjects();
    assertEquals(3, objects.size());
    assertTrue(objects.contains("Hello"));
    assertTrue(objects.contains("World"));
}

@Test
public void testToString() {
    Queue queue = new Queue();
    queue.enqueue("Hello");
    queue.enqueue("World");
    String expected = "biblestudy_68.Queue:[numItems=2, maxNumItems=2, maxCapacity=-1, getObjects()=[Hello, World]\r\n]";
    assertEquals(expected, queue.toString());
}

}