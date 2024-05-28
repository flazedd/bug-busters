package biblestudy_68;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.*;
public class Test__Queue__Meta_Llama_3_70B_Instruct__2 {
@Test
public void testIsEmpty() {
    Queue queue = new Queue();
    assertTrue(queue.isEmpty());
}

@Test
public void testEnqueueDequeue() {
    Queue queue = new Queue();
    queue.enqueue("Hello");
    queue.enqueue("World");
    assertEquals("Hello", queue.dequeue());
}

@Test
public void testGetNumberItems() {
    Queue queue = new Queue();
    queue.enqueue("Item1");
    queue.enqueue("Item2");
    assertEquals(2, queue.getNumberItems());
}

@Test
public void testRefreshElement() {
    Queue queue = new Queue();
    queue.enqueue("Item1");
    queue.enqueue("Item2");
    queue.refreshElement("Item1");
    assertEquals("Item2", queue.dequeue());
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
public void testGetObjects() {
    Queue queue = new Queue();
    queue.enqueue("Item1");
    queue.enqueue("Item2");
    Vector objects = queue.getObjects();
    assertEquals(2, objects.size());
    assertTrue(objects.contains("Item1"));
    assertTrue(objects.contains("Item2"));
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