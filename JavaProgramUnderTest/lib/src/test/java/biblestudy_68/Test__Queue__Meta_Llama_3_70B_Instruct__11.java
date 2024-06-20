package biblestudy_68;
import static org.junit.jupiter.api.Assertions.*;
import java.util.*;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
public class Test__Queue__Meta_Llama_3_70B_Instruct__11 {
@Test
public void testEnqueueAndDequeue() {
    Queue queue = new Queue();
    queue.enqueue("Item1");
    queue.enqueue("Item2");
    assertEquals("Item1", queue.dequeue());
}
@Test
public void testRemove() {
    Queue queue = new Queue();
    queue.enqueue("Item1");
    queue.enqueue("Item2");
    queue.enqueue("Item1");
    assertEquals(2, queue.remove("Item1"));
    assertEquals(1, queue.getNumberItems());
}
@Test
public void testRefreshElement() {
    Queue queue = new Queue();
    queue.enqueue("Item1");
    queue.enqueue("Item2");
    queue.enqueue("Item3");
    queue.refreshElement("Item2");
    assertEquals("Item1", queue.dequeue());
    assertEquals("Item3", queue.dequeue());
    assertEquals("Item2", queue.dequeue());
}
@Test
public void testMaxCapacityExceeded() {
    Queue queue = new Queue(2);
    queue.enqueue("Item1");
    queue.enqueue("Item2");
    queue.enqueue("Item3");
    assertTrue(queue.maxCapacityExceeded());
}
@Test
public void testIsEmpty() {
    Queue queue = new Queue();
    assertTrue(queue.isEmpty());
    queue.enqueue("Item1");
    assertFalse(queue.isEmpty());
}
@Test
public void testGetObjects() {
    Queue queue = new Queue();
    queue.enqueue("Item1");
    queue.enqueue("Item2");
    queue.enqueue("Item3");
    Vector objects = queue.getObjects();
    assertEquals(3, objects.size());
    assertTrue(objects.contains("Item1"));
    assertTrue(objects.contains("Item2"));
    assertTrue(objects.contains("Item3"));
}
@Test
public void testGetPeakNumberItems() {
    Queue queue = new Queue();
    queue.enqueue("Item1");
    queue.enqueue("Item2");
    queue.enqueue("Item3");
    assertEquals(3, queue.getPeakNumberItems());
    queue.dequeue();
    assertEquals(3, queue.getPeakNumberItems());
}
@Test
public void testToString() {
    Queue queue = new Queue();
    queue.enqueue("Item1");
    queue.enqueue("Item2");
    String queueString = queue.toString();
    assertTrue(queueString.contains("numItems=2"));
    assertTrue(queueString.contains("maxNumItems=2"));
    assertTrue(queueString.contains("maxCapacity=-1"));
    assertTrue(queueString.contains("getObjects()=[Item1, Item2]"));
}
}