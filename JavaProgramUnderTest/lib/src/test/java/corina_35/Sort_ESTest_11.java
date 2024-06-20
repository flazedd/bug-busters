package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.ConcurrentModificationException;
import java.util.LinkedList;
import java.util.List;
public class Sort_ESTest_11 {

  @Test
  public void test0()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      List<Object> list0 = linkedList0.subList(0, 0);
      linkedList0.add((Object) "");
      // Undeclared exception!
      try { 
        Sort.sort(list0, "", false);
        fail("Expecting exception: ConcurrentModificationException");
      
      } catch(ConcurrentModificationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("java.util.SubList", e);
      }
  }

  @Test
  public void test1()  throws Throwable  {
      // Undeclared exception!
      try { 
        Sort.sort((List) null, "", false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.Sort", e);
      }
  }

  @Test
  public void test2()  throws Throwable  {
      // Undeclared exception!
      try { 
        Sort.sort((List) null, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.Sort", e);
      }
  }

  @Test
  public void test3()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      linkedList0.offer("!");
      try { 
        Sort.sort((List) linkedList0, "!", true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // No such field '! exists in class java.lang.String!
         //
         //verifyException("corina.util.Sort", e);
      }
  }

  @Test
  public void test4()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      Sort.sort((List) linkedList0, "", true);
      assertEquals(0, linkedList0.size());
  }

  @Test
  public void test5()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      linkedList0.add((Object) "");
      try { 
        Sort.sort((List) linkedList0, "hIo$dg'vDnn");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // No such field 'hIo$dg'vDnn exists in class java.lang.String!
         //
         //verifyException("corina.util.Sort", e);
      }
  }

  @Test
  public void test6()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      Sort.sort((List) linkedList0, "hIo$dg'vDnn");
      assertFalse(linkedList0.contains("hIo$dg'vDnn"));
  }
}
