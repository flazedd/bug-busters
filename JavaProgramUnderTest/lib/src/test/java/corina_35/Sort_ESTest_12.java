package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.ConcurrentModificationException;
import java.util.LinkedList;
import java.util.List;
public class Sort_ESTest_12 {

  @Test
  public void test0()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      List<Object> list0 = linkedList0.subList(0, 0);
      linkedList0.add(0, (Object) list0);
      // Undeclared exception!
      try { 
        Sort.sort(list0, "U", false);
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
        Sort.sort((List) linkedList0, "Gtc[eH", true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // No such field 'Gtc[eH exists in class java.util.LinkedList!
         //
         //verifyException("corina.util.Sort", e);
      }
  }

  @Test
  public void test4()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      Sort.sort((List) linkedList0, "D>Lf,;@YZy(<", false);
      assertEquals(0, linkedList0.size());
  }

  @Test
  public void test5()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      linkedList0.add((Object) linkedList0);
      try { 
        Sort.sort((List) linkedList0, "No access to method '");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // No such field 'No access to method ' exists in class java.util.LinkedList!
         //
         //verifyException("corina.util.Sort", e);
      }
  }

  @Test
  public void test6()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      Sort.sort((List) linkedList0, "No access to method '");
      assertFalse(linkedList0.contains("No access to method '"));
  }
}
