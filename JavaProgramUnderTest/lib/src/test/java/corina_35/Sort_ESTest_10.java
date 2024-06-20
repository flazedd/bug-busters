package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.ConcurrentModificationException;
import java.util.LinkedList;
import java.util.List;
public class Sort_ESTest_10 {

  @Test
  public void test0()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      linkedList0.add((Object) linkedList0);
      try { 
        Sort.sort((List) linkedList0, ";d'1B% %;>zOS!", true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // No such field ';d'1B% %;>zOS! exists in class java.util.LinkedList!
         //
         //verifyException("corina.util.Sort", e);
      }
  }

  @Test
  public void test1()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      List<Object> list0 = linkedList0.subList(0, 0);
      linkedList0.add((Object) list0);
      // Undeclared exception!
      try { 
        Sort.sort(list0, "FaFo,Abf");
        fail("Expecting exception: ConcurrentModificationException");
      
      } catch(ConcurrentModificationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("java.util.SubList", e);
      }
  }

  @Test
  public void test2()  throws Throwable  {
      // Undeclared exception!
      try { 
        Sort.sort((List) null, "");
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
      linkedList0.add((Object) linkedList0);
      try { 
        Sort.sort((List) linkedList0, "JZlkxE'd)m2:[");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // No such field 'JZlkxE'd)m2:[ exists in class java.util.LinkedList!
         //
         //verifyException("corina.util.Sort", e);
      }
  }

  @Test
  public void test4()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      Sort.sort((List) linkedList0, "", true);
      assertFalse(linkedList0.contains(""));
  }

  @Test
  public void test5()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      Object object0 = new Object();
      linkedList0.addLast(object0);
      // Undeclared exception!
      try { 
        Sort.sort((List) linkedList0, (String) null, true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test6()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      Sort.sort((List) linkedList0, (String) null);
      assertEquals(0, linkedList0.size());
  }
}
