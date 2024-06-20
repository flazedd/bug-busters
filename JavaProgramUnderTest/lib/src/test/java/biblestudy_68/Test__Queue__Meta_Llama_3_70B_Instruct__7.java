package biblestudy_68;
import java.util.*;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Queue__Meta_Llama_3_70B_Instruct__7 {
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
    queue.refreshElement("Item1");
    assertEquals("Item2", queue.dequeue());
    assertEquals("Item1", queue.dequeue());
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
public void testIsEmpty() {
    Queue queue = new Queue();
    assertTrue(queue.isEmpty());
    queue.enqueue("Item1");
    assertTrue(!queue.isEmpty());
}

@Test
public void testGetPeakNumberItems() {
    Queue queue = new Queue();
    assertEquals(0, queue.getPeakNumberItems());
    queue.enqueue("Item1");
    assertEquals(1, queue.getPeakNumberItems());
    queue.enqueue("Item2");
    assertEquals(2, queue.getPeakNumberItems());
    queue.dequeue();
    assertEquals(2, queue.getPeakNumberItems());
}

@Test
public void testToString() {
    Queue queue = new Queue();
    queue.enqueue("Item1");
    queue.enqueue("Item2");
    String expected = "biblestudy_68.Queue:[numItems=2, maxNumItems=2, maxCapacity=-1, getObjects()=[Item1, Item2]\r\n]";
    assertEquals(expected, queue.toString());
}

@Test
public void testGetNumberItems() {
    Queue queue = new Queue();
    assertEquals(0, queue.getNumberItems());
    queue.enqueue("Item1");
    assertEquals(1, queue.getNumberItems());
    queue.enqueue("Item2");
    assertEquals(2, queue.getNumberItems());
}


}