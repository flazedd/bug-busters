package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.ConcurrentModificationException;
import java.util.LinkedList;
import java.util.List;

public class Sort_ESTest_8 {

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
        Sort.sort((List) null, "]p^YZ<`r4-YlzKDFG", false);
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
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      List<Object> list0 = linkedList0.subList(0, 0);
      linkedList0.add((Object) "");
      // Undeclared exception!
      try { 
        Sort.sort(list0, "");
        fail("Expecting exception: ConcurrentModificationException");
      
      } catch(ConcurrentModificationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("java.util.SubList", e);
      }
  }

  @Test
  public void test3()  throws Throwable  {
      // Undeclared exception!
      try { 
        Sort.sort((List) null, "3#");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.Sort", e);
      }
  }

  @Test
  public void test4()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      linkedList0.add((Object) "3#");
      try { 
        Sort.sort((List) linkedList0, "3#", true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // No such field '3# exists in class java.lang.String!
         //
         //verifyException("corina.util.Sort", e);
      }
  }

  @Test
  public void test5()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      Sort.sort((List) linkedList0, "", false);
      assertFalse(linkedList0.contains(false));
  }

  @Test
  public void test6()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      linkedList0.add((Object) "3#");
      try { 
        Sort.sort((List) linkedList0, "3#");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // No such field '3# exists in class java.lang.String!
         //
         //verifyException("corina.util.Sort", e);
      }
  }

  @Test
  public void test7()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      Sort.sort((List) linkedList0, "3#");
      assertFalse(linkedList0.contains("3#"));
  }
}
