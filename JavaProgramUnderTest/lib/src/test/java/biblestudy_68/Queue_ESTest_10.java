package biblestudy_68;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Vector;
public class Queue_ESTest_10 {

  @Test
  public void test00()  throws Throwable  {
      Queue queue0 = new Queue((-1338));
      boolean boolean0 = queue0.maxCapacityExceeded();
      assertTrue(boolean0);
      assertEquals(0, queue0.getNumberItems());
      assertEquals(0, queue0.getPeakNumberItems());
  }

  @Test
  public void test01()  throws Throwable  {
      Queue queue0 = new Queue(1384);
      boolean boolean0 = queue0.maxCapacityExceeded();
      assertFalse(boolean0);
      assertEquals(0, queue0.getPeakNumberItems());
      assertEquals(0, queue0.getNumberItems());
  }

  @Test
  public void test02()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.refreshElement(object0);
      queue0.enqueue(object0);
      queue0.refreshElement(object0);
      assertFalse(queue0.isEmpty());
  }

  @Test
  public void test03()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.refreshElement(object0);
      int int0 = queue0.getPeakNumberItems();
      assertEquals(1, queue0.getNumberItems());
      assertEquals(1, int0);
  }

  @Test
  public void test04()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.enqueue(object0);
      int int0 = queue0.getNumberItems();
      assertEquals(1, int0);
  }

  @Test
  public void test05()  throws Throwable  {
      Queue queue0 = new Queue((-1338));
      queue0.dequeue();
      int int0 = queue0.getNumberItems();
      assertEquals((-1), int0);
  }

  @Test
  public void test06()  throws Throwable  {
      Queue queue0 = new Queue();
      queue0.dequeue();
      // Undeclared exception!
      try { 
        queue0.toString();
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal Capacity: -1
         //
         //verifyException("java.util.Vector", e);
      }
  }

  @Test
  public void test07()  throws Throwable  {
      Queue queue0 = new Queue();
      queue0.dequeue();
      // Undeclared exception!
      try { 
        queue0.getObjects();
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal Capacity: -1
         //
         //verifyException("java.util.Vector", e);
      }
  }

  @Test
  public void test08()  throws Throwable  {
      Queue queue0 = new Queue();
      queue0.dequeue();
      queue0.enqueue("bible.util.Queue:[numItems=0, maxNumItems=0, maxCapacity=-1, getObjects()=[]\r\n]");
      assertEquals(0, queue0.getNumberItems());
  }

  @Test
  public void test09()  throws Throwable  {
      Queue queue0 = new Queue();
      queue0.enqueue("bible.util.Queue:[numItems=0, maxNumItems=0, maxCapacity=-1, getObjects()=[]\r\n]");
      boolean boolean0 = queue0.isEmpty();
      assertEquals(1, queue0.getNumberItems());
      assertFalse(boolean0);
  }

  @Test
  public void test10()  throws Throwable  {
      Queue queue0 = new Queue();
      queue0.isEmpty();
      assertEquals(0, queue0.getNumberItems());
      assertFalse(queue0.maxCapacityExceeded());
      assertEquals(0, queue0.getPeakNumberItems());
  }

  @Test
  public void test11()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      Queue.Node queue_Node0 = queue0.new Node(object0);
      assertEquals(0, queue0.getNumberItems());
      assertEquals(0, queue0.getPeakNumberItems());
      assertFalse(queue0.maxCapacityExceeded());
  }

  @Test
  public void test12()  throws Throwable  {
      Queue queue0 = new Queue();
      boolean boolean0 = queue0.maxCapacityExceeded();
      assertFalse(boolean0);
      assertEquals(0, queue0.getNumberItems());
      assertEquals(0, queue0.getPeakNumberItems());
  }

  @Test
  public void test13()  throws Throwable  {
      Queue queue0 = new Queue(0);
      boolean boolean0 = queue0.maxCapacityExceeded();
      assertEquals(0, queue0.getNumberItems());
      assertEquals(0, queue0.getPeakNumberItems());
      assertTrue(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Queue queue0 = new Queue();
      queue0.dequeue();
      queue0.dequeue();
      boolean boolean0 = queue0.maxCapacityExceeded();
      assertEquals((-2), queue0.getNumberItems());
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.enqueue(object0);
      queue0.getObjects();
      assertEquals(1, queue0.getNumberItems());
  }

  @Test
  public void test16()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.refreshElement(object0);
      Object object1 = new Object();
      Object object2 = new Object();
      queue0.refreshElement(object1);
      queue0.refreshElement(object2);
      int int0 = queue0.remove(object1);
      assertFalse(queue0.isEmpty());
      assertEquals(1, int0);
  }

  @Test
  public void test17()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      Object object1 = new Object();
      queue0.refreshElement(object1);
      queue0.enqueue(object0);
      int int0 = queue0.remove(object0);
      assertFalse(queue0.isEmpty());
      assertEquals(1, int0);
  }

  @Test
  public void test18()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.refreshElement(object0);
      queue0.enqueue(object0);
      Object object1 = new Object();
      int int0 = queue0.remove(object1);
      assertFalse(queue0.isEmpty());
      assertEquals(0, int0);
  }

  @Test
  public void test19()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.refreshElement(object0);
      int int0 = queue0.remove(object0);
      assertTrue(queue0.isEmpty());
      assertEquals(1, int0);
  }

  @Test
  public void test20()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.refreshElement(object0);
      queue0.enqueue(object0);
      queue0.dequeue();
      queue0.dequeue();
      queue0.getObjects();
      assertEquals(2, queue0.getPeakNumberItems());
  }

  @Test
  public void test21()  throws Throwable  {
      Queue queue0 = new Queue();
      queue0.enqueue((Object) null);
      assertEquals(0, queue0.getPeakNumberItems());
      assertFalse(queue0.maxCapacityExceeded());
      assertEquals(0, queue0.getNumberItems());
  }

  @Test
  public void test22()  throws Throwable  {
      Queue queue0 = new Queue();
      int int0 = queue0.getPeakNumberItems();
      assertEquals(0, queue0.getNumberItems());
      assertFalse(queue0.maxCapacityExceeded());
      assertEquals(0, int0);
  }

  @Test
  public void test23()  throws Throwable  {
      Queue queue0 = new Queue(0);
      int int0 = queue0.getNumberItems();
      assertEquals(0, int0);
      assertTrue(queue0.maxCapacityExceeded());
      assertEquals(0, queue0.getPeakNumberItems());
  }

//  @Test
//  public void test24()  throws Throwable  {
//      Queue queue0 = new Queue();
//      String string0 = queue0.toString();
//      assertEquals("bible.util.Queue:[numItems=0, maxNumItems=0, maxCapacity=-1, getObjects()=[]\r\n]", string0);
//  }
}
