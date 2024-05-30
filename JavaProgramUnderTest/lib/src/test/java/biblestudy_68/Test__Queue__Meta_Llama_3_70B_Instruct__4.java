package biblestudy_68;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import java.util.*;
public class Test__Queue__Meta_Llama_3_70B_Instruct__4 {
@Test
public void testDequeue() {
    Queue queue = new Queue();
    queue.enqueue("A");
    queue.enqueue("B");
    queue.enqueue("C");
    assertEquals("A", queue.dequeue());
}

@Test
public void testRemove() {
    Queue queue = new Queue();
    queue.enqueue("A");
    queue.enqueue("B");
    queue.enqueue("B");
    queue.enqueue("C");
    assertEquals(2, queue.remove("B"));
    assertEquals("A", queue.dequeue());
    assertEquals("C", queue.dequeue());
}

@Test
public void testGetPeakNumberItems() {
    Queue queue = new Queue();
    queue.enqueue("A");
    queue.enqueue("B");
    queue.enqueue("C");
    assertEquals(3, queue.getPeakNumberItems());
    queue.dequeue();
    assertEquals(3, queue.getPeakNumberItems());
}

@Test
public void testIsEmpty() {
    Queue queue = new Queue();
    assertTrue(queue.isEmpty());
    queue.enqueue("A");
    assertFalse(queue.isEmpty());
}

@Test
public void testGetObjects() {
    Queue queue = new Queue();
    queue.enqueue("A");
    queue.enqueue("B");
    queue.enqueue("C");
    Vector objects = queue.getObjects();
    assertEquals(3, objects.size());
    assertTrue(objects.contains("A"));
    assertTrue(objects.contains("B"));
    assertTrue(objects.contains("C"));
}

@Test
public void testToString() {
    Queue queue = new Queue();
    queue.enqueue("A");
    queue.enqueue("B");
    queue.enqueue("C");
    String queueString = queue.toString();
    assertTrue(queueString.contains("numItems=3"));
    assertTrue(queueString.contains("maxNumItems=3"));
    assertTrue(queueString.contains("maxCapacity=-1"));
    assertTrue(queueString.contains("getObjects()=[A, B, C]"));
}

@Test
public void testEnqueueNull() {
    Queue queue = new Queue();
    queue.enqueue(null);
    assertEquals(0, queue.getNumberItems());
}

@Test
public void testDequeueEmptyQueue() {
    Queue queue = new Queue();
    Object dequeued = queue.dequeue();
    assertNull(dequeued);
}

}