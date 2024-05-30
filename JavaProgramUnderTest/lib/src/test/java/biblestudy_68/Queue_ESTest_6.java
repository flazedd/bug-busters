package biblestudy_68;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.Vector;

public class Queue_ESTest_6 {

  @Test
  public void test00()  throws Throwable  {
      Queue queue0 = new Queue((-14));
      boolean boolean0 = queue0.maxCapacityExceeded();
      assertEquals(0, queue0.getPeakNumberItems());
      assertEquals(0, queue0.getNumberItems());
      assertTrue(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      Queue queue0 = new Queue(1346);
      boolean boolean0 = queue0.maxCapacityExceeded();
      assertFalse(boolean0);
      assertEquals(0, queue0.getPeakNumberItems());
      assertEquals(0, queue0.getNumberItems());
  }

  @Test
  public void test02()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.dequeue();
      queue0.enqueue(object0);
      queue0.refreshElement(object0);
      assertFalse(queue0.isEmpty());
  }

  @Test
  public void test03()  throws Throwable  {
      Queue queue0 = new Queue();
      Vector vector0 = queue0.getObjects();
      int int0 = queue0.remove(vector0);
      assertFalse(queue0.maxCapacityExceeded());
      assertEquals(0, int0);
      assertEquals(0, vector0.capacity());
      assertEquals(0, queue0.getPeakNumberItems());
  }

  @Test
  public void test04()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.enqueue(object0);
      int int0 = queue0.getPeakNumberItems();
      assertFalse(queue0.isEmpty());
      assertEquals(1, int0);
  }

  @Test
  public void test05()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.enqueue(object0);
      int int0 = queue0.getNumberItems();
      assertFalse(queue0.isEmpty());
      assertEquals(1, int0);
  }

  @Test
  public void test06()  throws Throwable  {
      Queue queue0 = new Queue();
      queue0.dequeue();
      int int0 = queue0.getNumberItems();
      assertEquals((-1), int0);
  }

  @Test
  public void test07()  throws Throwable  {
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
  public void test08()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.enqueue(object0);
      queue0.getObjects();
      assertFalse(queue0.isEmpty());
  }

  @Test
  public void test09()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.enqueue(object0);
      assertFalse(queue0.isEmpty());
      
      int int0 = queue0.remove(object0);
      assertEquals(1, int0);
  }

  @Test
  public void test10()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.enqueue(object0);
      boolean boolean0 = queue0.isEmpty();
      assertFalse(boolean0);
  }

  @Test
  public void test11()  throws Throwable  {
      Queue queue0 = new Queue();
      queue0.isEmpty();
      assertFalse(queue0.maxCapacityExceeded());
      assertEquals(0, queue0.getPeakNumberItems());
      assertEquals(0, queue0.getNumberItems());
  }

  @Test
  public void test12()  throws Throwable  {
      Queue queue0 = new Queue((-22));
      Queue.Node queue_Node0 = queue0.new Node(queue0);
      assertEquals(0, queue0.getNumberItems());
      assertEquals(0, queue0.getPeakNumberItems());
      assertTrue(queue0.maxCapacityExceeded());
  }

  @Test
  public void test13()  throws Throwable  {
      Queue queue0 = new Queue(1);
      Vector vector0 = queue0.getObjects();
      queue0.enqueue(vector0);
      boolean boolean0 = queue0.maxCapacityExceeded();
      assertFalse(queue0.isEmpty());
      assertTrue(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Queue queue0 = new Queue();
      boolean boolean0 = queue0.maxCapacityExceeded();
      assertFalse(boolean0);
      assertEquals(0, queue0.getPeakNumberItems());
      assertEquals(0, queue0.getNumberItems());
  }

  @Test
  public void test15()  throws Throwable  {
      Queue queue0 = new Queue(1);
      boolean boolean0 = queue0.maxCapacityExceeded();
      assertFalse(boolean0);
      assertEquals(0, queue0.getPeakNumberItems());
  }

  @Test
  public void test16()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.enqueue(object0);
      queue0.toString();
      assertFalse(queue0.isEmpty());
  }

  @Test
  public void test17()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.enqueue(object0);
      queue0.refreshElement("bible.util.Queue:[numItems=1, maxNumItems=1, maxCapacity=-1, getObjects()=[java.lang.Object@54fe67a5]\r\n]");
      queue0.refreshElement("bible.util.Queue:[numItems=0, maxNumItems=0, maxCapacity=-1, getObjects()=[]\r\n]");
      int int0 = queue0.remove("bible.util.Queue:[numItems=1, maxNumItems=1, maxCapacity=-1, getObjects()=[java.lang.Object@54fe67a5]\r\n]");
      assertEquals(3, queue0.getPeakNumberItems());
      assertEquals(1, int0);
  }

  @Test
  public void test18()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.enqueue(object0);
      queue0.enqueue(object0);
      queue0.refreshElement("bible.util.Queue:[numItems=1, maxNumItems=1, maxCapacity=-1, getObjects()=[java.lang.Object@54fe67a5]\r\n]");
      assertFalse(queue0.isEmpty());
  }

  @Test
  public void test19()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.enqueue(object0);
      queue0.refreshElement("bible.util.Queue:[numItems=1, maxNumItems=1, maxCapacity=-1, getObjects()=[java.lang.Object@54fe67a5]\r\n]");
      int int0 = queue0.remove("bible.util.Queue:[numItems=1, maxNumItems=1, maxCapacity=-1, getObjects()=[java.lang.Object@54fe67a5]\r\n]");
      assertFalse(queue0.isEmpty());
      assertEquals(1, int0);
  }

  @Test
  public void test20()  throws Throwable  {
      Queue queue0 = new Queue();
      Object object0 = new Object();
      queue0.enqueue(object0);
      queue0.enqueue(object0);
      queue0.dequeue();
      Object object1 = queue0.dequeue();
      queue0.enqueue(object1);
      assertEquals(1, queue0.getNumberItems());
  }

  @Test
  public void test21()  throws Throwable  {
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
  public void test22()  throws Throwable  {
      Queue queue0 = new Queue();
      queue0.enqueue((Object) null);
      assertEquals(0, queue0.getNumberItems());
      assertFalse(queue0.maxCapacityExceeded());
      assertEquals(0, queue0.getPeakNumberItems());
  }

  @Test
  public void test23()  throws Throwable  {
      Queue queue0 = new Queue();
      int int0 = queue0.getPeakNumberItems();
      assertEquals(0, queue0.getNumberItems());
      assertEquals(0, int0);
      assertFalse(queue0.maxCapacityExceeded());
  }

  @Test
  public void test24()  throws Throwable  {
      Queue queue0 = new Queue();
      int int0 = queue0.getNumberItems();
      assertFalse(queue0.maxCapacityExceeded());
      assertEquals(0, queue0.getPeakNumberItems());
      assertEquals(0, int0);
  }
}
